import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

def nearbySeats(i, j, z, w):
    nearby = []
    for di in range(3):
        for dj in range(3):
            for dz in range(3):
                for dw in range(3):
                    if di == 1 and dj == 1 and dz == 1 and dw == 1:
                        continue
                    power = 1

                    thisI = i + (di - 1) * power
                    thisJ = j + (dj - 1) * power
                    thisZ = z + (dz - 1) * power
                    thisW = w + (dw - 1) * power
                    nearby.append((thisI, thisJ, thisZ, thisW))
    #print(nearby)
    return nearby

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    oldSeats = data
    active = set()
    for i in range(len(oldSeats)):
        for j in range(len(oldSeats[0])):
            if (oldSeats[i][j] == "#"):
                active.add((i, j, 0, 0))
    for i in range(6):
        neighbours = {}
        stateChanges = 0

        for seat in active:
            for neighbour in nearbySeats(seat[0], seat[1], seat[2], seat[3]):
                if neighbour not in neighbours.keys():
                    neighbours[neighbour] = 0
                neighbours[neighbour] += 1
        newActive = set()
        for loc, amount in neighbours.items():
            if loc in active:
                if amount == 2 or amount == 3:
                    newActive.add(loc)
            else:
                if amount == 3:
                    newActive.add(loc)
        active = newActive
    print(active)
    print(len(active))
