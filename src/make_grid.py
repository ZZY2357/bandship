# make_grid.py
# 用来创建二维地图

import random


def make2dArray(rows, cols, defult=0):
    array = []
    for i in range(rows):
        array.append([])
        for j in range(cols):
            array[i].append(defult)
    return array


def putMap(grid, shipLength, shipCount):
    heads = ['up', 'right', 'down', 'left']
    for i in range(shipCount):
        x = random.randint(0, len(grid[0]) - 1)
        y = random.randint(0, len(grid) - 1)
        # 可以为所欲为地放的坐标
        if x >= shipLength and x <= len(grid[0]) - shipLength and y >= shipLength and y <= len(grid) - shipLength:
            head = random.choice(heads)
        elif x == 0:
            head = 'right'
        elif x > len(grid[0]) - shipLength:
            head = 'left'
        elif y == 0:
            head = 'down'
        else:
            head  = 'up'
        putShip(grid, x, y, shipLength, head)



def putShip(map, x, y, length, head='right'):
    try:
        if head == 'right':
            for i in range(length):
                map[y][x + i] = 1
        elif head == 'down':
            for i in range(length):
                map[y + i][x] = 1
        elif head == 'left':
            for i in range(length):
                map[y][x - i] = 1
        elif head == 'up':
            for i in range(length):
                map[y-i][x] = 1
    except:
        pass