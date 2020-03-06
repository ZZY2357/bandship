import os

import render
import make_grid
import think_user

map = []
guessMap = []
mapRows = 7
mapCols = 7
shipLength = 3
shipCount = 3
round = 1
score = 0

def gameHello():
    print('''                      *       *       **       
****                  *       *                
*   *  ***  ****   ****  ***  ****  ***   **** 
*   *     * *  *  *   * *     *  *    *   **  *
****   **** *  *  *   * **    *  *    *   *   *
*   * *   * *  *  *   *   **  *  *    *   *   *
*   * *  ** *  *  *  **    *  *  *    *   *   *
****   **** *  *   ** * ***   *  *  ****  **** 
                                          *    
                                          *    

=================================================================================
#: 未知格子\to: 击中军舰身体的一部分\tx: 未打到的格子
回合: {}\t得分: {}'''.format(round, score))

def gameInit():
    global map
    map = make_grid.make2dArray(mapRows, mapCols, 0)
    global guessMap
    guessMap = make_grid.make2dArray(mapRows, mapCols, '#')
    make_grid.putMap(map, shipLength, shipCount)

def gameMain():
    gameHello()
    global guessMap
    global map
    global round
    render.rendGrid(guessMap)
    try:
        userThink = input('你要炸的x和y坐标(如: "B4"): ')
        pos = think_user.isBlast(userThink, map)
    except:
        print('出错了哦 :(')
    global score
    if (pos[2]):
        score += 1
        guessMap[pos[1]][pos[0]] = 'o'
    else:
        guessMap[pos[1]][pos[0]] = 'x'

    round += 1