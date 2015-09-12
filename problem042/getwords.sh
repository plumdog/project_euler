#!/bin/bash

NAME="$1"
NAMETMP="words_tmp.txt"
URL="https://projecteuler.net/project/resources/p042_words.txt"

../../common/bash/getfile.sh "$URL" "$NAME" || exit 1
cat "$NAME" | tr ',', '\n' | sed -e 's/"//g' | cat > "$NAMETMP" && mv "$NAMETMP" "$NAME"
