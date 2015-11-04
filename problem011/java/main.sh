#!/bin/bash

FNAME="../matrix.txt"

../getmatrix.sh "$FNAME"
javac Problem11.java && java Problem11 "$FNAME"
