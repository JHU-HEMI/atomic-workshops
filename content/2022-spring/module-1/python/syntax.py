#!/usr/bin/env python

print('hello world')

# ints
a = 1
b = 2
c = a + b
print('c = ' + str(c))

# floats
d = 3.
e = 2.
f = d / e
print('f = ' + str(f))

# strings
string = 'I am a string of characters'
print(string)

# booleans
a = True
b = False
c = None
print(a == b)
print(d > e)
print(a is b)

# lists
l = [1, 2, 3]
print(l[0])
print(l[-1])

# dictionaries
d = {
  'school': 'Hopkins',
  'class': 'ATOMIC',
}

# files (explicit open/close)
f = open('syntax.py', 'r') # w, a
text = f.read()
print(text)
f.close()

# files (more foolproof)
with open('syntax.py', 'r') as f:
  counter = 0
  for line in f:
    print('%d: %s' % (counter, line))
    counter += 1
  print('eof')

# loops (for)
print(l)
for element in l:
  print(element)

print(d)
for key in d:
  print(key, d[key])

for i in range(10, 20):
  print(i)

# loops (while)
print()
a = 10
while a < 20:
  print(a)
  a += 2

# functions
def get_input():
  I = input('Type something: ')
  return I

inputted_text = get_input()
print(inputted_text)

def check_length(string):
  if len(string) < 1:
    print('Empty')
  elif len(string) < 2:
    print('Character')
  else:
    print('String')

check_length(get_input())





