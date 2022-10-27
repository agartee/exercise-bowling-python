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
# Deactivate Python Virtual Environment
# **************************************************************************************
deactivate 2> /dev/null

# **************************************************************************************
# Delete Python Virtual Environment (if exists)
# **************************************************************************************
VENV_PATH="$ROOT_DIR/.venv"

if [ -d "$VENV_PATH" ]; 
    then rm -Rf $VENV_PATH; 
    echo -e "${GREEN}Python virtual environment deleted.${NC}"
fi

# **************************************************************************************
# Delete pytest Cache (if exists)
# **************************************************************************************
PYTEST_CACHE_PATH="$ROOT_DIR/.pytest_cache"

if [ -d "$PYTEST_CACHE_PATH" ]; 
    then rm -Rf $PYTEST_CACHE_PATH; 
    echo -e "${GREEN}pytest cache deleted.${NC}"
fi

# **************************************************************************************
# Delete pytest Coverage File (if exists)
# **************************************************************************************
PYTEST_COVERAGE_FILE_PATH="$ROOT_DIR/.coverage"

if [ -d "$PYTEST_COVERAGE_FILE_PATH" ]; 
    then rm $PYTEST_COVERAGE_FILE_PATH; 
    echo -e "${GREEN}pytest coverage file deleted.${NC}"
fi

# **************************************************************************************
# Bootstrap
# **************************************************************************************
. "$ROOT_DIR/scripts/bootstrap.sh"
