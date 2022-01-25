#!/usr/bin/env python

import random
import sys

# tell the user how to use this script
if len(sys.argv) != 3:
  print('use: sort-random.py infile outfile')
  print('     infile === name of infile')
  print('     outfile === name of outfile')
  exit(1)

# read input from command line
infile = sys.argv[1]
outfile = sys.argv[2]

# read random numbers from file and write as we go
with open(infile, 'r') as fin:
  in_data = fin.read()

# get list of unsorted numbers
unsort = list()
for i in in_data.split(',')[:-1]:
  unsort.append(int(i))

# sort
sort = list()
while unsort:
  # find minimum in unsorted list
  minimum = unsort[0]
  position = 0
  for i in range(1, len(unsort)):
    if unsort[i] < minimum:
      position = i
      minimum = unsort[position]
  # put minimum into sorted list
  sort.append(minimum)
  # remove minimum from unsorted list
  unsort.pop(position)

# write sorted output file
with open(outfile, 'w') as fout:
  for i in sort:
    fout.write('%d,' % i)
