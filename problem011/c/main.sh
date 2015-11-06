#!/bin/bash

FNAME="../matrix.txt"
../getmatrix.sh "$FNAME"

matrix_options=(
    -c ../../common/c/get_matrix.c
    -o ../../common/c/get_matrix.o
    -std=gnu99
)

main_options=(
    problem11.c
    -o problem11.out
    -I../../common/c ../../common/c/get_matrix.o
    -std=gnu99
)

gcc "${matrix_options[@]}" && gcc "${main_options[@]}" && ./problem11.out "$FNAME"
