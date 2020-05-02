#!/usr/bin/env python3

from typing import List

"""
  This module implement functions for sorted Arrays
"""

def index(sarr: List, e: int) -> int:
    q = len(sarr)
    if q == 0:
        return None
    pos = q // 2
    m = sarr[pos]
    print("pos = {}, m = {}".format(pos, m))
    if m == e:
        return pos
    elif m > e:
        return index(sarr[:pos], e)
    else:
        try:
            return pos + 1 + index(sarr[pos+1:], e)
        except:
            return None

def elem(e: int, sarr: List) -> bool:
    a = 0
    b = len(sarr) - 1
    q = b - a
    while (q > 1):
        pos = q // 2
        if sarr[pos] == e:
            return True
        elif sarr[pos] > e:
            b = pos - 1
        else:
            a = pos + 1
        q = b - a
    return (b >= 0 and (sarr[a] == e or sarr[b] == e))
            

