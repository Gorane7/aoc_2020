import random
import math
import numpy as np
from functools import reduce
import string

def search(bagDict, possibleContainers, searchFor, nest):
    #print(nest)
    for key, value in bagDict.items():
        if searchFor in value:
            if key not in possibleContainers:
                possibleContainers.append(key)
                search(bagDict, possibleContainers, key, nest + 1)

def dfs(bagDict, searchFor, currentPath, paths, visited):
    for key, value in bagDict.items():
        thisPath = currentPath[:] + [key]
        if searchFor in value:
            paths.append(thisPath)
        visited.append(key)
        for inner in value:
            if inner not in visited:
                print(inner)
                dfs(bagDict, searchFor, thisPath, paths, visited)

def count(bagAmounts, searchFor, path):
    total = 0
    for key, value in bagAmounts[searchFor].items():
        thisPath = path[:] + [str(value) + " " + key]
        total += value
        if key == "other":
            total += 0
        else:
            total += value * count(bagAmounts, key, thisPath)
    return total

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(".\n"), lines))
    bagDict = {}
    bagAmounts = {}
    for line in data:
        #print(line)
        split = line.split(" bags contain ")
        container = split[0]
        #print(split[1].split(", "))
        inners = list(map(lambda x: x.replace(" bags", "").replace(" bag", ""), split[1].split(", ")))
        #print(inners)
        bagDict[container] = inners

    for key, value in bagDict.items():
        #print(value)
        bagDict[key] = [" ".join(x.split(" ")[1:]) for x in value]
        bagAmounts[key] = {}
        for bagType in value:
            splitted = bagType.split(" ")
            bagAmounts[key][" ".join(splitted[1:])] = int(splitted[0]) if splitted[0] != "no" else 0
    canContain = []
    search(bagDict, canContain, "shiny gold", 0)
    for item in canContain:
        pass
        #search(bagDict, canContain, item, 0)
    print("Test")
    print(len(bagDict))
    print(len(canContain))
    print("shiny gold" in canContain)
    amount = count(bagAmounts, "shiny gold", ["1 shiny gold"])
    print(amount)
