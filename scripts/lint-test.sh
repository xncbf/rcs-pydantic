#!/usr/bin/env bash

set -x

poetry run black rcs_pydantic --check
poetry run isort --check-only rcs_pydantic
poetry run ruff check --exit-zero .
