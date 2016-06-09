'''
Created on Apr 16, 2016

@author: chris_000
'''

#from SpaceSmasher import SpaceSmasher #optional code (only needed if you want to delete the start screen)
from SpaceSmasher_FunctionalAPI import *
from Engine import GameWindow as _GameWindow


class CustomSpaceMaker(SpaceSmasherFunctionalAPI):
    # Here we have methods/functions to be called (these are actually just references).
    doBlockSetInitialize = None
    
    def blockSetInitialize(self):
        """Initialize the blocks."""
        # The "CustomSpaceMaker.doBlockSetInitialize(self)" could actually be shortened
        # to just "self.doBlockSetInitialize()". But this way we have the opportunity to
        # use another parameter than just as reference to "self" (e.g. "blockSet").
        if CustomSpaceMaker.doBlockSetInitialize is not None:
            CustomSpaceMaker.doBlockSetInitialize(self)
            
    """method foils"""
            
    def getNumBlocks(self):
        self.blockSetGetNumBlocks()

    def initializeRowSize(self, numCols):
        self.blockSetInitializeRowSize(numCols)
        
    def addIceBlock(self):
        self.blockSetAddIceBlock()
    
    def addFireBlock(self):
        self.blockSetAddFireBlock()
    
    def revealAllPowers(self):
        self.blockSetRevealAllPowers()
        
    def testMethod(self):
        print "success"




    

# This function will later be used as an annotation. It sets the function to be called
# in order to initialize the block set.
#
# Example usage:
#
# | @initializeBlockSet
# | def my_init(spaceMaker):
# |     <do something here>
#
# Python will translate this to:
#
# | def my_init(spaceMaker):
# |     <do something here>
# | my_init = initializeBlockSet(my_init)
def initializeBlockSet(f):
    """Set a function to be used to initialize the block set."""
    CustomSpaceMaker.doBlockSetInitialize = f
    return f

# Again, we use an underscore to make this class "private".
class _Main(_GameWindow):

    def __init__(self):
        super(_GameWindow, self).__init__()
        
        self.setRunner(spaceMaker)

def startProgram(showFlashScreen = False):
    """Start the program."""
    #SpaceSmasher.SetShowFlashScreen(showFlashScreen)
    m = _Main()
    m.startProgram()
    
spaceMaker = CustomSpaceMaker()
class_dict = CustomSpaceMaker.__dict__
for key in class_dict:
        if callable(class_dict[key]):
            print key
            #exec "def %(key)s(): return myObject.%(key)s()" % {'key': key}
            exec ("def %(key)s(*args, **nargs): " + "return spaceMaker.%(key)s(*args, **nargs)") % {'key': key}
                
testMethod()
