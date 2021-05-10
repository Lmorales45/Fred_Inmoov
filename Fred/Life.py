##############################################################
#                                                            #
# Program Code for Fred Inmoov                               #
# Of the Cyber_One YouTube Channel                           #
# https://www.youtube.com/cyber_one                          #
#                                                            #
# This is version 5                                          #
# Divided up into sub programs                               #
# Coded for the Nixie Version of MyRobotLab.                 #
#                                                            #
# Running on MyRobotLab (MRL) http://myrobotlab.org/         #
# Fred in a modified Inmmov robot, you can find all the      #
# origonal files on the Inmoov web site. http://inmoov.fr/   #
#                                                            #
# Life.py                                                    #
# This file is to Simulate movements associated with a       #
# living entity                                              #
#                                                            #
##############################################################
import math
import time
import random

print "Creating the various life simulation functions"
# Load the configuration for the IO devices.
execfile(RuningFolder+'/1_Configuration/C_Life_Config.py')

# When ever you look at a robot just standing there, it looks
# lifeless and dead, that is until it starts to move.
# To make our robot appear to be alive, we need it to move.
# The movements don't need to be large, a small eye movement
# or the eyes blinking can help to bring the robot to life.
# In this file, we will call on a series of small programs
# designed to provide small random movements to simulate a
# living being and in some cases provide simplified interface
# for controlling the robot.


# The Eye Balls are controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/1_Eye_Movements.py')

# The Eye Lids are controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/2_Eye_Lids.py')

# The neck is controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/3_Neck_Control.py')

# The Torso is controlled from this sub program
execfile(RuningFolder+'/6_Life_Functions/4_Torso_Control.py')

# We don't want our robot being active all the time, so we
# need to put the robot to sleep when it's been idel for a
# while and wake it up when a sense event occurs.
execfile(RuningFolder+'/6_Life_Functions/Wake_Up_And_Sleep.py')

# Use the PIR sensor to wake up or keep awake
if EnablePIR: # /1_Configuration/A_IO_Config.py
    # Here if we are using the PIR sensor, we create the method 
    # for the PIR event handler.
    def PirLifeEvent(Sense):
        global Awake
        if Sense:
            print "Warm body movement detected !!!"
            if EnableSleepTimer==True:
                WakeUpEvent()
    pir.addListener("publishSense",python.name,"PirLifeEvent")

    
# There is provision for two Ultrasonic sensors, Left and right.
if EnableLeftUltrasonic or EnableRightUltraSonic: # /1_Configuration/A_IO_Config.py
# Here we define the Ping Event handler
    def PingTimeEvent(timedata):
        global LastLeftPing
        global LastRightPing
        global LastPingLeft
        if LastPingLeft:
            LastPingLeft = False
            if EnableLeftUltrasonic:
                LastLeftPing = LeftUltraSonic.range()
                if LastLeftPing > 10 and LastLeftPing < 200:
                    WakeUpEvent()
        else:
            LastPingLeft = True
            if EnableRightUltraSonic:
                LastRightPing = RightUltraSonic.range()
                if LastRightPing > 10 and LastRightPing < 200:
                    WakeUpEvent()
        print "Left Ping = ", LastLeftPing, ", Last Right Ping = ", LastRightPing
    PingTimer = Runtime.createAndStart("PingTimer", "Clock")
    PingTimer.addListener("pulse", python.name, "PingTimeEvent")
    PingTimer.setInterval(PingTime) # /1_Configuration/A_IO_Config.py
    PingTimer.startClock(False)

# Jaw control based on MarySpeech.
# This section will cause the jaw to open and close as the robot is speaking.
if (UseMarySpeech or UseMimicSpeech or UseEspeak) and EnableMouthControl and EnableJawServo:
    # Before we can use this feature, we first need to create it :-)
    mouthcontrol = Runtime.create("mouthcontrol","MouthControl")
    #mouthcontrol = Runtime.start("mouthcontrol","MouthControl")
    # Once created we need to link it to the servo that controls the mouth opening and closing
    # in out case we called that Jaw back in the Servo.py file.
    #mouthcontrol.attach(Jaw)
    mouthcontrol.setJaw(Jaw)
    # Next we need to link it to the TTS service, we called that Mouth
    #mouthcontrol.attach(Mouth)
    mouthcontrol.setMouth(Mouth)
    # We need to set the range of motion for the Jaw
    #mouthcontrol.setmouth(JawMinPos, JawMaxPos)
    mouthcontrol.setmouth(10, 80)
    #mouthcontrol.mouthClosedPos = JawMinPos
    #mouthcontrol.mouthOpenedPos = JawMaxPos
    # next we need to setup the delays for the jaw movement.
    # Thanks to Steve Rayner for explaining this group of settings
    # on his YouTube Channel https://www.youtube.com/watch?v=jswk8lDtGOc
    mouthcontrol.delaytime = 75
    mouthcontrol.delaytimestop = 150
    mouthcontrol.delaytimeletter = 40
    mouthcontrol.startService()
