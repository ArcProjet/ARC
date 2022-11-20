# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:57:28 2022

@author: jeanh
"""

class Population:
    
    taille = 100
    
    def __init__(self):
        self.individus = [None] * taille
        
    def ajouterIndividu(self, index):
        self.individus[index] = genererIndividu()    
        
    def genererPopulation():
        for i in range (0, taille): # remplissage complet de la liste
            self.ajouterIndividu(i)
            
    def trierPopulation(self):
        for i in range (0, taille):
            self.individus[i].attribuerScore()
        varTemp = null
        for i in range (0, taille):

        