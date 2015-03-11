﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using GhostFinder.Interface;
using GhostFinder.GhostEngine;
using CustomWindower.Driver;
using System.Windows.Forms;


/**
 * Moving Enemies, updating turn, and setAnimationTime
 * As well as setting Default InteractableObject State
 * Uses the 2D API
 * @author Michael Letter
 */
public class APIExample4a : GhostFinderInterface { 

	public override void initialize() {
		//Setting Default Status
		//This allows you to set the health and score that enemies of a given objectType start with
		//All enemies should start with 4 health
		InteractableObject.setDefualtHealth(4);
		//Uhhh... Except Angry Ghost they should only start with 2 health
		InteractableObject.setDefualtHealth(2, InteractableObject.ObjectType.ANGRY);
		//All Pumpkins should start worth 13 points
		InteractableObject.setDefualtMaxScore(13, InteractableObject.ObjectType.PUMPKIN);
		InteractableObject.setDefualtMinScore(13, InteractableObject.ObjectType.PUMPKIN);
		//All Ghosts should start worth between 10 and 50 points with intervals of 10 points
		InteractableObject.setDefualtMaxScore(50, InteractableObject.ObjectType.GHOST);
		InteractableObject.setDefualtMinScore(10, InteractableObject.ObjectType.GHOST);
		InteractableObject.setDefualtScoreInterval(10, InteractableObject.ObjectType.GHOST);
		
		//The number updates that will be missed when animation occures
		//increasing this number makes animation go longer
		//Decreasing this number makes animations go slower
		//setting as 0 will make it so they don't happen at all
		gameState.setAnimationTime(20);
		
		//See APIExample3a for an explanation of the code following in this function
		InteractableObject[] iOset = new InteractableObject[5];
		
		iOset[0] = new InteractableObject();
		iOset[4] = new InteractableObject();
		iOset[0].setObjectType(InteractableObject.ObjectType.PUMPKIN, true);
		iOset[0].setRevealStatus(true);
		iOset[4].setObjectType(InteractableObject.ObjectType.GHOST, true);
		iOset[4].setRevealStatus(true);
		
		objectGrid.setNumberOfRows(5);
		objectGrid.setObjectGrid(iOset, 2);
		
	}
	public override void update() {
		//to Move an Enemy simply move it to the array position you want it to reside at
		if(keyboard.isKeyDown(Keys.Enter)){
			 InteractableObject[] iOset = objectGrid.getObjectRow(2);
			 InteractableObject temp = iOset[0];
			 iOset[0] = iOset[4];
			 iOset[4] = temp;
		}
		//Updating turn
		//Some enemies evolve over time and they are allowed to do this at the passing of a turn
		//This is done by marking this update as the last update in a turn
		//Note this evolution will not occur until the conclusion of this update and the
		//effects will not be visible until the next update
        if (keyboard.isKeyDown(Keys.Space)) {
			gameState.markTurnEnd(true);
		}
		
	}
	public override void end() {
		// TODO Auto-generated method stub
		
	}

}
