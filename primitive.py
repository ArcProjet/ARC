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


def rotateHalf(grid):
    return gridCopy(grid)[::-1]


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


def xHalf(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(int(len(grid)/2))]
    for i in range(0, int(len(grid)/2)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res


def yHalf(grid):
    res = [[0 for _ in range(int(len(grid[0])/2))] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i])/2)):
            res[i][j] = grid[i][j]
    return res


def changeAColor(grid):
    res = gridCopy(grid)
    c = res[randint(0, len(res) - 1)][randint(0, len(res[0]) - 1)]
    newC = randint(0,9)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == c):
                res[i][j] = newC
    return res

#AU FINAL, TRES SIMILAIRE A CHANGECOLOR...
#AFFICHAGE SOUVENT BUGUER
def completeColor(grid):
    res = gridCopy(grid)
    newC = randint(0, 9)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = newC
    return res


def doubleRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*2)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid)+i][j] = grid[i][j]
    return res


def tripleRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*3)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid)+i][j] = grid[i][j]
            res[(len(grid)*2)+i][j] = grid[i][j]
    return res


def doubleColumn(grid):
    res = [[0 for _ in range((len(grid[0]))*2)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0])+j] = grid[i][j]
    return res


def tripleColumn(grid):
    res = [[0 for _ in range((len(grid[0]))*3)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0])+j] = grid[i][j]
            res[i][(len(grid[0])*2)+j] = grid[i][j]
    return res


def doubleSymetryRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*2)]
    sym = axialSymmetryX(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid)+i][j] = sym[i][j]
    return res


def doubleSymetryColumn(grid):
    res = [[0 for _ in range((len(grid[0]))*2)] for _ in range(len(grid))]
    sym = axialSymmetryY(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0])+j] = sym[i][j]
    return res

# NE FONCTIONNE QUE POUR UN CARRE SINON RETOURNE COPY
def centralSymetry(grid):
    if (len(grid) == len(grid[0])):
        res = gridCopy(grid)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = grid[j][i]
        return res
    else:
        res2 = gridCopy(grid)
        return res2


def inversion(grid):
    inverted_grid = [[9 - grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    return inverted_grid


def removeNoiseFromGrid(grid, seuil=9):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < seuil:
                res[i][j] = 0
    return res


def lenghtReduction(grid):
    t = randint(1,len(grid))
    res = [[0 for _ in range(len(grid[0]))] for _ in range(t)]
    for i in range(0, t):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res


def widthReduction(grid):
    t = randint(1,len(grid[0]))
    res = [[0 for _ in range(t)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, t):
            res[i][j] = grid[i][j]
    return res


def translationVerticaleEnHaut(grid):
    res = gridCopy(grid)
    for i in range(0,len(grid)-1):
        for j in range(0,len(grid[0])):
            res[i][j] = grid[i+1][j]
    for l in range(0,len(grid[0])):
        res[len(grid)-1][l] = grid[0][l]
    return res


def translationHorizontaleADroite(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            res[i][j + 1] = grid[i][j]
        res[i][0] = grid[i][len(grid[0])-1]
    return res


def translationVerticaleEnBas(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            res[i + 1][j] = grid[i][j]
    for l in range(0, len(grid[0])):
        res[0][l] = grid[len(grid)-1][l]
    return res


def translationHorizontaleAGauche(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            res[i][j - 1] = grid[i][j]
        res[i][len(grid[0])-1] = grid[i][0]
    return res


#PAS COMPRIS + ERREUR INDEX
# def rotational_symmetry(grid, angle):
#     n = len(grid)
#     new_grid = [[0 for j in range(n)] for i in range(n)]
#     center = (n-1) / 2
#     radians = math.radians(angle)
#     for i in range(n):
#         for j in range(n):
#             x = (i - center) * math.cos(radians) + (j - center) * math.sin(radians)
#             y = -(i - center) * math.sin(radians) + (j - center) * math.cos(radians)
#             x = int(round(x + center))
#             y = int(round(y + center))
#             if x >= 0 and x < n and y >= 0 and y < n:
#                 new_grid[x][y] = grid[i][j]
#     return new_grid


#ERREUR INDEX
#DEJA COUVERT PAR LES AXIALSYMETRY ?
# def mirrorGrid (grid, angle):
#     new_grid =  rotational_symmetry(grid, 180 + angle)
#     for i in range (len(grid)//2):
#         for j in range (len(grid)//2):
#             new_grid [i][j] = grid [i][j]
#
#     return new_grid


# NE FONCTIONNE QUE SI LES TAILLES DES 2 GRILLES SONT LES MEMES
# EST CE QU'ON GARDE ?
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
