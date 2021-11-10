#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    # List comprehension
    seq2 = [x * 2 for x in seq]
    # List comprehension using IF
    seq3 = [x for x in seq if x % 3 == 0]
    # List comprehension using tuple
    seq4 = [(x, x ** 2) for x in seq]
    # List comprehension using function
    from math import pi
    seq5 = [round(pi, i) for i in seq]
    # List comprehension to create dictionary
    dict1 = {x: x ** 2 for x in seq}
    # List comprehension to create set
    set1 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print_list(dict1)
    print_list(set1)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__': main()
