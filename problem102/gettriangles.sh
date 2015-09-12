#!/bin/bash
NAME="$1"
URL="https://projecteuler.net/project/resources/p102_triangles.txt"
../../common/bash/getfile.sh "$URL" "$NAME" || exit 1
