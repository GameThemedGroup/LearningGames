'''
@author: Christian Gebhart
'''
from Corrupted_API_Support import *


    
@build_Game
def buildGame(Game):
    Game.drawLaser() 
    
    # How many tiles need to be matched before they will delete?
    Game.setTilesInMatchSet(3) 
    
    #Build a board!  At least one column
    Game.drawTile(7, 0, "light blue") 
    Game.drawTile(7, 1, "red") 
    Game.drawTile(7, 2, "green") 
    Game.drawTile(7, 3, "yellow") 
    Game.drawTile(7, 4, "blue") 
    Game.drawTile(7, 5, "light blue") 
    Game.drawTile(7, 6, "green") 
    Game.drawTile(7, 7, "purble") 
    Game.drawTile(7, 8, "blue") 
    Game.drawTile(7, 9, "red") 
    
    Game.drawTile(8, 0, "green") 
    Game.drawTile(8, 1, "red") 
    Game.drawTile(8, 2, "green") 
    Game.drawTile(8, 3, "blue") 
    Game.drawTile(8, 4, "yellow") 
    Game.drawTile(8, 5, "blue") 
    Game.drawTile(8, 6, "purple") 
    Game.drawTile(8, 7, "red") 
    Game.drawTile(8, 8, "green") 
    Game.drawTile(8, 9, "blue") 
    
    Game.drawTile(9, 0, "blue") 
    Game.drawTile(9, 1, "green") 
    Game.drawTile(9, 2, "red") 
    Game.drawTile(9, 3, "light blue") 
    Game.drawTile(9, 4, "green") 
    Game.drawTile(9, 5, "yellow") 
    Game.drawTile(9, 6, "purple") 
    Game.drawTile(9, 7, "light blue") 
    Game.drawTile(9, 8, "light blue") 
    Game.drawTile(9, 9, "green") 
    
    Game.drawTile(10, 0, "red") 
    Game.drawTile(10, 1, "blue") 
    Game.drawTile(10, 2, "red") 
    Game.drawTile(10, 3, "light blue") 
    Game.drawTile(10, 4, "yellow") 
    Game.drawTile(10, 5, "blue") 
    Game.drawTile(10, 6, "green") 
    Game.drawTile(10, 7, "yellow") 
    Game.drawTile(10, 8, "red") 
    Game.drawTile(10, 9, "blue") 

@update_Game 
def updateGame(Game):
    #Handle player input
    if(Game.pressingUp()):
        Game.moveLaserUp() 
        
    elif(Game.pressingDown()):
        Game.moveLaserDown() 
        
    elif(Game.pressingRight()):
        Game.drawNewTileFromLaser() 
        Game.matches = Game.getNumberOfMatchingTiles() 
        
        if (Game.matches >= Game.tilesInMatchSet):
            Game.deleteMatchingTiles() 
        Game.setNewLaserColor() 

startProgram()