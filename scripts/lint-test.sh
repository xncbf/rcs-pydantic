#!/usr/bin/env bash

set -x

black rcs_pydantic --check
isort --check-only rcs_pydantic
flake8
