#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten(5, 6, 7)
    print(f'in main: x in {x}')
    print(type(x), x)


def kitten(a, b, c):
    y = a + 2
    print(f'{y, b, c}: Meow.')
    return 41


if __name__ == '__main__': main()
