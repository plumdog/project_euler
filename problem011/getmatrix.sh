#!/bin/bash
URL="https://projecteuler.net/problem=11"
FNAME="$1"
START="<p style=\"font-family:'courier new';text-align:center;font-size:10pt;\">"
END="</p>"
BREAKS="<br></br>"
../../common/bash/getnumfromhtml.sh "$URL" "$FNAME" "$START" "$END" "$BREAKS"
