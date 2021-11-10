#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

if False:
    print('if true')
elif False:
    print('elif 1 true')
elif False:
    print('elif 2 true')
elif True:
    print('elif 3 true')
elif False:
    print('elif 4 true')
else:
    print('neither true')

# Kind of like a case function
x = 4

if x == 0:
    print('zero true')
elif x == 1:
    print('1 true')
elif x == 2:
    print('2 true')
elif x == 3:
    print('3 true')
elif x == 4:
    print('4 true')
else:
    print('neither true')
