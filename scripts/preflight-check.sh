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

DEPLOY_ENV="${DEPLOY_ENV:-}"
if [[ -z "$DEPLOY_ENV" ]]; then
  echo "ERROR: DEPLOY_ENV must be set (staging|production)." >&2
  exit 1
fi

case "$DEPLOY_ENV" in
  staging)
    require_env STAGING_DEPLOY_TARGET
    ;;
  production)
    require_env PRODUCTION_DEPLOY_TARGET
    ;;
  *)
    echo "ERROR: DEPLOY_ENV must be one of: staging, production." >&2
    exit 1
    ;;
esac

# TODO: Replace with real health/dependency probes (database, cache, queue, image registry).
if [[ -z "${MIGRATION_COMMAND:-}" ]]; then
  echo "ERROR: MIGRATION_COMMAND is not configured. Add environment-specific migration command." >&2
  exit 1
fi

echo "Preflight checks passed for DEPLOY_ENV=$DEPLOY_ENV"
