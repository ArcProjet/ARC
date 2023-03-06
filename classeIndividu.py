# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:37:39 2022

@author: jeanh
"""

from primitive import *
from random import randint
import classeGrille
from JsonLoader import *

toutesNosFonctions = [completed,gridCopy,rotateHalf,rotateLeft,rotateRight,extendLine,extendColumn,extendColorUp,extendColorDown,extendColorLeft,extendColorRight,growingColor,axialSymmetryX,axialSymmetryY,copyHalfX,copyHalfY,xHalf,yHalf,changeAColor,completeColor,doubleRow,tripleRow,doubleColumn,tripleColumn,doubleSymetryRow,doubleSymetryColumn,centralSymetry,inversion,lenghtReduction,widthReduction,translationVerticaleEnHaut,translationHorizontaleADroite,translationVerticaleEnBas,translationHorizontaleAGauche]#[completed,gridCopy,rotateHalf,rotateLeft,rotateRight,extendLine,extendColumn,extendColorUp,extendColorDown,extendColorLeft,extendColorRight,growingColor,axialSymmetryX,axialSymmetryY,copyHalfX,copyHalfY,xHalf,yHalf,changeAColor,completeColor,centralSymetry,inversion,removeNoiseFromGrid] # variables de classe partagées par toutes les instances
taille = 20 # taille du tableau "fonctions",

class Individu:

    def __init__(self, numeroConstructeur, imageDepart, imageEsperee):
        
        if(numeroConstructeur == 0):
            self.score = 0
            self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
            self.grille = None # visiblement null n'existe pas en python
            self.population # bien utile pour accéder à l'image espérée utilisée dans "attribuerScore"       
    # def genererIndividu(self): # peut être le mettre sous la forme d'un constructeur
        else:
            self.score = 0
            self.imageDepart = imageDepart.copy()
            self.imageEsperee = imageEsperee.copy()
            self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
            self.grille = None # visiblement null n'existe pas en python
            for i in range (0, taille): # remplissage complet de la liste
                self.ajouterFonction(i)
            self.genererGrille()
            #self.attribuerScore()
    
    def genererGrille(self):
        self.grille = classeGrille.Grille(self.imageDepart)
        
    def ajouterFonction(self, index):
        self.fonctions[index] = toutesNosFonctions[randint(0, len(toutesNosFonctions) - 1)] # remplissage à l'index donné de la liste   
          
    def attribuerScore(self):
        # compare l'image générée par l'individu à l'image attendue
        self.score = self.grille.comparer(self.imageEsperee) # compare est une méthode de la classe Grid
        #print(self.score if self.score > 50 else "")
        
    def croiser2Individus(self, individu2): # on fabrique unn nouvel individu à partir de 2 individus de la génération précédente
        newIndividu = Individu(1,self.imageDepart,self.imageEsperee)
        for i in range (0,taille//2):
            newIndividu.fonctions[i * 2] = self.fonctions[i * 2] # les index pairs du tableau "fonctions" associé au
            #nouvel individu seront remplis avec les index pairs du tableau associé à l'individu "self"
            newIndividu.fonctions[i * 2 + 1] = individu2.fonctions[i * 2 + 1] #idem en remplaçant pair par impair """
            
    def muter(self): # modifie un individu de la génération précédente
        index = randint(0, taille - 1)
        self.fonctions[index] = toutesNosFonctions[randint(0, len(toutesNosFonctions) - 1)] # on remplace une
        #fonction au hasard de notre individu par une fonction choisie au hasard présente dans notre base de fonctions
        
        
        
            
            
        
        
        
        
