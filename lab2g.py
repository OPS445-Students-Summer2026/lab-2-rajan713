#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    counter = int(sys.argv[1])
else:
    counter = 3

while counter > 0:
    print(counter)
    counter -= 1

print('blast off!')
