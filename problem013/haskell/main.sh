#!/bin/bash
FNAME="../numbers.txt"
../getnumbers.sh "$FNAME"
runhaskell problem13.hs "$FNAME"
