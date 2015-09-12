#!/bin/bash

NAME="$1"
URL="https://projecteuler.net/project/resources/p022_names.txt"

function error() {
	echo "$1"
	exit 1;
}

../../common/bash/getfile.sh "$URL" "$NAME" || exit 1
cat "$NAME" | tr ',', '\n' | sed -e 's/"//g' | sort -o "$NAME" || error "Sorting failed"
