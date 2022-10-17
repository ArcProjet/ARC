import json
import matplotlib.pyplot as plt
from random import randrange

indexTab = []
index = open('indexTab.txt','r').readlines()
for i in index:
    indexTab.append(i.replace('\n',''))

def openJsonFile():
    f = open('data/training/' + indexTab[randrange(len(indexTab))] + '.json','r')
    y = json.loads(f.read())

    grille1 = y['test'][0]
    grille2 = y['train'][0]

    return (grille1,grille2)

def draw(grille1,grille2):
    grille1Input = grille1['input']
    grille1Output = grille1['output']
    grille2Input = grille2['input']
    grille2Output = grille2['output']

    fig = plt.figure(figsize=(5, 5))
    fig.add_subplot(2, 2, 1)
    plt.title("Input 1")
    plt.axis('off')
    plt.imshow(grille1Input)
    fig.add_subplot(2, 2, 2)
    plt.title("Output 1")
    plt.axis('off')
    plt.imshow(grille1Output)
    fig.add_subplot(2, 2, 3)
    plt.title("Input 2")
    plt.axis('off')
    plt.imshow(grille2Input)
    fig.add_subplot(2, 2, 4)
    plt.title("Output 2")
    plt.axis('off')
    plt.imshow(grille2Output)
    plt.show()

(grille1,grille2) = openJsonFile()
draw(grille1,grille2)