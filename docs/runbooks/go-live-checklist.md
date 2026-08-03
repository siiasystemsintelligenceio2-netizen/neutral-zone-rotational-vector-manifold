# Go-Live Checklist

- [ ] Confirm release tag is created and mapped to a changelog entry.
- [ ] Confirm required secrets are configured for staging and production workflows.
- [ ] Confirm deployment scripts are executable (`chmod +x scripts/*.sh`).
- [ ] Confirm CI (`ci.yml`) and security (`security.yml`) workflows are green on the release commit.
- [ ] Confirm staging deployment completed and smoke test passed.
- [ ] Confirm production environment approval rules are enabled in GitHub.
- [ ] Confirm canary rollout plan, bake time, and success thresholds are defined.
- [ ] Confirm rollback operator and on-call contact are assigned.
- [ ] Confirm incident and rollback runbooks are linked in release ticket.
