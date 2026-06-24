# New Project Intake

Use this protocol after the user has selected `$tender-skills` in an AI client and expresses a new-project intent.

## First Reply

State that the project is entering `商机登记`. Ask only for this first batch:

1. Temporary project name and city or region
2. Client organization or customer type
3. What should be built and which scenario it serves
4. Known tender, presentation, or approval deadline
5. Available materials such as tender files, meeting notes, requirement lists, drawings, or other source files

Accept partial answers. Do not ask for L1 to L5, cost, or detailed technical architecture in the first batch unless the user volunteers them.

## Create The Project Center

After the first batch, ask for or confirm a project root directory. Create the project center only after that confirmation. Populate `PROJECT.md` from confirmed values and preserve unknown fields as `待确认`.

Create one `OPEN-ITEMS.md` entry for each missing material, deadline, owner, or decision. Set `CONTEXT.md` to the current phase and next actions.

## Second Reply

Report the created project location, confirmed project-card fields, and the next smallest action. For a digital-twin modeling request, offer the next role choice:

- Business: clarify customer scenario, scope, and acceptance intent
- Technical: enter digital-twin requirement intake and feasibility assessment
- Bid lead: confirm participation conditions, owners, and推进节奏

Do not present a long questionnaire unless the user asks for a full form.
