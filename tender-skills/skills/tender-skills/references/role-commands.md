# Role Commands

Use natural-language commands. The exact wording may vary by agent, but preserve the required output and update files.

## Business

### Register An Opportunity

Collect client background, project scope, timeline, budget signals, stakeholders, competitors, available sources, and immediate questions. Update `PROJECT.md`, `OPPORTUNITY.md`, and `OPEN-ITEMS.md`.

### Clarify Customer Needs

Convert each client statement into a traceable requirement. Capture priority, acceptance intent, source, ambiguity, and technical or cost impact. Update `REQUIREMENTS.md` and `OPEN-ITEMS.md`. Do not assess a level yet.

## Technical

### Assess Feasibility

For every evaluated requirement, state `可做`, `条件可做`, or `不可做`. List prerequisites, dependencies, implementation path, evidence, and risk. Update `FEASIBILITY.md`.

### Assess A Solution Level

Read `LEVEL-MODEL.md` first. Map feasible requirements to the configured level, explain the rationale, and identify upgrade or downgrade conditions. Update `LEVEL-ASSESSMENT.md`. Do not invent level definitions.

## Cost Control

### Estimate Solution Cost

Use the assessed level and stated technical path. Record resource assumptions, cost drivers, exclusions, sensitivity, and commercial boundary. Update `COST-BASELINE.md`. Mark an estimate provisional until its assumptions are confirmed.

## Bid Lead

### Make A Tender Decision

Review opportunity, feasibility, level assessment, cost baseline, and unresolved items. Choose `参与`, `不参与`, or `有条件参与`. Record conditions, owners, deadlines, and permitted external wording in `DECISIONS.md`.

## Shared

### Record A Decision

Record the decision, evidence, owner, date, impact, and follow-up. Update affected topic files before `DECISIONS.md`.

### Restore Project Context

Read the minimum context in the documented order. Return the current phase, hard boundaries, active role actions, unresolved blockers, and the next useful action.
