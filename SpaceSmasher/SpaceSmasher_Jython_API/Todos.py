'''
Created on Apr 16, 2016

@author: chris_000
'''

from SS_API import  *

class TODO15(SpaceSmasherFunctionalAPI):
   
    def blockSetInitialize(self):       #overloading method       
        numRows = 6
        numCols = 6
        l_blockSetInitializeRowSize(numCols)
        count = 0
        for y in range(0, numRows):
            for x in range(0, y):
                l_blockSetAddIceBlock()
                count += 1
            for x in range(0, numRows-y):
                l_blockSetAddFireBlock()
                count += 1
                testMethod()
        l_blockSetRevealAllPowers()
        

class Main(GameWindow):

    def __init__(self):                 #basically a constructor (Might be overloading?)
        super(GameWindow, self).__init__()
        self.setRunner(TODO15())        #Builds TODO15 (not sure how it runs the code)

#
#Actual code being Run
#
#SpaceSmasher.SetShowFlashScreen(False)  #code simply removes the start screen (optional code)
m = Main()                              #Creating a new instance of the Main class (calls constructor)
m.startProgram()                        #running the startprogram defined by the engine 