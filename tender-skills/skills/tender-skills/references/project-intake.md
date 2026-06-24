# New Project Intake

Use this protocol after the user has selected the installed `$tender-skills` in an AI client and expresses a new-project intent. The client controls slash-command menus and visual dialogs; provide the intake as concise conversational prompts when no form UI is available.

## First Reply

State that the project is entering `商机登记`. Ask only for this first batch:

1. 暂定项目名称与城市/区域
2. 甲方单位或客户类型
3. 想建设什么，服务哪个场景
4. 已知的投标/汇报/立项截止时间
5. 已有材料：招标文件、会议纪要、需求清单、图纸或其他资料

Accept partial answers. Do not ask for L1-L5, cost, or detailed technical architecture in the first batch unless the user volunteers them.

## Create the Project Center

After the first batch, ask for or confirm a project root directory. Create the project center only after that confirmation. Populate `PROJECT.md` from confirmed values and preserve unknown fields as `待确认`.

Create one `OPEN-ITEMS.md` entry for each material, deadline, owner, or decision that is not yet known. Set `CONTEXT.md` to the current phase and next actions.

## Second Reply

Report the created project location, confirmed project card fields, and the next smallest action. For a digital-twin modeling request, offer the next role choice:

- 商务：继续澄清甲方场景、范围和验收意图
- 技术：进入数字孪生需求采集与可行性评估
- 负责人：确认参与条件、责任人与推进节奏

Do not present a long questionnaire unless the user asks for a full form.
