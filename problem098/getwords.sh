#!/bin/bash

FNAME="$1"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p098_words.txt" -O "$FNAME" || exit 1
fi
