#!/usr/bin/env bash
# Start one INTERACTIVE Claude session, with the heartbeat request prefilled.
set -euo pipefail
workspace="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd -- "$workspace"
if ! command -v claude >/dev/null 2>&1; then
  printf '%s\n' 'Claude Code is not on PATH. See the official installation guide.' >&2
  exit 127
fi
exec claude '/heartbeat'
