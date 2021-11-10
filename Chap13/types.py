#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""Numeric functions"""
x = '47'
y = int(x)
z = float(x)
a = abs(x)
# Tuple of division and remainder
b = divmod(x, 3)
# complex
c = complex(x, 73)


print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
