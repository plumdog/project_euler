#!/bin/bash

NAME="poker.txt"

if [ ! -f "$NAME" ]
then
	wget --no-check-certificate "https://projecteuler.net/project/resources/p054_poker.txt" -q -O "$NAME" || exit 1
fi

javac Problem54.java && java Problem54 "$NAME"
