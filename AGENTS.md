# Repository Guidelines

## Project Purpose

This repository publishes the `Tender-Skills` marketplace and three portable plugins: `tender-skills`, `tender-writing-spec`, and `tender-roadshow-voiceover`. Keep it focused on reusable agent skills, not the separate MVP web app.

## Structure

- `.claude-plugin/marketplace.json` is the marketplace entrypoint for remote installs.
- `.agents/plugins/marketplace.json` mirrors marketplace metadata for Codex-style local workflows.
- `tender-skills/.codex-plugin/plugin.json` and sibling plugin manifests define installable plugins.
- Each plugin keeps its portable skill under `skills/<skill-name>/` with optional `agents/`, `references/`, `scripts/`, and `assets/`.

## Editing Rules

Keep `SKILL.md` concise and trigger-focused. Put detailed process guidance in `references/`, deterministic helpers in `scripts/`, and reusable output materials in `assets/`.

Use lowercase hyphen-case for marketplace, plugin, and skill names. Preserve relative paths because marketplace installers depend on them exactly.

## Validation

Before publishing, check:

- both marketplace JSON files parse correctly
- each `plugin.json` uses valid semver
- every `SKILL.md` frontmatter includes only `name` and `description`
- all referenced relative paths exist
- Python helper scripts compile cleanly

Suggested local checks:

```bash
node -e "JSON.parse(require('fs').readFileSync('.claude-plugin/marketplace.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('tender-skills/.codex-plugin/plugin.json','utf8'))"
python -m py_compile tender-skills/skills/tender-skills/scripts/init_tender_project.py
```

## Pull Requests

Summarize changes in distribution terms: marketplace metadata, plugin manifest, skill behavior, or helper script behavior. For workflow changes, include one concrete trigger example such as `开始投标项目`, `Assess a solution level`, or `Generate a roadshow voiceover`.
