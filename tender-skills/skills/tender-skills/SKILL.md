---
name: tender-skills
description: Coordinate smart-city tender opportunity assessment across business, technical, cost-control, and bid-lead roles. Use when a team needs to record customer requirements, assess feasibility, assign configurable solution levels, estimate cost boundaries, make a bid or no-bid decision, or restore a tender project's shared context across Codex, Claude Code, Gemini CLI, or another file-capable agent.
---

# Tender Skills

Coordinate a tender project through a portable, file-based project center. Treat project files as the source of truth and do not rely on chat history as durable memory.

## Start Or Restore

1. Treat the skill as already installed and selected by the user's AI client.
2. Detect a new-project intent from prompts such as `开始投标项目` or `我想开始对某城市进行建模项目`.
3. For a new project, run the progressive intake in [references/project-intake.md](references/project-intake.md).
4. Confirm the project root, then create `.tender/` with `scripts/init_tender_project.py <project-root>`.
5. Write confirmed intake values to `.tender/PROJECT.md` and list unknown items in `.tender/OPEN-ITEMS.md`.
6. Read `.tender/PROJECT.md` and `.tender/CONTEXT.md` at the start of each later substantive session.
7. Read only the smallest role-specific files needed for the current task.
8. State the active role, the requested decision, and the missing evidence before giving a conclusion.

Read [references/document-center.md](references/document-center.md) before initializing a project, restoring context, or recording a session.

## Route By Role

Read [references/role-commands.md](references/role-commands.md) and route by role or clear intent:

| Role | Supported intents |
| --- | --- |
| Business | Register an opportunity; clarify customer needs |
| Technical | Assess feasibility; assess a solution level |
| Cost control | Estimate solution cost |
| Bid lead | Make a tender decision; resolve cross-role trade-offs |
| Any team member | Record a decision; restore project context |

If the role is not stated, infer it only when clear. Otherwise ask one focused question.

## Keep Evidence And Decisions Separate

1. Store customer statements, supplied files, and meeting facts as evidence with a source.
2. Store technical judgments, cost assumptions, and team choices as decisions with an owner and date.
3. Mark unknown items as `待确认`.
4. Mark a requirement `不可做` or `条件可做` when the evidence warrants it.
5. Require technical feasibility and cost impact before confirming an external proposal level or price commitment.

## Treat Solution Levels As Configurable

Do not assume what `L1` through `L5` mean, their order, or their price multiplier. Read `.tender/LEVEL-MODEL.md` before assessing a level. If it is not configured, collect the team's definitions before assigning one.

Read [references/level-model.md](references/level-model.md) when creating or reviewing a level model.

## Close Every Substantive Turn

1. Update the relevant `.tender/` topic file with new evidence, conclusions, or open items.
2. Add a concise record to `.tender/SESSIONS/`.
3. Refresh `.tender/CONTEXT.md` with the current phase, hard boundaries, latest decisions, role-specific next actions, and pointers to detail.
4. Report confirmed items, unresolved items, changed files, and the smallest useful next action.

If the active agent cannot modify files, return exact proposed changes and explicitly state that the project center was not updated.
