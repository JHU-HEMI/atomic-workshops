#!/usr/bin/env python

import random
import sys

# tell the user how to use this script
if len(sys.argv) != 3:
  print('use: generate-random.py total outfile')
  print('     total === number of random numbers')
  print('     outfile === name of output file')
  exit(1)

# read input from command line
total = int(sys.argv[1])
outfile = sys.argv[2]

# write random numbers to file
with open(outfile, 'w') as f:
  for i in range(total):
    f.write('%d,' % random.randrange(0,1e9))
