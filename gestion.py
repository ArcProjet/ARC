from grid import Grid
from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0,7))
    return tab

def generateFctTab(nb,stage):
    tab = []
    for _ in range(nb):
        tab.append(fctChoice(stage))
    return tab

#La fonction utilise des primitives précisé dans le tableau tabFunctions
def applyFunctions(tabFunctions,grid):
    for i in tabFunctions:
        match i:
            case 0:
                grid.setOutput(empty(grid))
            case 1:
                grid.setOutput(rotateHalf(grid))
            case 2:
                grid.setOutput(rotateLeft(grid))
            case 3:
                grid.setOutput(rotateRight(grid))
            case 4:
                grid.setOutput(centralSymetry(grid))
            case 5:
                grid.setOutput(symetryFourPart(grid))
            case 6:
                grid.setOutput(extendsLine(grid,randint(0,grid.nbRow-1),randint(0,9)))
            case 7:
                grid.setOutput(extendsLine(grid,randint(0,grid.nbColumn-1),randint(0,9)))