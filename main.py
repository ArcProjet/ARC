from matplotlib.colors import BoundaryNorm, ListedColormap
from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid
from classeGrille import Grille
from classeIndividu import Individu
from classePopulation import Population

NB_POPULATIONS = 50

def displayGrid(gridInput,gridOutput,gridObtain,title1,title2,title3):
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'purple', 'darkgreen', 'grey', 'black']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(values, cmap.N)
    fig, axs = plt.subplots(2,11)
    axs[0,0].set_title(title1)
    axs[0,0].axis('off')
    axs[0,0].matshow(gridInput[0], cmap=cmap,norm=norm)
    axs[0,1].set_title(title2)
    axs[0,1].axis('off')
    axs[0,1].matshow(gridOutput[0], cmap=cmap,norm=norm)
    axs[0,2].set_title(title3)
    axs[0,2].axis('off')
    axs[0,2].matshow(gridObtain[0], cmap=cmap,norm=norm)
    axs[0,4].set_title(title1)
    axs[0,4].axis('off')
    axs[0,4].matshow(gridInput[1], cmap=cmap,norm=norm)
    axs[0,5].set_title(title2)
    axs[0,5].axis('off')
    axs[0,5].matshow(gridOutput[1], cmap=cmap,norm=norm)
    axs[0,6].set_title(title3)
    axs[0,6].axis('off')
    axs[0,6].matshow(gridObtain[1], cmap=cmap,norm=norm)
    axs[0,8].set_title(title1)
    axs[0,8].axis('off')
    axs[0,8].matshow(gridInput[2], cmap=cmap,norm=norm)
    axs[0,9].set_title(title2)
    axs[0,9].axis('off')
    axs[0,9].matshow(gridOutput[2], cmap=cmap,norm=norm)
    axs[0,10].set_title(title3)
    axs[0,10].axis('off')
    axs[0,10].matshow(gridObtain[2], cmap=cmap,norm=norm)
    axs[1,4].set_title(title1)
    axs[1,4].axis('off')
    axs[1,4].matshow(gridInput[3], cmap=cmap,norm=norm)
    axs[1,5].set_title(title2)
    axs[1,5].axis('off')
    axs[1,5].matshow(gridOutput[3], cmap=cmap,norm=norm)
    axs[1,6].set_title(title3)
    axs[1,6].axis('off')
    axs[1,6].matshow(gridObtain[3], cmap=cmap,norm=norm)
    axs[0,3].axis('off')
    axs[0,7].axis('off')
    axs[1,0].axis('off')
    axs[1,1].axis('off')
    axs[1,2].axis('off')
    axs[1,3].axis('off')
    axs[1,7].axis('off')
    axs[1,8].axis('off')
    axs[1,9].axis('off')
    axs[1,10].axis('off')

def optimizePrimitive(gridInput,fonctions):
    #fonctions = bestIndividu.fonctions
    newFonctions = []
    for f in fonctions:
        isEqual = True
        for data in gridInput:
            if(len(data) >= 1 and len(data[0]) >= 1):
                isEqual = isEqual and (data == f(data))
        if isEqual:
            newFonctions.append(gridCopy)
        else:
            newFonctions.append(f)
    return newFonctions

def KingOfTheHill(gridInput,gridWishes):

    leaderboard = []

    print("[+] --------- KingOfTheHill ---------")

    for _ in range(NB_POPULATIONS):

        
        p1 = Population(gridInput,gridWishes)
        
        p1.genererPopulation()

        if _ != 0:
            p1.individus[0] = leaderboard[_-1] 

        p1.evolutionPopulation()

        leaderboard.append(p1.individus[0])

        print("[+] ["+str(_)+"/"+str(NB_POPULATIONS-1)+"] Score : " + str(p1.individus[0].score))

    return leaderboard


def solveGrid(grid):

    grillestrain,grillestest = grid
    gridInput = grillestrain[0]['input'],grillestrain[1]['input'],grillestrain[2]['input']
    gridWishes = grillestrain[0]['output'],grillestrain[1]['output'],grillestrain[2]['output']
    #gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']
    grillestest = grillestest[0],grillestest[1]
    
    print("[+] Populations choose their King")

    leaderboard1 = KingOfTheHill(gridInput,gridWishes) 

    if leaderboard1[-1].score == 100:
        bestIndividu = leaderboard1[-1]
    else:

        p1 = Population(gridInput,gridWishes)

        p1.genererPopulation()

        for i in range(NB_POPULATIONS-1):
            p1.individus[i] = leaderboard1[i]

        p1.evolutionPopulation()

        bestIndividu = p1.individus[0]

    print("[+] Populations have chosen their King")

    print("[+] --------- Prepare for King Battle ---------")

  #  bestP1.grille.modifierGrille([gridTrain2[0]],bestP1.fonctions)
  #  print("[+] P1 score in train2 : " + str(bestP1.grille.comparer(gridTrain2[1])))
  #  scoreP1 += bestP1.grille.comparer(gridTrain2[1])

  #  bestP2.grille.modifierGrille([gridTrain1[0]],bestP2.fonctions)
  #  print("[+] P2 score in train1 : " + str(bestP2.grille.comparer(gridTrain1[1])))
  #  scoreP2 += bestP2.grille.comparer(gridTrain1[1])

  #  print("[+] Score for P1 : " + str(scoreP1/2) + " , Score for P2 : " + str(scoreP2/2))

    #print(bestIndividu.fonctions)

    fonctions = optimizePrimitive(gridInput,bestIndividu.fonctions)   

    for i in range(len(fonctions)):
        if fonctions[i] != bestIndividu.fonctions[i]: print(bestIndividu.fonctions[i])

    alldata = []

    g = Grille(grillestrain[0]['input'])
    g.modifierGrille(grillestrain[0]['input'],bestIndividu.fonctions)
    print("[+] Best individu score in final grid : " + str(g.comparer(grillestrain[0]['output'])))
    alldata.append(g.data)

    #displayGrid(grillestrain[0]['input'],grillestrain[0]['output'],g.data,"Grille de départ","Grille de Fin","Grille obtenu")

    g = Grille(grillestrain[1]['input'])
    g.modifierGrille(grillestrain[1]['input'],bestIndividu.fonctions)
    print("[+] Best individu score in final grid : " + str(g.comparer(grillestrain[1]['output'])))
    alldata.append(g.data)

    #displayGrid(grillestrain[1]['input'],grillestrain[1]['output'],g.data,"Grille de départ","Grille de Fin","Grille obtenu")

    g = Grille(grillestrain[2]['input'])
    g.modifierGrille(grillestrain[2]['input'],bestIndividu.fonctions)
    print("[+] Best individu score in final grid : " + str(g.comparer(grillestrain[2]['output'])))
    alldata.append(g.data)

    #displayGrid(grillestrain[2]['input'],grillestrain[2]['output'],g.data,"Grille de départ","Grill)e de Fin","Grille obtenu")

    g = Grille(grillestest[0])
    g.modifierGrille(grillestest[0],bestIndividu.fonctions)
    print("[+] Best individu score in final grid : " + str(g.comparer(grillestest[1])))
    alldata.append(g.data)

    #displayGrid(grillestest[0],grillestest[1],g.data,"Grille de départ","Grille de Fin","Grille obtenu")
    displayGrid([grillestrain[0]['input'],grillestrain[1]['input'],grillestrain[2]['input'],grillestest[0]],[grillestrain[0]['output'],grillestrain[1]['output'],grillestrain[2]['output'],grillestest[1]],alldata,"Départ","Fin","Obtenu")
    plt.show()
    return g.comparer(grillestest[1])

if __name__ == '__main__':
    #score = []
    #for i in indexTab:
    #    print(i)
    solveGrid(openJsonFile())
