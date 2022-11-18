from grid import Grid
from primitive import *
from random import randint

#La fonction utilise des primitives de facon aléatoire avec un nombre de répétition
def fctChoice(stage,grid):

    for i in range(stage):
        n = randint(1,4)
        if n==1:
            grid.setOutput(rotateHalf(grid))
        if n==2:
            grid.setOutput(rotateLeft(grid))
        if n==3:
            grid.setOutput(rotateRight(grid))
        if n==4:
            grid.setOutput(centralSymetry(grid))


