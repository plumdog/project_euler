#!/bin/bash

NAME="../names.txt"

../getnames.sh "$NAME"
gcc problem22.c -o problem22.out -std=c99 && ./problem22.out "$NAME"
