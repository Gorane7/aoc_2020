import random
import math
import numpy as np
from functools import reduce
import string
# from console import Console

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    allergenDict = {}
    allFoods = []
    for line in data:
        splited = line.split(" (contains ")
        foods = splited[0].split(" ")
        allFoods = allFoods + foods
        allergens = splited[1].strip(")").split(", ")
        for allergen in allergens:
            if allergen in allergenDict.keys():
                allergenDict[allergen] = allergenDict[allergen].intersection(set(foods))
            else:
                allergenDict[allergen] = set(foods)
        #print(allergens)
    forSure = {}
    for i in range(4):
        for key, value in allergenDict.items():
            if len(value) == 1:
                forSure[key] = list(value)[0]
                for key2, value2 in allergenDict.items():
                    if forSure[key] in value2:
                        value2.remove(forSure[key])
    print(allergenDict)
    print(forSure)
    allergenSet = set()
    for val in forSure.values():
        allergenSet.add(val)
    counter = 0
    for food in allFoods:
        if food not in allergenSet:
            counter += 1
    print(counter)
    items = forSure.items()
    print(items)
    sortedItems = sorted(items, key=lambda x: x[0])
    print(sortedItems)
    print(','.join(list(map(lambda x: x[1], sortedItems))))
