import json
import matplotlib.pyplot as plt
from random import randrange

f = open('data/training/0b148d64.json')
y = json.load(f)['train']

print(y[1])

#g = open('ttt.txt','a')
#with open('data.json', 'w') as mon_fichier:
#	json.dump(y.replace(']]}, ',']]}, nouvelleGrille'), mon_fichier)
