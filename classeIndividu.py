# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:37:39 2022

@author: jeanh
"""

from primitive import *
from ramdom import randint
from grid import Grid

class Individu:
    
    toutesNosFonctions = [rotateHalf, rotateLeft, rotateRight, centralSymetry] # variables de classe partagées par toutes les instances
    taille = 20 # taille du tableau "fonctions"
    
    def __init__(self):
        self.score = 0
        self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
        
    def ajouterFonction(self, index):
        self.fonctions[index] = toutesNosFonctions[random.randint(0, length(toutesNosFonctions) - 1)] # remplissage à l'index donné de la liste
        
    def genererIndividu(self):
        for i in range (0, taille): # remplissage complet de la liste
            self.ajouterFonction(i)
            
    def attribuerScore(self):
        self.score = self.input.compare(self.ouput) # compare est une méthode de la classe Grid
        
    def croiser2Individus(self, individu2): # on fabrique unn nouvel individu à partir de 2 individus de la génération précédente
        newIndividu = Individu()
        for i in range (0,taille//2):
            newIndividu.fonctions[i * 2] = self.fonctions[i * 2] """ les index pairs du tableau "fonctions" associé au
            nouvel individu seront remplis avec les index pairs du tableau associé à l'individu "self" """
            newIndividu.fonctions[i * 2 + 1] = individu2.fonctions[i * 2 + 1] """ idem en remplaçant pair par impair """
            
     def  muter(self): # modifie un individu de la génération précédente
         index = random.randint(O, taille - 1)
         self.fonctions[index] = toutesNosFonctions[random.randint(0, length(toutesNosFonctions) - 1)] """ on remplace une
         fonction au hasard de notre individu par une fonction choisie au hasard présente dans notre base de fonctions"""
         
            
    
            
            
        
        
        
        
