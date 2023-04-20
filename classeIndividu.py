# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:37:39 2022

@author: jeanh
"""

from primitive import *
from random import randint
import classeGrille
from JsonLoader import *

toutesNosFonctions = [axialSymmetryX,axialSymmetryY,centralSymetry,copyHalfX,copyHalfY,doubleSymetryRow,doubleSymetryColumn,xHalf,yHalf,doubleRow,doubleColumn,rotateLeft,rotateRight,translationEnHaut,translationADroite,translationEnBas,translationAGauche,extendColorUp0,extendColorUp1,extendColorUp2,extendColorUp3,extendColorUp4,extendColorUp5,extendColorUp6,extendColorUp7,extendColorUp8,extendColorUp9,extendColorDown0,extendColorDown1,extendColorDown2,extendColorDown3,extendColorDown4,extendColorDown5,extendColorDown6,extendColorDown7,extendColorDown8,extendColorDown9,extendColorLeft0,extendColorLeft1,extendColorLeft2,extendColorLeft3,extendColorLeft4,extendColorLeft5,extendColorLeft6,extendColorLeft7,extendColorLeft8,extendColorLeft9,extendColorRight0,extendColorRight1,extendColorRight2,extendColorRight3,extendColorRight4,extendColorRight5,extendColorRight6,extendColorRight7,extendColorRight8,extendColorRight9,growingColor0,growingColor1,growingColor2,growingColor3,growingColor4,growingColor5,growingColor6,growingColor7,growingColor8,growingColor9,removeNoise0,removeNoise1,removeNoise2,removeNoise3,removeNoise4,removeNoise5,removeNoise6,removeNoise7,removeNoise8,removeNoise9,changeAColor0_1,changeAColor0_2,changeAColor0_3,changeAColor0_4,changeAColor0_5,changeAColor0_6,changeAColor0_7,changeAColor0_8,changeAColor0_9,changeAColor1_0,changeAColor1_2,changeAColor1_3,changeAColor1_4,changeAColor1_5,changeAColor1_6,changeAColor1_7,changeAColor1_8,changeAColor1_9,changeAColor2_0,changeAColor2_1,changeAColor2_3,changeAColor2_4,changeAColor2_5,changeAColor2_6,changeAColor2_7,changeAColor2_8,changeAColor2_9,changeAColor3_0,changeAColor3_1,changeAColor3_2,changeAColor3_4,changeAColor3_5,changeAColor3_6,changeAColor3_7,changeAColor3_8,changeAColor3_9,changeAColor4_0,changeAColor4_1,changeAColor4_2,changeAColor4_3,changeAColor4_5,changeAColor4_6,changeAColor4_7,changeAColor4_8,changeAColor4_9,changeAColor5_0,changeAColor5_1,changeAColor5_2,changeAColor5_3,changeAColor5_4,changeAColor5_6,changeAColor5_7,changeAColor5_8,changeAColor5_9,changeAColor6_0,changeAColor6_1,changeAColor6_2,changeAColor6_3,changeAColor6_4,changeAColor6_5,changeAColor6_7,changeAColor6_8,changeAColor6_9,changeAColor7_0,changeAColor7_1,changeAColor7_2,changeAColor7_3,changeAColor7_4,changeAColor7_5,changeAColor7_6,changeAColor7_8,changeAColor7_9,changeAColor8_0,changeAColor8_1,changeAColor8_2,changeAColor8_3,changeAColor8_4,changeAColor8_5,changeAColor8_6,changeAColor8_7,changeAColor8_9,changeAColor9_0,changeAColor9_1,changeAColor9_2,changeAColor9_3,changeAColor9_4,changeAColor9_5,changeAColor9_6,changeAColor9_7,changeAColor9_8]
taille = 20 # taille du tableau "fonctions",

class Individu:

    def __init__(self, numeroConstructeur, gridInput, gridWishes):
        
        if(numeroConstructeur == 0):
            self.score = 0
            self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
            self.grille = [] # visiblement null n'existe pas en python
            self.population # bien utile pour accéder à l'image espérée utilisée dans "attribuerScore"       
    # def genererIndividu(self): # peut être le mettre sous la forme d'un constructeur
        else:
            self.score = 0
            self.gridInput = gridInput#.copy()
            self.gridWishes = gridWishes#.copy()
            self.fonctions = [None] * taille # création d'une nouvelle liste vide pour chaque individu
            self.grille = [] # visiblement null n'existe pas en python
            for i in range (0, taille): # remplissage complet de la liste
                self.ajouterFonction(i)
            self.genererGrille()
            #self.attribuerScore()
    
    def genererGrille(self):
        for g in self.gridInput:
            self.grille.append(classeGrille.Grille(g))
        
    def ajouterFonction(self, index):
        self.fonctions[index] = toutesNosFonctions[randint(0, len(toutesNosFonctions) - 1)] # remplissage à l'index donné de la liste   
          
    def attribuerScore(self):
        # compare l'image générée par l'individu à l'image attendue
        tmp = 0
        for i in range(len(self.gridInput)):
            tmp += self.grille[i].comparer(self.gridWishes[i]) # compare est une méthode de la classe Grid
        self.score = tmp/(len(self.gridInput))
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
        
        
        
            
            
        
        
        
        
