#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#x = (1, 2, 3, 4, 5)
x=(1, 'two', 3.0, [4, 'four'], True)
y=[1, 'two', 3.0, [4, 'four'], True]

print('x is {}'.format(x))
print(type(x))
#print(type(x[1]))
print(id(x))
print(id(y))

var=type(x)
print(var)
if var==tuple:
    print('it is a tuple')
"""
if x[0] is y[0]:
    print("yep")
else:
    print("nope")
    
"""
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')
