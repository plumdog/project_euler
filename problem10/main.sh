#!/bin/bash

gcc -c ../common/c/prime.c -o ../common/c/prime.o -std=c99 && gcc problem10.c -o problem10.out -I../common/c ../common/c/prime.o -lm -std=c99 && ./problem10.out
