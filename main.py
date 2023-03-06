from matplotlib.colors import BoundaryNorm, ListedColormap
from primitive import *
from JsonLoader import *
from gestion import *
from grid import Grid
from classeGrille import Grille
from classeIndividu import Individu
from classePopulation import Population

def displayGrid(gridInput,gridOutput,title1,title2):
    colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'purple', 'darkgreen', 'grey', 'black']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(values, cmap.N)
    fig, axs = plt.subplots(1,2)
    axs[0].set_title(title1)
    axs[0].axis('off')
    axs[0].matshow(gridInput, cmap=cmap,norm=norm)
    axs[1].set_title(title2)
    axs[1].axis('off')
    axs[1].matshow(gridOutput, cmap=cmap,norm=norm)

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
        res = cpt#100*(cpt/(len(data)*len(data[0])))
        #res = 100*(cpt/cptVide)
        #print("Le pourcentage de réussite est de " + str(res) + "%")
        return res

if __name__ == '__main__':
    grillestrain,grillestest = openJsonFile()
    gridTrain1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridTrain2 = grillestrain[1]['input'],grillestrain[1]['output']

    p1 = Population(gridTrain1[1],gridTrain1[0])
        
    displayGrid(p1.imageDepart,p1.imageEsperee,"Grille de départ","Grille Attendu")

    p1.genererPopulation()
    p1.evolutionPopulation()
    
    displayGrid(p1.imageDepart,p1.individus[0].grille.data,"Grille de départ","Grille obtenu") 
    plt.show()
