'''
Created on May 1, 2016

@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@build_Game
def buildGame(Game):

    for currentNum in range(8,26):
    
        Game.drawColumn(currentNum)
    
    Game.drawLaser()  
    Game.drawCounter() 
    Game.setTilesInMatchSet(3)
    Game.startTimerForTiles(200)

@update_Game 
def updateGame(Game):

    Game.checkGameWon()
   
    if(Game.pressingUp()):
    
        Game.moveLaserUp()
    
    elif(Game.pressingDown()):
    
        Game.moveLaserDown()
    
    elif(Game.pressingRight()):
    
        Game.drawNewTileFromLaser()
        matches = Game.getNumberOfMatchingTiles()
        if(matches >= Game.tilesInMatchSet):
        
            Game.deleteMatchingTiles()
        
        Game.setNewLaserColor()
    
    
    if(Game.isTimeToShift() == True):
    
        Game.shiftTilesLeft()
    
   
    
    Game.updateCounter()        
    Game.deleteMissedTiles()
    

startProgram()