#!/usr/bin/env bash

ROOT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pytest "$ROOT_DIR/tests"
