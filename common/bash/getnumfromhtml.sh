#!/bin/bash

# Yuck. We have to get the HTML and parse it (badly) for the
# numbers. We just have find the div that holds the numbers, and trim
# from there to the next closing div tag.
URL="$1"
FNAME="$2"
START="$3"
END="$4"
BREAKS="$5"
# Get the full html
HTML="`wget --no-check-certificate -qO- $URL`"

# Trim from the start line to the end. (This could probably be made
# neater.
STARTLINE=$(($(echo "$HTML" | grep -n "$START" | sed -e 's/:.*//') + 1))
ENDLINE=$(echo "$HTML" | wc -l)
HTML=$(echo "$HTML" | sed -n "$STARTLINE,$ENDLINE""p")

# Trim from the start to the first closing tag.
ENDLINE=$(($(echo "$HTML" | grep -n "$END" | head -n 1 | sed -e 's/:.*//')))
HTML=$(echo "$HTML" | sed -n "1,$ENDLINE""p" | sed -e 's|'$END'||')

# Replace the <br />s with $BREAKS
# echo "$HTML" | sed -e 's|<br />|'"$BREAKS"'|g' | tr -d '\n' > "$FNAME"
NUM=$(echo "$HTML" | sed -e 's|<br />||g')

if [[ -z $BREAKS ]]; then
    NUM=$(echo "$NUM" | tr -d "\n")
fi

# Remove any HTML tags
NUM=$(echo "$NUM" | sed -e 's/<[^>]*>//g')

echo "$NUM" > "$FNAME"
