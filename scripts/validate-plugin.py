#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path


def duplicates(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def normalize_plugin_paths(paths: list[str]) -> tuple[list[str], list[str]]:
    names = []
    errors = []
    for raw_path in paths:
        if not isinstance(raw_path, str):
            errors.append(f"plugin skill path is not a string: {raw_path!r}")
            continue
        path = Path(raw_path)
        if path.is_absolute() or len(path.parts) != 2 or path.parts[0] != "skills":
            errors.append(f"invalid plugin skill path: {raw_path}")
            continue
        names.append(path.parts[1])
    return names, errors


def registry_errors(
    actual_names: list[str], plugin_paths: list[str], manifest_names: list[str]
) -> list[str]:
    plugin_names, errors = normalize_plugin_paths(plugin_paths)
    expected = sorted(actual_names)

    duplicate_plugin_names = duplicates(plugin_names)
    if duplicate_plugin_names:
        errors.append("duplicate plugin skills: " + ", ".join(duplicate_plugin_names))

    duplicate_manifest_names = duplicates(manifest_names)
    if duplicate_manifest_names:
        errors.append("duplicate manifest skills: " + ", ".join(duplicate_manifest_names))

    if plugin_names != expected:
        errors.append(f"plugin skills {plugin_names} do not match actual skills {expected}")
    if manifest_names != expected:
        errors.append(f"manifest skills {manifest_names} do not match actual skills {expected}")
    return errors


root = Path(__file__).resolve().parents[1]
plugin = json.loads((root / ".claude-plugin" / "plugin.json").read_text())
skills = plugin.get("skills", [])
manifest = json.loads((root / "manifest.json").read_text())
manifest_skills = manifest.get("skills", [])
actual_skills = sorted(path.parent.name for path in root.glob("skills/*/SKILL.md"))

errors = registry_errors(actual_skills, skills, manifest_skills)
if errors:
    raise SystemExit("Skill registry mismatch: " + "; ".join(errors))

missing = [skill for skill in skills if not (root / skill / "SKILL.md").is_file()]
if missing:
    raise SystemExit("Missing plugin skill paths: " + ", ".join(missing))

for skill in skills:
    path = root / skill
    name_line = next(
        (line for line in (path / "SKILL.md").read_text().splitlines() if line.startswith("name: ")),
        None,
    )
    if name_line != f"name: {path.name}":
        raise SystemExit(f"Skill name does not match its directory: {path}")

guardrail_ref = "../00-blog-writing-guardrails/SKILL.md"
missing_ref = [
    skill for skill in skills
    if Path(skill).name != "00-blog-writing-guardrails"
    and guardrail_ref not in (root / skill / "SKILL.md").read_text()
]
if missing_ref:
    raise SystemExit("Skills missing the guardrails dependency: " + ", ".join(missing_ref))

if manifest.get("skill_count") != len(actual_skills):
    raise SystemExit(f"manifest.json skill_count is {manifest.get('skill_count')}, repo has {len(actual_skills)}")

source_index = json.loads((root / "SOURCE_INDEX.json").read_text())
if manifest.get("source_count") != len(source_index):
    raise SystemExit(f"manifest.json source_count is {manifest.get('source_count')}, registry has {len(source_index)}")

duplicate_urls = duplicates(list(source_index.values()))
if duplicate_urls:
    details = [
        f"{url} ({', '.join(sorted(sid for sid, u in source_index.items() if u == url))})"
        for url in duplicate_urls
    ]
    raise SystemExit("SOURCE_INDEX.json has duplicate URLs under multiple IDs: " + "; ".join(details))

print(f"validated {len(skills)} plugin skill paths")
