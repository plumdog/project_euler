#!/bin/bash

URL="$1"
FNAME="$2"

if [ ! -f "$FNAME" ]; then
	wget --no-check-certificate -q "$URL" -O "$FNAME" || exit 1
fi
