#!/usr/bin/python
"""
Calculate the return on a single round of tech investment.

If you invest N, you get a normal distribution around log(N+1) base 10, with
sigma 0.5

Takes as input two command line arguments:

tech_invest.py <current> <amount>

And prints out the new level.  Levels have precision to 0.1, but amounts can
only be invested in whole units.
"""

import math
import random
import sys

SIGMA = .5

def invest(cur_level, amount):
    return cur_level + round(random.gauss(math.log(amount+1, 10), SIGMA), 1)
                                  

if __name__ == '__main__':
    _ignore, cur_level, amount = sys.argv
    for _i in range(10):
        print invest(float(cur_level), int(amount)) 
