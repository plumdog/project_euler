#!/bin/bash

# Yuck. We have to get the HTML and parse it (badly) for the
# numbers. We just have find the div that holds the numbers, and trim
# from there to the next closing div tag.
FNAME="$1"

START="<div style='font-family:courier new;font-size:10pt;text-align:center;'>"
END="</div>"

# Get the full html
HTML="`wget --no-check-certificate -qO- https://projecteuler.net/problem=13`"

# Trim from the start line to the end. (This could probably be made
# neater.
STARTLINE=$(($(echo "$HTML" | grep -n "$START" | gawk '{print $1}' FS=":") + 1))
ENDLINE=$(echo "$HTML" | wc -l)
HTML=$(echo "$HTML" | sed -n "$STARTLINE,$ENDLINE""p")

# Trim from the start to the first closing tag.
ENDLINE=$(($(echo "$HTML" | grep -n "$END" | head -n 1 | gawk '{print $1}' FS=":") - 1))
HTML=$(echo "$HTML" | sed -n "1,$ENDLINE""p")

# Remove all of the <br />s
echo "$HTML" | sed -e 's|<br />||g' > "$FNAME"
