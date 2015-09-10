#!/bin/bash

FNAME="../matrix.txt"

../getmatrix.sh "$FNAME"
./problem_82.py "$FNAME"
