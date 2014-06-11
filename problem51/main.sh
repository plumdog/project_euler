#!/bin/bash

gcc -std=c99 -c ../common/c/prime.c -o ../common/c/prime.o -lm && gcc -std=c99 problem51.c -o problem51.out -I../common/c ../common/c/prime.o -lm && ./problem51.out
