from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid

if __name__ == '__main__':

    #On ne charge que des grilles carrées pour le moment
    isSquare = False
    while (not isSquare):
        grillestrain,grillestest = openJsonFile()
        gridTrain1 = Grid(grillestrain[0]['input'],grillestrain[0]['output'])
        gridTrain2 = Grid(grillestrain[1]['input'],grillestrain[1]['output'])
        gridTest = Grid(grillestest[0],grillestest[1])
        if(gridTrain1.isSquare() and gridTrain2.isSquare()):
            isSquare = True
    
    funcTab = generateFctTab(2,10)
    applyFunctions(funcTab[0],gridTrain1)
    applyFunctions(funcTab[1],gridTrain2)
    gridTrain1.displayGrid()
    gridTrain1.ExpectationVsreality()

    gridTrain1.getSuccess()

    plt.show()
    
    #gridTrain1.output = growingColor(gridTrain1, 5)
    #gridTrain1.displayGrid()

    #verif = "N"

    #On fait une boucle pour valider le résultat manuellement
    #while (verif != "Y"):
        #func = fctChoice(10)
        #applyFunctions(func,gridt)
        #draw(grillestrain,grillestest,gridt)
        #verif = "Y"
        #gridt.displayGrid()
        #verif = input("Est ce que c'est le bon résultat ? Y/N\n")
