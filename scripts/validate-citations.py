#!/usr/bin/env python3
import argparse
import datetime
import os
import re
import sys
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
warnings = []

USER_AGENT = "blog-writing-skills-link-checker/1.0 (+https://github.com/wakqasahmed/blog-writing-skills)"
URL_TIMEOUT_SECONDS = 8
URL_CHECK_DELAY_SECONDS = 0.5
HEAD_FALLBACK_STATUSES = {403, 405, 501}
# Bot-management challenges (rate-limiting, Cloudflare scoring CI IPs, etc.) can return
# these codes intermittently for reasons unrelated to real link rot. Treat them as
# warnings, not build-failing errors, so the weekly job isn't permanently/flakily red.
BLOCKED_STATUSES = {401, 403, 405, 429}

STALE_WARN_DAYS = 180
STALE_ERROR_DAYS = 365


def fetch_status(url, method):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=URL_TIMEOUT_SECONDS) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code


def classify_status(status):
    """Classify an HTTP status code as ("ok"|"warning"|"error", message-or-None)."""
    if 200 <= status < 400:
        return "ok", None
    if status in BLOCKED_STATUSES:
        return "warning", f"returned HTTP {status} (access blocked, may be bot-detection, not necessarily dead)"
    return "error", f"returned HTTP {status}"


def classify_staleness(age_days):
    """Classify a last_reviewed age in days as ("ok"|"warning"|"error")."""
    if age_days > STALE_ERROR_DAYS:
        return "error"
    if age_days > STALE_WARN_DAYS:
        return "warning"
    return "ok"


def check_urls(index):
    items = sorted(index.items())
    for i, (source_id, url) in enumerate(items):
        if i > 0:
            time.sleep(URL_CHECK_DELAY_SECONDS)
        try:
            status = fetch_status(url, "HEAD")
            if status in HEAD_FALLBACK_STATUSES:
                status = fetch_status(url, "GET")
            level, message = classify_status(status)
            print(f"  {source_id}: {status}{'' if level == 'ok' else f' ({level.upper()})'}")
            if level == "warning":
                warnings.append(f"{source_id} [{url}] {message}")
            elif level == "error":
                errors.append(f"{source_id} [{url}] {message}")
        except Exception as e:
            print(f"  {source_id}: ERROR ({e})")
            errors.append(f"{source_id} [{url}] request failed: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="fetch every registered source URL and fail on hard-dead responses (network required)",
    )
    args = parser.parse_args()

    index = json.loads((root / "SOURCE_INDEX.json").read_text())
    table_ids = set(re.findall(r"^\| `([A-Z0-9-]+)` \|", (root / "SOURCES.md").read_text(), re.M))

    if set(index) != table_ids:
        errors.append(
            f"SOURCE_INDEX.json and SOURCES.md disagree: only in index {sorted(set(index) - table_ids)}, "
            f"only in table {sorted(table_ids - set(index))}"
        )

    skill_files = sorted(root.glob("skills/*/SKILL.md"))

    used = set()
    for path in skill_files:
        unregistered = set()
        for cite in re.findall(r"\[([A-Z][A-Z0-9-]*-\d+)\]", path.read_text()):
            used.add(cite)
            if cite not in index:
                unregistered.add(cite)
        for cite in sorted(unregistered):
            errors.append(f"{path.relative_to(root)} cites unregistered ID [{cite}]")

    unused = sorted(set(index) - used)
    if unused:
        errors.append(f"registered but never cited: {unused}")

    today = datetime.date.today()
    for path in [root / "SOURCES.md", *skill_files]:
        match = re.search(r"^(?:last_reviewed|Last reviewed): (\d{4}-\d{2}-\d{2})$", path.read_text(), re.M)
        if not match:
            errors.append(f"{path.relative_to(root)} has no last_reviewed date")
            continue
        age = (today - datetime.date.fromisoformat(match.group(1))).days
        level = classify_staleness(age)
        if level == "error":
            errors.append(f"{path.relative_to(root)} last reviewed {age} days ago (>{STALE_ERROR_DAYS}); sources must be re-verified")
        elif level == "warning":
            warnings.append(f"{path.relative_to(root)} last reviewed {age} days ago; re-verify its sources")

    if args.check_urls:
        print(f"checking {len(index)} registered URLs...")
        check_urls(index)

    for warning in warnings:
        prefix = "::warning::" if os.environ.get("GITHUB_ACTIONS") else "WARNING: "
        print(f"{prefix}{warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)

    print(f"validated {len(used)} cited source IDs across {len(skill_files)} skills")


if __name__ == "__main__":
    main()
