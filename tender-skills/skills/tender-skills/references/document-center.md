# Tender Project Document Center

Use `.tender/` inside each tender project root. Keep it portable: UTF-8 Markdown files, ordinary folders, and no vendor-specific database.

```text
project-root/
├─ .tender/
│  ├─ PROJECT.md
│  ├─ CONTEXT.md
│  ├─ OPPORTUNITY.md
│  ├─ REQUIREMENTS.md
│  ├─ FEASIBILITY.md
│  ├─ LEVEL-MODEL.md
│  ├─ LEVEL-ASSESSMENT.md
│  ├─ COST-BASELINE.md
│  ├─ DECISIONS.md
│  ├─ OPEN-ITEMS.md
│  └─ SESSIONS/
├─ sources/
└─ deliverables/
```

## Read Order

Read `PROJECT.md` and `CONTEXT.md` first. Then choose the smallest relevant topic file:

| Intent | Read |
| --- | --- |
| Business intake | `OPPORTUNITY.md`, `REQUIREMENTS.md`, `OPEN-ITEMS.md` |
| Technical assessment | `REQUIREMENTS.md`, `FEASIBILITY.md`, `LEVEL-MODEL.md`, `LEVEL-ASSESSMENT.md` |
| Cost assessment | `LEVEL-ASSESSMENT.md`, `COST-BASELINE.md`, `DECISIONS.md` |
| Leadership decision | `OPPORTUNITY.md`, `FEASIBILITY.md`, `LEVEL-ASSESSMENT.md`, `COST-BASELINE.md`, `OPEN-ITEMS.md` |

Read source files only to verify a specific claim. Keep source locations in the topic files.

## Record Format

Use a stable ID, status, source, owner, impact, and update date for material records. Use the statuses `已确认`, `待确认`, `风险`, `不适用`, and `已完成`.

```markdown
| ID | 状态 | 内容 | 来源 | 负责人 | 影响范围 | 最后更新 |
| --- | --- | --- | --- | --- | --- | --- |
| RQ-001 | 待确认 | ... | 甲方会议纪要 2026-06-23 | 商务 | 技术/成本 | 2026-06-23 |
```

Do not duplicate full detail in `CONTEXT.md`. Use it as a concise navigation and handoff summary.
