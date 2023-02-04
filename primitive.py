from random import randint

#Copie proprement les grilles
def gridCopy(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            res[i][j] = grid[i][j]
    return res


def completed(grid):
    res = gridCopy(grid)
    c = randint(0, 9)
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = c
    return res


#On utilise le gridCopy ou pas ?
def rotateHalf(grid):
    return grid.copy()[::-1]


def rotateLeft(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = 0
        for j in range(len(res[0])):
            res[i][j] = grid[cpt][len(grid[0]) - i - 1]
            cpt += 1
    return res


def rotateRight(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = len(grid)
        for j in range(len(res[0])):
            cpt -= 1
            res[i][j] = grid[cpt][i]
    return res


def extendLine(grid):
    res = gridCopy(grid)
    line = randint(0,len(grid)-1)
    c = res[line][randint(0,len(res[0])-1)]
    for i in range(len(res)):
        for j in range(len(res[0])):
            if(i == line):
                res[i][j] = c
    return res


def extendColumn(grid):
    res = gridCopy(grid)
    column = randint(0,len(grid[0])-1)
    c = res[randint(0, len(res) - 1)][column]
    for i in range(len(res)):
        for j in range(len(res[0])):
            if(j == column):
                res[i][j] = c
    return res


def extendColorUp(grid):
    res = gridCopy(grid)
    c = res[randint(0,len(res)-1)][randint(0,len(res[0])-1)]
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == c):
                res[i-1][j] = c
    return res


def extendColorDown(grid):
    res = gridCopy(grid)
    c = res[randint(0,len(res)-1)][randint(0,len(res[0])-1)]
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == c):
                res[i+1][j] = c
    return res


def extendColorLeft(grid):
    res = gridCopy(grid)
    c = res[randint(0,len(res)-1)][randint(0,len(res[0])-1)]
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == c):
                res[i][j-1] = c
    return res


def extendColorRight(grid):
    res = gridCopy(grid)
    c = res[randint(0,len(res)-1)][randint(0,len(res[0])-1)]
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == c):
                res[i][j+1] = c
    return res


def growingColor(grid):
    res = gridCopy(grid)
    c = grid[randint(0,len(grid)-1)][randint(0,len(grid[0])-1)]
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == c):
                res[i-1][j] = c
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == c):
                res[k][l+1] = c
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == c):
                res[m+1][n] = c
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == c):
                res[o][p-1] = c
    return res


def axialSymmetryX(grid):
    res = gridCopy(grid)
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
                    res[i][j] = grid[len(grid)-i-1][j]
    return res


def axialSymmetryY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][len(grid[0])-j-1]
    return res


def copyHalfX(grid):
    res = gridCopy(grid)
    for i in range(0,int(len(grid)/2)):
        for j in range(0,len(grid[i])):
                    res[i][j] = grid[len(grid)-i-1][j]
    return res


def copyHalfY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i])/2)):
            res[i][j] = grid[i][len(grid[0])-j-1]
    return res

# EST CE QU'ON GARDE ? ON A PLUS SIMPLE JE PENSE MAINTENANT ?
# LES 2 COPY HALF FONT LE JOB JE PENSE...
# def symetryFourPart(grid):
#    res = gridCopy(grid)
#    tmp = grid.getCornerUpLeft()
#    nbRow = len(tmp)
#    nbColumn = len(tmp[0])
#    for i in range(0,nbRow):
#        for j in range(0,nbColumn):
#            res[i][j] = tmp[i][j]
#    tmp = rotateRight(tmp)
#    for i in range(0,nbRow):
#        for j in range(0,nbColumn):
#            res[i][j+nbColumn] = tmp[i][j]
#    tmp = rotateRight(tmp)
#    for i in range(0,nbRow):
#        for j in range(0,nbColumn):
#            res[i+nbRow][j+nbColumn] = tmp[i][j]
#    tmp = rotateRight(tmp)
#    for i in range(0,nbRow):
#        for j in range(0,nbColumn):
#            res[i+nbRow][j] = tmp[i][j]
#    return (res)

# NE FONCTIONNE QUE POUR UN CARRE
# def centralSymetry(grid):
#     res = gridCopy(grid)
#     for i in range(len(res)):
#         for j in range(len(res[0])):
#             res[i][j] = grid[j][i]
#     return res

# NE FONCTIONNE QUE SI LES TAILLES DES 2 GRILLES SONT LES MEMES
#def commonElement(grid,grid2):
#     res = gridCopy(grid)
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if(grid[i][j] - grid2[i][j] == 0):
#                 res[i][j] = grid[i][j]
#             else:
#                 res[i][j] = 0
#             #res[i][j] = grid[i][j] - grid2[i][j]
#     return res
