# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:29:33 2022

@author: jeanh
"""

class Grille :
    
    def __init__(self, grilleEntree):
        self.data = grilleEntree
               
    def modifierGrille(self, grilleEntree, sequence):
        self.data =  grilleEntree
        for fonction in sequence:
            self.data = fonction(self.data)
    
    def comparer(self, grilleEsperee):
        cpt = 0
        cptPixelNoir = 0
        if(len(self.data) != len(self.grilleEsperee) or len(self.data[0]) != len(self.grilleEsperee[0])): # Temporaire avec les grilles non carré
            return 0
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[0])):
                # if(self.imageEsperee[i][j] != 0): # compte les pixels noirs
                    # cptPixelNoir += 1
                if(self.imageEsperee[i][j] == self.data[i][j]):   #and self.expected[i][j] != 0):
                    cpt += 1
        res = 100*(cpt/(len(self.output)*len(self.output[0])))
        #res = 100*(cpt/cptVide)
        #print("Le pourcentage de réussite est de " + str(res) + "%")
        return res
    
    

          