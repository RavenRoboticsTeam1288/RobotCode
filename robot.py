#!/usr/bin/env python3

#library includes
import wpilib
from wpilib import RobotDrive

from networktables import NetworkTables

#User Includes
from Utilities import UtilityFunctions
from AutonomousStates import AutoStates

#Raven Robotics 2018 PowerUp
#This robot uses Tank Drive
class MyRobot(wpilib.IterativeRobot):

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''

        self.goalPos = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        self.scalePos = ''
        self.switchPos = ''

        if self.sd.containsKey('STARTPOS'):
            self.startPos = self.sd.getValue('STARTPOS')

        if self.sd.containsKey('TARGET'):
            self.autoTarget = self.sd.getValue('TARGET')

        if len(self.goalPos) == 3:
            if self.goalPos[0] == 'L':
                self.switchPos = 'left'
            elif self.goalPos[0] == 'R':
                self.switchPos = 'right'

            if self.goalPos[1] == 'L':
                self.scalePos = 'left'
            elif self.goalPos[1] == 'R':
                self.scalePos = 'right'
        
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.sd = NetworkTables.getTable('SmartDashboard')

        self.goalPos = ''
        
        #Encoder
        self.encoder = wpilib.Counter(1)

        # Joysticks
        self.stick1 = wpilib.Joystick(2)#left
        self.stick2 = wpilib.Joystick(1)#right
        self.game_pad = wpilib.Joystick(3)
        
        # Drive Train Motors
        self.leftFrontMotor = wpilib.Talon(0) #front left 
        self.leftBackMotor = wpilib.VictorSP(1) #back left 
        self.rightFrontMotor = wpilib.VictorSP(2) #front right 
        self.rightBackMotor = wpilib.Talon(3) #back right
        
        # Shooter Motors
        #Front is front of shooter
        self.shooterLeftFront = wpilib.Talon(4)
        self.shooterLeftBack = wpilib.Talon(5)
        self.shooterRightFront = wpilib.Talon(6)
        self.shooterRightBack = wpilib.Talon(7)
        
        # Intake Arm Motors
        '''TO BE EDITED'''
        self.intakeMotorRight = wpilib.Talon(8)
        self.intakeMotorLeft = wpilib.Talon(9)

        #Climbing Solenoids
        #Second Argument is forward channel; Third Argument is backward channel
        self.climberLeft = wpilib.DoubleSolenoid(0, 0, 1)
        self.climberRight = wpilib.DoubleSolenoid(0, 2, 3)

        #Shooter Pistons
        #Second Argument is forward channel; Third Argument is backward channel
        self.shooterElev = wpilib.DoubleSolenoid(0, 4, 5)
        self.shooterDoor = wpilib.DoubleSolenoid(0, 6, 7)
        
        #robot drive
        self.robotDrive = wpilib.RobotDrive(self.leftFrontMotor,
                                            self.leftBackMotor,
                                            self.rightFrontMotor,
                                            self.rightBackMotor)
                                         
        
        
        ## invert the front motors
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontRight, True)
        #
        ## you may need to change or remove this to match your robot
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kRearLeft, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True) 
        
        # Sensors
        
        
        # initialize the gyro (ANALOG INPUT)
        self.gyro = wpilib.AnalogGyro(1)
        
        #Timer
        self.timer = wpilib.Timer()
        self.timer.start()
        self.startTime = 0
        
        #shooter speed variable
        '''TO BE EDITED'''
        self.fastShootSpeed = -0.8
        self.slowShootSpeed = -0.4
            
        #autonomous
        self.start_position = "left"
        self.cross_on = "none"
        self.autonomous_state = "begin"
        self.initialTime = 0
        self.initialHeading = 0
        self.autoSafeToGetHeading = True
        self.autoSafeToResetEncoder = True
        self.autoSafeToGetTime = True
        
        self.acceptable_heading_error = 5 # the range (+- degrees) that the heading can be off of desired that we still consider good
        self.slower_speed_band = 20  # When +-20 degrees from desired heading, turn slower to avoid overshooting
        
        self.autoSlowTurnSpeed = 0.3 #slow speed
        self.autoNormalTurnSpeed = 0.6 #normal speed
        
        #AutoStates variables
        '''
        self.choose_direction_state = "begin"
        self.handle_obstacle_state = "begin"
        self.shooting_state = "begin"
        '''
        #Possible values are:
        #startPos = left, center, right
        #autoTarget = switch, scale, line
        self.startPos = "left"
        self.autoTarget = "switch"
        
    def autonomousPeriodic(self):
        #try:
            """This function is called periodically during autonomous."""
            self.robotDrive.setSafetyEnabled(False) #IMPORTANT! DO NOT REMOVE
            
                        #################### AUTO TESTING CODE ####################
            
            # Test Encoder
                # Drive for 24 inches
                #done = UtilityFunctions.driveNumInches(self, 32, 1, 0.3)
            # Test Gyro
                # Turn 90 Degrees Right
                #done = UtilityFunctions.turnNumDegrees(self, 90)
            # Test Camera
                # Follow a target
                #AutoStates.findDatGoal(self, 0.3, "none")
            #################### END AUTO TESTING #####################
            
            '''if done:
                self.autonomous_state = "done"
                self.leftBackMotor.set(0)
                self.leftFrontMotor.set(0)
                self.rightBackMotor.set(0)
                self.rightFrontMotor.set(0)'''

            #Starting Left
            if self.startPos == 'left':
                
                #Goal Switch
                if self.autoTarget == 'switch':
                    if self.switchPos == 'left':
                        #Insert swLL
                        pass
                    elif self.switchPos == 'right':
                        #InsertswLR
                        pass
                    else:
                        #Drive Forward
                        pass

                #Goal Scale
                elif self.autoTarget == 'scale':
                    if self.scalePos == 'left':
                        #Insert scLL
                        pass
                    elif self.scalePos == 'right':
                        #Insert scLR
                        pass
                    else:
                        #Drive Forward
                        pass

                #No Goal
                else:
                    if self.switchPos == 'left':
                        #Insert swLL
                        pass
                    elif self.switchPos == 'right':
                        #Insert swLR
                        pass
                    else:
                        #Drive Forward
                        pass


            #Starting Right
            elif self.startPos == 'right':

                #Goal Switch
                if self.autoTarget == 'switch':
                    if self.switchPos == 'left':
                        #Insert swRL
                        pass
                    elif self.switchPos == 'right':
                        #InsertswRR
                        pass
                    else:
                        #Drive Forward
                        pass

                #Goal Scale
                elif self.autoTarget == 'scale':
                    if self.scalePos == 'left':
                        #Insert scRL
                        pass
                    elif self.scalePos == 'right':
                        #Insert scRR
                        pass
                    else:
                        #Drive Forward
                        pass

                #No Goal
                else:
                    if self.switchPos == 'left':
                        #Insert swRL
                        pass
                    elif self.switchPos == 'right':
                        #Insert swRR
                        pass
                    else:
                        #Drive Forward
                        pass


            #Start Center
            elif self.startPos == 'center':

                #Goal Switch
                if self.autoTarget == 'switch':
                    if self.switchPos == 'left':
                        #Insert swCL
                        pass
                    elif self.switchPos == 'right':
                        #InsertswCR
                        pass
                    else:
                        #Drive Forward
                        pass

                #Goal Scale
                elif self.autoTarget == 'scale':
                    if self.scalePos == 'left':
                        #Insert scCL
                        pass
                    elif self.scalePos == 'right':
                        #Insert scCR
                        pass
                    else:
                        #Drive Forward
                        pass

                #No Goal
                else:
                    if self.switchPos == 'left':
                        #Insert swCL
                        pass
                    elif self.switchPos == 'right':
                        #Insert swCR
                        pass
                    else:
                        #Cross Field
                        pass

            #No Starting Position
            else:
                #Drive Forward
                pass
                    
            
        #except:
        #    pass
            
    def disabledInit(self):
        '''Calledonly ar the beginning of disabled mode'''
        pass
       
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        pass

    def teleopPeriodic(self):
        #try:
            """This function is called periodically during operator control."""
            self.robotDrive.setSafetyEnabled(True) #IMPORTANT! DO NOT REMOVE!
            
            stick1_Y = self.stick1.getY()#left
            stick2_Y = self.stick2.getY()#right
            
            """ dead-band """
            if stick1_Y > -0.05 and stick1_Y < 0.05:
                stick1_Y = 0
            if stick2_Y > -0.05 and stick2_Y < 0.05:
                stick2_Y = 0
           
        
            # Use the Stick 1 joystick Y axis for the right wheels, and the Stick 2 Y axis for the left wheels.
            self.robotDrive.tankDrive(stick1_Y, stick2_Y)
                                                   
            # Other Controls Below
            
            # Shooter Controls:
            
            # SHOOT!
            #Forward
            if self.game_pad.getRawButton(8):
                self.shooterDoor.set(1)
            #Backward
            elif self.game_pad.getRawButton(7):
                self.shooterDoor.set(2)

            #Elevate Shooter
            #Up
            if self.game_pad.getRawButton(5):
                self.shooterElev.set(1)
            #Down
            if self.game_pad.getRawButton(2):
                self.shooterElev.set(2)
            # Spin up shooter
            #Fast
            if self.game_pad.getRawButton(6):
                self.shooterLeftFront.set(self.fastShootSpeed)
                self.shooterLeftBack.set(self.fastShootSpeed)
                self.shooterRightFront.set(-self.fastShootSpeed)
                self.shooterRightBack.set(-self.fastShootSpeed)
            #Slow
            elif self.game_pad.getRawButton(3):
                self.shooterLeftFront.set(self.slowShootSpeed)
                self.shooterLeftBack.set(self.slowShootSpeed)
                self.shooterRightFront.set(-self.slowShootSpeed)
                self.shooterRightBack.set(-self.slowShootSpeed)
            else:
                self.shooterLeftFront.set(0)
                self.shooterLeftBack.set(0)
                self.shooterRightFront.set(0)
                self.shooterRightBack.set(0)

            # Intake Arm Controls
            if self.stick2.getRawButton(1):
                self.intakeMotorLeft.set(1)
                self.intakeMotorRight.set(-1)
            elif self.stick1.getRawButton(1):
                self.intakeMotorLeft.set(-1)
                self.intakeMotorRight.set(1)
            elif self.stick1.getRawButton(2):
                self.intakeMotorLeft.set(0)
                self.intakeMotorRight.set(0)
            
            # Climbing Controls
            climbTggl = False
            self.climbButtonState = False
            if self.climbButtonState == False:
                if self.game_pad.getRawButton(4) and self.climbTggl == False:
                    self.climberLeft.set(1)
                    self.climberRight.set(1)
                    self.climbButtonState = True
                    self.climbTggl = True
                elif self.game_pad.getRawButton(4) and self.climbTggl == True:
                    self.climberLeft.set(2)
                    self.climberRight.set(2)
                    self.climbButtonState = True
                    elf.climbTggl = False
        
        
        #except:
            #pass
           
#print(MyRobot)
if __name__ == '__main__':
    wpilib.run(MyRobot)
