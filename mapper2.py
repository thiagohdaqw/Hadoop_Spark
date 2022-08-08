#!/bin/python3
import sys

for line in sys.stdin:
    if not line.strip():
        continue
    if line.startswith('__TOTAL_'):
        print(line)
