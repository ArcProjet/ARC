from grid import Grid
from listeFunctions import *

def empty(grid):
    return grid.getInputCopy()

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

def extendsLine(grid, line, c):
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