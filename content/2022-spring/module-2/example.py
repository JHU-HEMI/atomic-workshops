#!/usr/bin/env python

print('example!')

with open('data.txt', 'r') as f:
  counter = 0
  for l in f:
    counter += 1
    print('%d: %s' % (counter, l))
