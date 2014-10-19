#!/bin/bash

FNAME="keylog.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p079_keylog.txt" -O "$FNAME" || exit 1
fi

./problem_79.py "$FNAME"