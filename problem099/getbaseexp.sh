#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p099_base_exp.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
