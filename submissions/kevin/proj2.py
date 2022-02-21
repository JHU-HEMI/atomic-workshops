#!/usr/bin/env python3

# This program reads numbers from a .csv and sorts them

numList=[]
with open('randNums.csv','r') as f:
    for line in f:
            temp=line

for i in temp.split():
    numList.append(i.strip(','))

unSortList=list(numList) # can't do unSortList=numList b/c of referencing
sortedList=[]

for i in range(len(numList)):
    minN=unSortList[0]
    for j in range(len(unSortList)):
        if minN > unSortList[j]:
            minN = unSortList[j]
    unSortList.remove(minN)
    sortedList.append(minN)

print(sortedList)
