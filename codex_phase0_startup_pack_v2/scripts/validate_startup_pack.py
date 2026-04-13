#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "AGENTS.md",
    ROOT / "planning" / "PLANS.md",
    ROOT / "prompts" / "phase0_prompt.md",
    ROOT / "schemas" / "output_schema_phase0.json",
    ROOT / "schemas" / "dev_plan.schema.json",
    ROOT / "schemas" / "acceptance_spec.schema.json",
    ROOT / "schemas" / "run_policy.schema.json",
    ROOT / "templates" / "spec.template.md",
    ROOT / "templates" / "dev_plan.template.yaml",
    ROOT / "templates" / "acceptance_spec.template.yaml",
    ROOT / "templates" / "run_policy.template.yaml",
    ROOT / "templates" / "implement.template.md",
    ROOT / "templates" / "documentation.template.md",
    ROOT / "templates" / "contracts" / "contract.template.yaml",
]

missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
if missing:
    print(json.dumps({"ok": False, "missing": missing}, ensure_ascii=False, indent=2))
    sys.exit(1)

print(json.dumps({"ok": True, "checked": [str(p.relative_to(ROOT)) for p in required]}, ensure_ascii=False, indent=2))
