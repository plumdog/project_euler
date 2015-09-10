#!/bin/bash

FNAME="../sudoku.txt"
../getsudoku.sh "$FNAME"
./problem_96.py "$FNAME"
