#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import platform

import game
import is_win

if __name__ == "__main__":
    game.gameInit()
    while True:
        game.gameMain()
        if is_win.isWin(game.map):
            break
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

print('''         **         *
*    *              *
*    * ***   ****   *
*    *   *   *  *   *
* ** *   *   *  *   *
 ****    *   *  *   *
 * **    *   *  *    
 *  *  ****  *  *   *

你赢了!''')
