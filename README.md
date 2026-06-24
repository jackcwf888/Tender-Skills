# Tender Skills

Portable tender workflow skills for smart-city and digital-twin bidding teams.

This repository is published as a multi-plugin marketplace. It is designed for:

- `Codex CLI`
- `Claude Code`
- `Gemini CLI`
- future Chinese domestic agent CLIs that can read local skill folders

The repository keeps one marketplace and three focused plugins instead of one oversized skill.

## Included Plugins

- `tender-skills`
  Coordinates opportunity intake, requirement capture, level assessment, feasibility review, and `.tender/` project memory.
- `tender-writing-spec`
  Drafts or revises formal tender content while preserving scope, procurement boundaries, and document structure.
- `tender-roadshow-voiceover`
  Converts narration sheets or plain-text scripts into professional Chinese MP3 roadshow audio.

## Repository Layout

```text
Tender-Skills/
├─ .claude-plugin/marketplace.json
├─ .agents/plugins/marketplace.json
├─ tender-skills/
│  ├─ .codex-plugin/plugin.json
│  └─ skills/tender-skills/
├─ tender-writing-spec/
│  ├─ .codex-plugin/plugin.json
│  └─ skills/tender-writing-spec/
└─ tender-roadshow-voiceover/
   ├─ .codex-plugin/plugin.json
   └─ skills/tender-roadshow-voiceover/
```

## Install

### Codex CLI

```bash
codex plugin marketplace add jackcwf888/Tender-Skills
codex plugin add tender-skills@tender-skills
codex plugin add tender-writing-spec@tender-skills
codex plugin add tender-roadshow-voiceover@tender-skills
```

### Claude Code

If your Claude Code build exposes marketplace commands, use the equivalent flow:

```bash
claude plugin marketplace add jackcwf888/Tender-Skills
claude plugin add tender-skills@tender-skills
claude plugin add tender-writing-spec@tender-skills
claude plugin add tender-roadshow-voiceover@tender-skills
```

### Gemini CLI And Other Agent CLIs

If a tool does not support plugin marketplaces, copy one or more portable skill folders into that tool's local skill or prompt library:

```text
tender-skills/skills/tender-skills/
tender-writing-spec/skills/tender-writing-spec/
tender-roadshow-voiceover/skills/tender-roadshow-voiceover/
```

These skills are intentionally file-based. They rely on:

- `SKILL.md` instructions
- Markdown references under `references/`
- optional helper scripts under `scripts/`

That makes them easier to reuse across different local agent runtimes.

## Compatibility Notes

- `tender-skills` is the main project-memory and decision skill.
- `tender-writing-spec` should usually be used after project scope and feasibility are already clarified.
- `tender-roadshow-voiceover` depends on Python plus `openpyxl`, `edge-tts`, `ffmpeg`, and `ffprobe` in the target environment.

## Development

Suggested local checks before publishing:

```bash
node -e "JSON.parse(require('fs').readFileSync('.claude-plugin/marketplace.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('.agents/plugins/marketplace.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('tender-skills/.codex-plugin/plugin.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('tender-writing-spec/.codex-plugin/plugin.json','utf8'))"
node -e "JSON.parse(require('fs').readFileSync('tender-roadshow-voiceover/.codex-plugin/plugin.json','utf8'))"
python -m py_compile tender-skills/skills/tender-skills/scripts/init_tender_project.py
python -m py_compile tender-roadshow-voiceover/skills/tender-roadshow-voiceover/scripts/generate_voiceover.py
```

## Scope Boundary

This repository publishes reusable skills and marketplace metadata. The separate Tender Skills MVP web application, database, Docker deployment, and production server operations should remain in a different repository.
