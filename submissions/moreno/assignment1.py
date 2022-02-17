#!/usr/bin/env python

import random
import csv


n = int(input('How many numbers?: '))

random_number_lst = []
tmp_number_lst = []
sorted_number_lst = []

for i in range(n):
    random_number_lst.append(random.uniform(1,100))

with open('random_numbers.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(random_number_lst)

with open('random_numbers.csv','r') as f:
    reader = csv.reader(f)
    for line_no, line in enumerate(reader):
        if line_no == 0:
            tmp_number_lst = line
            
tmp_number_lst_float = [float(x) for x in tmp_number_lst]


for i in range(n):
    tmp = min(tmp_number_lst_float)
    sorted_number_lst.append(tmp)
    tmp_number_lst_float.remove(tmp)
    
    

with open('sorted_numbers.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(sorted_number_lst)


