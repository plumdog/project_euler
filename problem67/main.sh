#!/bin/bash

FNAME="triangle.txt"

if [ ! -f "$FNAME" ]
then
	wget -q "https://projecteuler.net/project/triangle.txt" -O "$FNAME" || exit 1
fi

./problem_67.py "$FNAME"
