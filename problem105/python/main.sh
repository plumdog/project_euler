#!/bin/bash

FNAME="../sets.txt"
../getsets.sh "$FNAME"
./problem105.py "$FNAME"
