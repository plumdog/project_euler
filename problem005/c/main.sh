#!/bin/bash

prime_options=(
    -c ../../common/c/prime.c
    -o ../../common/c/prime.o
    -std=c99
)

main_options=(
    problem5.c
    -o problem5.out
    -I ../../common/c ../../common/c/prime.o
    -lm
    -std=c99
)

$CC "${prime_options[@]}" && gcc "${main_options[@]}" && ./problem5.out
