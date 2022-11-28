from grid import Grid

def rotateHalf(grid):
    grid.setOutput(grid.getInput()[::-1])

def rotateLeft(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = 0
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[cpt][grid.getNbRow()-i-1]
            cpt += 1
    grid.setOutput(res)

def rotateRight(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        cpt = grid.getNbRow() - 1
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[cpt][i]
            cpt -= 1
    grid.setOutput(res)

def centralSymetry(grid):
    res = grid.getInputCopy()
    for i in range(0,grid.getNbRow()):
        for j in range(0,grid.getNbColumn()):
            res[i][j] = grid.getInput()[j][i]
    grid.setOutput(res)


def axialSymetryX(grid):
    res = grid.getInputCopy() 
    for i in range(0,grid.getNbColumn()):
        for j in range(0,grid.getNbRow()):
            if (j == 0): 
                res[i][j] = res[i][j]
        
            res[i][j] = res[i][-j]
    grid.setOutput(res)


def axialSymetryY(grid):
    res = grid.getInputCopy() 
    for j in range(0,grid.getNbColumn()):
        for i in range(0,grid.getNbRow()):
            if(i == 0):
                res[i][j] = res[i][j]

            res[i][j] = res[-i][j]
    grid.setOutput(res)


