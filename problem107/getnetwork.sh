#!/bin/bash
FNAME="$1"
URL="https://projecteuler.net/project/resources/p107_network.txt"
../../common/bash/getfile.sh "$URL" "$FNAME" || exit 1
