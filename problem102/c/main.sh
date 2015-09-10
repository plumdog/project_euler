#!/bin/bash

NAME="../triangles.txt"
../gettriangles.sh "$NAME"
gcc -g problem102.c -o problem102.out -std=c99 && ./problem102.out "$NAME"
