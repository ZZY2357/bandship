# think_user.py
# 处理用户输入



def isBlast(posStr, _map):
    splitList = posStr
    y = charToY(splitList[0])
    x = int(splitList[1])
    theReturn = [x, y]
    if _map[y][x] == 1:
        theReturn.append(True)
    else:
        theReturn.append(False)
    return theReturn

def charToY(char):
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(chars)):
        if char == chars[i]:
            return i
