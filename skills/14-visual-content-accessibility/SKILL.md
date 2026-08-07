---
name: 14-visual-content-accessibility
description: Guidance for images, diagrams, and embedded video/audio in blog posts — when a visual earns its place, alt text quality, captioning, color contrast, and accessible transcripts. Apply when adding or reviewing any non-text media in a blog post.
version: 1.0.0
last_reviewed: 2026-08-07
---

# Visual Content and Media Accessibility

Apply `../00-blog-writing-guardrails/SKILL.md` first; its accessibility gate is a hard prerequisite. This skill gives the concrete authoring rules that satisfy that gate for images, diagrams, and embedded video/audio.

## 1. Does the visual earn its place?
- Add an image, diagram, or embed only when it conveys meaning the surrounding text cannot as efficiently — a screenshot showing an actual state, a diagram showing a relationship, a chart showing a trend; do not add stock imagery purely for visual break-up, since it still needs an accessibility treatment (alt text or explicit decorative marking) and adds no reader value. [W3C-WCAG-01]
- If a graphic or diagram carries information required to understand the post (a flow, a comparison, a labeled chart), also state that information in the surrounding text or a caption so a reader who cannot perceive the graphic is not missing content. [W3C-IMGALT-01]

## 2. Alt text quality gate (not just presence)
- Classify every image before writing its alt text, using the applicable case: informative (the image conveys a message — write alt text that conveys that same message, not a literal visual description), decorative (the image adds no information — use an empty `alt=""` so assistive technology skips it), or functional (the image is inside a link or button — the alt text must describe the destination or action, not the image's appearance). [W3C-IMGALT-01][W3C-WCAG-01]
- For a complex image (a chart, graph, or diagram whose content cannot fit in a short alt attribute), keep the alt attribute short and put the full data or explanation in adjacent text, a table, or a long description linked from the image — never leave the underlying data reachable only through the image. [W3C-IMGALT-01]
- An alt attribute that restates the filename, says only "image" or "graphic," or describes the image's visual style instead of its meaning fails this gate even though the attribute is technically present. [W3C-IMGALT-01]

## 3. Color and contrast gate
- Body text and text rendered inside images must reach a contrast ratio of at least 4.5:1 against its background; large text (18pt+, or 14pt+ bold) may drop to 3:1. [W3C-CONTRAST-01]
- Lines, icons, chart segments, and other non-text graphical elements that are required to understand a diagram or chart must reach a contrast ratio of at least 3:1 against adjacent colors, unless the specific coloring itself is the essential information being shown (a screenshot, a photo, a brand logo). [W3C-NONTEXTCONTRAST-01]
- Do not use color as the only way to distinguish data series, states, or callouts (e.g., "the red line" or "the green box"); pair color with a label, pattern, or icon so the distinction survives grayscale or color-vision deficiency. [W3C-WCAG-01]

## 4. Embedded video and audio gate
- Provide a synchronized text caption for every prerecorded video that has a soundtrack, covering both dialogue and non-speech audio information (sound effects, music cues, speaker identification) needed to follow the content. [W3C-CAPTIONS-01]
- Provide a transcript for every embedded audio-only or video piece — the transcript is the text equivalent of the full speech and non-speech audio content, and it also makes the media's content indexable and skimmable on the page itself. [W3C-MEDIA-01]
- For prerecorded video where meaningful visual information (on-screen actions, text, scene changes) is not already conveyed by the audio track, provide audio description — either narrated in pauses in the existing dialogue or as an alternative track — or ensure the same information is available in the surrounding post text. [W3C-AUDIODESC-01]
- Plan captions, transcripts, and audio description during scripting, not as a post-publish afterthought; embedding the description into the primary audio track at production time is easier than retrofitting a separate track later. [W3C-MEDIA-01]

## 5. Pre-publish checklist for this skill
- Every image has alt text classified and written per Section 2, or is explicitly marked decorative.
- Every complex chart/diagram's data also appears in surrounding text, a table, or a linked long description.
- Text and meaningful non-text graphics pass the contrast ratios in Section 3.
- No information is conveyed by color alone.
- Every embedded video has captions; every audio-only or video embed has a transcript; video with unnarrated meaningful visuals has audio description or equivalent text coverage.
