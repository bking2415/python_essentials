#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

"""String functions"""


class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'the number of bunnier is {self._n}'

    def __str__(self):
        return f'str: the number of bunnier is {self._n}'


st = bunny(47)
s = 'Hello, World.'
print(st)
print(repr(st))
# windows reading
print(ascii(st))
# character function for emojis
print(chr(128406))

"""Container functions"""

x = (1, 2, 3, 4, 5)
# Reverse
y = reversed(x)
for i in y:
    print(i)
# Sum
y = sum(x, 10)
# Max or Min
y = max(x)
# Any value is true
y = any(x)
# Zip
y = reversed(x)
z = zip(x, y)
for a, b in z:
    print(f'{a} - {b}')
# Enumerate
x = ('cat', 'dog', 'rabbit', 'velociraptor')
for a, b in enumerate(x):
    print(f'{a} : {b}')
print(x)
print(y)

"""Object and Class functions"""

x = 42
y = type(x)
ii = isinstance(x, int)
i_d = id(x)
print(x)
print(y)
