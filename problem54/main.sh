#!/bin/bash

NAME="poker.txt"

if [ ! -f "$NAME" ]
then
	wget "https://projecteuler.net/project/$NAME" -q -O "$NAME" || exit 1
fi

javac Problem54.java && java Problem54 "$NAME"
