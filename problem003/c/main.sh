#!/bin/bash

prime_options=(
    -c ../../common/c/prime.c
    -o ../../common/c/prime.o
    -std=c99
)

main_options=(
    problem3.c
    -o problem3.out
    -I ../../common/c ../../common/c/prime.o
    -lm
    -std=c99
)

gcc "${prime_options[@]}" && gcc "${main_options[@]}" && ./problem3.out
