from JsonLoader import *
from gestion import *

def displayGrid(gridInput,gridOutput,title1,title2):
    fig, axs = plt.subplots(1,2)
    axs[0].set_title(title1)
    axs[0].axis('off')
    axs[0].matshow(gridInput, cmap='rainbow')
    axs[1].set_title(title2)
    axs[1].axis('off')
    axs[1].matshow(gridOutput, cmap='rainbow')

if __name__ == '__main__':

    grillestrain,gridEvaluation = openJsonFile()

    gridEntree1, gridExpected1 = grillestrain[0]['input'],grillestrain[0]['output']
    gridEntree2, gridExpected2 = grillestrain[1]['input'],grillestrain[1]['output']
    gridEvaluationEntree, gridEvaluationExpected = gridEvaluation[0],gridEvaluation[1]

    #Pour générer des vecteurs de primitives
    res = generateFctTab(1,1)
    grilleSortie = applyFunctions(res[0],gridEntree1)

    #Pour tester sa primitive il faut remplacer le empty par le nom de sa fonction
    #grilleSortie = inversion(gridEntree1)

    displayGrid(gridEntree1,grilleSortie,"Grille Entrée", "Grille obtenu après primitive")
    displayGrid(grilleSortie,gridExpected1,"Grille obtenu après primitive", "Grille qu'on est censé obtenir")
    
    plt.show()