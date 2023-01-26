def copy(grid):
    res = []
    for i in range(len(grid)):
        tmp = []
        for j in range(len(grid[i])):
            tmp.append(grid[i][j])
        res.append(tmp)
    return res

def leftCornerUp(grid):
    res = []
    for i in range(len(grid)//2):
        tmp = []
        for j in range(len(grid[i])//2):
            tmp.append(grid[i][j])
        res.append(tmp)
    return res


def empty(grid, c=0):
    return copy(grid)

def completed(grid, c):
    res = copy(grid)#[[0 for i in range(len(grid))] for j in range(len(grid[0]))] 
    for i in range(len(grid)):
        for j in range(0,len(grid[i])):
            res[i][j] = c
    return (res)

def rotateHalf(grid, c=0):
    return (copy(grid)[::-1])

def rotateLeft(grid, c=0):
    res = copy(grid)
    if(len(grid) == len(grid[0])):
        for i in range(len(grid)):
            cpt = 0
            for j in range(len(grid[0])):
                res[i][j] = grid[cpt][len(grid[0])-i-1]
                cpt += 1
    return (res)


def rotateRight(grid, c=0):
    res = copy(grid) 
    if(len(grid) == len(grid[0])):
        for i in range(len(grid)):
            cpt = len(grid) - 1
            for j in range(len(grid[0])):
                res[i][j] = grid[cpt][i]
                cpt -= 1
    return (res)

def centralSymetry(grid, c=0):
    res = copy(grid)
    if(len(grid) == len(grid[0])):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = grid[j][i]
    return (res)

# EN TRAVAUX
def symetryFourPart(grid, c=0):
    res = copy(grid)#[[0 for i in range(len(grid[0]))] for j in range(len(grid))] 
    if(len(grid)%2==0 and len(grid[0])%2==0):
        tmp = leftCornerUp(grid)
        nbRow = len(tmp)
        nbColumn = len(tmp[0])
        for i in range(0,nbRow):
            for j in range(0,nbColumn):
                res[i][j] = tmp[i][j]
        tmp = rotateRight(tmp)
        for i in range(0,nbRow):
            for j in range(0,nbColumn):
                res[i][j+nbColumn] = tmp[i][j]
        tmp = rotateRight(tmp)
        for i in range(0,nbRow):
            for j in range(0,nbColumn):
                res[i+nbRow][j+nbColumn] = tmp[i][j]
        tmp = rotateRight(tmp)
        for i in range(0,nbRow):
            for j in range(0,nbColumn):
                res[i+nbRow][j] = tmp[i][j]
    return (res)

def extendLine(grid, c, line):
    res = copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(i == line):
                res[i][j] = c
    return (res)

def extendColumn(grid, c, column):
    res = copy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(j == column):
                res[i][j] = c
    return (res)

def extendColorUp(grid, c):
    res = copy(grid)
    for i in range(1,len(grid)): # for i in range(1,len(grid)()-1):
        for j in range(len(grid[0])): # for j in range(1,len(grid[0])-1):
            if(res[i][j] == c):
                res[i-1][j] = c
    return (res)

def extendColorDown(grid, c):
    res = copy(grid)
    for i in range(len(grid)-2,0,-1): # for i in range(len(grid)()-1,1,-1):
        for j in range(len(grid[0])): # for j in range(1,len(grid[0])-1):
            if(res[i][j] == c):
                res[i+1][j] = c
    return (res)

def extendColorLeft(grid, c):
    res = copy(grid)
    for i in range(len(grid)): # for i in range(1,len(grid)()-1):
        for j in range(1,len(grid[0])): # for j in range(1,len(grid[0])-1):
            if(res[i][j] == c):
                res[i][j-1] = c
    return (res)

def extendColorRight(grid, c):
    res = copy(grid)
    for i in range(len(grid)): # for i in range(1,len(grid)()-1):
        for j in range(len(grid[0])-2,0,-1): # for j in range(len(grid[0])-1,1,-1):
            if(res[i][j] == c):
                res[i][j+1] = c
    return (res)

def growingColor(grid, c):
    res = copy(grid)
    for i in range(1,len(grid)): # for i in range(1,len(grid)()):
        for j in range(len(grid[0])): # for j in range(1,len(grid[0])-1):
            if(res[i][j] == c):
                res[i-1][j] = c
    for k in range(0,len(grid)): # for k in range(1,len(grid)()-1):
        for l in range(len(grid[0])-2,0,-1): # for l in range(len(grid[0])-1,1,-1):
            if(res[k][l] == c):
                res[k][l+1] = c
    for m in range(len(grid)-2,0,-1): # for m in range(len(grid)()-1,1,-1):
        for n in range(len(grid[0])): # for n in range(1,len(grid[0])-1):
            if(res[m][n] == c):
                res[m+1][n] = c
    for o in range(len(grid)): # for o in range(1,len(grid)()-1):
        for p in range(1,len(grid[0])): # for p in range(1,len(grid[0])-1):
            if(res[o][p] == c):
                res[o][p-1] = c
    return (res)
    
def axialSymmetryX(grid, c=0):
    res = copy(grid)
    if(len(grid[0])%2==0):
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if (j != 0): 
                    res[i][j] = grid[i][-j]
                    res[i][-j] = grid[i][j]             
    
    return (res)


def axialSymmetryY(grid, c=0):
    res = copy(grid)
    if(len(grid)%2==0):
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if(i != 0):
                    res[i][j] = grid[-i][j]
                    res[-i][j] = grid[i][j]
    
    return (res)

def commonElement(grid,grid2):
    res = copy(grid)#[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] - grid2[i][j] == 0):
                res[i][j] = grid[i][j]
            else:
                res[i][j] = 0
            #res[i][j] = grid[i][j] - grid2[i][j]
    return (res)

