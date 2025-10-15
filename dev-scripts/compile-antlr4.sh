#!/usr/bin/env bash
set -e

uv run antlr4 -Dlanguage=Python3 -visitor UnitLang.g4 -o unit_lang

echo -e "${BOLD}Compiled Unit language${RESET}"
