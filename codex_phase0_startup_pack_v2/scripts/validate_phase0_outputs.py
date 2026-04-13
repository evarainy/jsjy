#!/usr/bin/env python3
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path.cwd()

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))

required_files = [
    ROOT / "spec.md",
    ROOT / "dev_plan.yaml",
    ROOT / "acceptance_spec.yaml",
    ROOT / "run_policy.yaml",
    ROOT / "implement.md",
    ROOT / "documentation.md",
    ROOT / "phase0_result.json",
]

missing = [str(p) for p in required_files if not p.exists()]
if missing:
    print(json.dumps({"ok": False, "missing_output_files": missing}, ensure_ascii=False, indent=2))
    sys.exit(1)

schema_dir = ROOT / "schemas"
schemas = {
    "dev_plan.yaml": load_json(schema_dir / "dev_plan.schema.json"),
    "acceptance_spec.yaml": load_json(schema_dir / "acceptance_spec.schema.json"),
    "run_policy.yaml": load_json(schema_dir / "run_policy.schema.json"),
    "phase0_result.json": load_json(schema_dir / "output_schema_phase0.json"),
}

docs = {
    "dev_plan.yaml": load_yaml(ROOT / "dev_plan.yaml"),
    "acceptance_spec.yaml": load_yaml(ROOT / "acceptance_spec.yaml"),
    "run_policy.yaml": load_yaml(ROOT / "run_policy.yaml"),
    "phase0_result.json": load_json(ROOT / "phase0_result.json"),
}

errors = {}
for name, schema in schemas.items():
    validator = Draft202012Validator(schema)
    current = docs[name]
    errs = sorted(validator.iter_errors(current), key=lambda e: list(e.absolute_path))
    if errs:
        errors[name] = [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in errs]

# Cross-link checks
if "dev_plan.yaml" not in errors and "acceptance_spec.yaml" not in errors:
    task_ids = {task["id"] for task in docs["dev_plan.yaml"]["tasks"]}
    acceptance_ids = {item["id"] for item in docs["acceptance_spec.yaml"]["acceptance"]}
    unknown_acceptance_refs = {}
    for task in docs["dev_plan.yaml"]["tasks"]:
        bad = [aid for aid in task["acceptance_ids"] if aid not in acceptance_ids]
        if bad:
            unknown_acceptance_refs[task["id"]] = bad
    if unknown_acceptance_refs:
        errors["cross_links"] = [f"{task}: unknown acceptance ids {bad}" for task, bad in unknown_acceptance_refs.items()]

result = {"ok": not bool(errors), "errors": errors}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if result["ok"] else 1)
