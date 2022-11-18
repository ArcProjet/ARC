from grid import Grid

def rotateHalf(grid):
    return (grid.getInput()[::-1])

def rotateLeft(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = 0
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[cpt][grid.getNbRow()-i-1]
            cpt += 1
    return (res)

def rotateRight(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = grid.getNbRow() - 1
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[cpt][i]
            cpt -= 1
    return (res)

def centralSymetry(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[j][i]
    return (res)