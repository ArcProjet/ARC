from grid import Grid
from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0,13))
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
                grid.setOutput(completed(grid,randint(0,9)))
            case 2:
                grid.setOutput(rotateHalf(grid))
            case 3:
                grid.setOutput(rotateLeft(grid))
            case 4:
                grid.setOutput(rotateRight(grid))
            case 5:
                grid.setOutput(centralSymetry(grid))
            case 6:
                grid.setOutput(empty(grid))
            case 7:
                grid.setOutput(extendLine(grid,randint(0,grid.nbRow-1),randint(0,9)))
            case 8:
                grid.setOutput(extendColumn(grid,randint(0,grid.nbColumn-1),randint(0,9)))
            case 9:
                grid.setOutput(extendColorUp(grid,randint(0,9)))
            case 10:
                grid.setOutput(extendColorDown(grid,randint(0,9)))
            case 11:
                grid.setOutput(extendColorLeft(grid,randint(0,9)))
            case 12:
                grid.setOutput(extendColorRight(grid,randint(0,9)))
            case 13:
                grid.setOutput(growingColor(grid,randint(0,9)))