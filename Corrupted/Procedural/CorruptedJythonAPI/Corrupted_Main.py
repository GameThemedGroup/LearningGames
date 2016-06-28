from Corrupted_API_Support import *

"""@gameBuild
def build_Game(corruptedMaker):
    
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
    corruptedMaker.drawTile()
        
    #Player tile start
    corruptedMaker.drawTile(0,0, "yellow");
    
    # Build the maze board!
    corruptedMaker.drawTile(1,1, "Blue")
    corruptedMaker.drawTile(2, 1, "blue")
    corruptedMaker.drawTile(3, 1, "blue")
    corruptedMaker.drawTile(4, 1, "blue")
    corruptedMaker.drawTile(5, 1, "blue")
    corruptedMaker.drawTile(6, 1, "blue")
    corruptedMaker.drawTile(7, 1, "blue")
    corruptedMaker.drawTile(8, 1, "blue")
    corruptedMaker.drawTile(18, 1, "blue")
    corruptedMaker.drawTile(19, 1, "blue")
    corruptedMaker.drawTile(20, 1, "blue")
    
    corruptedMaker.drawTile(1, 2, "blue")
    corruptedMaker.drawTile(2, 2, "blue")
    corruptedMaker.drawTile(3, 2, "blue")
    corruptedMaker.drawTile(4, 2, "blue")
    corruptedMaker.drawTile(5, 2, "blue")
    corruptedMaker.drawTile(6, 2, "blue")
    corruptedMaker.drawTile(7, 2, "blue")
    corruptedMaker.drawTile(8, 2, "blue")
    corruptedMaker.drawTile(10, 2, "blue")
    corruptedMaker.drawTile(11, 2, "blue")
    corruptedMaker.drawTile(12, 2, "blue")
    corruptedMaker.drawTile(13, 2, "blue")
    corruptedMaker.drawTile(14, 2, "blue")
    corruptedMaker.drawTile(15, 2, "blue")
    corruptedMaker.drawTile(16, 2, "blue")
            
    corruptedMaker.drawTile(5, 3, "blue")
    corruptedMaker.drawTile(8, 3, "blue")
    corruptedMaker.drawTile(10, 3, "blue")
    corruptedMaker.drawTile(11, 3, "blue")
    corruptedMaker.drawTile(12, 3, "blue")
    corruptedMaker.drawTile(13, 3, "blue")
    corruptedMaker.drawTile(14, 3, "blue")
    corruptedMaker.drawTile(15, 3, "blue")
    corruptedMaker.drawTile(16, 3, "blue")
    corruptedMaker.drawTile(18, 3, "blue")
    corruptedMaker.drawTile(19, 3, "blue")
    corruptedMaker.drawTile(20, 3, "blue")

    corruptedMaker.drawTile(0, 4, "blue")
    corruptedMaker.drawTile(2, 4, "blue")
    corruptedMaker.drawTile(3, 4, "blue")
    corruptedMaker.drawTile(5, 4, "blue")
    corruptedMaker.drawTile(6, 4, "blue")
    corruptedMaker.drawTile(8, 4, "blue")
    corruptedMaker.drawTile(10, 4, "blue")
    corruptedMaker.drawTile(11, 4, "blue")
    corruptedMaker.drawTile(12, 4, "blue")
    corruptedMaker.drawTile(13, 4, "blue")
    corruptedMaker.drawTile(14, 4, "blue")
    corruptedMaker.drawTile(15, 4, "blue")
    corruptedMaker.drawTile(16, 4, "blue")
    corruptedMaker.drawTile(18, 4, "blue")
    corruptedMaker.drawTile(19, 4, "blue")
    corruptedMaker.drawTile(20, 4, "blue")
    
    corruptedMaker.drawTile(0, 5, "blue")
    corruptedMaker.drawTile(2, 5, "blue")
    corruptedMaker.drawTile(3, 5, "blue")
    corruptedMaker.drawTile(5, 5, "blue")
    corruptedMaker.drawTile(6, 5, "blue")
    corruptedMaker.drawTile(8, 5, "blue")
    corruptedMaker.drawTile(16, 5, "blue")
    corruptedMaker.drawTile(18, 5, "blue")
    corruptedMaker.drawTile(19, 5, "blue")
    corruptedMaker.drawTile(20, 5, "blue")
    
    corruptedMaker.drawTile(0, 6, "blue")
    corruptedMaker.drawTile(5, 6, "blue")
    corruptedMaker.drawTile(6, 6, "blue")
    corruptedMaker.drawTile(8, 6, "blue")
    corruptedMaker.drawTile(9, 6, "blue")
    corruptedMaker.drawTile(10, 6, "blue")
    corruptedMaker.drawTile(11, 6, "blue")
    corruptedMaker.drawTile(12, 6, "blue")
    corruptedMaker.drawTile(13, 6, "blue")
    corruptedMaker.drawTile(14, 6, "blue")
    corruptedMaker.drawTile(16, 6, "blue")
    corruptedMaker.drawTile(18, 6, "blue")
    corruptedMaker.drawTile(19, 6, "blue")
    corruptedMaker.drawTile(20, 6, "blue")
    
    corruptedMaker.drawTile(0, 7, "blue")
    corruptedMaker.drawTile(1, 7, "blue")
    corruptedMaker.drawTile(2, 7, "blue")
    corruptedMaker.drawTile(3, 7, "blue")
    corruptedMaker.drawTile(5, 7, "blue")
    corruptedMaker.drawTile(6, 7, "blue")
    corruptedMaker.drawTile(8, 7, "blue")
    corruptedMaker.drawTile(9, 7, "blue")
    corruptedMaker.drawTile(10, 7, "blue")
    corruptedMaker.drawTile(11, 7, "blue")
    corruptedMaker.drawTile(12, 7, "blue")
    corruptedMaker.drawTile(13, 7, "blue")
    corruptedMaker.drawTile(14, 7, "blue")
    corruptedMaker.drawTile(16, 7, "blue")
    corruptedMaker.drawTile(18, 7, "blue")
    corruptedMaker.drawTile(19, 7, "blue")
    corruptedMaker.drawTile(20, 7, "blue")
   
    corruptedMaker.drawTile(0, 8, "blue")
    corruptedMaker.drawTile(1, 8, "blue")
    corruptedMaker.drawTile(2, 8, "blue")
    corruptedMaker.drawTile(3, 8, "blue")
    corruptedMaker.drawTile(16, 8, "blue")
    corruptedMaker.drawTile(18, 8, "blue")
    corruptedMaker.drawTile(19, 8, "blue")
    corruptedMaker.drawTile(20, 8, "blue")
    
    corruptedMaker.drawTile(0, 9, "blue")
    corruptedMaker.drawTile(1, 9, "blue")
    corruptedMaker.drawTile(2, 9, "blue")
    corruptedMaker.drawTile(3, 9, "blue")
    corruptedMaker.drawTile(5, 9, "blue")
    corruptedMaker.drawTile(6, 9, "blue")
    corruptedMaker.drawTile(7, 9, "blue")
    corruptedMaker.drawTile(8, 9, "blue")
    corruptedMaker.drawTile(9, 9, "blue")
    corruptedMaker.drawTile(10, 9, "blue")
    corruptedMaker.drawTile(11, 9, "blue")
    corruptedMaker.drawTile(12, 9, "blue")
    corruptedMaker.drawTile(13, 9, "blue")
    corruptedMaker.drawTile(14, 9, "blue")
    corruptedMaker.drawTile(15, 9, "blue")
    corruptedMaker.drawTile(16, 9, "blue")"""



@gameUpdate 
def update_Game(corruptedMaker):
    
    if(corruptedMaker.pressingRight()):
        corruptedMaker.x = corruptedMaker.x + 1;
        corruptedMaker.drawTile(corruptedMaker.x, corruptedMaker.y, "yellow")
    elif(corruptedMaker.pressingLeft()):
        corruptedMaker.x = corruptedMaker.x - 1;
        corruptedMaker.drawTile(corruptedMaker.x, corruptedMaker.y, "yellow")
    elif(corruptedMaker.pressingUp()):
        corruptedMaker.y = corruptedMaker.y + 1;
        corruptedMaker.drawTile(corruptedMaker.x, corruptedMaker.y, "yellow")
    elif(corruptedMaker.pressingDown()):
        corruptedMaker.y = corruptedMaker.y - 1;
        corruptedMaker.drawTile(corruptedMaker.x, corruptedMaker.y, "yellow")



startProgram()