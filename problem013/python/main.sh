#!/bin/bash

FNAME="../numbers.txt"

if [ ! -f "$FNAME" ]
then
    ../getnumbers.sh "$FNAME"
fi

./problem_13.py "$FNAME"
