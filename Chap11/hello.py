#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hello, World.')
print(s)
# Upper case
print('Hello, World.'.upper())
# Capitalize the fist letter in word
print('Hello, World.'.capitalize())
# Title case
print('Hello, World.'.title())
# Swap case
print('Hello, World.'.swapcase())
# casefold case (works like lower
print('Hello, World.'.casefold())
# Format
print('Hello, World. {}'.format(42 * 7))

# Concat 2 strings
s1 = 'Hello, World.'
s2 = 'this is another string.'

print (s1 + ' ' + s2)

# Format strings (String interpolation)
x = 42
y = 73
print('the number is {} {}'.format(x, y))

z = 42 * 747 * 10000
print('the number is {:,f}'.format(z))