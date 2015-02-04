#!/bin/bash

NAME="triangles.txt"

function error() {
	echo "$1"
	exit 1;
}

if [ ! -f "$NAME" ]
then
    wget --no-check-certificate https://projecteuler.net/project/resources/p102_triangles.txt -q -O "$NAME" || error "Unable to download data file"
fi

gcc -g problem102.c -o problem102.out -std=c99 && ./problem102.out "$NAME"
