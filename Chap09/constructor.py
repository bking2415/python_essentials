#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    def __init__(self, **kwargs):
        self._a_type = kwargs['a_type'] if 'a_type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    def type(self):
        return self._a_type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(a_type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(a_type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(a_type='velociraptor', name='veronica', sound='hello'))
    # Default values
    print_animal(Animal())


if __name__ == '__main__': main()
