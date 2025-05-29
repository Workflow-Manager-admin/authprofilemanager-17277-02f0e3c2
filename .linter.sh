#!/bin/bash
cd /home/kavia/workspace/code-generation/authprofilemanager-17277-02f0e3c2/auth_profile_manager
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

