from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid

if __name__ == '__main__':

    #On ne charge que des grilles carrées pour le moment
    isSquare = False
    while (not isSquare):
        grillestrain,grillestest = openJsonFile()
        grid = Grid(grillestrain[0]['input'],grillestrain[1]['output'])
        gridt = Grid(grillestest[0],grillestest[0])
        if(grid.isSquare()):
            isSquare = True
    
    #grid.output = symetryFourPart(grid)
    #grid.displayGrid()
    #grid.output = centralSymetry(grid)
    #grid.displayGrid()

    verif = "N"

    #On fait une boucle pour valider le résultat manuellement
    while (verif != "Y"):
        fctChoice(10,gridt)
        #draw(grillestrain,grillestest,gridt)
        verif = "Y"
        gridt.displayGrid()
        grid.displayGrid()
        #verif = input("Est ce que c'est le bon résultat ? Y/N\n")
