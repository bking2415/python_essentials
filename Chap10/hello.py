#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys


def main():
    # ValueError
    try:
        x = 5 / 0
    # Value Error
    except ValueError:
        print('I caught a ValueError')
    # Division by zero
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    # Unknown error
    except:
        print(f'unknown error: {sys.exc_info()[1]}')
    else:
        print('good job')
        print(x)


if __name__ == '__main__':
    main()
