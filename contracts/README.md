# contracts README

## Current status
No business API/event/queue/RPC contracts can be truthfully defined yet because this repository currently lacks business source/config/runtime evidence.

## Contract generation rule
Create `contracts/*.yaml` only when interfaces are supported by real repository evidence, for example:
- route handlers/controllers
- protobuf/openapi/graphql schemas
- queue/topic producers/consumers
- service-to-service message schemas

## Deferred contract backlog
- CONTRACT-BACKLOG-001: API boundary contracts (pending business backend code evidence)
- CONTRACT-BACKLOG-002: Data exchange contracts (pending integration code evidence)
- CONTRACT-BACKLOG-003: Async messaging contracts (pending queue/event infrastructure evidence)
