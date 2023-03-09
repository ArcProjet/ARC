from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0,87))
    return tab

def generateFctTab(nb,stage):
    tab = []
    for _ in range(nb):
        tab.append(fctChoice(stage))
    return tab

#La fonction utilise des primitives précisé dans le tableau tabFunctions
def applyFunctions(tabFunctions,grid):
    for i in tabFunctions:
        match i:
            case 0:
                grid = gridCopy(grid)
            case 1:
                grid = axialSymmetryX(grid)
            case 2:
                grid = axialSymmetryY(grid)
            case 3:
                grid = centralSymetry(grid)
            case 4:
                grid = copyHalfX(grid)
            case 5:
                grid = copyHalfY(grid)
            case 6:
                grid = doubleSymetryRow(grid)
            case 7:
                grid = doubleSymetryColumn(grid)
            case 8:
                grid = xHalf(grid)
            case 9:
                grid = yHalf(grid)
            case 10:
                grid = doubleRow(grid)
            case 11:
                grid = doubleColumn(grid)
            case 12:
                grid = rotateLeft(grid)
            case 13:
                grid = rotateRight(grid)
            case 14:
                grid = translationEnHaut(grid)
            case 15:
                grid = translationADroite(grid)
            case 16:
                grid = translationEnBas(grid)
            case 17:
                grid = translationAGauche(grid)
            case 18:
                grid = extendColorUp0(grid)
            case 19:
                grid = extendColorUp1(grid)
            case 20:
                grid = extendColorUp2(grid)
            case 21:
                grid = extendColorUp3(grid)
            case 22:
                grid = extendColorUp4(grid)
            case 23:
                grid = extendColorUp5(grid)
            case 24:
                grid = extendColorUp6(grid)
            case 25:
                grid = extendColorUp7(grid)
            case 26:
                grid = extendColorUp8(grid)
            case 27:
                grid = extendColorUp9(grid)
            case 28:
                grid = extendColorDown0(grid)
            case 29:
                grid = extendColorDown1(grid)
            case 30:
                grid = extendColorDown2(grid)
            case 31:
                grid = extendColorDown3(grid)
            case 32:
                grid = extendColorDown4(grid)
            case 33:
                grid = extendColorDown5(grid)
            case 34:
                grid = extendColorDown6(grid)
            case 35:
                grid = extendColorDown7(grid)
            case 36:
                grid = extendColorDown8(grid)
            case 37:
                grid = extendColorDown9(grid)
            case 38:
                grid = extendColorLeft0(grid)
            case 39:
                grid = extendColorLeft1(grid)
            case 40:
                grid = extendColorLeft2(grid)
            case 41:
                grid = extendColorLeft3(grid)
            case 42:
                grid = extendColorLeft4(grid)
            case 43:
                grid = extendColorLeft5(grid)
            case 44:
                grid = extendColorLeft6(grid)
            case 45:
                grid = extendColorLeft7(grid)
            case 46:
                grid = extendColorLeft8(grid)
            case 47:
                grid = extendColorLeft9(grid)
            case 48:
                grid = extendColorRight0(grid)
            case 49:
                grid = extendColorRight1(grid)
            case 50:
                grid = extendColorRight2(grid)
            case 51:
                grid = extendColorRight3(grid)
            case 52:
                grid = extendColorRight4(grid)
            case 53:
                grid = extendColorRight5(grid)
            case 54:
                grid = extendColorRight6(grid)
            case 55:
                grid = extendColorRight7(grid)
            case 56:
                grid = extendColorRight8(grid)
            case 57:
                grid = extendColorRight9(grid)
            case 58:
                grid = growingColor0(grid)
            case 59:
                grid = growingColor1(grid)
            case 60:
                grid = growingColor2(grid)
            case 61:
                grid = growingColor3(grid)
            case 62:
                grid = growingColor4(grid)
            case 63:
                grid = growingColor5(grid)
            case 64:
                grid = growingColor6(grid)
            case 65:
                grid = growingColor7(grid)
            case 66:
                grid = growingColor8(grid)
            case 67:
                grid = growingColor9(grid)
            case 68:
                grid = completeColor0(grid)
            case 69:
                grid = completeColor1(grid)
            case 70:
                grid = completeColor2(grid)
            case 71:
                grid = completeColor3(grid)
            case 72:
                grid = completeColor4(grid)
            case 73:
                grid = completeColor5(grid)
            case 74:
                grid = completeColor6(grid)
            case 75:
                grid = completeColor7(grid)
            case 76:
                grid = completeColor8(grid)
            case 77:
                grid = completeColor9(grid)
            case 78:
                grid = removeNoise0(grid)
            case 79:
                grid = removeNoise1(grid)
            case 80:
                grid = removeNoise2(grid)
            case 81:
                grid = removeNoise3(grid)
            case 82:
                grid = removeNoise4(grid)
            case 83:
                grid = removeNoise5(grid)
            case 84:
                grid = removeNoise6(grid)
            case 85:
                grid = removeNoise7(grid)
            case 86:
                grid = removeNoise8(grid)
            case 87:
                grid = removeNoise9(grid)


    return grid