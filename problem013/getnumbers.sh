#!/bin/bash
URL="https://projecteuler.net/problem=13"
FNAME="$1"
START="<div style=\"font-family:'courier new';font-size:10pt;text-align:center;\">"
END="</div>"
BREAKS="\n"
../../common/bash/getnumfromhtml.sh "$URL" "$FNAME" "$START" "$END" "$BREAKS"
