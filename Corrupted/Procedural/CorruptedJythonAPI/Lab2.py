'''
@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@build_Game
def buildGame(Game):
        # Draw a few tiles at specific locations
        Game.drawTile(3,5) 
        Game.drawTile(10,10) 
        Game.drawTile(7,1) 
        
        # Determine the size of the screen
        Game.drawTile(0, 0) 
        Game.drawTile(25, 0) 
        Game.drawTile(0,9) 
        Game.drawTile(25,9) 
        
        # Experiment with colors
        
        Game.drawTile(1, 1, "red") 
        Game.drawTile(2,2, "purple") 
        Game.drawTile(3,3, "yellow") 
        Game.drawTile(4,4, "blue") 
        Game.drawTile(5,5, "light blue") 
        Game.drawTile(6,6, "green") 

startProgram()