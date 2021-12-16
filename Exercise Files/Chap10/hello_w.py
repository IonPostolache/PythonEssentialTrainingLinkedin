#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

def main():
    try:
        #x=int("guu")
        x=5/0
    except ValueError:
        print('I caught a ValueError!')
    #except ZeroDivisionError:
        #print("Don't divide by zero!")
    except:
        print(f"unknown error: {sys.exc_info()}")
        print(f"unknown error: {sys.exc_info()[1]}")

    else:
        print(x)

if __name__ == '__main__': main()
