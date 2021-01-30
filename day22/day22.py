import random
import math
import numpy as np
from functools import reduce
import string
#from console import Console

def recurse(card1, deck1, card2, deck2, depth):
    if len(deck1) < card1 or len(deck2) < card2:
        if card1 > card2:
            return 1
        return 2
    deck1copy = deck1[:card1]
    deck2copy = deck2[:card2]
    return game(deck1copy, deck2copy, depth + 1)[0]


def game(p1, p2, depth):
    round = 0
    history = set()
    while len(p1) > 0 and len(p2) > 0:
        gameState = ','.join([str(x) for x in p1]) + ':' + ','.join([str(x) for x in p2])
        if gameState in history:
            return 1, p1
        history.add(gameState)
        p1c = p1[0]
        p2c = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]
        winner = recurse(p1c, p1, p2c, p2, depth)
        if winner == 1:
            p1.append(p1c)
            p1.append(p2c)
        else:
            p2.append(p2c)
            p2.append(p1c)
        #print(p1)
        #print(p2)
        #print()
        print(' ' * depth + str(round))
        round += 1
        if len(p1) == 0:
            return 2, p2
        if len(p2) == 0:
            return 1, p1


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    counter = 1
    p1 = []
    p2 = []
    while True:
        if len(data[counter]) == 0:
            counter += 2
            break
        p1.append(int(data[counter]))
        counter += 1
    while True:
        if len(data[counter]) == 0:
            break
        p2.append(int(data[counter]))
        counter += 1
    print(p1)
    print(p2)

    winnersDeck = game(p1, p2, 0)[1]
    score = 0
    for i, sc in enumerate(winnersDeck[::-1]):
        score += (i + 1) * sc
    print(score)
