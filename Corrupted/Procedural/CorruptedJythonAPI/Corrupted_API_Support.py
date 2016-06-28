'''

@author: Christian Gebhart and Tobias Kohn
'''

# We use an underscore to hide the "GameWindow" when this module is imported.
from Engine import GameWindow as _GameWindow
from Corrupted_FunctionalAPI import *

class CustomCorruptedMaker(CorruptedFunctionalAPI):
    
    """local variables used to store references to student written methods."""
    doBuildGame = None
    doUpdateGame = None
    doCheckGameWon = None
    doUpdateCounter = None
    doDeleteMissedTiles = None
    doDrawColumn = None
    doDrawBoard = None
    doSetTilesToWin = None
    doSetGameWon = None
    doHandlePlayerTileCollision = None
    
    """local variables used throughout the labs."""
    x = 0
    y = 0
    matches = 0 
    
    """Overwrites of all methods students may need to implement throughout the course of their learning.
    overwritten methods check to see if they are being implemented by each Lab. If they are, then the program will run the new method written
    as stored in a local variable by reference. If not, the superclass method will be called instead. """
    def buildGame(self):
        if CustomCorruptedMaker.doBuildGame is not None:
            CustomCorruptedMaker.doBuildGame(self)
        else:
            super(CustomCorruptedMaker, self).buildGame() 
            
    def updateGame(self):
        if CustomCorruptedMaker.doUpdateGame is not None:
            CustomCorruptedMaker.doUpdateGame(self)
        else:
            super(CustomCorruptedMaker, self).updateGame() 
            
    def checkGameWon(self):
        if CustomCorruptedMaker.doCheckGameWon is not None:
            CustomCorruptedMaker.doCheckGameWon(self)
        else:
            super(CustomCorruptedMaker, self).checkGameWon()      
            
    def drawColumn(self, a):
        if CustomCorruptedMaker.doDrawColumn is not None:
            CustomCorruptedMaker.doDrawColumn(a)
        else:
            super(CustomCorruptedMaker, self).drawColumn(a)  

    def updateCounter(self):
        if CustomCorruptedMaker.doUpdateCounter is not None:
            CustomCorruptedMaker.doUpdateCounter()
        else:
            super(CustomCorruptedMaker, self).updateCounter()
            
    def deleteMissedTiles(self):
        if CustomCorruptedMaker.doDeleteMissedTiles is not None:
            CustomCorruptedMaker.doDeleteMissedTiles()
        else:
            super(CustomCorruptedMaker, self).deleteMissedTiles()
            
    def drawBoard(self):
        if CustomCorruptedMaker.doDrawBoard is not None:
            CustomCorruptedMaker.doDrawBoard()
        else:
            super(CustomCorruptedMaker, self).drawBoard()
            
    def setTilesToWin(self, tilesToWin):
        if CustomCorruptedMaker.doSetTilesToWin is not None:
            CustomCorruptedMaker.doSetTilesToWin(tilesToWin)
        else:
            super(CustomCorruptedMaker, self).setTilesToWin(tilesToWin)
            
    def setGameWon(self, gameWon):
        if CustomCorruptedMaker.doSetGameWon is not None:
            CustomCorruptedMaker.doSetGameWon(gameWon)
        else:
            super(CustomCorruptedMaker, self).setGameWon(gameWon)
            
    """def handlePlayerTileCollision(self):
        if CustomCorruptedMaker.doHandlePlayerTileCollision is not None:
            CustomCorruptedMaker.doHandlePlayerTileCollision()
        else:
            super(CustomCorruptedMaker, self).handlePlayerTileCollision()"""


"""these methods are what actually define re references to each method in 
the CorruptedMaker class. See below for more documentation"""       
# This function will later be used as an annotation. It sets the function to be called
# in order to build the game.
#
# Example usage:
#
# | @build_Game
# | def my_init(CustomCorruptedMaker):
# |     <do something here>
#
# Python will translate this to:
#
# | def my_init(CustomCorruptedMaker):
# |     <do something here>
# | my_init = build_Game(my_init)

def build_Game(f):
    CustomCorruptedMaker.doBuildGame = f
    return f;

def update_Game(f):
    CustomCorruptedMaker.doUpdateGame = f
    return f;

def draw_Column(f):
    CustomCorruptedMaker.doCheckGameWon = f
    return f;

def check_Game_Won(f):
    CustomCorruptedMaker.doCheckGameWon = f
    return f;

def update_Counter(f):
    CustomCorruptedMaker.doUpdateCounter = f
    return f;

def delete_Missed_Tiles(f):
    CustomCorruptedMaker.doDeleteMissedTiles = f
    return f;

def draw_Board(f):
    CustomCorruptedMaker.doDrawBoard = f
    return f;

def set_Tiles_To_Win(f):
    CustomCorruptedMaker.doSetTilesToWin = f
    return f;

def setGameWon(f):
    CustomCorruptedMaker.doSetGameWon = f
    return f;

class _Main(_GameWindow):

    """Python constructor"""
    def __init__(self):
        super(_GameWindow, self).__init__()
        self.gameMaker = CustomCorruptedMaker()
        self.setRunner(self.gameMaker)

def startProgram(showFlashScreen = False):
    """Start the program."""
    m = _Main()
    m.startProgram()
