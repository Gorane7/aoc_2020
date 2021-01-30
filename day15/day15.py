import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

if __name__ == "__main__":
    file = open("input.txt", "r")
    #lines = file.readlines()
    #data = list(map(int, lines))
    #data = list(map(lambda x: x.strip(), lines))
    starting = [1,0,15,2,10,13]
    history = []
    historySet = set()
    historyDict = {}
    temp = None
    for i in range(30000000):
        if i % 1000 == 0:
            print(i / 30000000)
        if len(history) < len(starting):
            number = starting[len(history)]
            history.append(number)
            if temp is not None:
                historySet.add(temp)
                historyDict[temp] = i - 1
            temp = number
            continue

        last = temp
        count = 0
        #print("Iter")
        #print(last)
        if last not in historySet:
            #print("Here")
            history.append(0)
            historySet.add(temp)
            historyDict[temp] = i - 1
            temp = 0
            continue
        lastIt = historyDict[temp]
        count = i - 1 - lastIt
        history.append(count)
        historySet.add(temp)
        historyDict[temp] = i - 1
        temp = count
    print(history[-1])
    #print(history)
    #print(historySet)
