#!/bin/bash

prime_options=(
    -c ../../common/c/prime.c
    -o ../../common/c/prime.o
    -std=c99
)

main_options=(
    -o problem7.out
    -I../../common/c ../../common/c/prime.o
    -lm -std=c99
)

gcc "${prime_options[@]}" && gcc problem7.c "${main_options[@]}" && ./problem7.out
