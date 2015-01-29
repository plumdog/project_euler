#!/bin/bash

FNAME="sudoku.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p096_sudoku.txt" -O "$FNAME" || exit 1
fi

./problem_96.py "$FNAME"
