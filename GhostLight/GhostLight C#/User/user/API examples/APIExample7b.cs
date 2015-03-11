﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using GhostFinder.Interface;
using GhostFinder.GhostEngine;
using CustomWindower.Driver;
using System.Windows.Forms;

namespace user {
    /**
     * Demonstrates how to use the primitiveGrin instead of the objectGrid using the 2D api
     * @author Michael Letter
     */
    public class APIExample7b : GhostFinderInterface{

    
        bool incrementScoreConfirm = false;
        bool incrementRevealConfirm = false;

	    public override void initialize() {
		
		    //Will ensure any changes to the primitiveState take precedence over the state of the
		    //objectGrid
		    gameState.givePrimitiveGridPriority();
		
		    //inititializing primitiveGrid
		    //IDs
		    //primitiveGrid uses an ID system to dictate enemy existence and position
		    //this is implemented as an int[row][collumn] where each element containing a unique positive integer denotes an enemy position
		    //all other elements are ignored and treated as empy positions
		
		    //initilializing ID array
		    int[][] idArray = new int[5][];
		    for(int loopRow = 0; loopRow < idArray.Length; loopRow++){
			    idArray[loopRow] = new int[5];
			    for(int loopCollumn = 0; loopCollumn < idArray[loopRow].Length; loopCollumn++){
				    idArray[loopRow][loopCollumn] = 0; //negative numbers indicate no Enemy at this position
			    }
		    }
		    primitiveGrid.setIDArray(idArray);
		    //Adding an enemy
		    idArray[1][3] = 2; //any integer that is greater than or equal to zero and unique in the set will be made an enemy
		    //At this point health type and score are not defined. As a result, defualt values will be used 
		    //if they are not defined by the end of this update
		 
	    }

	    public override void update() {
		    //Add and move Enemies
		    if(keyboard.isKeyDown(Keys.Enter)){
			    int[][] idArray = primitiveGrid.getIDArray();
			    //move enemy
			    int temp = idArray[1][0];
			    idArray[1][0] = idArray[1][3];
			    idArray[1][3] = temp;
			    //Note Becuase the values of the health score and reveal arrays are unchanged,
			    //the state of the enemy at [0][0] will swap with the state of the enemy at [0][3]
			
			    //add enemy
			    idArray[1][3] = 1;
		    }
		    //setting Health
		    if(keyboard.isKeyDown(Keys.H)){
			    //heath is dictated by an array of floats 
			    float[][] healthArray = primitiveGrid.getHealthArray();
			    //each elemenent between 0 and 1 represents the precent health of the enemy at that location
			    //a 0 represents 0 health and a 1 represents 100% health
			    //a negative value means there is no information on this enemies health. 
			    //if an enemy does exist at this location then defualt values are used
			    healthArray[1][3] = 0.5f;
		    }
		    //setting Score
		    if(keyboard.isKeyDown(Keys.S)){
                if(!incrementScoreConfirm){
			        //Score is dictated by an array of ints
			        int[][] scoreArray = primitiveGrid.getScoreArray();
			        //each element represents the score of the enemy at that location
			        scoreArray[1][3]++;
                    incrementScoreConfirm = true;
                }
		    }
            else{
                incrementScoreConfirm = false;
            }
		    //Setting Reveal
		    if(keyboard.isKeyDown(Keys.R)){
                if(!incrementRevealConfirm){
			        //reveal status is dictated by an array of booleans
			        bool[][] revealArray = primitiveGrid.getRevealedArray();
			        //if an element is True then the enemy at that location will be made revealed
			        //if an element is false then the enemy at that location will be made hidden
			        revealArray[1][3] = !revealArray[1][3];
                    incrementRevealConfirm = true;
                }
		    }
            else{
                incrementRevealConfirm = false;
            }
		    //Setting Type
		    if(keyboard.isKeyDown(Keys.T)){
			    //type is dictated by an array of Enums of InteractableObject.ObjectType
			    int[][] typeArray = primitiveGrid.getTypeArray();
			    //each int element represents the ordinal value of the ObjectType of the enemy at that location
			    //an element that is not represented by an ObjectType.ordinal indicates that there is no information on the enemy at that location
			    //if an enemy does exist at such a location, then the enemy will be made ObjectType PUMPKIN
			    typeArray[1][3] = (int)InteractableObject.ObjectType.SPIDER;
		    }
	    }
	    public override void end() {
			
	    }
    }
}