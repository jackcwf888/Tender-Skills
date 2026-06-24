---
name: tender-writing-spec
description: Write, expand, and revise bid/tender technical documents, implementation plans, AI module sections, proposal narratives, and response text that must stay consistent with project scope, procurement boundaries, and the original document structure/style. Use when working on tender documents,标书技术实现,投标方案,AI辅助决策方案,采购清单配套说明, or Word-based bid content that requires formal business tone, section-level continuation, and strict consistency with existing quotations and architecture assumptions.
---

# Tender Writing Spec

## Overview

Use this skill to draft or revise tender text that must be credible, implementable, and internally consistent with the project's pricing, procurement scope, delivery boundary, and existing document framework.

Read the target document and any reference document first. Reuse the target document's structure and terminology. Add or revise content locally instead of rewriting entire chapters unless the user explicitly asks for a rewrite.

## Workflow

1. Read the target tender document, identify the exact chapter, existing headings, nearby paragraphs, and insertion boundary.
2. Read any reference documents only to learn writing pattern, granularity, and section organization. Do not copy business background or irrelevant solution details.
3. Read the latest confirmed quotation, procurement list, architecture boundary, deployment assumption, and operation period before writing.
4. Write only the requested section. Keep the surrounding numbering, chapter order, and heading hierarchy unchanged.
5. If editing a `.docx`, preserve the original font, size, paragraph style, and layout. Insert content after the specified anchor unless asked to replace.
6. Recheck consistency after writing: product names, deployment mode, purchased services, time span, roles, interfaces, and cost boundary must align.

## Writing Rules

- Write in formal tender language: objective, implementation-oriented, and defensible.
- Prefer concrete capability statements over slogans. Explain what the system does, how it works, what it connects to, and what management value it brings.
- Keep wording moderate. Avoid exaggerated claims such as "fully autonomous", "zero error", or unverifiable performance commitments unless they are explicitly provided by the user or source material.
- Match the document's existing naming. If the document uses `AI辅助决策系统`, do not casually switch to unrelated productized labels.
- Use complete, business-ready paragraphs. Avoid outline fragments unless the surrounding chapter already uses short bullet items.
- When expanding a subsection, keep the same granularity as adjacent sections. Do not make one capability overly detailed while leaving sibling sections thin unless the user explicitly wants that emphasis.

## Scope Alignment Rules

- Keep all technical text consistent with the latest confirmed procurement scope.
- Do not introduce heavy local hardware, self-built model clusters, or extra platforms when the confirmed方案 is lightweight cloud services plus existing business systems.
- Distinguish clearly between `本项目建设内容`, `对接既有系统`, and `复用甲方既有能力`.
- If the project already has an Agent system, write the AI capability around model service, knowledge base, voice service, orchestration, and integration rather than rebuilding a full agent platform from zero.
- If a capability is based on third-party or existing subsystem output, write it as `对接结果接入/联动应用`, not as newly self-developed core algorithm capability.
- Keep the deployment boundary explicit: what is deployed in the project application layer, what is procured from the cloud, and what remains outside the bid scope.

## AI Module Rules

When writing AI-related tender content, anchor the text around five dimensions:

1. Entry and interaction: how users trigger the capability from large screen, medium screen, mobile, or management backend.
2. Recognition and reasoning: how speech, text, data, or event input is parsed into intent, query, judgment, or workflow action.
3. Business linkage: which data base, digital twin, video platform, or business subsystem is called.
4. Result feedback: what the user sees, hears, confirms, exports, or dispatches after processing.
5. Governance and safety: permission control, audit trail, confirmation mechanism, operation record, and model optimization loop.

For smart-city and IOC scenarios, prefer language such as:

- `辅助决策`, `智能研判`, `联动查询`, `异常识别与归因`, `流程触发`, `结果回显`, `指令确认`, `审计留痕`

Avoid drifting into generic internet-product wording that sounds detached from exhibition venue, command center, or operations management.

## DOCX Edit Rules

- Preserve existing content unless the user asks for replacement or rewrite.
- Insert after the precise anchor paragraph or heading named by the user.
- Back up the original file before substantial edits.
- If the target file is open and locked by Word, use Word's own editing path rather than forcing filesystem overwrite.
- After editing, verify that the new content sits in the correct location and that nearby headings did not inherit wrong styles.

## Consistency Check

Before finishing, verify:

- Chapter position is correct.
- Original content remains intact.
- New text matches nearby font/style conventions.
- Terminology is consistent with the tender and quotation.
- Procurement and deployment boundaries are not contradicted.
- The written capability can be defended in a bid review meeting.

Read [references/checklist.md](references/checklist.md) when you need a fast pre-delivery review checklist for tender writing or document insertion tasks.
