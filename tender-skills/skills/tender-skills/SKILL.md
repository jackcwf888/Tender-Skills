---
name: tender-skills
description: Coordinate smart-city tender opportunity assessment across business, technical, cost-control, and bid-lead roles. Use when a team needs to record customer requirements, assess feasibility, assign configurable solution levels, estimate cost boundaries, make a bid/no-bid decision, or restore a tender project's shared context across Codex, Claude Code, Gemini CLI, or another file-capable agent.
---

# Tender Skills

Coordinate a tender project through a portable, file-based project center. Treat the project files as the source of truth; do not rely on chat history as durable memory.

## Start or Restore

1. Treat the Skill as already installed and selected by the user's AI client. Do not explain or attempt client-side installation during project work.
2. Detect a new-project intent from prompts such as `开始投标项目` or `我想开始对某城市进行建模项目`.
3. For a new project, run the progressive intake in [references/project-intake.md](references/project-intake.md). Collect the minimum project card before asking technical or cost questions.
4. Confirm the project root with the user, then create `.tender/` with `scripts/init_tender_project.py <project-root>`.
5. Write confirmed intake values to `.tender/PROJECT.md` and list missing items in `.tender/OPEN-ITEMS.md`.
6. Read `.tender/PROJECT.md` and `.tender/CONTEXT.md` at the start of every later substantive session.
7. Read only the role-specific files required for the task. Do not load all session history by default.
8. State the active role, the requested decision, and the missing evidence before giving a conclusion.

Read [references/document-center.md](references/document-center.md) before initializing a project, restoring context, or recording a session.

## Route By Role

Use the user's role or intent to select the workflow below. Read [references/role-commands.md](references/role-commands.md) for required inputs, files, and outputs.

| Role | Supported intents |
| --- | --- |
| Business | Register an opportunity; clarify customer needs |
| Technical | Assess feasibility; assess a solution level |
| Cost control | Estimate solution cost |
| Bid lead | Make a tender decision; resolve cross-role trade-offs |
| Any team member | Record a decision; restore project context |

If the role is not stated, infer it only when clear; otherwise ask one focused question.

## Keep Evidence and Decisions Separate

1. Store customer statements, documents, and supplied facts as evidence with a source.
2. Store technical judgments, cost assumptions, and team choices as decisions with an owner and date.
3. Mark unknown items as `待确认`; never turn an assumption into a client commitment.
4. Mark a requirement `不可做` or `条件可做` when the evidence warrants it. Do not soften the conclusion to make a bid appear viable.
5. Require technical feasibility and cost impact before confirming a proposal level or external price commitment.

## Treat Solution Levels as Configurable

Do not assume what `L1` through `L5` mean, their order, or their price multiplier. Read `.tender/LEVEL-MODEL.md` before assessing a level. If it is not configured, collect the team's definitions before assigning one.

Read [references/level-model.md](references/level-model.md) when creating or reviewing a level model.

## Close Every Substantive Turn

1. Update the relevant `.tender/` topic file with new evidence, conclusions, or open items.
2. Add a concise record to `.tender/SESSIONS/`.
3. Refresh `.tender/CONTEXT.md` with current phase, hard boundaries, latest decisions, role-specific next actions, and pointers to detail. Keep it below 2,000 Chinese characters unless the project requires otherwise.
4. Report: confirmed items, unresolved items, changed files, and the smallest useful next action.

If the active agent cannot modify files, return exact proposed changes and explicitly state that the project center was not updated.
