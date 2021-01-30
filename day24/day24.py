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
    tiles = set()
    for line in data:
        tile = [0, 0, 0]
        cache = ''
        for char in line:
            if cache == '':
                if char == 'e':
                    tile[0] += 1
                elif char == 'w':
                    tile[0] -= 1
                else:
                    cache = char
            elif cache == 'n':
                if char == 'e':
                    tile[1] += 1
                elif char == 'w':
                    tile[2] -= 1
                cache = ''
            elif cache == 's':
                if char == 'e':
                    tile[2] += 1
                elif char == 'w':
                    tile[1] -= 1
                cache = ''
            else:
                print('Problem')
        thisTile = (tile[0] + tile[2], tile[0] + tile[1], tile[1] - tile[2])
        if thisTile in tiles:
            tiles.remove(thisTile)
        else:
            tiles.add(thisTile)
    deltas = [(0, 0, 0), (0, 1, 1), (1, 1, 0), (1, 0, -1), (0, -1, -1), (-1, -1, 0), (-1, 0, 1)]
    print(len(tiles))
    for tile in tiles:
        print(tile)
    print()
    for i in range(100):
        newTiles = {}
        for tile in tiles:
            for delta in deltas:
                thisTile = (tile[0] + delta[0], tile[1] + delta[1], tile[2] + delta[2])
                if thisTile in newTiles.keys():
                    continue
                neighbourCount = 0
                for delta2 in deltas[1:]:
                    neighbour = (thisTile[0] + delta2[0], thisTile[1] + delta2[1], thisTile[2] + delta2[2])
                    if neighbour in tiles:
                        neighbourCount += 1
                if thisTile in tiles:
                    if neighbourCount == 0 or neighbourCount > 2:
                        newTiles[thisTile] = False
                    else:
                        newTiles[thisTile] = True
                else:
                    if neighbourCount == 2:
                        newTiles[thisTile] = True
                    else:
                        newTiles[thisTile] = False
        newTileSet = set()
        for key, val in newTiles.items():
            #print(key, val)
            if val:
                newTileSet.add(key)
        #break
        tiles = newTileSet
        print(len(tiles))
