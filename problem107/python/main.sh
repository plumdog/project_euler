#!/bin/bash

FNAME="../network.txt"
../getnetwork.sh "$FNAME"
./problem107.py "$FNAME"
