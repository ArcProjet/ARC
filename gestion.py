from grid import Grid
from primitive import *
from random import randint

#La fonction utilise des primitives de facon aléatoire avec un nombre de répétition
def fctChoice(stage,grid):

    tabFunctions = []

    for i in range(stage):
        n = randint(0,7)
        tabFunctions.append(n)
        print(n)
        match n:
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