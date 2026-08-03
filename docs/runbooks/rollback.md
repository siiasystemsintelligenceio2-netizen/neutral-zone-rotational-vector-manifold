# Rollback Runbook

## Preconditions
- [ ] Incident commander approval documented.
- [ ] Target rollback version identified and validated.
- [ ] Rollback reason recorded.

## Execution
1. Trigger `.github/workflows/rollback.yml` with:
   - `environment`
   - `target_version`
   - `reason`
2. Verify rollback workflow completes successfully.
3. Run smoke checks and key business-flow checks.

## Verification checklist
- [ ] Health endpoint returns HTTP 200.
- [ ] Error rate returns to baseline.
- [ ] Latency SLO returns to baseline.
- [ ] Critical user flows confirmed.

## TODO (project-specific)
- [ ] Add data rollback criteria and process.
- [ ] Add artifact registry lookup command.
