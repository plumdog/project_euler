#!/bin/bash

NAME="../poker.txt"
../getpoker.sh "$NAME"
javac Problem54.java && java Problem54 "$NAME"
