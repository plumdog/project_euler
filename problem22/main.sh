#!/bin/bash

NAME="names.txt"

function error() {
	echo "$1"
	exit 1;
}

function main() {
	if [ ! -f "$NAME" ]
	then
		wget https://projecteuler.net/project/names.txt -q -O "$NAME" || error "Unable to download data file"
	fi

	cat "$NAME" | tr ',', '\n' | sed -e 's/"//g' | sort -o "$NAME" || error "Sorting failed"
	gcc problem22.c -o problem22.out -std=c99 && ./problem22.out "$NAME"
}

main
