#!/usr/bin/python
"""
Calcuate revenue for a given player's set of planets

Can be called with a filename or with data piped to stdio.

Expects input as one planetary population per line, with blank lines
separating empire provinces.  E.g.

3
7
2

8
2

Would be two provinces, one with 3 planets (populations 3, 7 and 2), and one
with 2 planets (populations 8 and 2).

The script ignores any data after a number + whitespace, so the planets can
be named if that makes them easier to track.

Revenue for each planet is: population * log2(planets in province+1)
"""

import math
import re
import sys
from StringIO import StringIO

test_file = StringIO("""
3 Askelon
7 Beta Tauri
2 Crempl

8 Diadoumos
2 Euphria
""")

pop_re = re.compile(r'^(\d+)')

def total_revenue(file_obj):
    """
    Revenue calculated as described in module docstring (an integer is
    returned -- the ceiling of the exact number)
    """
    return int(math.ceil(sum(map(province_revenue,
                                 break_into_provinces(file_obj)))))

def province_revenue(province):
    """
    Revenue for a single province
    """
    multiplier = math.log(len(province)+1,2)    

    return sum(multiplier*p for p in province)

def break_into_provinces(file_obj):
    """
    Given a file object with the described format, return a list of
    provinces, where each province is a list of populations
    """
    provinces = []
    cur_province = None
    for line in file_obj:
        m = pop_re.match(line)
        if m:
            if cur_province == None:
                cur_province = []
                provinces.append(cur_province)
            cur_province.append(int(m.group(1)))
        else:
            cur_province = None
    return provinces

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_obj = open(sys.argv[1], 'r')
    else:
        input_file_obj = sys.stdin

    print "Total revenue is: %s" % total_revenue(input_file_obj)
            
