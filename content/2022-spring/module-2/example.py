#!/usr/bin/env python

print('example!')

with open('data.txt', 'r') as f:
  for l in f:
    print(l)
