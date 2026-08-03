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
require_env ROLLBACK_TARGET_VERSION
require_env ROLLBACK_REASON
require_env ROLLBACK_COMMAND

echo "Rolling back DEPLOY_ENV=$DEPLOY_ENV to version=$ROLLBACK_TARGET_VERSION"
echo "Reason: $ROLLBACK_REASON"
# TODO: Replace with deterministic rollback command for your runtime platform.
# shellcheck disable=SC2086
bash -lc "$ROLLBACK_COMMAND"
echo "Rollback completed"
