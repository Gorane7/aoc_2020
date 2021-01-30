import random
import math
import numpy as np
from functools import reduce
import string
# from console import Console

class Rule:
    def __init__(self, string, allRules, me):
        self.me = me
        self.allRules = allRules
        self.subRules = []
        self.possible = None
        split = string.split(" | ")
        for sub in split:
            subsplit = sub.split(" ")
            anded = []
            for subsub in subsplit:
                try:
                    inted = int(subsub)
                    anded.append(inted)
                except ValueError:
                    anded.append(subsub[1])
            self.subRules.append(anded)
        self.cache = {"": False}
        self.cacheSize = 10
        print(self.subRules)

    def matches(self, string, level):
        if string in self.cache.keys():
            return self.cache[string]
        #print("    " * level + string)
        for sub in self.subRules:
            if len(sub) == 1:
                if isinstance(sub[0], str):
                    if string == sub[0]:
                        #print("    " * level + "Ok")
                        self.cache[string] = True
                        return True
                else:
                    if self.allRules[sub[0]].matches(string, level + 1):
                        #print("    " * level + "Ok")
                        if len(string) < self.cacheSize:
                            self.cache[string] = True
                        return True
            elif len(sub) == 3:
                for i in range(1, len(string)):
                    for j in range(i + 1, len(string)):
                        aSize = i
                        bSize = j - i
                        cSize = len(string) - j
                        aSub = string[0:i]
                        bSub = string[i:j]
                        cSub = string[j:len(string)]
                        aRule = self.allRules[sub[0]]
                        bRule = self.allRules[sub[1]]
                        cRule = self.allRules[sub[2]]
                        comps = [[aSize, aSub, aRule], [bSize, bSub, bRule], [cSize, cSub, cRule]]
                        #print(comps)
                        comps = sorted(comps, key=lambda x: x[0])
                        if comps[0][2].matches(comps[0][1], level + 1) and comps[1][2].matches(comps[1][1], level + 1) and comps[2][2].matches(comps[2][1], level + 1):
                            if len(string) < self.cacheSize:
                                self.cache[string] = True
                            return True
            else:
                for i in range(0, len(string)):
                    if i < len(string) / 2:
                        #print(string)
                        #print(string[0:i] + string[i:len(string)])
                        #print()
                        if self.allRules[sub[0]].matches(string[0:i], level + 1) and self.allRules[sub[1]].matches(string[i:len(string)], level + 1):
                            #print("    " * level + "Ok")
                            if len(string) < self.cacheSize:
                                self.cache[string] = True
                            return True
                    else:
                        if self.allRules[sub[1]].matches(string[i:len(string)], level + 1) and self.allRules[sub[0]].matches(string[0:i], level + 1):
                            #print("    " * level + "Ok")
                            if len(string) < self.cacheSize:
                                self.cache[string] = True
                            return True
        if len(string) < self.cacheSize:
            self.cache[string] = False
        return False


    def genRecursivePossible(self, depthLeft, possibleSoFar):
        print(depthLeft)
        if depthLeft == -1:
            self.possible = possibleSoFar
            return possibleSoFar
        for sub in self.subRules:
            if self.me in sub and depthLeft == 0:
                continue
            possibleSoFar += self.genFromSingle(sub)
        return self.genRecursivePossible(depthLeft - 1, possibleSoFar)

    def genPossible(self):
        if self.possible is not None:
            return self.possible
        self.possible = []
        for sub in self.subRules:
            self.possible += self.genFromSingle(sub)
        return self.possible

    def genFromSingle(self, subRule):
        rulesFromFirst = self.allRules[subRule[0]].genPossible() if isinstance(subRule[0], int) else [subRule[0]]
        rulesFromSecond = (self.allRules[subRule[1]].genPossible() if isinstance(subRule[1], int) else [subRule[1]]) if len(subRule) > 1 else ['']
        all = []
        for a in rulesFromFirst:
            for b in rulesFromSecond:
                all.append(a + b)
        return all

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    rules = []
    cases = []
    counter = 0
    while True:
        if len(data[counter]) == 0:
            counter += 1
            break
        rules.append(data[counter])
        counter += 1
    while counter < len(data):
        cases.append(data[counter])
        counter += 1

    rulesDict = {}
    for rule in rules:
        split = rule.split(": ")
        rulesDict[int(split[0])] = Rule(split[1], rulesDict, int(split[0]))

    counter = 0
    for i, line in enumerate(cases):
        print(i / len(cases))
        #print(len(line))
        #print()
        if rulesDict[0].matches(line, 0):
            counter += 1
    print(counter)
    #print()
    #print(rulesDict[0].matches("babbbbababbbababaabaabab", 0))


    exit()
    print(val.genPossible())
    print()
    print(rulesDict[31].possible)
    print(rulesDict[42].possible)
    rulesDict[8].genRecursivePossible(1, [])
    print(len(rulesDict[8].possible))
    print(len(set(rulesDict[8].possible)))
    print(len(rulesDict[42].possible))
    #print(rulesDict[8].possible)
    #rulesDict[11].genRecursivePossible(1, [])
    #print(len(rulesDict[11].possible))
    exit()
    possible = set(rulesDict[1].genPossible())
    counter = 0
    for line in cases:
        if line in possible:
            counter += 1
    print(counter)