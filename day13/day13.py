import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    #data = list(map(lambda x: x.strip(), lines))
    # time = int(lines[0])
    ids = []
    idDict = {}
    indices = []
    for i, thing in enumerate(lines[1].split(',')):
        if 'x' in thing:
            ids.append(None)
            continue
        ids.append(int(thing))
        idDict[i] = int(thing)
        indices.append(i)
    arv = 0
    cycleSize = 1
    start = 1
    for i in indices:
        deltaMod = cycleSize % idDict[i]
        counter = 0
        while True:
            inStart = start + counter * cycleSize
            if (inStart + i) % idDict[i] == 0:
                break
            counter += 1
        start = start + counter * cycleSize
        counter = 1
        while True:
            inStart = start + counter * cycleSize
            if (inStart + i) % idDict[i] == 0:
                break
            counter += 1
        cycleSize *= counter
        #print(start)
        #print(cycleSize)
        #print()
    print(start)
    #print(cycleSize)