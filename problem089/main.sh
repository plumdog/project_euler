#!/bin/bash

FNAME="roman.txt"
URL="https://projecteuler.net/project/resources/p089_roman.txt"

if [ ! -f "$FNAME" ]
then
    wget --no-check-certificate -q "$URL" -O "$FNAME" || exit 1
fi

./problem_89.py "$FNAME"
