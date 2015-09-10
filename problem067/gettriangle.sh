#!/bin/bash

FNAME="$1"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p067_triangle.txt" -O "$FNAME" || exit 1
fi
