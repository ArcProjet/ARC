import matplotlib.pyplot as plt
import numpy as np

class Grid:

    #Constructor
    def __init__(self,input,expected):
        self.input = input
        self.output = input
        self.expected = expected
        self.nbRow = len(self.input)
        self.nbColumn = len(self.input[0])

    #Only square tab for the moment
    def getSuccess(self):
        cpt = 0
        cptVide = 0
        if(len(self.expected) != len(self.output) or len(self.expected[0]) != len(self.output[0])): # Temporaire avec les grilles non carré
            return 0
        for i in range(0,len(self.output)):
            for j in range(0,len(self.output[0])):
                if(self.expected[i][j] != 0):
                    cptVide += 1
                if(self.expected[i][j] == self.output[i][j]):   #and self.expected[i][j] != 0):
                    cpt += 1
        res = 100*(cpt/(len(self.output)*len(self.output[0])))
        #res = 100*(cpt/cptVide)
        #print("Le pourcentage de réussite est de " + str(res) + "%")
        return res

    def ExpectationVsreality(self):
        fig, axs = plt.subplots(1,2)
        axs[0].set_title('Expectation')
        axs[0].axis('off')
        axs[0].matshow(self.expected, cmap='rainbow')
        axs[1].set_title('Reality')
        axs[1].axis('off')
        axs[1].matshow(self.output, cmap='rainbow')

    def displayGrid(self):
        fig, axs = plt.subplots(1,2)
        axs[0].set_title('Test Input')
        axs[0].axis('off')
        axs[0].matshow(self.input, cmap='rainbow')
        axs[1].set_title('System Output')
        axs[1].axis('off')
        axs[1].matshow(self.output, cmap='rainbow')
        #fig = plt.figure(figsize=(6, 6))
        #fig.add_subplot(1,2,1)
        #plt.title("Test Input")
        #plt.axis('off')
        #plt.imshow(self.input)
        #fig.add_subplot(1,2,2)
        #plt.title("System Output")
        #plt.axis('off')
        #plt.imshow(self.output)
        #plt.show()

    def isSquare(self):
        return ((self.nbRow == self.nbColumn))# and (len(self.output) == len(self.output[0])))

    def getInputCopy(self):
        res = []
        for i in range(0,self.nbRow):
            tmp = []
            for j in range(0,self.nbColumn):
                tmp.append(self.output[i][j])
            res.append(tmp)
        return res
    
    def getGridCopy(self):
        return Grid(self.input,self.output)

    def getCornerUpLeft(self):
        res = []
        resRow = self.nbRow // 2
        resColumn = self.nbColumn // 2
        if(self.nbRow %2 != 0 and self.nbColumn%2 != 0):
            #print('Result is not compatible with this function')
            pass
        for i in range(0,resRow):
            tmpRow = []
            for j in range(0,resColumn):
                tmpRow.append(self.output[i][j])
            res.append(tmpRow)
        return(res)

    def getCornerUpRight(self):
        res = []
        resRow = self.nbRow // 2
        resColumn = self.nbColumn // 2
        if(self.nbRow %2 != 0 and self.nbColumn%2 != 0):
            #print('Result is not compatible with this function')
            pass
        for i in range(0,resRow):
            tmpRow = []
            for j in range(0,resColumn):
                tmpRow.append(self.output[i][j+resColumn])
            res.append(tmpRow)
        return(res)

    def getCornerDownLeft(self):
        res = []
        resRow = self.nbRow // 2
        resColumn = self.nbColumn // 2
        if(self.nbRow %2 != 0 and self.nbColumn%2 != 0):
            #print('Result is not compatible with this function')
            pass
        for i in range(0,resRow):
            tmpRow = []
            for j in range(0,resColumn):
                tmpRow.append(self.output[i+resRow][j+resColumn])
            res.append(tmpRow)
        return(res)

    def getCornerDownRight(self):
        res = []
        resRow = self.nbRow // 2
        resColumn = self.nbColumn // 2
        if(self.nbRow %2 != 0 and self.nbColumn%2 != 0):
            #print('Result is not compatible with this function')
            pass
        for i in range(0,resRow):
            tmpRow = []
            for j in range(0,resColumn):
                tmpRow.append(self.output[i+resRow][j])
            res.append(tmpRow)
        return(res)
    
    #Getters
    def getInput(self):
        return self.input
    
    def getOutput(self):
        return self.output

    def getNbRow(self):
        return self.nbRow
    
    def getNbColumn(self):
        return self.nbColumn

    #Setters
    def setOutput(self,tab):
        self.output = tab

    def setInput(self,tab):
        self.input = tab
