import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

def nearbySeats(i, j, seats):
    nearby = []
    for di in range(3):
        for dj in range(3):
            if di == 1 and dj == 1:
                continue
            power = 0
            while True:
                power += 1
                thisI = i + (di - 1) * power
                thisJ = j + (dj - 1) * power
                if thisI < 0 or thisJ < 0 or thisI >= len(seats) or thisJ >= len(seats[0]):
                    break
                if seats[thisI][thisJ] != ".":
                    nearby.append(seats[thisI][thisJ])
                    break
    #print(nearby)
    return nearby

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    oldSeats = data
    while True:
        newSeats = []
        stateChanges = 0
        for i in range(len(oldSeats)):
            thisString = ""
            for j in range(len(oldSeats[0])):
                if oldSeats[i][j] == ".":
                    thisString += "."
                    continue
                if oldSeats[i][j] == "L":
                    if "#" not in nearbySeats(i, j, oldSeats):
                        thisString += "#"
                        stateChanges += 1
                    else:
                        thisString += "L"
                    continue
                if oldSeats[i][j] == "#":
                    #print(nearbySeats(i, j, oldSeats))
                    if nearbySeats(i, j, oldSeats).count("#") >= 5:
                        thisString += "L"
                        stateChanges += 1
                    else:
                        thisString += "#"
            newSeats.append(thisString)
        print(stateChanges)
        if stateChanges == 0:
            break
        oldSeats = newSeats
    print(oldSeats)
    print(sum([x.count("#") for x in oldSeats]))
