#!/bin/bash

##################
##  Vit Pavlik  ##
##   xpavli0a   ##
##    251301    ##
##     2024     ##
##################

#
# a run script accompanying sudoku.py
# Usage: ./run.sh run
#

PY=python3
INPUT_FILE=input.txt
DIMACS_FILE=sudoku-dimacs.txt
MINISAT_FILE=minisat-output.txt

OPTION_Y="$2"

if [ "$1" != "run" -a "$1" != "clean" ]; then
    echo "Usage: ./run.sh run|clean [-y]"
    exit
fi

prompt_confirm () {
    if [ "$OPTION_Y" != "-y" ]; then
        echo -n "$@ (y/n) "
        read PROCEED
        if [ "$PROCEED" != "y" ]; then
            echo "abort"
            exit
        fi
    fi
}

safe_delete () {
    if [ -f "$1" ]; then
        prompt_confirm "delete $1?"
        rm "$1"
    fi
}

ask_overwrite () {
    if [ -f "$1" ]; then
        prompt_confirm "overwrite $1?"
    fi
}

################################################################################

# clean and exit
if [ "$1" = "clean" ]; then
    safe_delete $DIMACS_FILE
    safe_delete $MINISAT_FILE
    exit
fi

# run sudoku.py
ask_overwrite "$DIMACS_FILE"
$PY sudoku.py > $DIMACS_FILE < input.txt

# run minisat
ask_overwrite "$MINISAT_FILE"
minisat $DIMACS_FILE $MINISAT_FILE

# run view.py
$PY view.py < $MINISAT_FILE