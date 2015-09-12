#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p089_roman.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
