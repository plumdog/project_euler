#!/bin/bash

NAME="$1"

function error() {
	echo "$1"
	exit 1;
}

if [ ! -f "$NAME" ]
then
    wget --no-check-certificate https://projecteuler.net/project/resources/p102_triangles.txt -q -O "$NAME" || error "Unable to download data file"
fi
