## Roadmap

The DeepAgentLabs MCP Server roadmap focuses on expanding a unified MCP interface across the DeepAgentLabs ecosystem.

### Current Release

**Version:** `0.2.0`

**Released:** August 8, 2026

### Development Status

#### Phase 0: Foundation — Complete
Established the project foundation and initial structure.

#### Phase 1: Minimal MCP Server — Complete
Implemented the core MCP server and its initial capabilities.

#### Phase 2: Session Management and Diagnostics — Complete
Added session management and diagnostic capabilities.

#### Phase 3a: AgenticLens Integration — In Progress
Integrating workflow analysis and reporting capabilities through AgenticLens, including continued work on provenance support.

#### Phase 3b: Agentic Chaos Integration — Complete
Integrated resilience and fault-injection testing capabilities through Agentic Chaos.

#### Phase 3d: Agentic Sidecar Discovery — Implemented
Exposed Sidecar discovery and readiness information.

#### Phase 3c: AI Operations Specification Conformance — In Progress
Continuing work on conformance with the shared AI Operations Specification.

#### Phase 4: Unified Workflows — Planned
- Combine observability and resilience workflows.
- Compare baseline and chaos runs.
- Surface incident and readiness evidence through one MCP interface.

#### Phase 5: Publishing and Adoption — Planned
- Verify PyPI packaging.
- Publish the package and MCP Registry metadata.
- Add CI for package and registry publishing.

#### Phase 6: Operational Intelligence — Planned
- Guided onboarding.
- Saved artifact browsing.
- Explainable report recall and session history.
- Investigation and narrative generation.

### Ecosystem Dependencies

The MCP Server integrates with:

- **AgenticLens:** Workflow analysis and reporting.
- **Agentic Chaos:** Resilience and fault-injection testing.
- **Agentic Sidecar:** Discovery and readiness information.
- **AI Operations Specification:** Shared artifact and validation contract.

Future control-plane capabilities depend on the availability of AgenticOps Control Tower APIs.

### Known Limitations

- Long-running tool operations can block the server while they execute.
- `chaos.run_experiment` is confined to the workspace root but does not have a more restrictive script allowlist.

### Vision

The long-term goal is to provide one MCP-native interface for interacting with the DeepAgentLabs ecosystem across workflow observability, resilience testing, evaluation and readiness, decision supervision, and operational intelligence.