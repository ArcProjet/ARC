from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0,14))
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
                grid = (empty(grid))
            case 1:
                grid = (completed(grid,randint(0,9)))
            case 2:
                grid = (rotateHalf(grid))
            case 3:
                grid = (rotateLeft(grid))
            case 4:
                grid = (rotateRight(grid))
            case 5:
                grid = (centralSymetry(grid))
            case 6:
                grid = (empty(grid))
            case 7:
                grid = (extendLine(grid,randint(0,len(grid)-1),randint(0,9)))
            case 8:
                grid = (extendColumn(grid,randint(0,len(grid[0])-1),randint(0,9)))
            case 9:
                grid = (extendColorUp(grid,randint(0,9)))
            case 10:
                grid = (extendColorDown(grid,randint(0,9)))
            case 11:
                grid = (extendColorLeft(grid,randint(0,9)))
            case 12:
                grid = (extendColorRight(grid,randint(0,9)))
            case 13:
                grid = (growingColor(grid,randint(0,9)))
            case 14:
                grid = (commonElement(grid,grid))
    return grid