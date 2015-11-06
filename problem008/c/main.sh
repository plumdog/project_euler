#!/bin/bash

FNAME="../number.txt"
../getnumber.sh "$FNAME"

main_options=(
    problem8.c
    -o problem8.out
    -std=gnu99
)

gcc "${main_options[@]}" && ./problem8.out "$FNAME"
