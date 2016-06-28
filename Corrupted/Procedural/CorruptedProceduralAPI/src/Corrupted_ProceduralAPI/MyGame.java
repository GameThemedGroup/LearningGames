package Corrupted_ProceduralAPI;
import Corrupted_ProceduralAPI.*;

/**
 * Write a description of class MyGame here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyGame extends CorruptedProceduralAPI
{
    public void buildGame()
    {
      drawLaser();
      drawBoard();  
      drawCounter();  
      setTilesInMatchSet(3);
      startTimerForTiles();
    }
    
    public void updateGame()
    {
        
       checkGameWon();
       
        if(pressingUp())
        {
            moveLaserUp();
        }
        else if(pressingDown())
        {
            moveLaserDown();
        }
        else if (pressingRight())
        {
            drawNewTileFromLaser();
            int matches = getNumberOfMatchingTiles();
            if(matches >= tilesInMatchSet)
            {
                deleteMatchingTiles();
            }
            setNewLaserColor();
        }
        
        if(isTimeToShift() == true)
        {
             shiftTilesLeft();
        }
       
        
        updateCounter();        
        deleteMissedTiles();
        
    }
}
   
   
