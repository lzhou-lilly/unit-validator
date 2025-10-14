#!/usr/bin/env bash
set -e

source ./dev-scripts/helper/formatting.sh

echo -e "${BOLD}Build package${RESET}"
uv build