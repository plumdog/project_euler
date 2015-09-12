#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p082_matrix.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
