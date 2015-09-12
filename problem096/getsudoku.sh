#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p096_sudoku.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
