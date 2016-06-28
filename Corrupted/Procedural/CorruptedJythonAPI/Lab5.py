'''
@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@build_Game
def buildGame(Game):
    Game.drawTile(0, 0, "yellow") 
    Game.drawTile(4, 4, "blue") 
    Game.drawTile(4, 5, "blue") 
    Game.drawTile(5, 4, "blue") 
    Game.drawTile(5, 5, "blue") 
    
    Game.drawTile(11, 7, "green") 
    Game.drawTile(11, 8, "green") 
    Game.drawTile(10, 7, "green") 
    Game.drawTile(10, 8, "green") 
    
    Game.drawTile(11, 1, "red") 
    Game.drawTile(11, 2, "red") 
    Game.drawTile(11, 3, "red") 
    Game.drawTile(12, 1, "red") 
    Game.drawTile(12, 2, "red") 
    Game.drawTile(12, 3, "red") 
    
    Game.drawTile(20, 8, "light blue") 
    Game.drawTile(20, 9, "light blue") 
    Game.drawTile(21, 8, "light blue") 
    Game.drawTile(21, 9, "light blue") 
    Game.drawTile(22, 8, "light blue") 
    Game.drawTile(22, 9, "light blue") 
    
    Game.drawTile(18, 3, "purple") 
    Game.drawTile(18, 4, "purple") 
    Game.drawTile(17, 3, "purple") 
    Game.drawTile(17, 4, "purple") 
    
    print("Your mission: To find the TREASURE!") 
    print("First you must travel AROUND Pink-a-Dink island.") 
    print("Then you must travel THROUGH the orange mountains.") 
    print("Next go north along the right side of the green jungle.") 
    print("Be careful not to go in the jungle or the wild unicorns will eat you!") 
    print("Turn left and circle around the Blue-Bottom Sea.") 
    print("Then find your way to the light blue clouds where the treasure is located!") 
    print("Be careful not to stray from these instructions.") 
    print("If you do, the treasure will be lost to you forever!") 
    

@update_Game 
def updateGame(Game):
    if(Game.pressingRight()):
        Game.x = Game.x + 1 
        Game.drawTile(Game.x, Game.y, "yellow") 
    elif(Game.pressingLeft()):
        Game.x = Game.x - 1 
        Game.drawTile(Game.x, Game.y, "yellow") 
    elif(Game.pressingUp()):
        Game.y = Game.y + 1 
        Game.drawTile(Game.x, Game.y, "yellow") 
    elif(Game.pressingDown()):
        Game.y = Game.y - 1 
        Game.drawTile(Game.x, Game.y, "yellow") 

startProgram()