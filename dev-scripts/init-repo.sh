#!/usr/bin/env bash
# Setup venv
#
# Setup virtual environment and install dependencies
#  useful on container creation and after dependency changes after a git pull
set -e

source ./dev-scripts/helper/formatting.sh

echo -e "${BOLD}Creating .venv${RESET}"
uv python install

echo -e "${BOLD}Creating .venv${RESET}"
uv sync

echo -e "${BOLD}Install local commit hooks${RESET}"
uv run pre-commit install

echo -e "${BOLD}Setup complete!${RESET}"