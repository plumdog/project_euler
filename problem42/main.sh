#!/bin/bash

NAME="words.txt"
NAMETMP="words_tmp.txt"

if [ ! -f "$NAME" ]
then
	wget --no-check-certificate "https://projecteuler.net/project/resources/p042_words.txt" -q -O "$NAME" || exit 1
	cat "$NAME" | tr ',', '\n' | sed -e 's/"//g' | cat > "$NAMETMP" && mv "$NAMETMP" "$NAME"
fi

javac Problem42.java && java Problem42 "$NAME"
