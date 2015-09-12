#!/bin/bash

FNAME="../number.txt"
../getnumber.sh "$FNAME"
NUM=$(cat "$FNAME")

LEN=13

function main() {
	current=0

	for (( i=0; i < ${#NUM} - 12; i++))
	do
		s="${NUM:$i:$LEN}"
		m=$(mult_string "$s");

		if [ "$m" -gt "$current" ]
		then
			current=$m
		fi
	done

	echo $current;
}

function mult_string() {
	s="$1"

	out=1
	for (( j=0; j < ${#s}; j++))
	do
		ch="${s:$j:1}"
		out=$(($out * $ch));

		if [ "$out" -eq 0 ]
		then
			break
		fi
	done

	echo $out;
}

main
