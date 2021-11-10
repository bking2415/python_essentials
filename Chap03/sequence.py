#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1, 2, 3, 4, 5]
# Changing value in list
x[2] = 42
# loop through list
for i in x:
    print('i is {}'.format(i))

# Tuple
# Cant change list
x = (1, 2, 3, 4, 5)
# loop through list
for i in x:
    print('i is {}'.format(i))

# range
x = range(1, 10)
# loop through list
for i in x:
    print('i is {}'.format(i))

# range
x = {'one': 1, 'two': 2}
# loop through list
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))
