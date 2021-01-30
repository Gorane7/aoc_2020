import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

if __name__ == "__main__":
    #file = open("input.txt", "r")
    #lines = file.readlines()
    #data = list(map(int, lines))
    #data = list(map(lambda x: x.strip(), lines))
    pub1 = 1717001
    pub2 = 523731
    current = 7
    cycles = 0
    while current != pub1:
        current = current * current
        current = current % 20201227
        cycles += 1
        if cycles % 100 == 0:
            print(cycles)
    print(cycles)
    for i in range(201071):
        pub2 = pub2 * pub2
        pub2 = pub2 % 20201227
    print(pub2)