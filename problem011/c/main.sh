#!/bin/bash

FNAME="../matrix.txt"
../getmatrix.sh "$FNAME"
gcc problem11.c -o problem11.out -std=gnu99 && ./problem11.out "$FNAME"
