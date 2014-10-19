#!/bin/bash

FNAME="numbers.txt"

if [ ! -f "$FNAME" ]
then
    ./getnumbers.py "$FNAME"
fi

./problem_13.py "$FNAME"
