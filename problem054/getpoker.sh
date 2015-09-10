#!/bin/bash

NAME="$1"

if [ ! -f "$NAME" ]
then
	wget --no-check-certificate "https://projecteuler.net/project/resources/p054_poker.txt" -q -O "$NAME" || exit 1
fi
