#!/usr/bin/env bash
set -e

source ./dev-scripts/helper/formatting.sh

echo -e "${BOLD}Running ruff format...${RESET}"
uv run ruff format
 
echo -e "${BOLD}Running ruff check...${RESET}"
uv run ruff check --fix

echo -e "${BOLD}Running mypy...${RESET}"
uv run mypy .

echo -e "${BOLD}All checks passed!${RESET}"
