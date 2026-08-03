#!/usr/bin/env bash
# Scaffold note: make executable with `chmod +x scripts/*.sh`.
set -euo pipefail

phase="${1:-}"
if [[ -z "$phase" ]]; then
  echo "ERROR: Deployment phase is required (canary|full)." >&2
  exit 1
fi

if [[ "$phase" != "canary" && "$phase" != "full" ]]; then
  echo "ERROR: Unsupported deployment phase '$phase'. Use canary or full." >&2
  exit 1
fi

require_env() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    echo "ERROR: Required environment variable '$name' is not set." >&2
    exit 1
  fi
}

require_env DEPLOY_ENV
require_env RELEASE_VERSION
require_env DEPLOY_COMMAND

if [[ "$DEPLOY_ENV" != "production" ]]; then
  echo "ERROR: deploy-production.sh can only run with DEPLOY_ENV=production." >&2
  exit 1
fi

echo "Running production $phase deployment for release $RELEASE_VERSION"
# TODO: Implement production canary controls (traffic split, bake time, SLO gate).
# shellcheck disable=SC2086
bash -lc "$DEPLOY_COMMAND"
echo "Production $phase deployment completed"
