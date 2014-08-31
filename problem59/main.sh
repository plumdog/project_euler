#!/bin/bash

NAME="cipher1.txt"
ADDRESS="https://projecteuler.net/project/resources/p059_cipher.txt"

function error() {
	echo "$1";
	exit 1;
}

function download() {
	if [ ! -f "$NAME" ]
	then
		wget -q "$ADDRESS" -O "$NAME" || error "Download failed."
	fi
}

function main() {
	download
	./problem59.py "$NAME"
}

main
