#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # List
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1:5:2])
    # search a list
    i = game.index('Paper')
    print(i)
    # append to list
    game.append('Computer')
    # insert a item
    game.insert(0, 'Go')
    # Remove an item
    game.remove('Scissors')
    # Remove item form the end of the list
    x = game.pop()
    print(x)
    # Join the list object
    print(','.join(game))
    print_list(game)


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


if __name__ == '__main__':
    main()
