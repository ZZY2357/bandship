# render.py
# 用来渲染列表

def rendGrid(grid):
    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    print('\0\0\0', end='')
    for i in range(len(grid[0])):
        print(i, end='\t')
    print()
    for i in range(len(grid[0])):
        print('===', end='')
        print('====', end='')
    print()

    # 行
    for i in range(len(grid)):
        # 列
        print(cols[i], end='| ')
        for j in range(len(grid[i])):
            print(grid[i][j], end="\t")
        
        print() # 换行
