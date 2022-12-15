# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:57:28 2022

@author: jeanh
"""
from classeIndividu import *


taille = 100
nbCyclesMAX = 1000

class Population:
    
    def __init__(self,im,dep):
        self.individus = [None] * taille
        self.imageEsperee = im
        self.imageDepart = dep
        
    def ajouterIndividu(self, index):
        self.individus[index] = Individu(1,self.imageDepart,self.imageEsperee)
        
    def genererPopulation(self):
        for i in range (0, taille): # remplissage complet de la liste
            self.ajouterIndividu(i)
            
    def trierPopulation(self):
        for i in range (0, taille):
            self.individus[i].attribuerScore()
        #varTemp = null
        #for i in range (0, taille):
        dicoIndividusTemp = {}
        for i in self.individus:
            dicoIndividusTemp[i] = i.score
        sorted(dicoIndividusTemp.items(), key=lambda t: t[1])
        self.individus = list(dicoIndividusTemp.keys())
    
    def evoluerPopulation1Fois(self): # y a t il une fonction qui permet de trier une liste à partir d'un attribut des éléments de cette même liste
        
        # on suppose que la population de départ est triée
        
        # 1 On conserve les 50 meilleurs individus pour générer la population suivante
        # 2 les 10 premiers sont simplement mutés (1 fois)
        # 3 40 suivants sont créer par croisements entre les 50 premiers
        # 4 les 50 restants sont générés aléatoirement
        populationTemp = []
        self.trierPopulation()
        # commentaire 2
        for i in range (0, 10):
            self.individus[i].muter()
            populationTemp.append(self.individus[i])
        # commentaire 3
        for i in range(10, 20):
            self.individus[i].croiser2Individus(self.individus[0])
            populationTemp.append(self.individus[i])
        for i in range(20, 30):
            self.individus[i].croiser2Individus(self.individus[1])
            populationTemp.append(self.individus[i])
        for i in range(30, 40):
            self.individus[i].croiser2Individus(self.individus[2])
            populationTemp.append(self.individus[i])
        for i in range(40, 50):
            self.individus[i].croiser2Individus(self.individus[3])
            populationTemp.append(self.individus[i])
        # commentaire 4
        for i in range(50, 100):
            populationTemp.append(Individu(1,self.imageDepart,self.imageEsperee))
        self.modifierGrille()
        
    def evolutionPopulation(self):
        nbCycles = 0
        self.modifierGrille()
        while(self.individus[0].score != 100 and nbCycles < nbCyclesMAX):        
            self.evoluerPopulation1Fois()
            nbCycles += 1
        self.trierPopulation()
        return self.individus[0]
                
    def modifierGrille(self):
        for individu in self.individus:
            individu.grille.modifierGrille(self.imageDepart,individu.fonctions)
    
    
    
    
    
    
    
    
    
    
    
    
    
    