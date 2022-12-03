from grid import Grid
from listeFunctions import *

def empty(grid):
    return grid.getInputCopy()

def completed(grid, c):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            res[i][j] = c
    return (res)

def rotateHalf(grid):
    return (grid.getInputCopy()[::-1])

def rotateLeft(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = 0
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getOutput()[cpt][grid.getNbColumn()-i-1]
            cpt += 1
    return (res)


def rotateRight(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = grid.getNbRow() - 1
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getOutput()[cpt][i]
            cpt -= 1
    return (res)

def centralSymetry(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getOutput()[j][i]
    return (res)

def symetryFourPart(grid):
    res = grid.getInputCopy()
    tmp = grid.getCornerUpLeft()
    nbRow = len(tmp)
    nbColumn = len(tmp[0])
    for i in range(0,nbRow):
        for j in range(0,nbColumn):
            res[i][j] = tmp[i][j]
    tmp = rotateRightListe(tmp)
    for i in range(0,nbRow):
        for j in range(0,nbColumn):
            res[i][j+nbColumn] = tmp[i][j]
    tmp = rotateRightListe(tmp)
    for i in range(0,nbRow):
        for j in range(0,nbColumn):
            res[i+nbRow][j+nbColumn] = tmp[i][j]
    tmp = rotateRightListe(tmp)
    for i in range(0,nbRow):
        for j in range(0,nbColumn):
            res[i+nbRow][j] = tmp[i][j]
    return (res)

def extendLine(grid, line, c):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            if(i == line):
                res[i][j] = c
    return (res)

def extendColumn(grid, column, c):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            if(j == column):
                res[i][j] = c
    return (res)

def extendColorUp(grid, c):
    res = grid.getInputCopy()
    for i in range(1,grid.getNbRow()-1):
        for j in range(1,grid.getNbColumn()-1):
            if(res[i][j] == c):
                res[i-1][j] = c
    return (res)

def extendColorDown(grid, c):
    res = grid.getInputCopy()
    for i in range(grid.getNbRow()-1,1,-1):
        for j in range(1,grid.getNbColumn()-1):
            if(res[i][j] == c):
                res[i+1][j] = c
    return (res)

def extendColorLeft(grid, c):
    res = grid.getInputCopy()
    for i in range(1,grid.getNbRow()-1):
        for j in range(1,grid.getNbColumn()-1):
            if(res[i][j] == c):
                res[i][j-1] = c
    return (res)

def extendColorRight(grid, c):
    res = grid.getInputCopy()
    for i in range(1,grid.getNbRow()-1):
        for j in range(grid.getNbColumn()-1,1,-1):
            if(res[i][j] == c):
                res[i][j+1] = c
    return (res)

def growingColor(grid, c):
    res = grid.getInputCopy()
    for i in range(1,grid.getNbRow()-1):
        for j in range(1,grid.getNbColumn()-1):
            if(res[i][j] == c):
                res[i-1][j] = c
    for k in range(1,grid.getNbRow()-1):
        for l in range(grid.getNbColumn()-1,1,-1):
            if(res[k][l] == c):
                res[k][l+1] = c
    for m in range(grid.getNbRow()-1,1,-1):
        for n in range(1,grid.getNbColumn()-1):
            if(res[m][n] == c):
                res[m+1][n] = c
    for o in range(1,grid.getNbRow()-1):
        for p in range(1,grid.getNbColumn()-1):
            if(res[o][p] == c):
                res[o][p-1] = c
    return (res)
    