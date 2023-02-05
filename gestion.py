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
                grid = (gridCopy(grid))
            case 1:
                grid = (completed(grid))
            case 2:
                grid = (rotateHalf(grid))
            case 3:
                grid = (rotateLeft(grid))
            case 4:
                grid = (rotateRight(grid))
            case 5:
                grid = (extendLine(grid))
            case 6:
                grid = (extendColumn(grid))
            case 7:
                grid = (extendColorUp(grid))
            case 8:
                grid = (extendColorDown(grid))
            case 9:
                grid = (extendColorLeft(grid))
            case 10:
                grid = (extendColorRight(grid))
            case 11:
                grid = (growingColor(grid))
            case 12:
                grid = (axialSymmetryX(grid))
            case 13:
                grid = (axialSymmetryY(grid))
            case 14:
                grid = (copyHalfX(grid))
            case 15:
                grid = (copyHalfY(grid))
            case 16:
                grid = (xHalf(grid))
            case 17:
                grid = (yHalf(grid))
            case 18:
                grid = (doubleRow(grid))
            case 19:
                grid = (tripleRow(grid))
            case 20:
                grid = (doubleColumn(grid))
            case 21:
                grid = (tripleColumn(grid))
            case 22:
                grid = (doubleSymetryRow(grid))
            case 23:
                grid = (doubleSymetryColumn(grid))
            # case 24:
            #    grid = (symetryFourPart(grid))
            # case 25:
            #    grid = (centralSymetry(grid))
            # case 26:
            #    grid = (commonElement(grid, grid))

    return grid