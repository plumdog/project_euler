#!/bin/bash

FNAME="../numbers.txt"
../getnumbers.sh "$FNAME"
./problem_13.py "$FNAME"
