from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0,167))
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
                grid = removeNoise0(grid)
            case 69:
                grid = removeNoise1(grid)
            case 70:
                grid = removeNoise2(grid)
            case 71:
                grid = removeNoise3(grid)
            case 72:
                grid = removeNoise4(grid)
            case 73:
                grid = removeNoise5(grid)
            case 74:
                grid = removeNoise6(grid)
            case 75:
                grid = removeNoise7(grid)
            case 76:
                grid = removeNoise8(grid)
            case 77:
                grid = removeNoise9(grid)
            case 78:
                grid = changeAColor0_1(grid)
            case 79:
                grid = changeAColor0_2(grid)
            case 80:
                grid = changeAColor0_3(grid)
            case 81:
                grid = changeAColor0_4(grid)
            case 82:
                grid = changeAColor0_5(grid)
            case 83:
                grid = changeAColor0_6(grid)
            case 84:
                grid = changeAColor0_7(grid)
            case 85:
                grid = changeAColor0_8(grid)
            case 86:
                grid = changeAColor0_9(grid)
            case 87:
                grid = changeAColor1_0(grid)
            case 88:
                grid = changeAColor1_2(grid)
            case 89:
                grid = changeAColor1_3(grid)
            case 90:
                grid = changeAColor1_4(grid)
            case 91:
                grid = changeAColor1_5(grid)
            case 92:
                grid = changeAColor1_6(grid)
            case 93:
                grid = changeAColor1_7(grid)
            case 94:
                grid = changeAColor1_8(grid)
            case 95:
                grid = changeAColor1_9(grid)
            case 96:
                grid = changeAColor2_0(grid)
            case 97:
                grid = changeAColor2_1(grid)
            case 98:
                grid = changeAColor2_3(grid)
            case 99:
                grid = changeAColor2_4(grid)
            case 100:
                grid = changeAColor2_5(grid)
            case 101:
                grid = changeAColor2_6(grid)
            case 102:
                grid = changeAColor2_7(grid)
            case 103:
                grid = changeAColor2_8(grid)
            case 104:
                grid = changeAColor2_9(grid)
            case 105:
                grid = changeAColor3_0(grid)
            case 106:
                grid = changeAColor3_1(grid)
            case 107:
                grid = changeAColor3_2(grid)
            case 108:
                grid = changeAColor3_4(grid)
            case 109:
                grid = changeAColor3_5(grid)
            case 110:
                grid = changeAColor3_6(grid)
            case 111:
                grid = changeAColor3_7(grid)
            case 112:
                grid = changeAColor3_8(grid)
            case 113:
                grid = changeAColor3_9(grid)
            case 114:
                grid = changeAColor4_0(grid)
            case 115:
                grid = changeAColor4_1(grid)
            case 116:
                grid = changeAColor4_2(grid)
            case 117:
                grid = changeAColor4_3(grid)
            case 118:
                grid = changeAColor4_5(grid)
            case 119:
                grid = changeAColor4_6(grid)
            case 120:
                grid = changeAColor4_7(grid)
            case 121:
                grid = changeAColor4_8(grid)
            case 122:
                grid = changeAColor4_9(grid)
            case 123:
                grid = changeAColor5_0(grid)
            case 124:
                grid = changeAColor5_1(grid)
            case 125:
                grid = changeAColor5_2(grid)
            case 126:
                grid = changeAColor5_3(grid)
            case 127:
                grid = changeAColor5_4(grid)
            case 128:
                grid = changeAColor5_6(grid)
            case 129:
                grid = changeAColor5_7(grid)
            case 130:
                grid = changeAColor5_8(grid)
            case 131:
                grid = changeAColor5_9(grid)
            case 132:
                grid = changeAColor6_0(grid)
            case 133:
                grid = changeAColor6_1(grid)
            case 134:
                grid = changeAColor6_2(grid)
            case 135:
                grid = changeAColor6_3(grid)
            case 136:
                grid = changeAColor6_4(grid)
            case 137:
                grid = changeAColor6_5(grid)
            case 138:
                grid = changeAColor6_7(grid)
            case 139:
                grid = changeAColor6_8(grid)
            case 140:
                grid = changeAColor6_9(grid)
            case 141:
                grid = changeAColor7_0(grid)
            case 142:
                grid = changeAColor7_1(grid)
            case 143:
                grid = changeAColor7_2(grid)
            case 144:
                grid = changeAColor7_3(grid)
            case 145:
                grid = changeAColor7_4(grid)
            case 146:
                grid = changeAColor7_5(grid)
            case 147:
                grid = changeAColor7_6(grid)
            case 148:
                grid = changeAColor7_8(grid)
            case 149:
                grid = changeAColor7_9(grid)
            case 150:
                grid = changeAColor8_0(grid)
            case 151:
                grid = changeAColor8_1(grid)
            case 152:
                grid = changeAColor8_2(grid)
            case 153:
                grid = changeAColor8_3(grid)
            case 154:
                grid = changeAColor8_4(grid)
            case 155:
                grid = changeAColor8_5(grid)
            case 156:
                grid = changeAColor8_6(grid)
            case 157:
                grid = changeAColor8_7(grid)
            case 158:
                grid = changeAColor8_9(grid)
            case 159:
                grid = changeAColor9_0(grid)
            case 160:
                grid = changeAColor9_1(grid)
            case 161:
                grid = changeAColor9_2(grid)
            case 162:
                grid = changeAColor9_3(grid)
            case 163:
                grid = changeAColor9_4(grid)
            case 164:
                grid = changeAColor9_5(grid)
            case 165:
                grid = changeAColor9_6(grid)
            case 166:
                grid = changeAColor9_7(grid)
            case 167:
                grid = changeAColor9_8(grid)

    return grid