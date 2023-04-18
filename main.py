from matplotlib.colors import BoundaryNorm, ListedColormap
from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid
from classeGrille import Grille
from classeIndividu import Individu
from classePopulation import Population

NB_POPULATIONS = 100

def displayGrid(gridInput,gridOutput,gridObtain,title1,title2,title3):
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'purple', 'darkgreen', 'grey', 'black']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(values, cmap.N)
    fig, axs = plt.subplots(1,3)
    axs[0].set_title(title1)
    axs[0].axis('off')
    axs[0].matshow(gridInput, cmap=cmap,norm=norm)
    axs[1].set_title(title2)
    axs[1].axis('off')
    axs[1].matshow(gridOutput, cmap=cmap,norm=norm)
    axs[2].set_title(title3)
    axs[2].axis('off')
    axs[2].matshow(gridObtain, cmap=cmap,norm=norm)

def crossOver(l1,l2,ind1,ind2):
    
    print(len(ind1))

    for i in range(len(ind1)-int((NB_POPULATIONS/2))-1):
        ind1[i] = l1[i]
        ind2[i] = l2[i]

    for i in range(len(ind1)-int((NB_POPULATIONS/2))-1,len(ind1)-(NB_POPULATIONS)):
        ind1[i] = l2[i]
        ind2[i] = l1[i]

    return ind1,ind2

def KingOfTheHill(grid):

    leaderboard = []

    print("[+] --------- KingOfTheHill ---------")

    for _ in range(NB_POPULATIONS):
        
        p1 = Population(grid[1],grid[0])
        
        p1.genererPopulation()
        p1.evolutionPopulation()

        leaderboard.append(p1.individus[0])

        print("[+] ["+str(_)+"/"+str(NB_POPULATIONS-1)+"] Score : " + str(p1.individus[0].score))

    return leaderboard


def solveGrid(grid):

    grillestrain,grillestest = grid
    gridTrain1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']
    grillestest = grillestest[0],grillestest[1]

    print("[+] Populations choose their King")

    leaderboard1 = KingOfTheHill(gridTrain1)
    leaderboard2 = KingOfTheHill(gridTrain2)

    p1 = Population(gridTrain1[1],gridTrain1[0])
    p2 = Population(gridTrain2[1],gridTrain2[0])

    p1.genererPopulation()
    p2.genererPopulation()

    p1.individus,p2.individus = leaderboard1,leaderboard2#crossOver(leaderboard1,leaderboard2,p1.individus,p2.individus)

    p1.evolutionPopulation()
    p2.evolutionPopulation()
    
    bestP1 = p1.individus[0]
    bestP2 = p2.individus[0]

    scoreP1 = p1.individus[0].score
    scoreP2 = p2.individus[0].score 


    print("[+] Populations have chosen their King")

    print("[+] --------- Prepare for King Battle ---------")

    bestP1.grille.modifierGrille(gridTrain2[0],bestP1.fonctions)
    print("[+] P1 score in train2 : " + str(bestP1.grille.comparer(gridTrain2[1])))
    scoreP1 += bestP1.grille.comparer(gridTrain2[1])

    bestP2.grille.modifierGrille(gridTrain1[0],bestP2.fonctions)
    print("[+] P2 score in train1 : " + str(bestP2.grille.comparer(gridTrain1[1])))
    scoreP2 += bestP2.grille.comparer(gridTrain1[1])

    print("[+] Score for P1 : " + str(scoreP1/2) + " , Score for P2 : " + str(scoreP2/2))

    if scoreP1 > scoreP2:
        bestIndividu = bestP1
    else:
        bestIndividu = bestP2

    bestIndividu.grille.modifierGrille(grillestest[0],bestIndividu.fonctions)
    print("[+] Best individu score in final grid : " + str(bestIndividu.grille.comparer(grillestest[1])))

    displayGrid(grillestest[0],grillestest[1],bestIndividu.grille.data,"Grille de départ","Grille de Fin","Grille obtenu")
    plt.show()

    return bestP1.grille.comparer(grillestest[1])

if __name__ == '__main__':
    solveGrid(openJsonFile())