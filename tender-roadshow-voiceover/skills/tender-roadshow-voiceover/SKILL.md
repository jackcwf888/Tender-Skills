---
name: tender-roadshow-voiceover
description: Generate professional Chinese narration audio for tender, bid, proposal, and client-demo roadshow materials. Use when Codex needs to turn an Excel script, narration table, or plain-text voiceover into a polished MP3 for甲方/评标专家/项目汇报 audiences, especially when the request emphasizes clear diction, standard speech rate, male presenter voice, line-by-line pauses, or consistent roadshow-quality audio style.
---

# Tender Roadshow Voiceover

Use this skill to produce repeatable, expert-facing Chinese roadshow narration audio.

Default target:
- sound like a formal project presenter, not an ad read
- prioritize clear diction and steady phrasing over dramatic speed
- keep a natural pause between script lines so screen transitions can breathe
- prefer stable, professional Mainland Chinese male voices for bid demos

## Workflow

1. Confirm the source.
   Accept either:
   - an `.xlsx` workbook with a narration column such as `旁白文本`
   - a plain-text file with one narration line per paragraph or line

2. Normalize the script before synthesis.
   - Remove empty rows.
   - Preserve sentence punctuation.
   - Convert embedded line breaks inside one narration row into a spoken pause marker such as `，`.
   - Keep one logical roadshow sentence group per row whenever possible.

3. Synthesize with the default presentation profile.
   - Voice: `zh-CN-YunyangNeural`
   - Rate: `+0%`
   - Pitch: `-1Hz`
   - Volume: `+0%`
   - Inter-line pause: about `650ms`

4. Export a single final MP3 and verify it.
   - Check that the output file exists.
   - Confirm codec, duration, and bitrate with `ffprobe`.
   - Report the final path and measured duration.

## Default Standard

Apply these defaults unless the user explicitly asks for a different tone or timing:

- Audience: client-side experts, evaluation committees, tender reviewers, formal demo listeners
- Tone: professional, reliable, composed, slightly presentational
- Delivery: standard Mandarin speed, articulate consonants, no exaggerated emotion
- Rhythm: each narration row should feel like one presentation beat
- Editing rule: prefer a slightly longer natural pause over rushed transitions
- Voice preference: male voice first for formal technical roadshows unless the user asks otherwise

Read [production-standard.md](references/production-standard.md) when you need the detailed quality bar or need to decide whether a user request should override the default profile.

## Command Path

Use the bundled script when you want a deterministic result:

```powershell
& "<bundled-python>" "C:\Users\jackc\.codex\skills\tender-roadshow-voiceover\scripts\generate_voiceover.py" `
  --xlsx "<script.xlsx>" `
  --text-column "旁白文本" `
  --sheet "路演脚本拆解" `
  --output "<output.mp3>"
```

You may also use plain text:

```powershell
& "<bundled-python>" "C:\Users\jackc\.codex\skills\tender-roadshow-voiceover\scripts\generate_voiceover.py" `
  --text-file "<voiceover.txt>" `
  --output "<output.mp3>"
```

## Override Rules

Allow user overrides only when explicitly requested:
- voice gender or named voice
- faster or slower rate
- tighter or looser inter-line pause
- target duration alignment
- stronger emotion or softer tone

When a user asks for aggressive time compression, warn yourself that intelligibility for tender experts matters more than hitting an arbitrary number exactly. Prefer negotiating pauses and moderate rate changes before pushing the voice into unnatural speed.

## Deliverable

Return:
- the final MP3 link
- the measured duration
- one short sentence about the profile used, such as `standard male roadshow voice with clear diction and line pauses`

Do not narrate internal tooling details unless the user asks.
