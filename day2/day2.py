import random
import math
import numpy as np

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    data = []
    times = 0
    for line in lines:
        a = line.split(": ")
        pol = a[0].split(" ")
        timesa = pol[0].split("-")
        mini = int(timesa[0])
        maxi = int(timesa[1])
        letCount = 0
        isFirst = a[1][mini - 1] == pol[1]
        isSecond = a[1][maxi - 1] == pol[1]
        if isFirst and not isSecond or isSecond and not isFirst:
            times += 1
    print(times)
