#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    # Random number
    x = random.randint(1, 1000)
    print(x)
    # Random list of numbers
    rand = [random.randint(1, 1000) for x in range(1000)]
    print(rand)
    # Date
    now = datetime.datetime.now()
    print(now)
    print(f'{now.month}-{now.day}-{now.year}')


if __name__ == '__main__':
    main()
