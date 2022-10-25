#!/usr/bin/env bash

ROOT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

RED="\033[0;31m"
GREEN="\033[0;32m"
NC="\033[0m" # No Color

# **************************************************************************************
# Ensure Script is Sourced (remove if debugging this script)
# **************************************************************************************
if [ "${BASH_SOURCE[0]}" -ef "$0" ]; 
    then echo -e "${RED}ERROR: In order for the Python virtual environment to remain" \
        "active, this script must be sourced.${NC}"
    exit 1
fi

# **************************************************************************************
# Delete Python Virtual Environment (if exists)
# **************************************************************************************
VENV_PATH="$ROOT_DIR/.venv"

if [ -d "$VENV_PATH" ]; 
    then rm -Rf $VENV_PATH; 
    echo -e "${GREEN}Python virtual environment deleted.${NC}"
fi

# **************************************************************************************
# Bootstrap
# **************************************************************************************
. "$ROOT_DIR/scripts/bootstrap.sh"
