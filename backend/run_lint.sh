#!/bin/bash

echo "running flake8 ..."
flake8 --config=pyproject.toml --exclude=*/migrations/*

echo ""

echo "running black ..."
black --check --diff --exclude=migrations --config=pyproject.toml service
