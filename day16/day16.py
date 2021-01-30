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
    rules = []
    counter = -1
    while True:
        counter += 1
        line = data[counter]
        if line == '':
            break
        dat = line.split(": ")
        ranges = dat[1].split(" or ")
        ranges[0] = ranges[0].split("-")
        ranges[1] = ranges[1].split("-")
        ranges[0][0] = int(ranges[0][0])
        ranges[0][1] = int(ranges[0][1])
        ranges[1][0] = int(ranges[1][0])
        ranges[1][1] = int(ranges[1][1])
        rules.append([dat[0], ranges[0], ranges[1]])
    print(rules)
    counter += 2
    myTicket = list(map(lambda x: int(x), data[counter].split(',')))
    counter += 2
    print(myTicket)
    print(data[counter])
    nearby = []
    while True:
        counter += 1
        if counter == len(data) or data[counter] == '':
            break
        nearby.append(list(map(lambda x: int(x), data[counter].split(","))))
    print(nearby)
    errorTotal = 0
    correctTickets = []
    fieldsCanBe = []
    for ticket in nearby:
        isCorrect = True
        for j, number in enumerate(ticket):
            isIn = False
            for i, rule in enumerate(rules):
                if rule[1][0] <= number <= rule[1][1] or rule[2][0] <= number <= rule[2][1]:
                    isIn = True
            if not isIn:
                errorTotal += number
                isCorrect = False
        if isCorrect:
            correctTickets.append(ticket)
    print(errorTotal)
    print(len(nearby))
    print(len(correctTickets))
    fieldsCanBe = []
    for a, ticket in enumerate(correctTickets):
        for j, number in enumerate(ticket):
            canBe = set()
            for i, rule in enumerate(rules):
                if rule[1][0] <= number <= rule[1][1] or rule[2][0] <= number <= rule[2][1]:
                    canBe.add(i)
            if a == 0:
                fieldsCanBe.append(canBe)
            else:
                fieldsCanBe[j] = fieldsCanBe[j].intersection(canBe)
        #print(fieldsCanBe)
    print(fieldsCanBe)
    for i in range(len(fieldsCanBe)):
        fieldsCanBe[i] = [i, fieldsCanBe[i]]
    print(fieldsCanBe)
    fieldsCanBe = sorted(fieldsCanBe, key=lambda x: len(x[1]))
    print(fieldsCanBe)
    answers = []
    for i in range(len(fieldsCanBe)):
        if len(fieldsCanBe[i][1]) > 1:
            print("PROBLEM")
            print(fieldsCanBe[i])
            break
        value = fieldsCanBe[i][1].pop()
        for j in range(i + 1, len(fieldsCanBe)):
            if value in fieldsCanBe[j][1]:
                fieldsCanBe[j][1].remove(value)
        answers.append([fieldsCanBe[i][0], value])
    print(answers)
    answer = 1
    print(myTicket)
    for i, rule in enumerate(rules):
        if 'departure' in rule[0]:
            for pair in answers:
                if (pair[1] == i):
                    print(answer)
                    answer *= myTicket[pair[0]]
    print(answer)
