'''
Created on May 1, 2016

@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@build_Game
def buildGame(Game):
  
    for currentNum in range(8, 24):
        Game.drawColumn(currentNum) 
      
     
    Game.drawLaser() 
    Game.drawCounter() 
    Game.setCounterValue(30)  # Set number of tiles you need to match to win the game.
  

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
        if (matches >= Game.tilesInMatchSet):
          
            Game.deleteMatchingTiles() 
          
        Game.setNewLaserColor() 
      
     
    Game.updateCounter() 
  

@check_Game_Won
def checkGameWon(Game):
  
    if(Game.tilesNeededToWin <= 0):
      
        Game.winGame()
              
  

startProgram()