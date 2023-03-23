#from random import randint

#Copie proprement les grilles
def gridCopy(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            res[i][j] = grid[i][j]
    return res

#Effectue une symetrie sur l'axe des X
def axialSymmetryX(grid):
    res = gridCopy(grid)
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            res[i][j] = grid[len(grid)-i-1][j]
    return res

#Effectue une symetrie sur l'axe des Y
def axialSymmetryY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][len(grid[0])-j-1]
    return res

#Effectue une symetrie en diagonal si possible sinon gridCopy
def centralSymetry(grid):
    if (len(grid) == len(grid[0])):
        res = gridCopy(grid)
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = grid[j][i]
        return res
    else:
        res2 = gridCopy(grid)
        return res2

#Effectue une symetrie sur l'axe des X de le moitié de la grille et la copie dans l'autre moitié de la grille
def copyHalfX(grid):
    res = gridCopy(grid)
    for i in range(0,int(len(grid)/2)):
        for j in range(0,len(grid[i])):
            res[i][j] = grid[len(grid)-i-1][j]
    return res

#Effectue une symetrie sur l'axe des Y de le moitié de la grille et la copie dans l'autre moitié de la grille
def copyHalfY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i])/2)):
            res[i][j] = grid[i][len(grid[0])-j-1]
    return res

#Effectue une symetrie sur l'axe des X de la grille et la copie au dessus
def doubleSymetryRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*2)]
    sym = axialSymmetryX(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid)+i][j] = sym[i][j]
    return res

#Effectue une symetrie sur l'axe des Y de la grille et la copie sur le coté
def doubleSymetryColumn(grid):
    res = [[0 for _ in range((len(grid[0]))*2)] for _ in range(len(grid))]
    sym = axialSymmetryY(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0])+j] = sym[i][j]
    return res

#Coupe la grille en 2 sur l'axe des X
def xHalf(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(int(len(grid)/2))]
    for i in range(0, int(len(grid)/2)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res

#Coupe la grille en 2 sur l'axe des Y
def yHalf(grid):
    res = [[0 for _ in range(int(len(grid[0])/2))] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i])/2)):
            res[i][j] = grid[i][j]
    return res

#Double la grille sur la hauteur
def doubleRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*2)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid)+i][j] = grid[i][j]
    return res

#Double la grille sur la largeur
def doubleColumn(grid):
    res = [[0 for _ in range((len(grid[0]))*2)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0])+j] = grid[i][j]
    return res

#Effectue une rotation sur la gauche
def rotateLeft(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = 0
        for j in range(len(res[0])):
            res[i][j] = grid[cpt][len(grid[0]) - i - 1]
            cpt += 1
    return res

#Effectue une rotation sur la droite
def rotateRight(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = len(grid)
        for j in range(len(res[0])):
            cpt -= 1
            res[i][j] = grid[cpt][i]
    return res

#Effectue une tranlation de toute les couleurs vers le haut
def translationEnHaut(grid):
    res = gridCopy(grid)
    for i in range(0,len(grid)-1):
        for j in range(0,len(grid[0])):
            res[i][j] = grid[i+1][j]
    for l in range(0,len(grid[0])):
        res[len(grid)-1][l] = grid[0][l]
    return res

#Effectue une tranlation de toute les couleurs vers la droite
def translationADroite(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            res[i][j + 1] = grid[i][j]
        res[i][0] = grid[i][len(grid[0])-1]
    return res

#Effectue une tranlation de toute les couleurs vers le bas
def translationEnBas(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            res[i + 1][j] = grid[i][j]
    for l in range(0, len(grid[0])):
        res[0][l] = grid[len(grid)-1][l]
    return res

#Effectue une tranlation de toute les couleurs vers la gauche
def translationAGauche(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            res[i][j - 1] = grid[i][j]
        res[i][len(grid[0])-1] = grid[i][0]
    return res

#Etend la valeur 0 vers le haut
def extendColorUp0(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 0):
                res[i-1][j] = 0
    return res

#Etend la valeur 1 vers le haut
def extendColorUp1(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 1):
                res[i-1][j] = 1
    return res

#Etend la valeur 2 vers le haut
def extendColorUp2(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 2):
                res[i-1][j] = 2
    return res

#Etend la valeur 3 vers le haut
def extendColorUp3(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 3):
                res[i-1][j] = 3
    return res

#Etend la valeur 4 vers le haut
def extendColorUp4(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 4):
                res[i-1][j] = 4
    return res

#Etend la valeur 5 vers le haut
def extendColorUp5(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 5):
                res[i-1][j] = 5
    return res

#Etend la valeur 6 vers le haut
def extendColorUp6(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 6):
                res[i-1][j] = 6
    return res

#Etend la valeur 7 vers le haut
def extendColorUp7(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 7):
                res[i-1][j] = 7
    return res

#Etend la valeur 8 vers le haut
def extendColorUp8(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 8):
                res[i-1][j] = 8
    return res

#Etend la valeur 9 vers le haut
def extendColorUp9(grid):
    res = gridCopy(grid)
    for i in range(1,len(res)):
        for j in range(len(res[0])):
            if(res[i][j] == 9):
                res[i-1][j] = 9
    return res

#Etend la valeur 0 vers le bas
def extendColorDown0(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 0):
                res[i+1][j] = 0
    return res

#Etend la valeur 1 vers le bas
def extendColorDown1(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 1):
                res[i+1][j] = 1
    return res

#Etend la valeur 2 vers le bas
def extendColorDown2(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 2):
                res[i+1][j] = 2
    return res

#Etend la valeur 3 vers le bas
def extendColorDown3(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 3):
                res[i+1][j] = 3
    return res

#Etend la valeur 4 vers le bas
def extendColorDown4(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 4):
                res[i+1][j] = 4
    return res

#Etend la valeur 5 vers le bas
def extendColorDown5(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 5):
                res[i+1][j] = 5
    return res

#Etend la valeur 6 vers le bas
def extendColorDown6(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 6):
                res[i+1][j] = 6
    return res

#Etend la valeur 7 vers le bas
def extendColorDown7(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 7):
                res[i+1][j] = 7
    return res

#Etend la valeur 8 vers le bas
def extendColorDown8(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 8):
                res[i+1][j] = 8
    return res

#Etend la valeur 9 vers le bas
def extendColorDown9(grid):
    res = gridCopy(grid)
    for i in range(len(res)-2,-1,-1):
        for j in range(len(res[0])):
            if(res[i][j] == 9):
                res[i+1][j] = 9
    return res

#Etend la valeur 0 vers la gauche
def extendColorLeft0(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 0):
                res[i][j-1] = 0
    return res

#Etend la valeur 1 vers la gauche
def extendColorLeft1(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 1):
                res[i][j-1] = 1
    return res

#Etend la valeur 2 vers la gauche
def extendColorLeft2(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 2):
                res[i][j-1] = 2
    return res

#Etend la valeur 3 vers la gauche
def extendColorLeft3(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 3):
                res[i][j-1] = 3
    return res

#Etend la valeur 4 vers la gauche
def extendColorLeft4(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 4):
                res[i][j-1] = 4
    return res

#Etend la valeur 5 vers la gauche
def extendColorLeft5(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 5):
                res[i][j-1] = 5
    return res

#Etend la valeur 6 vers la gauche
def extendColorLeft6(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 6):
                res[i][j-1] = 6
    return res

#Etend la valeur 7 vers la gauche
def extendColorLeft7(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 7):
                res[i][j-1] = 7
    return res

#Etend la valeur 8 vers la gauche
def extendColorLeft8(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 8):
                res[i][j-1] = 8
    return res

#Etend la valeur 9 vers la gauche
def extendColorLeft9(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1,len(res[0])):
            if(res[i][j] == 9):
                res[i][j-1] = 9
    return res

#Etend la valeur 0 vers la droite
def extendColorRight0(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 0):
                res[i][j+1] = 0
    return res

#Etend la valeur 1 vers la droite
def extendColorRight1(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 1):
                res[i][j+1] = 1
    return res

#Etend la valeur 2 vers la droite
def extendColorRight2(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 2):
                res[i][j+1] = 2
    return res

#Etend la valeur 3 vers la droite
def extendColorRight3(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 3):
                res[i][j+1] = 3
    return res

#Etend la valeur 4 vers la droite
def extendColorRight4(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 4):
                res[i][j+1] = 4
    return res

#Etend la valeur 5 vers la droite
def extendColorRight5(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 5):
                res[i][j+1] = 5
    return res

#Etend la valeur 6 vers la droite
def extendColorRight6(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 6):
                res[i][j+1] = 6
    return res

#Etend la valeur 7 vers la droite
def extendColorRight7(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 7):
                res[i][j+1] = 7
    return res

#Etend la valeur 8 vers la droite
def extendColorRight8(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 8):
                res[i][j+1] = 8
    return res

#Etend la valeur 9 vers la droite
def extendColorRight9(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0])-2,-1,-1):
            if(res[i][j] == 9):
                res[i][j+1] = 9
    return res

#Fait grossir de 1 la valeur 0 dans la grille
def growingColor0(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 0):
                res[i-1][j] = 0
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 0):
                res[k][l+1] = 0
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 0):
                res[m+1][n] = 0
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 0):
                res[o][p-1] = 0
    return res

#Fait grossir de 1 la valeur 1 dans la grille
def growingColor1(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 1):
                res[i-1][j] = 1
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 1):
                res[k][l+1] = 1
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 1):
                res[m+1][n] = 1
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 1):
                res[o][p-1] = 1
    return res

#Fait grossir de 1 la valeur 2 dans la grille
def growingColor2(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 2):
                res[i-1][j] = 2
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 2):
                res[k][l+1] = 2
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 2):
                res[m+1][n] = 2
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 2):
                res[o][p-1] = 2
    return res

#Fait grossir de 1 la valeur 3 dans la grille
def growingColor3(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 3):
                res[i-1][j] = 3
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 3):
                res[k][l+1] = 3
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 3):
                res[m+1][n] = 3
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 3):
                res[o][p-1] = 3
    return res

#Fait grossir de 1 la valeur 4 dans la grille
def growingColor4(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 4):
                res[i-1][j] = 4
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 4):
                res[k][l+1] = 4
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 4):
                res[m+1][n] = 4
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 4):
                res[o][p-1] = 4
    return res

#Fait grossir de 1 la valeur 5 dans la grille
def growingColor5(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 5):
                res[i-1][j] = 5
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 5):
                res[k][l+1] = 5
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 5):
                res[m+1][n] = 5
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 5):
                res[o][p-1] = 5
    return res

#Fait grossir de 1 la valeur 6 dans la grille
def growingColor6(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 6):
                res[i-1][j] = 6
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 6):
                res[k][l+1] = 6
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 6):
                res[m+1][n] = 6
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 6):
                res[o][p-1] = 6
    return res

#Fait grossir de 1 la valeur 7 dans la grille
def growingColor7(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 7):
                res[i-1][j] = 7
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 7):
                res[k][l+1] = 7
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 7):
                res[m+1][n] = 7
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 7):
                res[o][p-1] = 7
    return res

#Fait grossir de 1 la valeur 8 dans la grille
def growingColor8(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 8):
                res[i-1][j] = 8
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 8):
                res[k][l+1] = 8
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 8):
                res[m+1][n] = 8
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 8):
                res[o][p-1] = 8
    return res

#Fait grossir de 1 la valeur 9 dans la grille
def growingColor9(grid):
    res = gridCopy(grid)
    for i in range(1,len(grid)):
        for j in range(len(grid[0])):
            if(grid[i][j] == 9):
                res[i-1][j] = 9
    for k in range(0,len(grid)):
        for l in range(len(grid[0])-2,-1,-1):
            if(grid[k][l] == 9):
                res[k][l+1] = 9
    for m in range(len(grid)-2,-1,-1):
        for n in range(len(grid[0])):
            if(grid[m][n] == 9):
                res[m+1][n] = 9
    for o in range(len(grid)):
        for p in range(1,len(grid[0])):
            if(grid[o][p] == 9):
                res[o][p-1] = 9
    return res

#Enlève le "bruit" déterminer par un seuil de 0
def removeNoise0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 0:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 1
def removeNoise1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 1:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 2
def removeNoise2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 2:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 3
def removeNoise3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 3:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 4
def removeNoise4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 4:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 5
def removeNoise5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 5:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 6
def removeNoise6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 6:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 7
def removeNoise7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 7:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 8
def removeNoise8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 8:
                res[i][j] = 0
    return res

#Enlève le "bruit" déterminer par un seuil de 9
def removeNoise9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 9:
                res[i][j] = 0
    return res

#Change la valeur 0 par 1
def changeAColor0_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 1
    return res

#Change la valeur 0 par 2
def changeAColor0_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 2
    return res

#Change la valeur 0 par 3
def changeAColor0_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 3
    return res

#Change la valeur 0 par 4
def changeAColor0_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 4
    return res

#Change la valeur 0 par 5
def changeAColor0_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 5
    return res

#Change la valeur 0 par 6
def changeAColor0_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 6
    return res

#Change la valeur 0 par 7
def changeAColor0_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 7
    return res

#Change la valeur 0 par 8
def changeAColor0_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 8
    return res

#Change la valeur 0 par 9
def changeAColor0_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 0):
                res[i][j] = 9
    return res

#Change la valeur 1 par 0
def changeAColor1_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 0
    return res

#Change la valeur 1 par 2
def changeAColor1_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 2
    return res

#Change la valeur 1 par 3
def changeAColor1_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 3
    return res

#Change la valeur 1 par 4
def changeAColor1_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 4
    return res

#Change la valeur 1 par 5
def changeAColor1_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 5
    return res

#Change la valeur 1 par 6
def changeAColor1_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 6
    return res

#Change la valeur 1 par 7
def changeAColor1_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 7
    return res

#Change la valeur 1 par 8
def changeAColor1_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 8
    return res

#Change la valeur 1 par 9
def changeAColor1_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 1):
                res[i][j] = 9
    return res

#Change la valeur 2 par 0
def changeAColor2_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 0
    return res

#Change la valeur 2 par 1
def changeAColor2_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 1
    return res

#Change la valeur 2 par 3
def changeAColor2_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 3
    return res

#Change la valeur 2 par 4
def changeAColor2_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 4
    return res

#Change la valeur 2 par 5
def changeAColor2_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 5
    return res

#Change la valeur 2 par 6
def changeAColor2_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 6
    return res

#Change la valeur 2 par 7
def changeAColor2_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 7
    return res

#Change la valeur 2 par 8
def changeAColor2_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 8
    return res

#Change la valeur 2 par 9
def changeAColor2_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 2):
                res[i][j] = 9
    return res

#Change la valeur 3 par 0
def changeAColor3_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 0
    return res

#Change la valeur 3 par 1
def changeAColor3_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 1
    return res

#Change la valeur 3 par 2
def changeAColor3_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 2
    return res

#Change la valeur 3 par 4
def changeAColor3_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 4
    return res

#Change la valeur 3 par 5
def changeAColor3_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 5
    return res

#Change la valeur 3 par 6
def changeAColor3_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 6
    return res

#Change la valeur 3 par 7
def changeAColor3_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 7
    return res

#Change la valeur 3 par 8
def changeAColor3_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 8
    return res

#Change la valeur 3 par 9
def changeAColor3_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 3):
                res[i][j] = 9
    return res

#Change la valeur 4 par 0
def changeAColor4_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 0
    return res

#Change la valeur 4 par 1
def changeAColor4_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 1
    return res

#Change la valeur 4 par 2
def changeAColor4_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 2
    return res

#Change la valeur 4 par 3
def changeAColor4_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 3
    return res

#Change la valeur 4 par 5
def changeAColor4_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 5
    return res

#Change la valeur 4 par 6
def changeAColor4_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 6
    return res

#Change la valeur 4 par 7
def changeAColor4_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 7
    return res

#Change la valeur 4 par 8
def changeAColor4_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 8
    return res

#Change la valeur 4 par 9
def changeAColor4_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 4):
                res[i][j] = 9
    return res

#Change la valeur 5 par 0
def changeAColor5_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 0
    return res

#Change la valeur 5 par 1
def changeAColor5_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 1
    return res

#Change la valeur 5 par 2
def changeAColor5_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 2
    return res

#Change la valeur 5 par 3
def changeAColor5_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 3
    return res

#Change la valeur 5 par 4
def changeAColor5_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 4
    return res

#Change la valeur 5 par 6
def changeAColor5_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 6
    return res

#Change la valeur 5 par 7
def changeAColor5_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 7
    return res

#Change la valeur 5 par 8
def changeAColor5_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 8
    return res

#Change la valeur 5 par 9
def changeAColor5_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 5):
                res[i][j] = 9
    return res

#Change la valeur 6 par 0
def changeAColor6_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 0
    return res

#Change la valeur 6 par 1
def changeAColor6_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 1
    return res

#Change la valeur 6 par 2
def changeAColor6_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 2
    return res

#Change la valeur 6 par 3
def changeAColor6_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 3
    return res

#Change la valeur 6 par 4
def changeAColor6_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 4
    return res

#Change la valeur 6 par 5
def changeAColor6_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 5
    return res

#Change la valeur 6 par 7
def changeAColor6_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 7
    return res

#Change la valeur 6 par 8
def changeAColor6_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 8
    return res

#Change la valeur 6 par 9
def changeAColor6_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 6):
                res[i][j] = 9
    return res

#Change la valeur 7 par 0
def changeAColor7_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 0
    return res

#Change la valeur 7 par 1
def changeAColor7_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 1
    return res

#Change la valeur 7 par 2
def changeAColor7_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 2
    return res

#Change la valeur 7 par 3
def changeAColor7_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 3
    return res

#Change la valeur 7 par 4
def changeAColor7_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 4
    return res

#Change la valeur 7 par 5
def changeAColor7_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 5
    return res

#Change la valeur 7 par 6
def changeAColor7_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 6
    return res

#Change la valeur 7 par 8
def changeAColor7_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 8
    return res

#Change la valeur 7 par 9
def changeAColor7_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 7):
                res[i][j] = 9
    return res

#Change la valeur 8 par 0
def changeAColor8_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 0
    return res

#Change la valeur 8 par 1
def changeAColor8_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 1
    return res

#Change la valeur 8 par 2
def changeAColor8_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 2
    return res

#Change la valeur 8 par 3
def changeAColor8_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 3
    return res

#Change la valeur 8 par 4
def changeAColor8_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 4
    return res

#Change la valeur 8 par 5
def changeAColor8_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 5
    return res

#Change la valeur 8 par 6
def changeAColor8_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 6
    return res

#Change la valeur 8 par 7
def changeAColor8_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 7
    return res

#Change la valeur 8 par 9
def changeAColor8_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 8):
                res[i][j] = 9
    return res

#Change la valeur 9 par 0
def changeAColor9_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 0
    return res

#Change la valeur 9 par 1
def changeAColor9_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 1
    return res

#Change la valeur 9 par 2
def changeAColor9_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 2
    return res

#Change la valeur 9 par 3
def changeAColor9_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 3
    return res

#Change la valeur 9 par 4
def changeAColor9_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 4
    return res

#Change la valeur 9 par 5
def changeAColor9_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 5
    return res

#Change la valeur 9 par 6
def changeAColor9_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 6
    return res

#Change la valeur 9 par 7
def changeAColor9_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 7
    return res

#Change la valeur 9 par 8
def changeAColor9_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if(res[i][j] == 9):
                res[i][j] = 8
    return res


#=================================================== FONCTIONNELLE ====================================================#
#================================================== MAIS MIS DE COTE ==================================================#

# #Complete entièrement une grille avec une couleur (VRAIMENT UTILE ?)
# def completed(grid):
#     res = gridCopy(grid)
#     c = randint(0, 9)
#     for i in range(len(res)):
#         for j in range(len(res[i])):
#             res[i][j] = c
#     return res

# #Effectue une inversion des couleurs (VRAIMENT UTILE ?)
# def inversion(grid):
#     inverted_grid = [[9 - grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
#     return inverted_grid

# #Triple la grille sur la hauteur (VRAIMENT UTILE ?)
# def tripleRow(grid):
#     res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid))*3)]
#     for i in range(0, len(grid)):
#         for j in range(0, len(grid[i])):
#             res[i][j] = grid[i][j]
#             res[len(grid)+i][j] = grid[i][j]
#             res[(len(grid)*2)+i][j] = grid[i][j]
#     return res
#
# #Triple la grille sur la largeur (VRAIMENT UTILE ?)
# def tripleColumn(grid):
#     res = [[0 for _ in range((len(grid[0]))*3)] for _ in range(len(grid))]
#     for i in range(0, len(grid)):
#         for j in range(0, len(grid[i])):
#             res[i][j] = grid[i][j]
#             res[i][len(grid[0])+j] = grid[i][j]
#             res[i][(len(grid[0])*2)+j] = grid[i][j]
#     return res

# #Dessine une ligne avec une couleur déjà présente sur la grille
# def extendLine(grid):
#     res = gridCopy(grid)
#     line = randint(0,len(grid)-1)                                             <-----
#     c = res[line][randint(0,len(res[0])-1)]
#     for i in range(len(res)):
#         for j in range(len(res[0])):
#             if(i == line):
#                 res[i][j] = c
#     return res
#
# #Dessine une colonne avec une couleur déjà présente sur la grille
# def extendColumn(grid):
#     res = gridCopy(grid)
#     column = randint(0,len(grid[0])-1)                                        <-----
#     c = res[randint(0, len(res) - 1)][column]
#     for i in range(len(res)):
#         for j in range(len(res[0])):
#             if(j == column):
#                 res[i][j] = c
#     return res

# #Reduit la hauteur de la grille de façon aléatoire
# def lenghtReduction(grid):
#     t = randint(1,len(grid))                                                  <-----
#     res = [[0 for _ in range(len(grid[0]))] for _ in range(t)]
#     for i in range(0, t):
#         for j in range(0, len(grid[i])):
#             res[i][j] = grid[i][j]
#     return res
#
# #Reduit la largeur de la grille de façon aléatoire
# def widthReduction(grid):
#     t = randint(1,len(grid[0]))                                               <-----
#     res = [[0 for _ in range(t)] for _ in range(len(grid))]
#     for i in range(0, len(grid)):
#         for j in range(0, t):
#             res[i][j] = grid[i][j]
#     return res

#======================================================================================================================#
#===================================================== EN TRAVAUX =====================================================#

