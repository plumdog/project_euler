#!/bin/bash

FNAME="sets.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p105_sets.txt" -O "$FNAME" || exit 1
fi

./problem105.py "$FNAME"
