#!/usr/bin/env python
# -*- coding: utf8 -*-


import itertools
import os
import re

bruteKeys = [0,0,0,0, 1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9]
#bruteKeys = [1,2,3,4,5,6,7,8,9]
#bruteKeys = range(0, 10)
regex = '0, 2, 3, 0'

fComb = 'combinations-combinations.list'
fPerm = 'combinations-permutations.list'

def unique(iterable):
    seen = set()
    for x in iterable:
        if x in seen:
            continue
        seen.add(x)
        yield x

if not os.path.isfile(fComb):
    totalKeys = 0
    with open(fComb, 'w') as f:
        for a in unique(itertools.combinations(bruteKeys, r=4)):
            totalKeys = totalKeys + 1
            f.write(str(a))
    f.close()

if not os.path.isfile(fPerm):
    totalKeys = 0
    with open(fPerm, 'w') as f:
        for a in unique(itertools.permutations(bruteKeys, r=4)):
            totalKeys = totalKeys + 1
            f.write(str(a))
    f.close()

# Search
with open(fComb, 'r') as f:
    count = len(re.findall(regex, f.read()))
    print(fComb, 'Regex:', regex, 'Count:', count)

with open(fPerm, 'r') as f:
    count = len(re.findall(regex, f.read()))
    print(fPerm, 'Regex:', regex, 'Count:', count)

# Total
with open(fComb, 'r') as f:
    regex = '., ., ., .'
    count = len(re.findall(regex, f.read()))
    print(fComb, 'Regex:', regex, 'Count:', count)

with open(fPerm, 'r') as f:
    regex = '., ., ., .'
    count = len(re.findall(regex, f.read()))
    print(fPerm, 'Regex:', regex, 'Count:', count)
