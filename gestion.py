from primitive import *
from random import randint

def fctChoice(stage):
    tab = []
    for _ in range(stage):
        tab.append(randint(0, 599))
    return tab


def generateFctTab(nb, stage):
    tab = []
    for _ in range(nb):
        tab.append(fctChoice(stage))
    return tab


# La fonction utilise des primitives précisé dans le tableau tabFunctions
def applyFunctions(tabFunctions, grid):
    for i in tabFunctions:
        match i:
            case 0:
                grid = gridCopy(grid)
            case 1:
                grid = completed0(grid)
            case 2:
                grid = completed1(grid)
            case 3:
                grid = completed2(grid)
            case 4:
                grid = completed3(grid)
            case 5:
                grid = completed4(grid)
            case 6:
                grid = completed5(grid)
            case 7:
                grid = completed6(grid)
            case 8:
                grid = completed7(grid)
            case 9:
                grid = completed8(grid)
            case 10:
                grid = completed9(grid)
            case 11:
                grid = axialSymmetryX(grid)
            case 12:
                grid = axialSymmetryY(grid)
            case 13:
                grid = centralSymetry(grid)
            case 14:
                grid = copyHalfX(grid)
            case 15:
                grid = copyHalfY(grid)
            case 16:
                grid = doubleSymetryRow(grid)
            case 17:
                grid = doubleSymetryColumn(grid)
            case 18:
                grid = xHalf(grid)
            case 19:
                grid = yHalf(grid)
            case 20:
                grid = lenghtReduction(grid)
            case 21:
                grid = widthReduction(grid)
            case 22:
                grid = doubleRow(grid)
            case 23:
                grid = doubleColumn(grid)
            case 24:
                grid = rotateLeft(grid)
            case 25:
                grid = rotateRight(grid)
            case 26:
                grid = translationEnHaut(grid)
            case 27:
                grid = translationADroite(grid)
            case 28:
                grid = translationEnBas(grid)
            case 29:
                grid = translationAGauche(grid)
            case 30:
                grid = extendColorUp0(grid)
            case 31:
                grid = extendColorUp1(grid)
            case 32:
                grid = extendColorUp2(grid)
            case 33:
                grid = extendColorUp3(grid)
            case 34:
                grid = extendColorUp4(grid)
            case 35:
                grid = extendColorUp5(grid)
            case 36:
                grid = extendColorUp6(grid)
            case 37:
                grid = extendColorUp7(grid)
            case 38:
                grid = extendColorUp8(grid)
            case 39:
                grid = extendColorUp9(grid)
            case 40:
                grid = extendColorDown0(grid)
            case 41:
                grid = extendColorDown1(grid)
            case 42:
                grid = extendColorDown2(grid)
            case 43:
                grid = extendColorDown3(grid)
            case 44:
                grid = extendColorDown4(grid)
            case 45:
                grid = extendColorDown5(grid)
            case 46:
                grid = extendColorDown6(grid)
            case 47:
                grid = extendColorDown7(grid)
            case 48:
                grid = extendColorDown8(grid)
            case 49:
                grid = extendColorDown9(grid)
            case 50:
                grid = extendColorLeft0(grid)
            case 51:
                grid = extendColorLeft1(grid)
            case 52:
                grid = extendColorLeft2(grid)
            case 53:
                grid = extendColorLeft3(grid)
            case 54:
                grid = extendColorLeft4(grid)
            case 55:
                grid = extendColorLeft5(grid)
            case 56:
                grid = extendColorLeft6(grid)
            case 57:
                grid = extendColorLeft7(grid)
            case 58:
                grid = extendColorLeft8(grid)
            case 59:
                grid = extendColorLeft9(grid)
            case 60:
                grid = extendColorRight0(grid)
            case 61:
                grid = extendColorRight1(grid)
            case 62:
                grid = extendColorRight2(grid)
            case 63:
                grid = extendColorRight3(grid)
            case 64:
                grid = extendColorRight4(grid)
            case 65:
                grid = extendColorRight5(grid)
            case 66:
                grid = extendColorRight6(grid)
            case 67:
                grid = extendColorRight7(grid)
            case 68:
                grid = extendColorRight8(grid)
            case 69:
                grid = extendColorRight9(grid)
            case 70:
                grid = widthColorAugmentation0(grid)
            case 71:
                grid = widthColorAugmentation1(grid)
            case 72:
                grid = widthColorAugmentation2(grid)
            case 73:
                grid = widthColorAugmentation3(grid)
            case 74:
                grid = widthColorAugmentation4(grid)
            case 75:
                grid = widthColorAugmentation5(grid)
            case 76:
                grid = widthColorAugmentation6(grid)
            case 77:
                grid = widthColorAugmentation7(grid)
            case 78:
                grid = widthColorAugmentation8(grid)
            case 79:
                grid = widthColorAugmentation9(grid)
            case 80:
                grid = lengthColorAugmentation0(grid)
            case 81:
                grid = lengthColorAugmentation1(grid)
            case 82:
                grid = lengthColorAugmentation2(grid)
            case 83:
                grid = lengthColorAugmentation3(grid)
            case 84:
                grid = lengthColorAugmentation4(grid)
            case 85:
                grid = lengthColorAugmentation5(grid)
            case 86:
                grid = lengthColorAugmentation6(grid)
            case 87:
                grid = lengthColorAugmentation7(grid)
            case 88:
                grid = lengthColorAugmentation8(grid)
            case 89:
                grid = lengthColorAugmentation9(grid)
            case 90:
                grid = growingColor0(grid)
            case 91:
                grid = growingColor1(grid)
            case 92:
                grid = growingColor2(grid)
            case 93:
                grid = growingColor3(grid)
            case 94:
                grid = growingColor4(grid)
            case 95:
                grid = growingColor5(grid)
            case 96:
                grid = growingColor6(grid)
            case 97:
                grid = growingColor7(grid)
            case 98:
                grid = growingColor8(grid)
            case 99:
                grid = growingColor9(grid)
            case 100:
                grid = removeNoise0(grid)
            case 101:
                grid = removeNoise1(grid)
            case 102:
                grid = removeNoise2(grid)
            case 103:
                grid = removeNoise3(grid)
            case 104:
                grid = removeNoise4(grid)
            case 105:
                grid = removeNoise5(grid)
            case 106:
                grid = removeNoise6(grid)
            case 107:
                grid = removeNoise7(grid)
            case 108:
                grid = removeNoise8(grid)
            case 109:
                grid = removeNoise9(grid)
            case 110:
                grid = changeAColor0_1(grid)
            case 111:
                grid = changeAColor0_2(grid)
            case 112:
                grid = changeAColor0_3(grid)
            case 113:
                grid = changeAColor0_4(grid)
            case 114:
                grid = changeAColor0_5(grid)
            case 115:
                grid = changeAColor0_6(grid)
            case 116:
                grid = changeAColor0_7(grid)
            case 117:
                grid = changeAColor0_8(grid)
            case 118:
                grid = changeAColor0_9(grid)
            case 119:
                grid = changeAColor1_0(grid)
            case 120:
                grid = changeAColor1_2(grid)
            case 121:
                grid = changeAColor1_3(grid)
            case 122:
                grid = changeAColor1_4(grid)
            case 123:
                grid = changeAColor1_5(grid)
            case 124:
                grid = changeAColor1_6(grid)
            case 125:
                grid = changeAColor1_7(grid)
            case 126:
                grid = changeAColor1_8(grid)
            case 127:
                grid = changeAColor1_9(grid)
            case 128:
                grid = changeAColor2_0(grid)
            case 129:
                grid = changeAColor2_1(grid)
            case 130:
                grid = changeAColor2_3(grid)
            case 131:
                grid = changeAColor2_4(grid)
            case 132:
                grid = changeAColor2_5(grid)
            case 133:
                grid = changeAColor2_6(grid)
            case 134:
                grid = changeAColor2_7(grid)
            case 135:
                grid = changeAColor2_8(grid)
            case 136:
                grid = changeAColor2_9(grid)
            case 137:
                grid = changeAColor3_0(grid)
            case 138:
                grid = changeAColor3_1(grid)
            case 139:
                grid = changeAColor3_2(grid)
            case 140:
                grid = changeAColor3_4(grid)
            case 141:
                grid = changeAColor3_5(grid)
            case 142:
                grid = changeAColor3_6(grid)
            case 143:
                grid = changeAColor3_7(grid)
            case 144:
                grid = changeAColor3_8(grid)
            case 145:
                grid = changeAColor3_9(grid)
            case 146:
                grid = changeAColor4_0(grid)
            case 147:
                grid = changeAColor4_1(grid)
            case 148:
                grid = changeAColor4_2(grid)
            case 149:
                grid = changeAColor4_3(grid)
            case 150:
                grid = changeAColor4_5(grid)
            case 151:
                grid = changeAColor4_6(grid)
            case 152:
                grid = changeAColor4_7(grid)
            case 153:
                grid = changeAColor4_8(grid)
            case 154:
                grid = changeAColor4_9(grid)
            case 155:
                grid = changeAColor5_0(grid)
            case 156:
                grid = changeAColor5_1(grid)
            case 157:
                grid = changeAColor5_2(grid)
            case 158:
                grid = changeAColor5_3(grid)
            case 159:
                grid = changeAColor5_4(grid)
            case 160:
                grid = changeAColor5_6(grid)
            case 161:
                grid = changeAColor5_7(grid)
            case 162:
                grid = changeAColor5_8(grid)
            case 163:
                grid = changeAColor5_9(grid)
            case 164:
                grid = changeAColor6_0(grid)
            case 165:
                grid = changeAColor6_1(grid)
            case 166:
                grid = changeAColor6_2(grid)
            case 167:
                grid = changeAColor6_3(grid)
            case 168:
                grid = changeAColor6_4(grid)
            case 169:
                grid = changeAColor6_5(grid)
            case 170:
                grid = changeAColor6_7(grid)
            case 171:
                grid = changeAColor6_8(grid)
            case 172:
                grid = changeAColor6_9(grid)
            case 173:
                grid = changeAColor7_0(grid)
            case 174:
                grid = changeAColor7_1(grid)
            case 175:
                grid = changeAColor7_2(grid)
            case 176:
                grid = changeAColor7_3(grid)
            case 177:
                grid = changeAColor7_4(grid)
            case 178:
                grid = changeAColor7_5(grid)
            case 179:
                grid = changeAColor7_6(grid)
            case 180:
                grid = changeAColor7_8(grid)
            case 181:
                grid = changeAColor7_9(grid)
            case 182:
                grid = changeAColor8_0(grid)
            case 183:
                grid = changeAColor8_1(grid)
            case 184:
                grid = changeAColor8_2(grid)
            case 185:
                grid = changeAColor8_3(grid)
            case 186:
                grid = changeAColor8_4(grid)
            case 187:
                grid = changeAColor8_5(grid)
            case 188:
                grid = changeAColor8_6(grid)
            case 189:
                grid = changeAColor8_7(grid)
            case 190:
                grid = changeAColor8_9(grid)
            case 191:
                grid = changeAColor9_0(grid)
            case 192:
                grid = changeAColor9_1(grid)
            case 193:
                grid = changeAColor9_2(grid)
            case 194:
                grid = changeAColor9_3(grid)
            case 195:
                grid = changeAColor9_4(grid)
            case 196:
                grid = changeAColor9_5(grid)
            case 197:
                grid = changeAColor9_6(grid)
            case 198:
                grid = changeAColor9_7(grid)
            case 199:
                grid = changeAColor9_8(grid)
            case 200:
                grid = extendLine5_0(grid)
            case 201:
                grid = extendLine5_1(grid)
            case 202:
                grid = extendLine5_2(grid)
            case 203:
                grid = extendLine5_3(grid)
            case 204:
                grid = extendLine5_4(grid)
            case 205:
                grid = extendLine5_5(grid)
            case 206:
                grid = extendLine5_6(grid)
            case 207:
                grid = extendLine5_7(grid)
            case 208:
                grid = extendLine5_8(grid)
            case 209:
                grid = extendLine5_9(grid)
            case 210:
                grid = extendLine10_0(grid)
            case 211:
                grid = extendLine10_1(grid)
            case 212:
                grid = extendLine10_2(grid)
            case 213:
                grid = extendLine10_3(grid)
            case 214:
                grid = extendLine10_4(grid)
            case 215:
                grid = extendLine10_5(grid)
            case 216:
                grid = extendLine10_6(grid)
            case 217:
                grid = extendLine10_7(grid)
            case 218:
                grid = extendLine10_8(grid)
            case 219:
                grid = extendLine10_9(grid)
            case 220:
                grid = extendLine15_0(grid)
            case 221:
                grid = extendLine15_1(grid)
            case 222:
                grid = extendLine15_2(grid)
            case 223:
                grid = extendLine15_3(grid)
            case 224:
                grid = extendLine15_4(grid)
            case 225:
                grid = extendLine15_5(grid)
            case 226:
                grid = extendLine15_6(grid)
            case 227:
                grid = extendLine15_7(grid)
            case 228:
                grid = extendLine15_8(grid)
            case 229:
                grid = extendLine15_9(grid)
            case 230:
                grid = extendLine20_0(grid)
            case 231:
                grid = extendLine20_1(grid)
            case 232:
                grid = extendLine20_2(grid)
            case 233:
                grid = extendLine20_3(grid)
            case 234:
                grid = extendLine20_4(grid)
            case 235:
                grid = extendLine20_5(grid)
            case 236:
                grid = extendLine20_6(grid)
            case 237:
                grid = extendLine20_7(grid)
            case 238:
                grid = extendLine20_8(grid)
            case 239:
                grid = extendLine20_9(grid)
            case 240:
                grid = extendLine25_0(grid)
            case 241:
                grid = extendLine25_1(grid)
            case 242:
                grid = extendLine25_2(grid)
            case 243:
                grid = extendLine25_3(grid)
            case 244:
                grid = extendLine25_4(grid)
            case 245:
                grid = extendLine25_5(grid)
            case 246:
                grid = extendLine25_6(grid)
            case 247:
                grid = extendLine25_7(grid)
            case 248:
                grid = extendLine25_8(grid)
            case 249:
                grid = extendLine25_9(grid)
            case 250:
                grid = extendLine30_0(grid)
            case 251:
                grid = extendLine30_1(grid)
            case 252:
                grid = extendLine30_2(grid)
            case 253:
                grid = extendLine30_3(grid)
            case 254:
                grid = extendLine30_4(grid)
            case 255:
                grid = extendLine30_5(grid)
            case 256:
                grid = extendLine30_6(grid)
            case 257:
                grid = extendLine30_7(grid)
            case 258:
                grid = extendLine30_8(grid)
            case 259:
                grid = extendLine30_9(grid)
            case 260:
                grid = extendLine35_0(grid)
            case 261:
                grid = extendLine35_1(grid)
            case 262:
                grid = extendLine35_2(grid)
            case 263:
                grid = extendLine35_3(grid)
            case 264:
                grid = extendLine35_4(grid)
            case 265:
                grid = extendLine35_5(grid)
            case 266:
                grid = extendLine35_6(grid)
            case 267:
                grid = extendLine35_7(grid)
            case 268:
                grid = extendLine35_8(grid)
            case 269:
                grid = extendLine35_9(grid)
            case 270:
                grid = extendLine40_0(grid)
            case 271:
                grid = extendLine40_1(grid)
            case 272:
                grid = extendLine40_2(grid)
            case 273:
                grid = extendLine40_3(grid)
            case 274:
                grid = extendLine40_4(grid)
            case 275:
                grid = extendLine40_5(grid)
            case 276:
                grid = extendLine40_6(grid)
            case 277:
                grid = extendLine40_7(grid)
            case 278:
                grid = extendLine40_8(grid)
            case 279:
                grid = extendLine40_9(grid)
            case 280:
                grid = extendLine45_0(grid)
            case 281:
                grid = extendLine45_1(grid)
            case 282:
                grid = extendLine45_2(grid)
            case 283:
                grid = extendLine45_3(grid)
            case 284:
                grid = extendLine45_4(grid)
            case 285:
                grid = extendLine45_5(grid)
            case 286:
                grid = extendLine45_6(grid)
            case 287:
                grid = extendLine45_7(grid)
            case 288:
                grid = extendLine45_8(grid)
            case 289:
                grid = extendLine45_9(grid)
            case 290:
                grid = extendLine50_0(grid)
            case 291:
                grid = extendLine50_1(grid)
            case 292:
                grid = extendLine50_2(grid)
            case 293:
                grid = extendLine50_3(grid)
            case 294:
                grid = extendLine50_4(grid)
            case 295:
                grid = extendLine50_5(grid)
            case 296:
                grid = extendLine50_6(grid)
            case 297:
                grid = extendLine50_7(grid)
            case 298:
                grid = extendLine50_8(grid)
            case 299:
                grid = extendLine50_9(grid)
            case 300:
                grid = extendLine55_0(grid)
            case 301:
                grid = extendLine55_1(grid)
            case 302:
                grid = extendLine55_2(grid)
            case 303:
                grid = extendLine55_3(grid)
            case 304:
                grid = extendLine55_4(grid)
            case 305:
                grid = extendLine55_5(grid)
            case 306:
                grid = extendLine55_6(grid)
            case 307:
                grid = extendLine55_7(grid)
            case 308:
                grid = extendLine55_8(grid)
            case 309:
                grid = extendLine55_9(grid)
            case 310:
                grid = extendLine60_0(grid)
            case 311:
                grid = extendLine60_1(grid)
            case 312:
                grid = extendLine60_2(grid)
            case 313:
                grid = extendLine60_3(grid)
            case 314:
                grid = extendLine60_4(grid)
            case 315:
                grid = extendLine60_5(grid)
            case 316:
                grid = extendLine60_6(grid)
            case 317:
                grid = extendLine60_7(grid)
            case 318:
                grid = extendLine60_8(grid)
            case 319:
                grid = extendLine60_9(grid)
            case 320:
                grid = extendLine65_0(grid)
            case 321:
                grid = extendLine65_1(grid)
            case 322:
                grid = extendLine65_2(grid)
            case 323:
                grid = extendLine65_3(grid)
            case 324:
                grid = extendLine65_4(grid)
            case 325:
                grid = extendLine65_5(grid)
            case 326:
                grid = extendLine65_6(grid)
            case 327:
                grid = extendLine65_7(grid)
            case 328:
                grid = extendLine65_8(grid)
            case 329:
                grid = extendLine65_9(grid)
            case 330:
                grid = extendLine70_0(grid)
            case 331:
                grid = extendLine70_1(grid)
            case 332:
                grid = extendLine70_2(grid)
            case 333:
                grid = extendLine70_3(grid)
            case 334:
                grid = extendLine70_4(grid)
            case 335:
                grid = extendLine70_5(grid)
            case 336:
                grid = extendLine70_6(grid)
            case 337:
                grid = extendLine70_7(grid)
            case 338:
                grid = extendLine70_8(grid)
            case 339:
                grid = extendLine70_9(grid)
            case 340:
                grid = extendLine75_0(grid)
            case 341:
                grid = extendLine75_1(grid)
            case 342:
                grid = extendLine75_2(grid)
            case 343:
                grid = extendLine75_3(grid)
            case 344:
                grid = extendLine75_4(grid)
            case 345:
                grid = extendLine75_5(grid)
            case 346:
                grid = extendLine75_6(grid)
            case 347:
                grid = extendLine75_7(grid)
            case 348:
                grid = extendLine75_8(grid)
            case 349:
                grid = extendLine75_9(grid)
            case 350:
                grid = extendLine80_0(grid)
            case 351:
                grid = extendLine80_1(grid)
            case 352:
                grid = extendLine80_2(grid)
            case 353:
                grid = extendLine80_3(grid)
            case 354:
                grid = extendLine80_4(grid)
            case 355:
                grid = extendLine80_5(grid)
            case 356:
                grid = extendLine80_6(grid)
            case 357:
                grid = extendLine80_7(grid)
            case 358:
                grid = extendLine80_8(grid)
            case 359:
                grid = extendLine80_9(grid)
            case 360:
                grid = extendLine85_0(grid)
            case 361:
                grid = extendLine85_1(grid)
            case 362:
                grid = extendLine85_2(grid)
            case 363:
                grid = extendLine85_3(grid)
            case 364:
                grid = extendLine85_4(grid)
            case 365:
                grid = extendLine85_5(grid)
            case 366:
                grid = extendLine85_6(grid)
            case 367:
                grid = extendLine85_7(grid)
            case 368:
                grid = extendLine85_8(grid)
            case 369:
                grid = extendLine85_9(grid)
            case 370:
                grid = extendLine90_0(grid)
            case 371:
                grid = extendLine90_1(grid)
            case 372:
                grid = extendLine90_2(grid)
            case 373:
                grid = extendLine90_3(grid)
            case 374:
                grid = extendLine90_4(grid)
            case 375:
                grid = extendLine90_5(grid)
            case 376:
                grid = extendLine90_6(grid)
            case 377:
                grid = extendLine90_7(grid)
            case 378:
                grid = extendLine90_8(grid)
            case 379:
                grid = extendLine90_9(grid)
            case 380:
                grid = extendLine95_0(grid)
            case 381:
                grid = extendLine95_1(grid)
            case 382:
                grid = extendLine95_2(grid)
            case 383:
                grid = extendLine95_3(grid)
            case 384:
                grid = extendLine95_4(grid)
            case 385:
                grid = extendLine95_5(grid)
            case 386:
                grid = extendLine95_6(grid)
            case 387:
                grid = extendLine95_7(grid)
            case 388:
                grid = extendLine95_8(grid)
            case 389:
                grid = extendLine95_9(grid)
            case 390:
                grid = extendLine100_0(grid)
            case 391:
                grid = extendLine100_1(grid)
            case 392:
                grid = extendLine100_2(grid)
            case 393:
                grid = extendLine100_3(grid)
            case 394:
                grid = extendLine100_4(grid)
            case 395:
                grid = extendLine100_5(grid)
            case 396:
                grid = extendLine100_6(grid)
            case 397:
                grid = extendLine100_7(grid)
            case 398:
                grid = extendLine100_8(grid)
            case 399:
                grid = extendLine100_9(grid)
            case 400:
                grid = extendColumn5_0(grid)
            case 401:
                grid = extendColumn5_1(grid)
            case 402:
                grid = extendColumn5_2(grid)
            case 403:
                grid = extendColumn5_3(grid)
            case 404:
                grid = extendColumn5_4(grid)
            case 405:
                grid = extendColumn5_5(grid)
            case 406:
                grid = extendColumn5_6(grid)
            case 407:
                grid = extendColumn5_7(grid)
            case 408:
                grid = extendColumn5_8(grid)
            case 409:
                grid = extendColumn5_9(grid)
            case 410:
                grid = extendColumn10_0(grid)
            case 411:
                grid = extendColumn10_1(grid)
            case 412:
                grid = extendColumn10_2(grid)
            case 413:
                grid = extendColumn10_3(grid)
            case 414:
                grid = extendColumn10_4(grid)
            case 415:
                grid = extendColumn10_5(grid)
            case 416:
                grid = extendColumn10_6(grid)
            case 417:
                grid = extendColumn10_7(grid)
            case 418:
                grid = extendColumn10_8(grid)
            case 419:
                grid = extendColumn10_9(grid)
            case 420:
                grid = extendColumn15_0(grid)
            case 421:
                grid = extendColumn15_1(grid)
            case 422:
                grid = extendColumn15_2(grid)
            case 423:
                grid = extendColumn15_3(grid)
            case 424:
                grid = extendColumn15_4(grid)
            case 425:
                grid = extendColumn15_5(grid)
            case 426:
                grid = extendColumn15_6(grid)
            case 427:
                grid = extendColumn15_7(grid)
            case 428:
                grid = extendColumn15_8(grid)
            case 429:
                grid = extendColumn15_9(grid)
            case 430:
                grid = extendColumn20_0(grid)
            case 431:
                grid = extendColumn20_1(grid)
            case 432:
                grid = extendColumn20_2(grid)
            case 433:
                grid = extendColumn20_3(grid)
            case 434:
                grid = extendColumn20_4(grid)
            case 435:
                grid = extendColumn20_5(grid)
            case 436:
                grid = extendColumn20_6(grid)
            case 437:
                grid = extendColumn20_7(grid)
            case 438:
                grid = extendColumn20_8(grid)
            case 439:
                grid = extendColumn20_9(grid)
            case 440:
                grid = extendColumn25_0(grid)
            case 441:
                grid = extendColumn25_1(grid)
            case 442:
                grid = extendColumn25_2(grid)
            case 443:
                grid = extendColumn25_3(grid)
            case 444:
                grid = extendColumn25_4(grid)
            case 445:
                grid = extendColumn25_5(grid)
            case 446:
                grid = extendColumn25_6(grid)
            case 447:
                grid = extendColumn25_7(grid)
            case 448:
                grid = extendColumn25_8(grid)
            case 449:
                grid = extendColumn25_9(grid)
            case 450:
                grid = extendColumn30_0(grid)
            case 451:
                grid = extendColumn30_1(grid)
            case 452:
                grid = extendColumn30_2(grid)
            case 453:
                grid = extendColumn30_3(grid)
            case 454:
                grid = extendColumn30_4(grid)
            case 455:
                grid = extendColumn30_5(grid)
            case 456:
                grid = extendColumn30_6(grid)
            case 457:
                grid = extendColumn30_7(grid)
            case 458:
                grid = extendColumn30_8(grid)
            case 459:
                grid = extendColumn30_9(grid)
            case 460:
                grid = extendColumn35_0(grid)
            case 461:
                grid = extendColumn35_1(grid)
            case 462:
                grid = extendColumn35_2(grid)
            case 463:
                grid = extendColumn35_3(grid)
            case 464:
                grid = extendColumn35_4(grid)
            case 465:
                grid = extendColumn35_5(grid)
            case 466:
                grid = extendColumn35_6(grid)
            case 467:
                grid = extendColumn35_7(grid)
            case 468:
                grid = extendColumn35_8(grid)
            case 469:
                grid = extendColumn35_9(grid)
            case 470:
                grid = extendColumn40_0(grid)
            case 471:
                grid = extendColumn40_1(grid)
            case 472:
                grid = extendColumn40_2(grid)
            case 473:
                grid = extendColumn40_3(grid)
            case 474:
                grid = extendColumn40_4(grid)
            case 475:
                grid = extendColumn40_5(grid)
            case 476:
                grid = extendColumn40_6(grid)
            case 477:
                grid = extendColumn40_7(grid)
            case 478:
                grid = extendColumn40_8(grid)
            case 479:
                grid = extendColumn40_9(grid)
            case 480:
                grid = extendColumn45_0(grid)
            case 481:
                grid = extendColumn45_1(grid)
            case 482:
                grid = extendColumn45_2(grid)
            case 483:
                grid = extendColumn45_3(grid)
            case 484:
                grid = extendColumn45_4(grid)
            case 485:
                grid = extendColumn45_5(grid)
            case 486:
                grid = extendColumn45_6(grid)
            case 487:
                grid = extendColumn45_7(grid)
            case 488:
                grid = extendColumn45_8(grid)
            case 489:
                grid = extendColumn45_9(grid)
            case 490:
                grid = extendColumn50_0(grid)
            case 491:
                grid = extendColumn50_1(grid)
            case 492:
                grid = extendColumn50_2(grid)
            case 493:
                grid = extendColumn50_3(grid)
            case 494:
                grid = extendColumn50_4(grid)
            case 495:
                grid = extendColumn50_5(grid)
            case 496:
                grid = extendColumn50_6(grid)
            case 497:
                grid = extendColumn50_7(grid)
            case 498:
                grid = extendColumn50_8(grid)
            case 499:
                grid = extendColumn50_9(grid)
            case 500:
                grid = extendColumn55_0(grid)
            case 501:
                grid = extendColumn55_1(grid)
            case 502:
                grid = extendColumn55_2(grid)
            case 503:
                grid = extendColumn55_3(grid)
            case 504:
                grid = extendColumn55_4(grid)
            case 505:
                grid = extendColumn55_5(grid)
            case 506:
                grid = extendColumn55_6(grid)
            case 507:
                grid = extendColumn55_7(grid)
            case 508:
                grid = extendColumn55_8(grid)
            case 509:
                grid = extendColumn55_9(grid)
            case 510:
                grid = extendColumn60_0(grid)
            case 511:
                grid = extendColumn60_1(grid)
            case 512:
                grid = extendColumn60_2(grid)
            case 513:
                grid = extendColumn60_3(grid)
            case 514:
                grid = extendColumn60_4(grid)
            case 515:
                grid = extendColumn60_5(grid)
            case 516:
                grid = extendColumn60_6(grid)
            case 517:
                grid = extendColumn60_7(grid)
            case 518:
                grid = extendColumn60_8(grid)
            case 519:
                grid = extendColumn60_9(grid)
            case 520:
                grid = extendColumn65_0(grid)
            case 521:
                grid = extendColumn65_1(grid)
            case 522:
                grid = extendColumn65_2(grid)
            case 523:
                grid = extendColumn65_3(grid)
            case 524:
                grid = extendColumn65_4(grid)
            case 525:
                grid = extendColumn65_5(grid)
            case 526:
                grid = extendColumn65_6(grid)
            case 527:
                grid = extendColumn65_7(grid)
            case 528:
                grid = extendColumn65_8(grid)
            case 529:
                grid = extendColumn65_9(grid)
            case 530:
                grid = extendColumn70_0(grid)
            case 531:
                grid = extendColumn70_1(grid)
            case 532:
                grid = extendColumn70_2(grid)
            case 533:
                grid = extendColumn70_3(grid)
            case 534:
                grid = extendColumn70_4(grid)
            case 535:
                grid = extendColumn70_5(grid)
            case 536:
                grid = extendColumn70_6(grid)
            case 537:
                grid = extendColumn70_7(grid)
            case 538:
                grid = extendColumn70_8(grid)
            case 539:
                grid = extendColumn70_9(grid)
            case 540:
                grid = extendColumn75_0(grid)
            case 541:
                grid = extendColumn75_1(grid)
            case 542:
                grid = extendColumn75_2(grid)
            case 543:
                grid = extendColumn75_3(grid)
            case 544:
                grid = extendColumn75_4(grid)
            case 545:
                grid = extendColumn75_5(grid)
            case 546:
                grid = extendColumn75_6(grid)
            case 547:
                grid = extendColumn75_7(grid)
            case 548:
                grid = extendColumn75_8(grid)
            case 549:
                grid = extendColumn75_9(grid)
            case 550:
                grid = extendColumn80_0(grid)
            case 551:
                grid = extendColumn80_1(grid)
            case 552:
                grid = extendColumn80_2(grid)
            case 553:
                grid = extendColumn80_3(grid)
            case 554:
                grid = extendColumn80_4(grid)
            case 555:
                grid = extendColumn80_5(grid)
            case 556:
                grid = extendColumn80_6(grid)
            case 557:
                grid = extendColumn80_7(grid)
            case 558:
                grid = extendColumn80_8(grid)
            case 559:
                grid = extendColumn80_9(grid)
            case 560:
                grid = extendColumn85_0(grid)
            case 561:
                grid = extendColumn85_1(grid)
            case 562:
                grid = extendColumn85_2(grid)
            case 563:
                grid = extendColumn85_3(grid)
            case 564:
                grid = extendColumn85_4(grid)
            case 565:
                grid = extendColumn85_5(grid)
            case 566:
                grid = extendColumn85_6(grid)
            case 567:
                grid = extendColumn85_7(grid)
            case 568:
                grid = extendColumn85_8(grid)
            case 569:
                grid = extendColumn85_9(grid)
            case 570:
                grid = extendColumn90_0(grid)
            case 571:
                grid = extendColumn90_1(grid)
            case 572:
                grid = extendColumn90_2(grid)
            case 573:
                grid = extendColumn90_3(grid)
            case 574:
                grid = extendColumn90_4(grid)
            case 575:
                grid = extendColumn90_5(grid)
            case 576:
                grid = extendColumn90_6(grid)
            case 577:
                grid = extendColumn90_7(grid)
            case 578:
                grid = extendColumn90_8(grid)
            case 579:
                grid = extendColumn90_9(grid)
            case 580:
                grid = extendColumn95_0(grid)
            case 581:
                grid = extendColumn95_1(grid)
            case 582:
                grid = extendColumn95_2(grid)
            case 583:
                grid = extendColumn95_3(grid)
            case 584:
                grid = extendColumn95_4(grid)
            case 585:
                grid = extendColumn95_5(grid)
            case 586:
                grid = extendColumn95_6(grid)
            case 587:
                grid = extendColumn95_7(grid)
            case 588:
                grid = extendColumn95_8(grid)
            case 589:
                grid = extendColumn95_9(grid)
            case 590:
                grid = extendColumn100_0(grid)
            case 591:
                grid = extendColumn100_1(grid)
            case 592:
                grid = extendColumn100_2(grid)
            case 593:
                grid = extendColumn100_3(grid)
            case 594:
                grid = extendColumn100_4(grid)
            case 595:
                grid = extendColumn100_5(grid)
            case 596:
                grid = extendColumn100_6(grid)
            case 597:
                grid = extendColumn100_7(grid)
            case 598:
                grid = extendColumn100_8(grid)
            case 599:
                grid = extendColumn100_9(grid)

    return grid
