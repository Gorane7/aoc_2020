import random
import math
import numpy as np
from functools import reduce
import string
#from console import Console

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    #data = list(map(int, lines))
    data = list(map(lambda x: x.strip(), lines))
    cups = []
    nodes = {}
    lastNode = None
    firstNode = None
    current = None
    for char in data[0]:
        node = Node(int(char))
        nodes[int(char)] = node
        if lastNode is None:
            lastNode = node
            firstNode = node
            current = node
            continue
        lastNode.right = node
        node.left = lastNode
        lastNode = node
    for i in range(10, 1000001):
        node = Node(i)
        nodes[i] = node
        lastNode.right = node
        node.left = lastNode
        if i == 1000000:
            node.right = firstNode
            firstNode.left = node
        lastNode = node
    mini = min(nodes.keys())
    maxi = max(nodes.keys())
    print("Here")

    for i in range(10000000):
        if i % 100000 == 0:
            print(i / 10000000)
        toMove = []
        toMove.append(current.right)
        toMove.append(current.right.right)
        toMove.append(current.right.right.right)
        forbidden = list(map(lambda x: x.value, toMove))
        target = current.value - 1
        while target not in nodes.keys() or target in forbidden:
            target -= 1
            if target < mini:
                target = maxi
        targetNode = nodes[target]
        current.right = current.right.right.right.right
        current.right.left = current
        afterTarget = targetNode.right
        targetNode.right = toMove[0]
        toMove[0].left = targetNode
        toMove[2].right = afterTarget
        afterTarget.left = toMove[2]
        current = current.right

    start = nodes[1]
    print(start.right.value)
    print(start.right.right.value)
    print(start.right.value * start.right.right.value)

