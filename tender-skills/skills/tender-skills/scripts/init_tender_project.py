#!/usr/bin/env python3
"""Create the portable .tender document center for one tender project."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "PROJECT.md": "# 项目卡\n\n| 字段 | 内容 |\n| --- | --- |\n| 项目名称 | 待确认 |\n| 城市/区域 | 待确认 |\n| 甲方单位/客户类型 | 待确认 |\n| 建设场景与目标 | 待确认 |\n| 当前阶段 | 商机登记 |\n| 投标/汇报/立项截止时间 | 待确认 |\n| 已有材料 | 待确认 |\n| 投标负责人 | 待确认 |\n| 最后更新 | 待确认 |\n",
    "CONTEXT.md": "# 项目上下文\n\n- 当前阶段：商机登记\n- 硬性边界：待确认\n- 最近决策：无\n- 高优先级待办：完善商机与客户需求\n- 详情索引：见 OPPORTUNITY.md、REQUIREMENTS.md、OPEN-ITEMS.md\n",
    "OPPORTUNITY.md": "# 商机\n\n| ID | 状态 | 内容 | 来源 | 负责人 | 影响范围 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "REQUIREMENTS.md": "# 客户需求\n\n| ID | 状态 | 内容 | 来源 | 负责人 | 影响范围 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "FEASIBILITY.md": "# 技术可行性\n\n| ID | 状态 | 结论 | 前置条件/风险 | 来源 | 负责人 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "LEVEL-MODEL.md": "# 方案等级模型\n\n> 在此定义团队的等级含义与排序规则；不要假定 L1-L5 的通用含义。\n",
    "LEVEL-ASSESSMENT.md": "# 方案等级评估\n\n| ID | 状态 | 关联需求 | 建议等级 | 理由 | 升级/降级条件 | 负责人 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "COST-BASELINE.md": "# 成本基线\n\n| ID | 状态 | 成本项/假设 | 关联等级 | 敏感项 | 负责人 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "DECISIONS.md": "# 决策日志\n\n| ID | 状态 | 决策 | 依据 | 责任人 | 影响范围 | 日期 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
    "OPEN-ITEMS.md": "# 待办与风险\n\n| ID | 状态 | 事项 | 所需输入 | 责任人 | 截止时间 | 最后更新 |\n| --- | --- | --- | --- | --- | --- | --- |\n",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path, help="Tender project root directory")
    args = parser.parse_args()

    project_root = args.project_root.expanduser().resolve()
    tender_dir = project_root / ".tender"
    tender_dir.mkdir(parents=True, exist_ok=True)
    (tender_dir / "SESSIONS").mkdir(exist_ok=True)
    (project_root / "sources").mkdir(parents=True, exist_ok=True)
    (project_root / "deliverables").mkdir(parents=True, exist_ok=True)

    created = []
    for filename, content in FILES.items():
      path = tender_dir / filename
      if not path.exists():
        path.write_text(content, encoding="utf-8")
        created.append(path.name)

    display_path = str(tender_dir).encode("ascii", "backslashreplace").decode("ascii")
    print(f"Project center: {display_path}")
    print("Created: " + (", ".join(created) if created else "none (existing files preserved)"))


if __name__ == "__main__":
    main()
