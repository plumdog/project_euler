#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p083_matrix.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
