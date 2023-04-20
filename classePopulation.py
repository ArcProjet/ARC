# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:57:28 2022

@author: jeanh
"""
from classeIndividu import *
import random
import copy

taille = 100

taux_mutation = 10

nbCyclesMAX = 10
#taille du groupe de la fonction generernouvelIndividu
#on prend le meilleur individu d'un groupe de taille_groupe
taille_groupe=5

class Population:
    
    def __init__(self,gridInput,gridWishes):
        self.individus = [None] * taille
        self.gridInput = gridInput
        self.gridWishes = gridWishes
        #self.imageEsperee = im
        #self.imageDepart = dep
        
    def ajouterIndividu(self, index):
        self.individus[index] = Individu(1,self.gridInput,self.gridWishes)
        
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
            #if i.score > 0:
           #     print(i.score)
            dicoIndividusTemp[i] = i.score
            #print(dicoIndividusTemp)
        l = sorted(dicoIndividusTemp.items(), key=lambda t: t[1])
        self.individus = list(map(lambda x: x[0],l))[::-1]
        #print("     [-] Best individu :",self.individus[0].score)
        #self.individus = list(dicoIndividusTemp.keys())
    
    def genererNouveauIndividu(self):
        # on sélectionne 5 individus random
        nombres_random = random.sample(range(taille), taille_groupe-1)
        #on choisit le plus petit nombre (correspond au meilleur individu car la liste est triée)
        
        vector_individu = {}

        for n in nombres_random:

            vector_individu[self.individus[n]] = self.individus[n].score

        meilleur_indiv_groupe1 = list(sorted(vector_individu.items(), key=lambda t: t[1])[-1])

        #On recommence avec un deuxième groupe
        nombres_random = random.sample(range(taille), taille_groupe-1)

        vector_individu = {}

        for n in nombres_random:

            vector_individu[self.individus[n]] = self.individus[n].score

        meilleur_indiv_groupe2 = list(sorted(vector_individu.items(), key=lambda t: t[1])[-1])

        #On fait un croisement de ces deux individus
        #on choisit quelle section intervertir
        numero_section = randint(0,20)
        #on les trie pour faciliter la suite

        #On extrait les tableaux de fonctiosn de chaque individus
        fun_indiv1 = meilleur_indiv_groupe1[0].fonctions#self.individus[meilleur_indiv_groupe1].fonctions
        fun_indiv2 = meilleur_indiv_groupe2[0].fonctions#self.individus[meilleur_indiv_groupe2].fonctions

        #On choisit si on met le vecteur de l'individu 1 avant l'individu 2
        new_fun1 = []
        new_fun2 = []

        for i in range(numero_section):
            new_fun1.append(fun_indiv1[i])
            new_fun2.append(fun_indiv2[i])
        
        for i in range(numero_section,20):
            new_fun1.append(fun_indiv2[i])
            new_fun2.append(fun_indiv1[i])

        #On créé un nouvel individu avec une des deux sections
        #/!\/!\/!\A l'avenir il faudra créé deux individus d'un coup pour gagner du temps
        nouvel_individu1 = Individu(1,self.gridInput,self.gridWishes)
        nouvel_individu1.fonctions = new_fun1
        if randint(0,taux_mutation)==0:
            nouvel_individu1.muter()
        nouvel_individu2 = Individu(1,self.gridInput,self.gridWishes)
        nouvel_individu2.fonctions = new_fun2
        if randint(0,taux_mutation)==0:
            nouvel_individu2.muter()
        return nouvel_individu1,nouvel_individu2


    def evoluerPopulation1Fois(self): # y a t il une fonction qui permet de trier une liste à partir d'un attribut des éléments de cette même liste


        populationTemp = []
        self.trierPopulation()
        # On conserve le meilleur individu
        populationTemp.append(copy.deepcopy(self.individus[0]))
        for i in range (1,int(taille//2)+1):
            ind1,ind2 = self.genererNouveauIndividu()
            populationTemp.append(ind1)
            populationTemp.append(ind2)
        self.individus = populationTemp
        self.modifierGrille()
        return

        
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
            for i in range(len(self.gridInput)):
                individu.grille[i].modifierGrille(self.gridInput[i],individu.fonctions)
    
    
    
    
    
    
    
    
    
    
    
    
    
    