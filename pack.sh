#!/bin/bash

EXCLUDE_FILES="assignment.txt|pack.sh"

FILES=$(ls | grep -v -E "$EXCLUDE_FILES")
FILES=$(echo "$FILES" | tr '\n' ' ')
echo "zipping $FILES"
zip iam-sudoku-xpavli0a.zip $FILES
