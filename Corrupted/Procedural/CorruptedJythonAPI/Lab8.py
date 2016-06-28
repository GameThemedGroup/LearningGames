'''
Created on May 1, 2016

@author: Christian Gebhart
'''
from Corrupted_API_Support import *

@build_Game
def buildGame(Game):
 
    for currentNum in range(8, 26):
     
        Game.drawColumn(currentNum)
     
 

 
 
@draw_Column
def drawColumn(Game, x):
    
    for i in range(0, 10):
     
        Game.drawTile(x, i, Game.getRandomColor())   
             
 

startProgram()