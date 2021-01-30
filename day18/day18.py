import random
import math
import numpy as np
from functools import reduce
import string
from console import Console

class Comp:
    def __init__(self, parent):
        self.parts = []
        self.parent = parent
        self.current = self

    def addChar(self, char):
        if self.current != self:
            self.current.addChar(char)
            return
        if char == "(":
            new = Comp(self)
            self.parts.append(new)
            self.current = new
            return
        if char == ")":
            self.parent.current = self.parent
            return
        if char == " ":
            return
        if char in "0123456789":
            if len(self.parts) == 0 or not isinstance(self.parts[-1], str) or self.parts[-1] in "+*":
                self.parts.append(char)
            else:
                self.parts[-1] = self.parts[-1] + char
            return
        self.parts.append(char)

    def __repr__(self):
        return str(self.parts)

    def compute(self):
        numbers = self.parts[2::2]
        symbols = self.parts[1::2]
        running = self.evali(self.parts[0])
        newNumbers = []
        newSymbols = []
        for symbol, number in zip(symbols, numbers):
            if symbol == '+':
                running += self.evali(number)
            elif symbol == '*':
                newNumbers.append(running)
                newSymbols.append('*')
                running = self.evali(number)
            else:
                print("Problem")
        newNumbers.append(running)
        print(newSymbols)
        print(newNumbers)
        total = reduce(lambda a, b: a * b, newNumbers)
        print(str(self.parts) + " = " + str(total))
        return total

    def evali(self, smt):
        return int(smt) if isinstance(smt, str) else smt.compute()

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    total = 0
    for line in data:
        comp = Comp(None)
        for char in line:
            comp.addChar(char)
        total += comp.compute()
    print(total)
