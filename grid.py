import matplotlib.pyplot as plt

class Grid:

    #Constructor
    def __init__(self,input,output):
        self.input = input
        self.output = output
        self.nbRow = len(self.input)
        self.nbColumn = len(self.input[0])

    #Only square tab for the moment
    def getSuccess(self):
        cpt = 0
        for i in range(0,self.nbRow):
            for j in range(0,self.nbColumn):
                if(self.input[i][j] == self.output[i][j]):
                    cpt += 1
        res = 100*(cpt/(self.nbRow*self.nbColumn))
        print("Le pourcentage de réussite est de " + str(res) + "%")
        return

    def displayGrid(self):
        fig = plt.figure(figsize=(6, 6))
        fig.add_subplot(1,2,1)
        plt.title("Test Input")
        plt.axis('off')
        plt.imshow(self.input)
        fig.add_subplot(1,2,2)
        plt.title("System Output")
        plt.axis('off')
        plt.imshow(self.output)
        plt.show()

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

    #Getters
    def getInput(self):
        return self.input
    
    def getOuput(self):
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