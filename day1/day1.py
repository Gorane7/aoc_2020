import random
import math
import numpy as np


if __name__ == "__main__":
    #test = np.array([1, 2])
    #other = np.array([3, 4])
    #print(test + other)
    a = 0
    file = open("input.txt", "r")
    lines = list(sorted(map(lambda line: int(line), file.readlines())))
    low = 0
    up = len(lines) - 1

    for i in range(200):
        for j in range(i + 1, 200):
            for k in range(j + 1, 200):
                if lines[i] + lines[j] + lines[k] == 2020:
                    print(lines[i] * lines[j] * lines[k])
    while False:
        thisSum = lines[low] + lines[up]
        if thisSum == 2020:
            print(f"({lines[low]}; {lines[up]})")
            print(lines[low] * lines[up])
            break
        if thisSum > 2020:
            up -= 1
        if thisSum < 2020:
            low += 1
        if up == low:
            print("Not possible")
            break

    #print(a)
