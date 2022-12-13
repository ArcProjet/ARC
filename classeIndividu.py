# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:37:39 2022

@author: jeanh
"""

from primitive import *
from random import randint
from grid import Grid

toutesNosFonctions = [rotateHalf, rotateLeft, rotateRight, centralSymetry] # variables de classe partagées par toutes les instances
taille = 20 # taille du tableau "fonctions"

class Individu:

    def __init__(self):
        self.score = 0
        self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
        self.grille = null
        self.population # bien utile pour accéder à l'image espérée utilisée dans "attribuerScore"
        
    def genererIndividu(self): # peut être le mettre sous la forme d'un constructeur
        for i in range (0, taille): # remplissage complet de la liste
            self.ajouterFonction(i)
        self.genererGrille()
        self.attribuerScore()
        
    def ajouterFonction(self, index):
        self.fonctions[index] = toutesNosFonctions[randint(0, len(toutesNosFonctions) - 1)] # remplissage à l'index donné de la liste   
          
    def attribuerScore(self):
        # compare l'image générée par l'individu à l'image attendue
        self.score = self.grille.comparer(self.ImageEsperee) # compare est une méthode de la classe Grid
        
    def croiser2Individus(self, individu2): # on fabrique unn nouvel individu à partir de 2 individus de la génération précédente
        newIndividu = Individu()
        for i in range (0,taille//2):
            newIndividu.fonctions[i * 2] = self.fonctions[i * 2] # les index pairs du tableau "fonctions" associé au
            #nouvel individu seront remplis avec les index pairs du tableau associé à l'individu "self"
            newIndividu.fonctions[i * 2 + 1] = individu2.fonctions[i * 2 + 1] #idem en remplaçant pair par impair """
            
    def muter(self): # modifie un individu de la génération précédente
        index = randint(0, taille - 1)
        self.fonctions[index] = toutesNosFonctions[randint(0, len(toutesNosFonctions) - 1)] # on remplace une
        #fonction au hasard de notre individu par une fonction choisie au hasard présente dans notre base de fonctions
        
        
        
            
            
        
        
        
        
