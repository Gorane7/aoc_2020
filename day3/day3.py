import random
import math
import numpy as np

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    data = []

    for line in lines:
        data.append(line.strip())
        print(line)
    total = 1
    # [(3, 1)]
    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        count = 0
        x = 0
        y = 0
        while y < len(data):
            x += dx
            y += dy
            if x >= len(data[0]):
                x = x % len(data[0])
            if y >= len(data):
                break
            if data[y][x] == "#":
                count += 1
        total *= count
    print(total)
