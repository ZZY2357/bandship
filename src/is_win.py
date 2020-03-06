# is_win.py
# 判断胜负

def isWin(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                return False
    return True