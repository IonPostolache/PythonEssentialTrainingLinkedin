#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n, y):
    print(n, y)

function(47, 5)


def function(n=1):
    print(n)

function(47)


def function(n=1):
    print(n)
    return n*2

x=function(47)
print(x)