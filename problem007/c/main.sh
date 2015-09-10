#!/bin/bash

gcc -c ../../common/c/prime.c -o ../../common/c/prime.o -std=c99 && gcc problem7.c -o problem7.out -I../../common/c ../../common/c/prime.o -lm -std=c99 && ./problem7.out
