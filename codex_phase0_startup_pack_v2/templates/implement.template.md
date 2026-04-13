# implement.md

## Execution principles
- Commander owns orchestration, git integration, and final merge gates.
- Task agents own bounded code changes, local verification, and structured result output.
- DB migrations are generated in tasks but applied only during integration.
- Use unique ports, env files, and temp directories per worktree.

## Per-task contract
Each task should:
1. read the relevant plan, acceptance items, and contracts
2. stay inside `touched_paths`
3. avoid `forbidden_paths`
4. run listed verification commands
5. write declared evidence artifacts
6. return a structured result

## Structured task result
At minimum, record:
- task_id
- status
- changed_files
- tests_run
- evidence_paths
- blockers
- next_action

## Subagent rule
Use subagents only for bounded jobs with a clear return format.
