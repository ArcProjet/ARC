import matplotlib.pyplot as plt

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
        for i in range(0,len(self.output)):
            for j in range(0,len(self.output[0])):
                if(self.expected[i][j] == self.output[i][j]):
                    cpt += 1
        res = 100*(cpt/(len(self.output)*len(self.output[0])))
        print("Le pourcentage de réussite est de " + str(res) + "%")
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
    
    def getOutput(self):
        return self.output

    #Setters
    def setOutput(self,tab):
        self.output = tab

    def setInput(self,tab):
        self.input = tab
