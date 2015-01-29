#!/bin/bash

FNAME="matrix.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p083_matrix.txt" -O "$FNAME" || exit 1
fi

./problem_83.py "$FNAME"
