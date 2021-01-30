import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

def noGapOfTwo(subList):
    return True

def evalWithNoThreeGaps(subList):
    if len(subList) <= 2:
        return 1
    if len(subList) == 3:
        return 2
    if len(subList) == 4:
        return 4
    if len(subList) == 5:
        return 7
    print("Problem: " + str(len(subList)))
    return 1

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    data = list(map(int, lines))
    #data = list(map(lambda x: x.strip(), lines))
    data = sorted(data)
    data = [0] + data + [data[-1] + 3]
    print(data)
    splitAtThrees = []
    cache = []
    last = -1
    for el in data:
        if el - last == 3:
            splitAtThrees.append(cache)
            cache = []
        last = el
        cache.append(last)
    splitAtThrees.append(cache)
    total = 1
    for subProblem in splitAtThrees:
        print(subProblem)
        total *= evalWithNoThreeGaps(subProblem)
    print(total)
