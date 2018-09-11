#!/bin/bash

success_status_code=0
failure_status_code=1

echo 'Running linter'
flake8 /bank_crabi/app

if [ $? -eq $success_status_code ]
    then
        echo "No source code problems found"
    else
        echo "Source code problems found, please fix them to continue"
        exit $failure_status_code
fi

exit $success_status_code

