# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:57:28 2022

@author: jeanh
"""
from classeIndividu import *

taille = 100

class Population:
    
    def __init__(self, im):
        self.individus = [None] * taille
        self.imageEsperee = im
        
    def ajouterIndividu(self, index):
        self.individus[index] = genererIndividu()    
        
    def genererPopulation():
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
        dicoIndividusTemp = sorted(dicoIndividusTemp.items(), key=lambda t: t[1])
        this.individus = dicoIndividusTemp.keys()
    
    def evoluerPopulation(self) # y a t il une fonction qui permet de trier une liste à partir d'un attribut des éléments de cette même liste
        # 1 On conserve les 50 meilleurs individus pour générer la population suivante
        # 2 les 10 premiers sont simplement mutés (1 fois)
        # 3 40 suivants sont créer par croisements entre les 50 premiers
        # 4 les 50 restants sont générés aléatoirement
        populationTemp = []
        #commentaire 2
        for i in range (0, 10):
            individus[i].muter()
            populationTemp.append(individus[i])
        for i in range(10, 20):
            individus[i].croiser2Individus(individus[0])
            populationTemp.append(individus[i])
        for i in range(20, 30):
            individus[i].croiser2Individus(individus[1])
            populationTemp.append(individus[i])
        for i in range(30, 40):
            individus[i].croiser2Individus(individus[2])
            populationTemp.append(individus[i])
        for i in range(40, 50):
            individus[i].croiser2Individus(individus[3])
            populationTemp.append(individus[i])
        for i in range(50, 100):
            populationTemp.append(Individu().genererIndividu())
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    