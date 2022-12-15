from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid
from classeGrille import Grille
from classeIndividu import Individu
from classePopulation import Population

def displayGrid(grid1,grid2,title1,title2):
    fig, axs = plt.subplots(1,2)
    axs[0].set_title(title1)
    axs[0].axis('off')
    axs[0].matshow(grid1, cmap='rainbow')
    axs[1].set_title(title2)
    axs[1].axis('off')
    axs[1].matshow(grid2, cmap='rainbow')

if __name__ == '__main__':
    grillestrain,grillestest = openJsonFile()
    gridTrain1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']

    p = Population(gridTrain1[1],gridTrain1[0])
        
    displayGrid(p.imageDepart,p.imageEsperee,"Grille de départ","Grille Attendu")

    p.genererPopulation()
    p.evolutionPopulation()
    
    displayGrid(p.imageDepart,p.individus[0].grille.data,"Grille de départ","Grille obtenu")
    
    #ttt.ExpectationVsreality()
    plt.show()
