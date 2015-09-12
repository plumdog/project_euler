#!/bin/bash
URL="https://projecteuler.net/project/resources/p079_keylog.txt"
FNAME="$1"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
