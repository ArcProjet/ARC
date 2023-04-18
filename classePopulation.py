# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:57:28 2022

@author: jeanh
"""
from classeIndividu import *
import random
import copy

taille = 100

nbCyclesMAX = 20
#taille du groupe de la fonction generernouvelIndividu
#on prend le meilleur individu d'un groupe de taille_groupe
taille_groupe=5

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
            #if i.score > 0:
           #     print(i.score)
            dicoIndividusTemp[i] = i.score
            #print(dicoIndividusTemp)
        l = sorted(dicoIndividusTemp.items(), key=lambda t: t[1])
        self.individus = list(map(lambda x: x[0],l))[::-1]
        #print("[+] Best individu :",self.individus[0].score)
        #self.individus = list(dicoIndividusTemp.keys())
    
    def genererNouveauIndividu(self):
        # on sélectionne 5 individus random
        nombres_random = random.sample(range(taille), taille_groupe)
        #on choisit le plus petit nombre (correspond au meilleur individu car la liste est triée)
        meilleur_indiv_groupe1 = min(nombres_random)

        #On recommence avec un deuxième groupe
        nombres_random = random.sample(range(taille), taille_groupe)

        meilleur_indiv_groupe2 = min(nombres_random)

        #On fait un croisement de ces deux individus
        #on choisit quelle section intervertir
        numero_section = random.sample(range(taille), 2)
        #on les trie pour faciliter la suite
        nombres_random.sort()

        #On extrait les tableaux de fonctiosn de chaque individus
        fun_indiv1 = self.individus[meilleur_indiv_groupe1].fonctions
        fun_indiv2 = self.individus[meilleur_indiv_groupe2].fonctions

        #
        index_section = slice(numero_section[0], numero_section[1])

        #On copie une section de chaque individus
        section_indiv1 = fun_indiv1[index_section]
        section_indiv2 = fun_indiv2[index_section]

        #On échange les sections
        fun_indiv1[index_section]=section_indiv2
        fun_indiv2[index_section]=section_indiv1

        #On créé un nouvel individu avec une des deux sections
        #/!\/!\/!\A l'avenir il faudra créé deux individus d'un coup pour gagner du temps
        nouvel_individu = Individu(1,self.imageDepart,self.imageEsperee)
        nouvel_individu.fonctions = fun_indiv1
        return nouvel_individu


    def evoluerPopulation1Fois(self): # y a t il une fonction qui permet de trier une liste à partir d'un attribut des éléments de cette même liste


        populationTemp = []
        self.trierPopulation()
        # On conserve le meilleur individu
        populationTemp.append(copy.deepcopy(self.individus[0]))
        for i in range (1,taille):
            populationTemp.append(self.genererNouveauIndividu())
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
            individu.grille.modifierGrille(self.imageDepart,individu.fonctions)
    
    
    
    
    
    
    
    
    
    
    
    
    
    