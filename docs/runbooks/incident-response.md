# Incident Response Runbook

## Severity levels
- **SEV1**: customer-facing outage or data corruption risk.
- **SEV2**: major degradation with workaround.
- **SEV3**: minor degradation or internal issue.

## Response checklist
- [ ] Create incident channel/ticket and assign incident commander.
- [ ] Record start time, impacted services, and customer impact.
- [ ] Apply immediate containment (feature flag disable, traffic shift, or rollback).
- [ ] Notify stakeholders using approved communication templates.
- [ ] Track mitigation actions with owners and timestamps.
- [ ] Confirm recovery and close communication loop.
- [ ] Schedule post-incident review with action items.

## TODO (project-specific)
- [ ] Add paging/escalation policy links.
- [ ] Add customer communication templates.
- [ ] Add service dependency map.
