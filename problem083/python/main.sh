#!/bin/bash

FNAME="../matrix.txt"
../getmatrix.sh "$FNAME"
./problem_83.py "$FNAME"
