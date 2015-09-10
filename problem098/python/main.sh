#!/bin/bash

FNAME="../words.txt"
../getwords.sh "$FNAME"
./problem98.py "$FNAME"
