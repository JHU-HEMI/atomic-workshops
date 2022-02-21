#!/usr/bin/env python

class Node():

    def __str__(self):  
            return '%d %s %s'%(self.value,str(self.left),str(self.right))

    def __init__(self,value = None,right = None,left = None):
        self.value = value
        self.right = right
        self.left = left

    def repeat(self,value):
        print('%s already in tree'%value)


    def insert(self,value):
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)

            else:
                self.left = Node(value)

        elif value == self.value:
            self.repeat(value)


    def find_value(self,value):
        if value == self.value:
            print('%s is in tree'%value)
        elif value > self.value:
            self.right.find_value(value)
        elif value < self.value:
            self.left.find_value(value)




