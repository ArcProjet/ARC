def getInputCopyListe(list):
    res = []
    for i in range(0,len(list)):
        tmp = []
        for j in range(0,len(list[0])):
            tmp.append(list[i][j])
        res.append(tmp)
    return res

def rotateRightListe(list):
    res = getInputCopyListe(list)
    for i in range(0,len(list)):
        cpt = len(list) - 1
        for j in range(0,len(list[0])):
            res[i][j] = list[cpt][i]
            cpt -= 1
    return res