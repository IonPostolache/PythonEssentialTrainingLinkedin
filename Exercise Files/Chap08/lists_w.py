#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    #print(game[1:6:2])
    i=game.index('Paper')
    print(i)
    game.append('Computer')
    game.insert(0, "Bamboo")
    game.remove("Paper")
    game.pop(1)

    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
