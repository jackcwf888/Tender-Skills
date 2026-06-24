---
name: tender-writing-spec
description: Write, expand, and revise bid or tender technical documents, implementation plans, AI module sections, proposal narratives, and response text that must stay consistent with project scope, procurement boundaries, and the original document structure and style. Use when working on tender documents, 标书技术实现, 投标方案, AI 辅助决策方案, 采购清单配套说明, or Word-based bid content that requires formal business tone, section-level continuation, and strict consistency with existing quotations and architecture assumptions.
---

# Tender Writing Spec

Use this skill to draft or revise tender text that must be credible, implementable, and internally consistent with the project's pricing, procurement scope, delivery boundary, and existing document framework.

## Workflow

1. Read the target tender document and identify the exact chapter, existing headings, nearby paragraphs, and insertion boundary.
2. Read any reference documents only to learn the writing pattern, granularity, and section organization.
3. Read the latest confirmed quotation, procurement list, architecture boundary, deployment assumption, and operation period before writing.
4. Write only the requested section. Keep the surrounding numbering, chapter order, and heading hierarchy unchanged.
5. If editing a `.docx`, preserve the original font, size, paragraph style, and layout.
6. Recheck consistency after writing: product names, deployment mode, purchased services, time span, roles, interfaces, and cost boundary must align.

## Writing Rules

- Write in formal tender language: objective, implementation-oriented, and defensible.
- Prefer concrete capability statements over slogans.
- Keep wording moderate and avoid exaggerated claims unless they are explicitly provided by the user or source material.
- Match the document's existing naming and surrounding granularity.
- Use complete, business-ready paragraphs unless the surrounding chapter already uses short bullet items.

## Scope Alignment Rules

- Keep all technical text consistent with the latest confirmed procurement scope.
- Do not introduce heavy local hardware, self-built model clusters, or extra platforms when the confirmed solution is lightweight cloud services plus existing business systems.
- Distinguish clearly between project-built content, connected existing systems, and reused client-side capabilities.
- Keep the deployment boundary explicit.

## AI Module Rules

When writing AI-related tender content, anchor the text around:

1. Entry and interaction
2. Recognition and reasoning
3. Business linkage
4. Result feedback
5. Governance and safety

## DOCX Edit Rules

- Preserve existing content unless the user asks for replacement or rewrite.
- Insert after the precise anchor paragraph or heading named by the user.
- Back up the original file before substantial edits.
- Verify the new content sits in the correct location and that nearby headings did not inherit the wrong style.

Read [references/checklist.md](references/checklist.md) when you need a fast pre-delivery review checklist for tender writing or document insertion tasks.
