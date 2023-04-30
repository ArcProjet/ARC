# Copie proprement les grilles
def gridCopy(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res


#Complete entièrement la grille avec la valeur 0
def completed0(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 0
 return res


#Complete entièrement la grille avec la valeur 1
def completed1(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 1
 return res


#Complete entièrement la grille avec la valeur 2
def completed2(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 2
 return res


#Complete entièrement la grille avec la valeur 3
def completed3(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 3
 return res


#Complete entièrement la grille avec la valeur 4
def completed4(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 4
 return res


#Complete entièrement la grille avec la valeur 5
def completed5(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 5
 return res


#Complete entièrement la grille avec la valeur 6
def completed6(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 6
 return res


#Complete entièrement la grille avec la valeur 7
def completed7(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 7
 return res


#Complete entièrement la grille avec la valeur 8
def completed8(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 8
 return res


#Complete entièrement la grille avec la valeur 9
def completed9(grid):
 res = gridCopy(grid)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
     res[i][j] = 9
 return res


# Effectue une symetrie sur l'axe des X
def axialSymmetryX(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[len(grid) - i - 1][j]
    return res


# Effectue une symetrie sur l'axe des Y
def axialSymmetryY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][len(grid[0]) - j - 1]
    return res


# Effectue une symetrie en diagonal si possible sinon gridCopy
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


# Effectue une symetrie sur l'axe des X de le moitié de la grille et la copie dans l'autre moitié de la grille
def copyHalfX(grid):
    res = gridCopy(grid)
    for i in range(0, int(len(grid) / 2)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[len(grid) - i - 1][j]
    return res


# Effectue une symetrie sur l'axe des Y de le moitié de la grille et la copie dans l'autre moitié de la grille
def copyHalfY(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i]) / 2)):
            res[i][j] = grid[i][len(grid[0]) - j - 1]
    return res


# Effectue une symetrie sur l'axe des X de la grille et la copie au dessus
def doubleSymetryRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid)) * 2)]
    sym = axialSymmetryX(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid) + i][j] = sym[i][j]
    return res


# Effectue une symetrie sur l'axe des Y de la grille et la copie sur le coté
def doubleSymetryColumn(grid):
    res = [[0 for _ in range((len(grid[0])) * 2)] for _ in range(len(grid))]
    sym = axialSymmetryY(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0]) + j] = sym[i][j]
    return res


# Coupe la grille en 2 sur l'axe des X
def xHalf(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(int(len(grid) / 2))]
    for i in range(0, int(len(grid) / 2)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res


# Coupe la grille en 2 sur l'axe des Y
def yHalf(grid):
    res = [[0 for _ in range(int(len(grid[0]) / 2))] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, int(len(grid[i]) / 2)):
            res[i][j] = grid[i][j]
    return res


# Enlève la dernière ligne de la grille
def lenghtReduction(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)-1)]
    for i in range(0, len(grid)-1):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
    return res


#Enlève la dernière colonne de la grille
def widthReduction(grid):
    res = [[0 for _ in range(len(grid[0])-1)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])-1):
            res[i][j] = grid[i][j]
    return res


# Double la grille sur la hauteur
def doubleRow(grid):
    res = [[0 for _ in range(len(grid[0]))] for _ in range((len(grid)) * 2)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[len(grid) + i][j] = grid[i][j]
    return res


# Double la grille sur la largeur
def doubleColumn(grid):
    res = [[0 for _ in range((len(grid[0])) * 2)] for _ in range(len(grid))]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            res[i][j] = grid[i][j]
            res[i][len(grid[0]) + j] = grid[i][j]
    return res


# Effectue une rotation sur la gauche
def rotateLeft(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = 0
        for j in range(len(res[0])):
            res[i][j] = grid[cpt][len(grid[0]) - i - 1]
            cpt += 1
    return res


# Effectue une rotation sur la droite
def rotateRight(grid):
    res = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
    for i in range(len(res)):
        cpt = len(grid)
        for j in range(len(res[0])):
            cpt -= 1
            res[i][j] = grid[cpt][i]
    return res


# Effectue une tranlation de toute les couleurs vers le haut
def translationEnHaut(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid) - 1):
        for j in range(0, len(grid[0])):
            res[i][j] = grid[i + 1][j]
    for l in range(0, len(grid[0])):
        res[len(grid) - 1][l] = grid[0][l]
    return res


# Effectue une tranlation de toute les couleurs vers la droite
def translationADroite(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            res[i][j + 1] = grid[i][j]
        res[i][0] = grid[i][len(grid[0]) - 1]
    return res


# Effectue une tranlation de toute les couleurs vers le bas
def translationEnBas(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            res[i + 1][j] = grid[i][j]
    for l in range(0, len(grid[0])):
        res[0][l] = grid[len(grid) - 1][l]
    return res


# Effectue une tranlation de toute les couleurs vers la gauche
def translationAGauche(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            res[i][j - 1] = grid[i][j]
        res[i][len(grid[0]) - 1] = grid[i][0]
    return res


# Etend la valeur 0 vers le haut
def extendColorUp0(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 0):
                res[i - 1][j] = 0
    return res


# Etend la valeur 1 vers le haut
def extendColorUp1(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 1):
                res[i - 1][j] = 1
    return res


# Etend la valeur 2 vers le haut
def extendColorUp2(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 2):
                res[i - 1][j] = 2
    return res


# Etend la valeur 3 vers le haut
def extendColorUp3(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 3):
                res[i - 1][j] = 3
    return res


# Etend la valeur 4 vers le haut
def extendColorUp4(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 4):
                res[i - 1][j] = 4
    return res


# Etend la valeur 5 vers le haut
def extendColorUp5(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 5):
                res[i - 1][j] = 5
    return res


# Etend la valeur 6 vers le haut
def extendColorUp6(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 6):
                res[i - 1][j] = 6
    return res


# Etend la valeur 7 vers le haut
def extendColorUp7(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 7):
                res[i - 1][j] = 7
    return res


# Etend la valeur 8 vers le haut
def extendColorUp8(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 8):
                res[i - 1][j] = 8
    return res


# Etend la valeur 9 vers le haut
def extendColorUp9(grid):
    res = gridCopy(grid)
    for i in range(1, len(res)):
        for j in range(len(res[0])):
            if (res[i][j] == 9):
                res[i - 1][j] = 9
    return res


# Etend la valeur 0 vers le bas
def extendColorDown0(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 0):
                res[i + 1][j] = 0
    return res


# Etend la valeur 1 vers le bas
def extendColorDown1(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 1):
                res[i + 1][j] = 1
    return res


# Etend la valeur 2 vers le bas
def extendColorDown2(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 2):
                res[i + 1][j] = 2
    return res


# Etend la valeur 3 vers le bas
def extendColorDown3(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 3):
                res[i + 1][j] = 3
    return res


# Etend la valeur 4 vers le bas
def extendColorDown4(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 4):
                res[i + 1][j] = 4
    return res


# Etend la valeur 5 vers le bas
def extendColorDown5(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 5):
                res[i + 1][j] = 5
    return res


# Etend la valeur 6 vers le bas
def extendColorDown6(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 6):
                res[i + 1][j] = 6
    return res


# Etend la valeur 7 vers le bas
def extendColorDown7(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 7):
                res[i + 1][j] = 7
    return res


# Etend la valeur 8 vers le bas
def extendColorDown8(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 8):
                res[i + 1][j] = 8
    return res


# Etend la valeur 9 vers le bas
def extendColorDown9(grid):
    res = gridCopy(grid)
    for i in range(len(res) - 2, -1, -1):
        for j in range(len(res[0])):
            if (res[i][j] == 9):
                res[i + 1][j] = 9
    return res


# Etend la valeur 0 vers la gauche
def extendColorLeft0(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 0):
                res[i][j - 1] = 0
    return res


# Etend la valeur 1 vers la gauche
def extendColorLeft1(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 1):
                res[i][j - 1] = 1
    return res


# Etend la valeur 2 vers la gauche
def extendColorLeft2(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 2):
                res[i][j - 1] = 2
    return res


# Etend la valeur 3 vers la gauche
def extendColorLeft3(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 3):
                res[i][j - 1] = 3
    return res


# Etend la valeur 4 vers la gauche
def extendColorLeft4(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 4):
                res[i][j - 1] = 4
    return res


# Etend la valeur 5 vers la gauche
def extendColorLeft5(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 5):
                res[i][j - 1] = 5
    return res


# Etend la valeur 6 vers la gauche
def extendColorLeft6(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 6):
                res[i][j - 1] = 6
    return res


# Etend la valeur 7 vers la gauche
def extendColorLeft7(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 7):
                res[i][j - 1] = 7
    return res


# Etend la valeur 8 vers la gauche
def extendColorLeft8(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 8):
                res[i][j - 1] = 8
    return res


# Etend la valeur 9 vers la gauche
def extendColorLeft9(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(1, len(res[0])):
            if (res[i][j] == 9):
                res[i][j - 1] = 9
    return res


# Etend la valeur 0 vers la droite
def extendColorRight0(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 0):
                res[i][j + 1] = 0
    return res


# Etend la valeur 1 vers la droite
def extendColorRight1(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 1):
                res[i][j + 1] = 1
    return res


# Etend la valeur 2 vers la droite
def extendColorRight2(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 2):
                res[i][j + 1] = 2
    return res


# Etend la valeur 3 vers la droite
def extendColorRight3(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 3):
                res[i][j + 1] = 3
    return res


# Etend la valeur 4 vers la droite
def extendColorRight4(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 4):
                res[i][j + 1] = 4
    return res


# Etend la valeur 5 vers la droite
def extendColorRight5(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 5):
                res[i][j + 1] = 5
    return res


# Etend la valeur 6 vers la droite
def extendColorRight6(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 6):
                res[i][j + 1] = 6
    return res


# Etend la valeur 7 vers la droite
def extendColorRight7(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 7):
                res[i][j + 1] = 7
    return res


# Etend la valeur 8 vers la droite
def extendColorRight8(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 8):
                res[i][j + 1] = 8
    return res


# Etend la valeur 9 vers la droite
def extendColorRight9(grid):
    res = gridCopy(grid)
    for i in range(len(res)):
        for j in range(len(res[0]) - 2, -1, -1):
            if (res[i][j] == 9):
                res[i][j + 1] = 9
    return res


#Ajoute une colonne qui a comme valeur 0
def widthColorAugmentation_0(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =0
 return res


#Ajoute une colonne qui a comme valeur 1
def widthColorAugmentation_1(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =1
 return res


#Ajoute une colonne qui a comme valeur 2
def widthColorAugmentation_2(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =2
 return res


#Ajoute une colonne qui a comme valeur 3
def widthColorAugmentation_3(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =3
 return res


#Ajoute une colonne qui a comme valeur 4
def widthColorAugmentation_4(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =4
 return res


#Ajoute une colonne qui a comme valeur 5
def widthColorAugmentation_5(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =5
 return res


#Ajoute une colonne qui a comme valeur 6
def widthColorAugmentation_6(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =6
 return res


#Ajoute une colonne qui a comme valeur 7
def widthColorAugmentation_7(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =7
 return res


#Ajoute une colonne qui a comme valeur 8
def widthColorAugmentation_8(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =8
 return res


#Ajoute une colonne qui a comme valeur 9
def widthColorAugmentation_9(grid):
 res = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid))]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
   res[i][len(grid[i])] =9
 return res


#Ajoute une ligne qui a comme valeur 0
def lengthColorAugmentation_0(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 0
 return res


#Ajoute une ligne qui a comme valeur 1
def lengthColorAugmentation_1(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 1
 return res


#Ajoute une ligne qui a comme valeur 2
def lengthColorAugmentation_2(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 2
 return res


#Ajoute une ligne qui a comme valeur 3
def lengthColorAugmentation_3(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 3
 return res


#Ajoute une ligne qui a comme valeur 4
def lengthColorAugmentation_4(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 4
 return res


#Ajoute une ligne qui a comme valeur 5
def lengthColorAugmentation_5(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 5
 return res


#Ajoute une ligne qui a comme valeur 6
def lengthColorAugmentation_6(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 6
 return res


#Ajoute une ligne qui a comme valeur 7
def lengthColorAugmentation_7(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 7
 return res


#Ajoute une ligne qui a comme valeur 8
def lengthColorAugmentation_8(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 8
 return res


#Ajoute une ligne qui a comme valeur 9
def lengthColorAugmentation_9(grid):
 res = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid)+1)]
 for i in range(0, len(grid)):
   for j in range(0, len(grid[i])):
       res[i][j] = grid[i][j]
 for k in range(0, len(grid[0])):
   res[len(grid)][k] = 9
 return res


# Fait grossir de 1 la valeur 0 dans la grille
def growingColor0(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 0):
                res[i - 1][j] = 0
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 0):
                res[k][l + 1] = 0
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 0):
                res[m + 1][n] = 0
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 0):
                res[o][p - 1] = 0
    return res


# Fait grossir de 1 la valeur 1 dans la grille
def growingColor1(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 1):
                res[i - 1][j] = 1
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 1):
                res[k][l + 1] = 1
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 1):
                res[m + 1][n] = 1
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 1):
                res[o][p - 1] = 1
    return res


# Fait grossir de 1 la valeur 2 dans la grille
def growingColor2(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 2):
                res[i - 1][j] = 2
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 2):
                res[k][l + 1] = 2
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 2):
                res[m + 1][n] = 2
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 2):
                res[o][p - 1] = 2
    return res


# Fait grossir de 1 la valeur 3 dans la grille
def growingColor3(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 3):
                res[i - 1][j] = 3
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 3):
                res[k][l + 1] = 3
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 3):
                res[m + 1][n] = 3
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 3):
                res[o][p - 1] = 3
    return res


# Fait grossir de 1 la valeur 4 dans la grille
def growingColor4(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 4):
                res[i - 1][j] = 4
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 4):
                res[k][l + 1] = 4
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 4):
                res[m + 1][n] = 4
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 4):
                res[o][p - 1] = 4
    return res


# Fait grossir de 1 la valeur 5 dans la grille
def growingColor5(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 5):
                res[i - 1][j] = 5
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 5):
                res[k][l + 1] = 5
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 5):
                res[m + 1][n] = 5
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 5):
                res[o][p - 1] = 5
    return res


# Fait grossir de 1 la valeur 6 dans la grille
def growingColor6(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 6):
                res[i - 1][j] = 6
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 6):
                res[k][l + 1] = 6
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 6):
                res[m + 1][n] = 6
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 6):
                res[o][p - 1] = 6
    return res


# Fait grossir de 1 la valeur 7 dans la grille
def growingColor7(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 7):
                res[i - 1][j] = 7
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 7):
                res[k][l + 1] = 7
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 7):
                res[m + 1][n] = 7
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 7):
                res[o][p - 1] = 7
    return res


# Fait grossir de 1 la valeur 8 dans la grille
def growingColor8(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 8):
                res[i - 1][j] = 8
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 8):
                res[k][l + 1] = 8
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 8):
                res[m + 1][n] = 8
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 8):
                res[o][p - 1] = 8
    return res


# Fait grossir de 1 la valeur 9 dans la grille
def growingColor9(grid):
    res = gridCopy(grid)
    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] == 9):
                res[i - 1][j] = 9
    for k in range(0, len(grid)):
        for l in range(len(grid[0]) - 2, -1, -1):
            if (grid[k][l] == 9):
                res[k][l + 1] = 9
    for m in range(len(grid) - 2, -1, -1):
        for n in range(len(grid[0])):
            if (grid[m][n] == 9):
                res[m + 1][n] = 9
    for o in range(len(grid)):
        for p in range(1, len(grid[0])):
            if (grid[o][p] == 9):
                res[o][p - 1] = 9
    return res


# Enlève le "bruit" déterminer par un seuil de 0
def removeNoise0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 0:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 1
def removeNoise1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 1:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 2
def removeNoise2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 2:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 3
def removeNoise3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 3:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 4
def removeNoise4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 4:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 5
def removeNoise5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 5:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 6
def removeNoise6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 6:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 7
def removeNoise7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 7:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 8
def removeNoise8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 8:
                res[i][j] = 0
    return res


# Enlève le "bruit" déterminer par un seuil de 9
def removeNoise9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if res[i][j] < 9:
                res[i][j] = 0
    return res


# Change la valeur 0 par 1
def changeAColor0_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 1
    return res


# Change la valeur 0 par 2
def changeAColor0_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 2
    return res


# Change la valeur 0 par 3
def changeAColor0_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 3
    return res


# Change la valeur 0 par 4
def changeAColor0_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 4
    return res


# Change la valeur 0 par 5
def changeAColor0_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 5
    return res


# Change la valeur 0 par 6
def changeAColor0_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 6
    return res


# Change la valeur 0 par 7
def changeAColor0_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 7
    return res


# Change la valeur 0 par 8
def changeAColor0_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 8
    return res


# Change la valeur 0 par 9
def changeAColor0_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 0):
                res[i][j] = 9
    return res


# Change la valeur 1 par 0
def changeAColor1_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 0
    return res


# Change la valeur 1 par 2
def changeAColor1_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 2
    return res


# Change la valeur 1 par 3
def changeAColor1_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 3
    return res


# Change la valeur 1 par 4
def changeAColor1_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 4
    return res


# Change la valeur 1 par 5
def changeAColor1_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 5
    return res


# Change la valeur 1 par 6
def changeAColor1_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 6
    return res


# Change la valeur 1 par 7
def changeAColor1_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 7
    return res


# Change la valeur 1 par 8
def changeAColor1_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 8
    return res


# Change la valeur 1 par 9
def changeAColor1_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 1):
                res[i][j] = 9
    return res


# Change la valeur 2 par 0
def changeAColor2_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 0
    return res


# Change la valeur 2 par 1
def changeAColor2_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 1
    return res


# Change la valeur 2 par 3
def changeAColor2_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 3
    return res


# Change la valeur 2 par 4
def changeAColor2_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 4
    return res


# Change la valeur 2 par 5
def changeAColor2_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 5
    return res


# Change la valeur 2 par 6
def changeAColor2_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 6
    return res


# Change la valeur 2 par 7
def changeAColor2_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 7
    return res


# Change la valeur 2 par 8
def changeAColor2_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 8
    return res


# Change la valeur 2 par 9
def changeAColor2_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 2):
                res[i][j] = 9
    return res


# Change la valeur 3 par 0
def changeAColor3_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 0
    return res


# Change la valeur 3 par 1
def changeAColor3_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 1
    return res


# Change la valeur 3 par 2
def changeAColor3_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 2
    return res


# Change la valeur 3 par 4
def changeAColor3_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 4
    return res


# Change la valeur 3 par 5
def changeAColor3_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 5
    return res


# Change la valeur 3 par 6
def changeAColor3_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 6
    return res


# Change la valeur 3 par 7
def changeAColor3_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 7
    return res


# Change la valeur 3 par 8
def changeAColor3_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 8
    return res


# Change la valeur 3 par 9
def changeAColor3_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 3):
                res[i][j] = 9
    return res


# Change la valeur 4 par 0
def changeAColor4_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 0
    return res


# Change la valeur 4 par 1
def changeAColor4_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 1
    return res


# Change la valeur 4 par 2
def changeAColor4_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 2
    return res


# Change la valeur 4 par 3
def changeAColor4_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 3
    return res


# Change la valeur 4 par 5
def changeAColor4_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 5
    return res


# Change la valeur 4 par 6
def changeAColor4_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 6
    return res


# Change la valeur 4 par 7
def changeAColor4_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 7
    return res


# Change la valeur 4 par 8
def changeAColor4_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 8
    return res


# Change la valeur 4 par 9
def changeAColor4_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 4):
                res[i][j] = 9
    return res


# Change la valeur 5 par 0
def changeAColor5_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 0
    return res


# Change la valeur 5 par 1
def changeAColor5_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 1
    return res


# Change la valeur 5 par 2
def changeAColor5_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 2
    return res


# Change la valeur 5 par 3
def changeAColor5_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 3
    return res


# Change la valeur 5 par 4
def changeAColor5_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 4
    return res


# Change la valeur 5 par 6
def changeAColor5_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 6
    return res


# Change la valeur 5 par 7
def changeAColor5_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 7
    return res


# Change la valeur 5 par 8
def changeAColor5_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 8
    return res


# Change la valeur 5 par 9
def changeAColor5_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 5):
                res[i][j] = 9
    return res


# Change la valeur 6 par 0
def changeAColor6_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 0
    return res


# Change la valeur 6 par 1
def changeAColor6_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 1
    return res


# Change la valeur 6 par 2
def changeAColor6_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 2
    return res


# Change la valeur 6 par 3
def changeAColor6_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 3
    return res


# Change la valeur 6 par 4
def changeAColor6_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 4
    return res


# Change la valeur 6 par 5
def changeAColor6_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 5
    return res


# Change la valeur 6 par 7
def changeAColor6_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 7
    return res


# Change la valeur 6 par 8
def changeAColor6_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 8
    return res


# Change la valeur 6 par 9
def changeAColor6_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 6):
                res[i][j] = 9
    return res


# Change la valeur 7 par 0
def changeAColor7_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 0
    return res


# Change la valeur 7 par 1
def changeAColor7_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 1
    return res


# Change la valeur 7 par 2
def changeAColor7_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 2
    return res


# Change la valeur 7 par 3
def changeAColor7_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 3
    return res


# Change la valeur 7 par 4
def changeAColor7_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 4
    return res


# Change la valeur 7 par 5
def changeAColor7_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 5
    return res


# Change la valeur 7 par 6
def changeAColor7_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 6
    return res


# Change la valeur 7 par 8
def changeAColor7_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 8
    return res


# Change la valeur 7 par 9
def changeAColor7_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 7):
                res[i][j] = 9
    return res


# Change la valeur 8 par 0
def changeAColor8_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 0
    return res


# Change la valeur 8 par 1
def changeAColor8_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 1
    return res


# Change la valeur 8 par 2
def changeAColor8_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 2
    return res


# Change la valeur 8 par 3
def changeAColor8_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 3
    return res


# Change la valeur 8 par 4
def changeAColor8_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 4
    return res


# Change la valeur 8 par 5
def changeAColor8_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 5
    return res


# Change la valeur 8 par 6
def changeAColor8_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 6
    return res


# Change la valeur 8 par 7
def changeAColor8_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 7
    return res


# Change la valeur 8 par 9
def changeAColor8_9(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 8):
                res[i][j] = 9
    return res


# Change la valeur 9 par 0
def changeAColor9_0(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 0
    return res


# Change la valeur 9 par 1
def changeAColor9_1(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 1
    return res


# Change la valeur 9 par 2
def changeAColor9_2(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 2
    return res


# Change la valeur 9 par 3
def changeAColor9_3(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 3
    return res


# Change la valeur 9 par 4
def changeAColor9_4(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 4
    return res


# Change la valeur 9 par 5
def changeAColor9_5(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 5
    return res


# Change la valeur 9 par 6
def changeAColor9_6(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 6
    return res


# Change la valeur 9 par 7
def changeAColor9_7(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 7
    return res


# Change la valeur 9 par 8
def changeAColor9_8(grid):
    res = gridCopy(grid)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if (res[i][j] == 9):
                res[i][j] = 8
    return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 0
def extendLine5_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 1
def extendLine5_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 2
def extendLine5_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 3
def extendLine5_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 4
def extendLine5_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 5
def extendLine5_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 6
def extendLine5_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 7
def extendLine5_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 8
def extendLine5_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 5% de la largeur de la grille avec une valeur de 9
def extendLine5_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 0
def extendLine10_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 1
def extendLine10_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 2
def extendLine10_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 3
def extendLine10_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 4
def extendLine10_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 5
def extendLine10_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 6
def extendLine10_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 7
def extendLine10_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 8
def extendLine10_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 10% de la largeur de la grille avec une valeur de 9
def extendLine10_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 0
def extendLine15_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 1
def extendLine15_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 2
def extendLine15_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 3
def extendLine15_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 4
def extendLine15_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 5
def extendLine15_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 6
def extendLine15_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 7
def extendLine15_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 8
def extendLine15_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 15% de la largeur de la grille avec une valeur de 9
def extendLine15_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 0
def extendLine20_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 1
def extendLine20_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 2
def extendLine20_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 3
def extendLine20_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 4
def extendLine20_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 5
def extendLine20_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 6
def extendLine20_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 7
def extendLine20_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 8
def extendLine20_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 20% de la largeur de la grille avec une valeur de 9
def extendLine20_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 0
def extendLine25_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 1
def extendLine25_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 2
def extendLine25_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 3
def extendLine25_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 4
def extendLine25_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 5
def extendLine25_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 6
def extendLine25_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 7
def extendLine25_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 8
def extendLine25_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 25% de la largeur de la grille avec une valeur de 9
def extendLine25_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 0
def extendLine30_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 1
def extendLine30_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 2
def extendLine30_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 3
def extendLine30_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 4
def extendLine30_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 5
def extendLine30_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 6
def extendLine30_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 7
def extendLine30_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 8
def extendLine30_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 30% de la largeur de la grille avec une valeur de 9
def extendLine30_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 0
def extendLine35_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 1
def extendLine35_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 2
def extendLine35_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 3
def extendLine35_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 4
def extendLine35_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 5
def extendLine35_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 6
def extendLine35_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 7
def extendLine35_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 8
def extendLine35_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 35% de la largeur de la grille avec une valeur de 9
def extendLine35_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 0
def extendLine40_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 1
def extendLine40_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 2
def extendLine40_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 3
def extendLine40_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 4
def extendLine40_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 5
def extendLine40_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 6
def extendLine40_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 7
def extendLine40_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 8
def extendLine40_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 40% de la largeur de la grille avec une valeur de 9
def extendLine40_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 0
def extendLine45_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 1
def extendLine45_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 2
def extendLine45_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 3
def extendLine45_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 4
def extendLine45_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 5
def extendLine45_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 6
def extendLine45_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 7
def extendLine45_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 8
def extendLine45_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 45% de la largeur de la grille avec une valeur de 9
def extendLine45_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 0
def extendLine50_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 1
def extendLine50_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 2
def extendLine50_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 3
def extendLine50_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 4
def extendLine50_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 5
def extendLine50_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 6
def extendLine50_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 7
def extendLine50_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 8
def extendLine50_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 50% de la largeur de la grille avec une valeur de 9
def extendLine50_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 0
def extendLine55_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 1
def extendLine55_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 2
def extendLine55_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 3
def extendLine55_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 4
def extendLine55_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 5
def extendLine55_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 6
def extendLine55_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 7
def extendLine55_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 8
def extendLine55_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 55% de la largeur de la grille avec une valeur de 9
def extendLine55_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 0
def extendLine60_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 1
def extendLine60_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 2
def extendLine60_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 3
def extendLine60_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 4
def extendLine60_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 5
def extendLine60_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 6
def extendLine60_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 7
def extendLine60_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 8
def extendLine60_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 60% de la largeur de la grille avec une valeur de 9
def extendLine60_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 0
def extendLine65_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 1
def extendLine65_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 2
def extendLine65_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 3
def extendLine65_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 4
def extendLine65_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 5
def extendLine65_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 6
def extendLine65_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 7
def extendLine65_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 8
def extendLine65_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 65% de la largeur de la grille avec une valeur de 9
def extendLine65_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 0
def extendLine70_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 1
def extendLine70_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 2
def extendLine70_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 3
def extendLine70_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 4
def extendLine70_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 5
def extendLine70_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 6
def extendLine70_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 7
def extendLine70_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 8
def extendLine70_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 70% de la largeur de la grille avec une valeur de 9
def extendLine70_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 0
def extendLine75_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 1
def extendLine75_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 2
def extendLine75_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 3
def extendLine75_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 4
def extendLine75_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 5
def extendLine75_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 6
def extendLine75_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 7
def extendLine75_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 8
def extendLine75_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 75% de la largeur de la grille avec une valeur de 9
def extendLine75_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 0
def extendLine80_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 1
def extendLine80_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 2
def extendLine80_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 3
def extendLine80_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 4
def extendLine80_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 5
def extendLine80_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 6
def extendLine80_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 7
def extendLine80_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 8
def extendLine80_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 80% de la largeur de la grille avec une valeur de 9
def extendLine80_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 0
def extendLine85_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 1
def extendLine85_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 2
def extendLine85_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 3
def extendLine85_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 4
def extendLine85_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 5
def extendLine85_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 6
def extendLine85_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 7
def extendLine85_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 8
def extendLine85_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 85% de la largeur de la grille avec une valeur de 9
def extendLine85_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 0
def extendLine90_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 1
def extendLine90_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 2
def extendLine90_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 3
def extendLine90_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 4
def extendLine90_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 5
def extendLine90_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 6
def extendLine90_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 7
def extendLine90_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 8
def extendLine90_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 90% de la largeur de la grille avec une valeur de 9
def extendLine90_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 0
def extendLine95_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 1
def extendLine95_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 2
def extendLine95_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 3
def extendLine95_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 4
def extendLine95_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 5
def extendLine95_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 6
def extendLine95_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 7
def extendLine95_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 8
def extendLine95_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 95% de la largeur de la grille avec une valeur de 9
def extendLine95_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 0
def extendLine100_0(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 0
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 1
def extendLine100_1(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 1
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 2
def extendLine100_2(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 2
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 3
def extendLine100_3(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 3
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 4
def extendLine100_4(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 4
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 5
def extendLine100_5(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 5
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 6
def extendLine100_6(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 6
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 7
def extendLine100_7(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 7
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 8
def extendLine100_8(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 8
 return res


#Dessine une ligne a 100% de la largeur de la grille avec une valeur de 9
def extendLine100_9(grid):
 res = gridCopy(grid)
 line = int((len(res)-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(i == line):
         res[i][j] = 9
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 0
def extendColumn5_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 1
def extendColumn5_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 2
def extendColumn5_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 3
def extendColumn5_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 4
def extendColumn5_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 5
def extendColumn5_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 6
def extendColumn5_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 7
def extendColumn5_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 8
def extendColumn5_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 5% de la largeur de la grille avec une valeur de 9
def extendColumn5_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.05)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 0
def extendColumn10_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 1
def extendColumn10_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 2
def extendColumn10_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 3
def extendColumn10_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 4
def extendColumn10_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 5
def extendColumn10_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 6
def extendColumn10_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 7
def extendColumn10_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 8
def extendColumn10_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 10% de la largeur de la grille avec une valeur de 9
def extendColumn10_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 0
def extendColumn15_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 1
def extendColumn15_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 2
def extendColumn15_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 3
def extendColumn15_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 4
def extendColumn15_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 5
def extendColumn15_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 6
def extendColumn15_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 7
def extendColumn15_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 8
def extendColumn15_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 15% de la largeur de la grille avec une valeur de 9
def extendColumn15_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.15)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 0
def extendColumn20_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 1
def extendColumn20_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 2
def extendColumn20_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 3
def extendColumn20_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 4
def extendColumn20_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 5
def extendColumn20_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 6
def extendColumn20_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 7
def extendColumn20_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 8
def extendColumn20_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 20% de la largeur de la grille avec une valeur de 9
def extendColumn20_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.2)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 0
def extendColumn25_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 1
def extendColumn25_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 2
def extendColumn25_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 3
def extendColumn25_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 4
def extendColumn25_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 5
def extendColumn25_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 6
def extendColumn25_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 7
def extendColumn25_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 8
def extendColumn25_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 25% de la largeur de la grille avec une valeur de 9
def extendColumn25_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.25)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 0
def extendColumn30_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 1
def extendColumn30_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 2
def extendColumn30_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 3
def extendColumn30_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 4
def extendColumn30_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 5
def extendColumn30_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 6
def extendColumn30_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 7
def extendColumn30_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 8
def extendColumn30_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 30% de la largeur de la grille avec une valeur de 9
def extendColumn30_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.3)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 0
def extendColumn35_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 1
def extendColumn35_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 2
def extendColumn35_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 3
def extendColumn35_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 4
def extendColumn35_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 5
def extendColumn35_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 6
def extendColumn35_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 7
def extendColumn35_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 8
def extendColumn35_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 35% de la largeur de la grille avec une valeur de 9
def extendColumn35_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.35)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 0
def extendColumn40_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 1
def extendColumn40_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 2
def extendColumn40_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 3
def extendColumn40_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 4
def extendColumn40_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 5
def extendColumn40_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 6
def extendColumn40_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 7
def extendColumn40_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 8
def extendColumn40_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 40% de la largeur de la grille avec une valeur de 9
def extendColumn40_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.4)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 0
def extendColumn45_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 1
def extendColumn45_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 2
def extendColumn45_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 3
def extendColumn45_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 4
def extendColumn45_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 5
def extendColumn45_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 6
def extendColumn45_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 7
def extendColumn45_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 8
def extendColumn45_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 45% de la largeur de la grille avec une valeur de 9
def extendColumn45_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.45)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 0
def extendColumn50_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 1
def extendColumn50_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 2
def extendColumn50_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 3
def extendColumn50_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 4
def extendColumn50_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 5
def extendColumn50_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 6
def extendColumn50_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 7
def extendColumn50_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 8
def extendColumn50_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 50% de la largeur de la grille avec une valeur de 9
def extendColumn50_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.5)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 0
def extendColumn55_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 1
def extendColumn55_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 2
def extendColumn55_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 3
def extendColumn55_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 4
def extendColumn55_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 5
def extendColumn55_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 6
def extendColumn55_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 7
def extendColumn55_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 8
def extendColumn55_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 55% de la largeur de la grille avec une valeur de 9
def extendColumn55_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.55)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 0
def extendColumn60_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 1
def extendColumn60_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 2
def extendColumn60_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 3
def extendColumn60_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 4
def extendColumn60_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 5
def extendColumn60_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 6
def extendColumn60_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 7
def extendColumn60_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 8
def extendColumn60_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 60% de la largeur de la grille avec une valeur de 9
def extendColumn60_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.6)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 0
def extendColumn65_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 1
def extendColumn65_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 2
def extendColumn65_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 3
def extendColumn65_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 4
def extendColumn65_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 5
def extendColumn65_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 6
def extendColumn65_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 7
def extendColumn65_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 8
def extendColumn65_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 65% de la largeur de la grille avec une valeur de 9
def extendColumn65_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.65)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 0
def extendColumn70_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 1
def extendColumn70_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 2
def extendColumn70_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 3
def extendColumn70_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 4
def extendColumn70_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 5
def extendColumn70_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 6
def extendColumn70_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 7
def extendColumn70_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 8
def extendColumn70_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 70% de la largeur de la grille avec une valeur de 9
def extendColumn70_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.7)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 0
def extendColumn75_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 1
def extendColumn75_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 2
def extendColumn75_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 3
def extendColumn75_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 4
def extendColumn75_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 5
def extendColumn75_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 6
def extendColumn75_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 7
def extendColumn75_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 8
def extendColumn75_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 75% de la largeur de la grille avec une valeur de 9
def extendColumn75_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.75)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 0
def extendColumn80_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 1
def extendColumn80_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 2
def extendColumn80_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 3
def extendColumn80_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 4
def extendColumn80_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 5
def extendColumn80_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 6
def extendColumn80_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 7
def extendColumn80_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 8
def extendColumn80_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 80% de la largeur de la grille avec une valeur de 9
def extendColumn80_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.8)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 0
def extendColumn85_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 1
def extendColumn85_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 2
def extendColumn85_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 3
def extendColumn85_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 4
def extendColumn85_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 5
def extendColumn85_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 6
def extendColumn85_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 7
def extendColumn85_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 8
def extendColumn85_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 85% de la largeur de la grille avec une valeur de 9
def extendColumn85_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.85)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 0
def extendColumn90_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 1
def extendColumn90_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 2
def extendColumn90_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 3
def extendColumn90_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 4
def extendColumn90_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 5
def extendColumn90_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 6
def extendColumn90_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 7
def extendColumn90_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 8
def extendColumn90_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 90% de la largeur de la grille avec une valeur de 9
def extendColumn90_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.9)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 0
def extendColumn95_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 1
def extendColumn95_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 2
def extendColumn95_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 3
def extendColumn95_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 4
def extendColumn95_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 5
def extendColumn95_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 6
def extendColumn95_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 7
def extendColumn95_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 8
def extendColumn95_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 95% de la largeur de la grille avec une valeur de 9
def extendColumn95_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*0.95)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 0
def extendColumn100_0(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 0
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 1
def extendColumn100_1(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 1
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 2
def extendColumn100_2(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 2
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 3
def extendColumn100_3(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 3
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 4
def extendColumn100_4(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 4
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 5
def extendColumn100_5(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 5
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 6
def extendColumn100_6(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 6
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 7
def extendColumn100_7(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 7
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 8
def extendColumn100_8(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 8
 return res


#Dessine une colonne a 100% de la largeur de la grille avec une valeur de 9
def extendColumn100_9(grid):
 res = gridCopy(grid)
 column = int((len(res[0])-1)*1)
 for i in range(0, len(res)):
   for j in range(0, len(res[0])):
       if(j == column):
         res[i][j] = 9
 return res
