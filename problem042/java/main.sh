#!/bin/bash

NAME="../words.txt"
../getwords.sh "$NAME"

javac Problem42.java && java Problem42 "$NAME"
