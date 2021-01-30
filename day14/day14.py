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
    memory = {}
    mask = None
    maskControl = None
    maskValues = None
    # 6386593869035
    for line in data:
        split = line.split(" = ")
        if split[0] == "mask":
            maskControl = 0
            maskValues = 0
            mask = split[1]
            for char in mask:
                maskControl *= 2
                maskValues *= 2
                if char == '0' or char == '1':
                    maskControl += 1
                if char == '1':
                    maskValues += 1
        else:
            address = int(split[0][4:-1])
            addressString = ''
            for i in range(36):
                addressString += str((address // (2**i)) % 2)
            addressString = addressString[::-1]
            newAddress = ''
            xCount = 0
            value = int(split[1])
            for i in range(36):
                if mask[i] == 'X':
                    newAddress += 'X'
                    xCount += 1
                elif mask[i] == '1':
                    newAddress += '1'
                else:
                    newAddress += addressString[i]
            for i in range(2**xCount):
                actualAddress = 0
                thisI = i
                for j in range(36):
                    actualAddress *= 2
                    if newAddress[j] == 'X':
                        actualVal = thisI % 2
                        thisI = thisI // 2
                        actualAddress += actualVal
                    else:
                        actualAddress += int(newAddress[j])
                memory[actualAddress] = value
            #print(memory)
    total = 0
    for val in memory.values():
        total += val
    print(total)


