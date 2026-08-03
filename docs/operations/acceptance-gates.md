# Acceptance Gates

A release is production-eligible only when all gates pass.

- [ ] CI gate: lint, typecheck, tests, build all pass.
- [ ] Security gate: CodeQL + dependency audit pass without unresolved critical findings.
- [ ] Staging gate: deploy succeeds and smoke tests pass.
- [ ] Observability gate: dashboards/alerts verified for current release.
- [ ] Operational gate: on-call, rollback operator, and runbook links confirmed.
- [ ] Change gate: release approval recorded with risk assessment.

## TODO (project-specific)
- [ ] Define numeric SLO thresholds for fail/pass.
- [ ] Define required approver groups.
