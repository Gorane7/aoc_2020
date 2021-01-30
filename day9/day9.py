import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    data = list(map(int, lines))
    #data = list(map(lambda x: x.strip(), lines))
    sizeTry = 2
    target = 776203571
    while True:
        found = False
        for i in range(sizeTry, len(data)):
            if sum(data[i - sizeTry:i]) == target:
                print(data[i - sizeTry:i])
                print(min(data[i - sizeTry:i]) + max(data[i - sizeTry:i]))
                found = True
        sizeTry += 1
        if found:
            break
