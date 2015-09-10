#!/bin/bash

NAME="$1"
ADDRESS="https://projecteuler.net/project/resources/p059_cipher.txt"

function error() {
	echo "$1";
	exit 1;
}

if [ ! -f "$NAME" ]
then
    wget --no-check-certificate -q "$ADDRESS" -O "$NAME" || error "Download failed."
fi
