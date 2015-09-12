#!/bin/bash
URL="https://projecteuler.net/problem=8"
FNAME="$1"
START="<p style=\"font-family:'courier new';text-align:center;\">"
END="</p>"
BREAKS=""
../../common/bash/getnumfromhtml.sh "$URL" "$FNAME" "$START" "$END" "$BREAKS"
