#!/bin/bash

FNAME="words.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p098_words.txt" -O "$FNAME" || exit 1
fi

./problem98.py "$FNAME"
