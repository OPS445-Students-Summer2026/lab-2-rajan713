#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    sys.exit(1)

counter = int(sys.argv[1])

while counter > 0:
    print(counter)
    counter -= 1

print('blast off!')
