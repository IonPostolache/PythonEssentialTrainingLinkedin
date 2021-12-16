#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    #for k, v in animals.items():
        #print(f'{k} is the key and {v} is the value')
    for k in animals.keys():
        print(k)
    for v in animals.values():
        print(v)
    animals['monkey']='haha'
    print('lion' in animals)
    print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k} is key, {v} is value')

if __name__ == '__main__': main()
