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
    data = list(map(lambda x: x.strip(), lines))
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir = 1
    location = [0, 0]
    ilmakaared = ["N", "E", "S", "W"]
    waypoint = [10, 1]
    for line in data:
        if line[0] == "L":
            amount = int(line[1:]) // 90
            if amount == 1:
                waypoint = [-waypoint[1], waypoint[0]]
            elif amount == 2:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif amount == 3:
                waypoint = [waypoint[1], -waypoint[0]]
            else:
                print("Problem, L is " + str(amount))
        if line[0] == "R":
            amount = int(line[1:]) // 90
            if amount == 1:
                waypoint = [waypoint[1], -waypoint[0]]
            elif amount == 2:
                waypoint = [-waypoint[0], -waypoint[1]]
            elif amount == 3:
                waypoint = [-waypoint[1], waypoint[0]]
            else:
                print("Proble, R is " + str(amount))
        if line[0] in ilmakaared:
            index = ilmakaared.index(line[0])
            amount = int(line[1:])
            thisDir = dirs[index]
            waypoint[0] += thisDir[0] * amount
            waypoint[1] += thisDir[1] * amount
        if line[0] == "F":
            amount = int(line[1:])
            thisDir = waypoint
            location[0] += thisDir[0] * amount
            location[1] += thisDir[1] * amount

        print(f"Waypoint: {waypoint}")
        print(f"Location: {location}")
        print()
    print(location)
    print(sum([abs(x) for x in location]))

