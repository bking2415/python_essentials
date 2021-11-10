#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
y = 'seven'.capitalize()

# String types
print('x is {}'.format(x))
print(type(x))
print('y is {}'.format(y))
# Leading variables
print('"{1:>09}" "{0:<09}"'.format(8, 9))
print(type(y))

# Numeric types
from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

# Bool Type
x = False
print('x is {}'.format(x))
print(type(x))

bol = 0
if bol:
    print("True")
else:
    print("False")

# Type vs. Id
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(type(y))
print(id(x))
print(id(y))

if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print('list')
else:
    print('no')

