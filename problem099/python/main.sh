#!/bin/bash

FNAME="../base_exp.txt"
../getbaseexp.sh "$FNAME"
./problem99.py "$FNAME"
