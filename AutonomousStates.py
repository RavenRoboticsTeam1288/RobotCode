#Put all autonomous code here (driving, state machine, etc.)
#The main loop will handle deciding which auto program
#we are running and will call functions that live here.

import wpilib
from wpilib import RobotDrive

from Utilities import UtilityFunctions

class AutoStates():
    gearPlaced = False
    step = ""
    
    def left(MyRobot, placeGear):
        if placeGear:
            #navigate to the gear peg
        else:
            #drive straight

    """
    placeGear is a boolean, crossOn is a string (left, right, leftFromPeg, rightFromPeg)
    """
    def middle(MyRobot, placeGear, crossOn):
        if step == "":
            if placeGear:
                step = "lineUp"
            elif crossOn != "":
                step = crossOn

        if step == "lineUp":
            #Spin robot to line up to goal
        if step == "go":
            done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to the peg
            if done:
                if crossOn != "":
                    step = crossOn
        if step == "leftFromPeg"
            done = UtilityFunctions.driveNumInches(self, 0, -1, 0.5) #replace 0 with the distance to back up
            if done:
                turn = UtilityFunctions.turnNumDegrees(self, 0) #replace 0 with degrees to turn
                if turn:
                    drive = UtilityFunctions.driveForTime(self, 0.5, 0) #replce 0 with amount of time to drive
        if step == "rightFromPeg"
                        done = UtilityFunctions.driveNumInches(self, 0, -1, 0.5) #replace 0 with the distance to back up
            if done:
                turn = UtilityFunctions.turnNumDegrees(self, 0) #replace 0 with degrees to turn
                if turn:
                    drive = UtilityFunctions.driveForTime(self, 0.5, 0) #replce 0 with amount of time to drive
            
    def right(MyRobot, placeGear, shootBalls):
        if step == "":
            if shootBalls:
                step = "shoot"
            else:
                step = "lineUp"
                
        if step == "shoot"
            #Shoot all of balls
        if step == "lineUp":
            #Spin robot to line up to goal
        if step == "go":
            #driveNumSeconds to the peg
            #At the end here set step = to 'leftFromPeg' or 'rightFromPeg'
        if step == "leftFromPeg"
            #cross the line on the left from the peg
        if step == "rightFromPeg"
            #cross the line on the right from the peg
        if step == "left":
            #cross the line on the left
        if step == "right"
            #cross the line on the right
