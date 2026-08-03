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

require_env DEPLOY_ENV
require_env STAGING_DEPLOY_TARGET
require_env DEPLOY_COMMAND

if [[ "$DEPLOY_ENV" != "staging" ]]; then
  echo "ERROR: deploy-staging.sh can only run with DEPLOY_ENV=staging." >&2
  exit 1
fi

echo "Deploying to staging target: $STAGING_DEPLOY_TARGET"
# TODO: Replace with actual deployment command (for example kubectl/helm/terraform).
# shellcheck disable=SC2086
bash -lc "$DEPLOY_COMMAND"
echo "Staging deployment completed"
