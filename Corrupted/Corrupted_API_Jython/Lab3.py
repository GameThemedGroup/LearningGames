'''
@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@update_Game 
def updateWorld(Game):
    if(Game.pressingRight()):
        Game.drawTile(22,5, "green")
    elif(Game.pressingLeft()):
        Game.drawTile(1,5, "red")
    elif (Game.pressingUp()):
        Game.drawTile(8,8,"yellow")
    elif (Game.pressingDown()):
        Game.drawTile(1,1,"blue")

startProgram()