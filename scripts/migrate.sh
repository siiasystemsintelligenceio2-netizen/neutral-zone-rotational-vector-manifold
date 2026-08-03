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
require_env MIGRATION_COMMAND

# TODO: Replace lock strategy with project-specific migration locking implementation.
lock_file="/tmp/${DEPLOY_ENV}-migration.lock"
if [[ -f "$lock_file" ]]; then
  echo "ERROR: Migration lock exists at $lock_file. Remove only after verifying no migration is running." >&2
  exit 1
fi
trap 'rm -f "$lock_file"' EXIT
touch "$lock_file"

echo "Running migrations for DEPLOY_ENV=$DEPLOY_ENV"
# shellcheck disable=SC2086
bash -lc "$MIGRATION_COMMAND"
echo "Migrations completed"
