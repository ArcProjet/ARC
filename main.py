from primitive import *
from JsonLoader import *
from grid import Grid

if __name__ == '__main__':

    #On ne charge que des grilles carrées pour le moment
    isSquare = False
    while (not isSquare):
        grillestrain,grillestest = openJsonFile()
        grid = Grid(grillestrain[0]['input'],grillestrain[1]['input'])
        if(grid.isSquare()):
            isSquare = True

    symetryFourPart(grid,4)
    grid.displayGrid()