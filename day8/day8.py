import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

def detectLoop(console):
    if console.index in console.commandHistory:
        #print(f"About to execute repeating command, accumulator: {console.accumulator}")
        console.running = False

def printAccValue(console):
    print(console.accumulator)

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    for i in range(len(lines)):
        program = Console(lines, [detectLoop, printAccValue])
        program.switch("jmp", "nop", i)
        program.run()