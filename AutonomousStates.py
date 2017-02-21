#Put all autonomous code here (driving, state machine, etc.)
#The main loop will handle deciding which auto program
#we are running and will call functions that live here.

import wpilib
from wpilib import RobotDrive

from Utilities import UtilityFunctions

class AutoStates():
    gearPlaced = False
    step = ""
    
    def findDatGoal(MyRobot, turnSpeed, defaultDirection = "right"):
        retVal = False
        direction = UtilityFunctions.getDirectionToGoal(MyRobot)
        print("finding dat goal")
        #Turn right if we can't see the goal or it is to our right
        if (direction == MyRobot.ERROR and defaultDirection == "right") or direction == MyRobot.GO_RIGHT:
            MyRobot.leftBackMotor.set(-turnSpeed)
            MyRobot.leftFrontMotor.set(-turnSpeed)
            MyRobot.rightFrontMotor.set(turnSpeed)
            MyRobot.rightBackMotor.set(turnSpeed)
            print("In the first if")
        #Turn left if we can't see the goal or it is to our left
        elif (direction == MyRobot.ERROR and defaultDirection == "left") or direction == MyRobot.GO_LEFT:
            MyRobot.leftBackMotor.set(turnSpeed)
            MyRobot.leftFrontMotor.set(turnSpeed)
            MyRobot.rightFrontMotor.set(-turnSpeed)
            MyRobot.rightBackMotor.set(-turnSpeed)
            print("in the second if")
        #We can see the target and are good to place a gear!
        elif direction == MyRobot.ON_TARGET:
            MyRobot.leftBackMotor.set(0)
            MyRobot.leftFrontMotor.set(0)
            MyRobot.rightFrontMotor.set(0)
            MyRobot.rightBackMotor.set(0)
            print("In the third if")
            retVal = True
        
        return retVal
    
    def left(MyRobot, placeGear = True, useCamera = False):
        retVal = False
        # Hopefully do some math to figure out how to place a gear using a Shaft encoder and a Gyro or Camera
        if placeGear:
            if MyRobot.choose_direction_state == "begin":
                # Use the digital shaft encoder to drive forward enough to get in line with the Lift.
                done = False
                done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to drive
                if done:
                    MyRobot.choose_direction_state = "turn_to_peg"
                    
            elif MyRobot.choose_direction_state == "turn_to_peg":
                # Use the gyro or camera to rotate to face the Lift
                done = False
                # if using a camera, use it to find the goal instead of a gyro
                if useCamera:
                    done = UtilityFunctions.findDatGoal(self, self.autoSlowTurnSpeed, "right")
                else:
                    done = UtilityFunctions.turnNumDegrees(self, 0) #replace 0 with degrees to turn
                if done:
                    MyRobot.choose_direction_state = "score_the_gear"
                    
            elif MyRobot.choose_direction_state == "score_the_gear":
                # Use the digital shaft encoder to drive forward enough to place the gear on the peg
                done = False
                done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to the peg
                if done:
                    retVal = True
            
        # Only Drive Forward to get 5 Points
        else:
            if MyRobot.choose_direction_state == "begin":
                done = False
                done = UtilityFunctions.driveNumInches(self, 72, 1, 0.5) #Drive 6 feet to cross the Base Line
                if done:
                    retVal = True
                
        return retVal
                    
    #def leftWithCam(MyRobot, placeGear = True):
    #    retVal = False
    #    
    #    # Same as normal Left, but instead of using a gyro, use the camera to aim at the Lift
    #    # Hopefully do some math to figure out how to place a gear using a Shaft encoder and a Camera
    #    if placeGear:
    #        if MyRobot.choose_direction_state == "begin":
    #            # Use the digital shaft encoder to drive forward enough to get in line with the Lift.
    #            done = False
    #            done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to drive
    #            if done:
    #                MyRobot.choose_direction_state = "turn_to_peg"
    #                
    #        elif MyRobot.choose_direction_state == "turn_to_peg":
    #            # Use the camera to rotate to face the Lift
    #            done = False
    #            done = UtilityFunctions.findDatGoal(self, self.autoSlowTurnSpeed, "right")
    #            if done:
    #                MyRobot.choose_direction_state = "score_the_gear"
    #                
    #        elif MyRobot.choose_direction_state == "score_the_gear":
    #            # Use the digital shaft encoder to drive forward enough to place the gear on the peg
    #            done = False
    #            done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to the peg
    #            if done:
    #                retVal = True
    #        
    #    # Only Drive Forward to get 5 Points
    #    else:
    #        if MyRobot.choose_direction_state == "begin":
    #            done = False
    #            done = UtilityFunctions.driveNumInches(self, 72, 1, 0.5) #Drive 6 feet to cross the Base Line
    #            if done:
    #                retVal = True
    #            
    #    return retVal


    """
    placeGear is a boolean, crossOn is a string (left, right, leftFromPeg, rightFromPeg)
    """
    #def middle(MyRobot, placeGear, crossOn):
    #    if step == "":
    #        if placeGear:
    #            step = "lineUp"
    #        elif crossOn != "":
    #            step = crossOn
    #
    #    if step == "lineUp":
    #        #Spin robot to line up to goal
    #    if step == "go":
    #        done = False
    #        done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to the peg
    #        if done:
    #            if crossOn != "":
    #                step = crossOn
    #    if step == "leftFromPeg"
    #        done = False
    #        done = UtilityFunctions.driveNumInches(self, 0, -1, 0.5) #replace 0 with the distance to back up
    #        if done:
    #            turn = False
    #            turn = UtilityFunctions.turnNumDegrees(self, 0) #replace 0 with degrees to turn
    #            if turn:
    #                UtilityFunctions.driveForTime(self, 0.5, 0) #replce 0 with amount of time to drive
    #    if step == "rightFromPeg"
    #        done= False
    #        done = UtilityFunctions.driveNumInches(self, 0, -1, 0.5) #replace 0 with the distance to back up
    #        if done:
    #            turn = False
    #            turn = UtilityFunctions.turnNumDegrees(self, 0) #replace 0 with degrees to turn
    #            if turn:
    #                UtilityFunctions.driveForTime(self, 0.5, 0) #replce 0 with amount of time to drive
    #        
    #def right(MyRobot, placeGear, shootBalls):
    #
    #    Myrobot.initialTime = UtilityFunctions.getAnInitialTimeStamp(Myrobot, Myrobot.initialTime, Myrobot.autoSafeToGetTime)
    #
    #    if step == "":
    #        if shootBalls:
    #            step = "shoot"
    #        elif placeGear:
    #            step = "lineUp"
    #            
    #    if step == "shoot"
    #        shooterMotors = []
    #        shooterMotors.append(Myrobot.shooterMotorOne, -0.8)
    #        shooterMotors.append(Myrobot.shooterMoterTwo, -0.8)
    #        reved = UtilityFunctions.driveMotorsNumSeconds(self, shooterMotors, 2, Myrobot.initialTime)
    #        if reved:
    #            done = False
    #            done = UtilityFunctions.driveMotorsNumSeconds(self, shooterMotors, 5, Myrobot.initialTime)
    #            UtilityFunctions.driveNumSeconds(self, Myrobot.hopperAgitatorMotor, 1, 0.5, 1, Myrobot.initialTime)
    #            if done and placeGear:
    #                step = "lineUp"
    #            
    #    if step == "lineUp":
    #        #Spin robot to line up to goal
    #        
    #    if step == "go":
    #        #driveNumSeconds to the peg
    #        #At the end here set step = to 'leftFromPeg' or 'rightFromPeg'
    #    if step == "leftFromPeg"
    #        #cross the line on the left from the peg
    #    if step == "rightFromPeg"
    #        #cross the line on the right from the peg
    #    if step == "left":
    #        #cross the line on the left
    #    if step == "right"
    #
        #cross the line on the right
