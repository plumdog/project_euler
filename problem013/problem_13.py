#!/usr/bin/env python3
import sys

with open(sys.argv[1]) as f:
    nums = [int(l.strip()) for l in f.readlines()]
print(str(sum(nums))[:10])
