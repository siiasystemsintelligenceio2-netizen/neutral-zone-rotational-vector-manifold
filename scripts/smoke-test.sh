#!/usr/bin/env bash
# Scaffold note: make executable with `chmod +x scripts/*.sh`.
set -euo pipefail

require_env() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    echo "ERROR: Required environment variable '$name' is not set." >&2
    exit 1
  fi
}

require_env SMOKE_TEST_URL

endpoint="${SMOKE_TEST_URL%/}/healthz"
echo "Running smoke test against $endpoint"

http_code="$(curl -sS -o /tmp/smoke-response.txt -w '%{http_code}' "$endpoint")"
if [[ "$http_code" != "200" ]]; then
  echo "ERROR: Smoke test failed with HTTP $http_code" >&2
  echo "Response body:" >&2
  cat /tmp/smoke-response.txt >&2 || true
  exit 1
fi

echo "Smoke test passed"
