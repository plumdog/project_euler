#!/bin/bash

FNAME="../matrix.txt"
../getmatrix.sh "$FNAME"
./problem_81.py "$FNAME"
