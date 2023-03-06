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

def comparer(data,grilleEsperee):
        cpt = 0
        cptPixelNoir = 0
        if(len(data) != len(grilleEsperee) or len(data[0]) != len(grilleEsperee[0])): # Temporaire avec les grilles non carré
            return 0
        for i in range(0,len(data)):
            for j in range(0,len(data[0])):
                # if(self.imageEsperee[i][j] != 0): # compte les pixels noirs
                    # cptPixelNoir += 1
                if(grilleEsperee[i][j] == data[i][j]):   #and self.expected[i][j] != 0):
                    cpt += 1
        res = 100*(cpt/(len(data)*len(data[0])))
        #res = 100*(cpt/cptVide)
        #print("Le pourcentage de réussite est de " + str(res) + "%")
        return res

if __name__ == '__main__':
    grillestrain,grillestest = openJsonFile()
    gridTrain1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']

    p = Population(gridTrain1[1],gridTrain1[0])
        
    displayGrid(p.imageDepart,p.imageEsperee,"Grille de départ","Grille Attendu")

    p.genererPopulation()
    p.evolutionPopulation()
    
    print(comparer(p.individus[-1].grille.data,p.imageEsperee))

    displayGrid(p.imageDepart,p.individus[0].grille.data,"Grille de départ","Grille obtenu")
    
    #ttt.ExpectationVsreality()
    plt.show()
