#!/bin/bash

FNAME="../keylog.txt"
../getkeylog.sh "$FNAME"
./problem_79.py "$FNAME"
