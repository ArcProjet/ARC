from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid
from classeGrille import Grille
from classeIndividu import Individu
from classePopulation import Population

if __name__ == '__main__':
    grillestrain,grillestest = openJsonFile()
    gridTrain1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']
    p = Population(gridTrain1[1],gridTrain1[0])
    p.genererPopulation()
    p.trierPopulation()
    p.modifierGrille()
    
 #   ttt = Grid(p.imageDepart,p.imageEsperee)
 #   ttt.output = p.individus[1].grille.data
 #   ttt.displayGrid()
 #   ttt.ExpectationVsreality()
 #   plt.show()

if __name__ == '__min__':

    #On ne charge que des grilles carrées pour le moment
    isSquare = False
    while (not isSquare):
        grillestrain,grillestest = openJsonFile()
        gridTrain1 = Grid(grillestrain[0]['input'],grillestrain[0]['output'])
        gridTrain2 = Grid(grillestrain[1]['input'],grillestrain[1]['output'])
        gridTest = Grid(grillestest[0],grillestest[1])
        if(gridTrain1.isSquare() and gridTrain2.isSquare()):
            isSquare = True
    
    index = 0
    max = gridTest

    for k in range(100):
        gridTrain1 = Grid(grillestrain[0]['input'],grillestrain[0]['output'])
        funcTab = generateFctTab(2,10)
        applyFunctions(funcTab[0],gridTrain1)
        applyFunctions(funcTab[1],gridTrain2)

        if(index < gridTrain1.getSuccess()):
            index = gridTrain1.getSuccess()
            max = gridTrain1

    max.displayGrid()
    max.getSuccess()
    max.ExpectationVsreality()
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
