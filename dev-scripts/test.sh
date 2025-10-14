#!/usr/bin/env bash
set -e

source ./dev-scripts/helper/formatting.sh

echo -e "${BOLD}Running pytest...${RESET}"
uv run pytest

echo -e "${BOLD}Running tox...${RESET}"
echo -e "${INDENT}Tox runs tests under different python versions and dependency versions"
uv run tox