#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print('Usage: ./lab2d.py name age')
else:
    name = sys.argv[1]
    age = sys.argv[2]

    print(f'Hi {name}, you are {age} years old.')
