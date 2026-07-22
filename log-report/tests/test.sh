#!/bin/bash
# pytest and pytest-json-ctrf are baked into environment/Dockerfile.
# Nothing is installed at verify time.
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
result=$?

if [ $result -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
