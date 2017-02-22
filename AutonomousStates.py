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
    def middle(MyRobot, placeGear, crossOn):
        retVal = False
        # Hopefully do some math to figure out how to place a gear using a Shaft encoder and a Gyro or Camera
        if placeGear:
            if MyRobot.choose_direction_state == "begin":
                # Use the digital shaft encoder to drive forward enough to get in line with the Lift.
                done = False
                done = UtilityFunctions.driveNumInches(self, 0, 1, 0.5) #replace 0 with the distance to drive
                if done:
                    MyRobot.choose_direction_state = "wait_for_pilot"
                    
            elif MyRobot.choose_direction_state == "wait_for_pilot":
                done = False
                done = UtilityFunctions.driveForTime(MyRobot, 0, 5)
                if done:
                    MyRobot.choose_direction_state = "backup"
                    
            elif MyRobot.choose_direction_state == "backup":
                # Backup off the lift... or don't
                done = False
                if crossOn == "left" or crossOn == "right":
                    done = UtilityFunctions.driveForTime
                else:
                    
                if done:
                    MyRobot.choose_direction_state = ""
                    
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
            
    def right(MyRobot, placeGear = True, useCamera = False, shoot = False):
        retVal = False
        # Hopefully do some math to figure out how to place a gear using a Shaft encoder and a Gyro or Camera
        if shoot:
            if MyRobot.choose_direction_state == "begin" or MyRobot.choose_direction_state == "prepare_to_shoot":
                done = False
                MyRobot.choose_direction_state = "prepare_to_shoot"
                MyRobot.shooterMotorOne.set(MyRobot.shooterSpeed)
                MyRobot.shooterMotorTwo.set(MyRobot.shooterSpeed)
                done = UtilityFunctions.driveForTime(MyRobot, 0, 0.5)
                if done:
                    MyRobot.choose_direction_state = "shoot"
                    
            elif MyRobot.choose_direction_state == "shoot":
                done = False
                MyRobot.shooterMotorOne.set(MyRobot.shooterSpeed)
                MyRobot.shooterMotorTwo.set(MyRobot.shooterSpeed)
                MyRobot.shooterServo.setAngle(90)
                MyRobot.hopperAgitatorMotor(0.8)
                done = UtilityFunctions.driveForTime(MyRobot, 0, 4)
                if done:
                    MyRobot.shooterMotorOne.set(0)
                    MyRobot.shooterMotorTwo.set(0)
                    MyRobot.shooterServo.setAngle(0)
                    MyRobot.hopperAgitatorMotor(0)
                    MyRobot.choose_direction_state = "gear_or_cross"
            
        if placeGear:
            if MyRobot.choose_direction_state == "begin" or MyRobot.choose_direction_state == "gear_or_cross":
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
                    done = UtilityFunctions.findDatGoal(self, self.autoSlowTurnSpeed, "left")
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
            if MyRobot.choose_direction_state == "begin" or MyRobot.choose_direction_state == "gear_or_cross":
                done = False
                done = UtilityFunctions.driveNumInches(self, 72, 1, 0.5) #Drive 6 feet to cross the Base Line
                if done:
                    retVal = True
                
        return retVal
