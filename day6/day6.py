import random
import math
import numpy as np
from functools import reduce
import string

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    groups = []
    rawGroups = []
    currentGroup = ""
    currentRaw = []
    for line in data:
        if line == "":
            groups.append(currentGroup)
            rawGroups.append(currentRaw)
            currentGroup = ""
            currentRaw = []
            continue
        currentGroup += line
        currentRaw.append(line)
    total = 0
    for group, rawGroup in zip(groups, rawGroups):
        correct = string.ascii_lowercase
        for line in rawGroup:
            newCorrect = ""
            for letter in correct:
                if letter in line:
                    newCorrect += letter
            correct = newCorrect
        print(correct)
        total += len(correct)
    print(total)