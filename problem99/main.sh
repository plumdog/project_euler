#!/bin/bash

FNAME="base_exp.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p099_base_exp.txt" -O "$FNAME" || exit 1
fi

./problem99.py "$FNAME"
