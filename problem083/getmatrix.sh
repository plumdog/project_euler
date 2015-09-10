#!/bin/bash

FNAME="$1"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p083_matrix.txt" -O "$FNAME" || exit 1
fi
