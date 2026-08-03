# Observability Architecture (Scaffold)

## Pillars
- Logs: structured JSON logs with request/trace identifiers.
- Metrics: request rate, error rate, latency, saturation, and business KPIs.
- Tracing: distributed trace propagation across API, storage, and async jobs.

## Baseline instrumentation checklist
- [ ] Standard log fields (`service`, `env`, `trace_id`, `request_id`, `event`).
- [ ] Redaction policy for secrets/PII before log export.
- [ ] Dashboards for RED metrics and key business workflows.
- [ ] Alerts for SLO burn and deployment regressions.

## TODO (project-specific)
- [ ] Add telemetry vendor endpoints and retention windows.
- [ ] Add ownership map for each alert.
