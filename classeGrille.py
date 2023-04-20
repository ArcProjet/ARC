# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:29:33 2022

@author: jeanh
"""

from classeIndividu import *
from classePopulation import *
from math import *

class Grille:
    
    def __init__(self, grilleEntree):
        self.data = grilleEntree
               
    def modifierGrille(self,grilleEntree,sequence):
        self.data = grilleEntree
        for fonction in sequence:
            if(len(self.data) >= 1 and len(self.data[0]) >= 1):
                self.data = fonction(self.data)
        #self.data = grilleEntree
        #for fonction in sequence:
        #    self.data = fonction(self.data)
    
    def comparer(self, grilleEsperee):
        if(len(self.data) > 0 and len(self.data[0]) > 0):
            nb_pixels = len(self.data) * len(self.data[0])
            nb_pixels_identiques = 0
            if len(self.data) != len(grilleEsperee) or len(self.data[0]) != len(grilleEsperee[0]):
                # Les deux grilles n'ont pas la même taille, on ne peut pas les comparer.
                return 0
            for i in range(len(self.data)):
                for j in range(len(self.data[0])):
                    if grilleEsperee[i][j] == self.data[i][j]:
                        # Le pixel (i, j) des deux grilles est identique.
                        nb_pixels_identiques += 1
            if nb_pixels == 0:
                # Les deux grilles sont vides, on considère qu'elles sont identiques.
                return 100
            return nb_pixels_identiques / nb_pixels * 100
        return 0

          