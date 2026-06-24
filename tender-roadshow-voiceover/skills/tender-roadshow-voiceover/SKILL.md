---
name: tender-roadshow-voiceover
description: Generate professional Chinese narration audio for tender, bid, proposal, and client-demo roadshow materials. Use when an agent needs to turn an Excel script, narration table, or plain-text voiceover into a polished MP3 for 甲方, 评标专家, or project-presentation audiences, especially when the request emphasizes clear diction, standard speech rate, male presenter voice, line-by-line pauses, or consistent roadshow-quality audio style.
---

# Tender Roadshow Voiceover

Use this skill to produce repeatable, expert-facing Chinese roadshow narration audio.

## Workflow

1. Confirm the source. Accept either an `.xlsx` workbook with a narration column or a plain-text file with one narration line per paragraph or line.
2. Normalize the script before synthesis.
3. Synthesize with the default presentation profile.
4. Export a single final MP3 and verify it.

## Default Standard

Apply these defaults unless the user explicitly asks for a different tone or timing:

- Audience: client-side experts, evaluation committees, tender reviewers, formal demo listeners
- Tone: professional, reliable, composed, slightly presentational
- Delivery: standard Mandarin speed, articulate consonants, no exaggerated emotion
- Rhythm: each narration row should feel like one presentation beat
- Editing rule: prefer a slightly longer natural pause over rushed transitions
- Voice preference: male voice first for formal technical roadshows unless the user asks otherwise

Read [references/production-standard.md](references/production-standard.md) when you need the detailed quality bar or need to decide whether a user request should override the default profile.

## Command Path

Use the bundled script when you want a deterministic result:

```powershell
& "<bundled-python>" "<skill-root>/scripts/generate_voiceover.py" `
  --xlsx "<script.xlsx>" `
  --text-column "旁白文本" `
  --sheet "路演脚本拆解" `
  --output "<output.mp3>"
```

You may also use plain text:

```powershell
& "<bundled-python>" "<skill-root>/scripts/generate_voiceover.py" `
  --text-file "<voiceover.txt>" `
  --output "<output.mp3>"
```

## Deliverable

Return:

- the final MP3 link
- the measured duration
- one short sentence about the profile used
