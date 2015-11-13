#!/bin/bash

FNAME="../numbers.txt"
../getnumbers.sh "$FNAME"

matrix_options=(
    -c ../../common/c/get_matrix.c
    -o ../../common/c/get_matrix.o
    -std=gnu99
)

main_options=(
    problem13.c
    -o problem13.out
    -I../../common/c ../../common/c/get_matrix.o
    -std=gnu99
)

gcc "${matrix_options[@]}" && gcc "${main_options[@]}" && ./problem13.out "$FNAME"
