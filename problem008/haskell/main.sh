#!/bin/bash
FNAME="../number.txt"
../getnumber.sh "$FNAME"
runhaskell problem8.hs "$FNAME"
