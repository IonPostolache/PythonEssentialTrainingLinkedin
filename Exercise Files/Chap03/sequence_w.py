#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#x = ( 1, 2, 3, 4, 5 )
#x=list(range(6))
#x[2]=44

x={'one':1, 'two':2, 'three':3, 'four':4}
x['three']=44
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))
