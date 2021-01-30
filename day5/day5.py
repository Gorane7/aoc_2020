import random
import math
import numpy as np
from functools import reduce

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    maxi = 0
    allIds = [i for i in range(128 * 8)]
    givenIds = []
    for line in lines:
        rowMin = 0
        rowMax = 128
        colMin = 0
        colMax = 8
        for letter in line:
            if letter == "F":
                rowMax = (rowMin + rowMax) // 2
            if letter == "B":
                rowMin = (rowMin + rowMax) // 2
            if letter == "L":
                colMax = (colMin + colMax) // 2
            if letter == "R":
                colMin = (colMin + colMax) // 2
        id = rowMin * 8 + colMin
        givenIds.append(id)
        allIds.remove(id)
    mine = []
    for missing in allIds:
        if missing - 1 in givenIds and missing + 1 in givenIds:
            mine.append(missing)
    print(mine)
