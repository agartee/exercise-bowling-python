#!/usr/bin/env bash

ROOT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pytest --cov=bowling "$ROOT_DIR/tests" --cov-report term-missing
