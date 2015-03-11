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
 * Object Grid how to initialize and navigate
 * IntractableObjects How to Add them, Remove them and change there state through the objectGrid
 * Uses the 1D API
 * @author Michael Letter
 */
namespace user{
    public class APIExample3a : GhostFinderInterface {

	    public override void initialize() {
		
		    //IntractableObject
		    //used to make pumpkins Ghosts etc...
		    InteractableObject newby = new InteractableObject();
		    //set State
		    newby.setObjectType(InteractableObject.ObjectType.FRANKENSTEIN, true);	//Setting Type(Ghost, Zombie, etc...)
		    newby.setMaxHealth(5);								//Setting Max Health 
		    newby.setCurrentHealth(2);							//Setting current Health
		    newby.setScore(9001); 								//Setting the number of points the enemy is worth
		    newby.setRevealStatus(true); 						//Making the Object Revealed
		
		
		    //objectGrid
		    //used to gain access to the Enemies that will appear on screen
		
		    //Creating an array to store the new IntractableObject
		    //When added to objectGrid the indices of this array will indicates its column position on the screen
		    //with the zeroth index representing the left most column and following indexes representing columns farther and farther right
		    //right screen edge: 0 -> 1 -> 2 -> ...      left screen edge
		    InteractableObject[] iOset = new InteractableObject[7];
		    iOset[3] = newby;
		
		    //setting the number of Rows that will exist on screen These Rows can be accessed or set via there index
		    //Although at this point all the Rows are null becuase they have not been set yet
		    //the Row with the least index will represent the Row at the Top of the screen with following Rows appearing further and further Down
		    // 0
		    // |
		    // V
		    // 1
		    // |
		    // ...
		    objectGrid.setNumberOfRows(5);
		    //setting Row iOset to be row 2
		    objectGrid.setObjectGrid(iOset, 2);
	    }
	    public override void update() {
		    //Removing an Enemy 2 Ways
		
		    //Set Health to zero
		    //THis will result in the enemy being removed from the set and destroyed between this update and the next
		    //you must leave the enemy in the array. if you want to remove the enemy from the array use the other method
		    if(base.keyboard.isKeyDown(Keys.D1)){
			    InteractableObject[] iOset = objectGrid.getObjectRow(2);
                if(iOset[3] != null){
			        iOset[3].setCurrentHealth(0);
                }
		    }
		    //OR
		    //Call .Destroy() and remove from array
		    //Note you must remove the enemy from the array if you do not the enemy will simply revert to defualt state
            if (base.keyboard.isKeyDown(Keys.D2)) {
			    InteractableObject[] iOset = objectGrid.getObjectRow(2);
                if(iOset[3] != null){
			        iOset[3].destroy();
			        iOset[3] = null;
                }
		    }
		    //Whatever you do do not simply remove the enemy from the array or bad things will happen
	    }
	    public override void end() {
		    // TODO Auto-generated method stub
		
	    }
    }
}
