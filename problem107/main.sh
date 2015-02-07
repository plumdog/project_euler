#!/bin/bash

FNAME="network.txt"

if [ ! -f "$FNAME" ]
then
	wget --no-check-certificate -q "https://projecteuler.net/project/resources/p107_network.txt" -O "$FNAME" || exit 1
fi

./problem107.py "$FNAME"
