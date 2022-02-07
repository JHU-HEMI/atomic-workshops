#!/usr/bin/env python3

# This program asks the user how many random numbers they want, then outputs $
import random

numTot=input('How many numbers would you like? ')
testNum=numTot.isdigit()
if testNum == True:
    randomList=[]
    for i in range(int(numTot)):
        randomList.append(random.random())
else:
    print('The input was not a number. Exiting program.')
    quit()

with open('randNums.csv','w') as f:
    for i in range(int(numTot)):
        f.write("%f" % (randomList[i]))
        if i != int(numTot) - 1:
            f.write(", ")