#!/usr/bin/env python3

#library includes
import wpilib
from wpilib import RobotDrive

from networktables import NetworkTable

#User Includes
from Utilities import UtilityFunctions
from AutonomousStates import AutoStates

#Raven Robotics 2018 PowerUp
#This robot uses Tank Drive
class MyRobot(wpilib.IterativeRobot):

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        pass
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.sd = NetworkTable.getTable('SmartDashboard')
        
        #Encoder
        self.encoder = wpilib.Counter(1)

        # Joysticks
        self.stick1 = wpilib.Joystick(1)#left
        self.stick2 = wpilib.Joystick(2)#right
        self.game_pad = wpilib.Joystick(3)
        
        # Drive Train Motors
        self.leftFrontMotor = wpilib.TalonSRX(0) #front left 
        self.leftBackMotor = wpilib.VictorSP(1) #back left 
        self.rightFrontMotor = wpilib.VictorSP(2) #front right 
        self.rightBackMotor = wpilib.TalonSRX(3) #back right
        
        # Shooter Motors
        #Front is front of shooter
        self.shooterLeftFront = wpilib.TalonSRX(4)
        self.shooterLeftBack = wpilib.TalonSRX(5)
        self.shooterRightFront = wpilib.TalonSRX(6)
        self.shooterRightBack = wpilib.TalonSRX(7)
        
        # Conveyor Motor(s)
        #TO BE EDITED
        self.conveyorMotor = wpilib.TalonSRX(8)
        
        
        #robot drive
        self.robotDrive = wpilib.RobotDrive(self.leftFrontMotor,
                                            self.leftBackMotor,
                                            self.rightFrontMotor,
                                            self.rightBackMotor)
                                            
        
        
        ## invert the front motors
        #self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True)
        #self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontRight, True)
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
        self.shooterSpeed = -0.8
            
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
            
                if done:
                    self.autonomous_state = "done"
                    self.leftBackMotor.set(0)
                    self.leftFrontMotor.set(0)
                    self.rightBackMotor.set(0)
                    self.rightFrontMotor.set(0)
            
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
        try:
            """This function is called periodically during operator control."""
            #self.robotDrive.setSafetyEnabled(True) #IMPORTANT! DO NOT REMOVE!
            
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
            if self.game_pad.getRawButton(8):
                self.
                self.
            else:
                self.
                self.
            
            # Spin up shooter
            if self.game_pad.getRawButton(7):
                self.shooterLeftFront.set(self.shooterSpeed)
                self.shooterLeftBack.set(self.shooterSpeed)
                self.shooterRightFront.set(self.shooterSpeed)
                self.shooterRightBack.set(self.shooterSpeed)
            else:
                self.shooterLeftFront.set(0)
                self.shooterLeftBack.set(0)
                self.shooterRightFront.set(0)
                self.shoterRightBack.set(0)
            
            # Conveyor Controls:
            if self.game_pad.getRawButton(6):
                self.conveyorMotor.set(1)
            elif self.game_pad.getRawButton(3):
                self.conveyorMotor.set(-0.6)
            else:
                self.conveyorMotor.set(0)
            
            # Climbing Controls
            if self.game_pad.getRawButton(4):
                self.climberMotor.set(-1)
            else:
                self.climberMotor.set(0)
         
            
        except:
            pass
           

print(MyRobot)

