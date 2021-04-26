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
# C_Life_Config.py                                           #
# This is where the configuration settings live for the      #
# varoius controllers.                                       #
#                                                            #
##############################################################
print "Loading the Life Simulation System Config"
##############################################################
#                                                            #
# Life Simulation Group Group                                #
#                                                            #
##############################################################

# The Blinking feature can be very anoying, 
# so the option to turn it of is here.
EnableBlinking = True           # Set to True or False

# Moves the eyes to make the robot appear more alive.
EnableRandomEyeMovements = True # Set to True or False

# From time to time, we will want the robot to stop running
# the life simulations, this is done by putting the robot
# to sleep after a period of no activity.
# This is only possible when there is a way to wake the Robot
# back up again, This auto sleep can be disabled by disabling
# the Sleep Timer
EnableSleepTimer = True         # Set to True or False

# There are times when setting up your robot, you don't want
# the jaw to move, this is where you can disable this feature.
EnableMouthControl = True       # Set to True or False

# Wakeup Message
# This message is spoken whenever the robot wakes up
# Set the message to OFF if you don't want this message.
WakeupMessage = u"Hello, How are you"
#WakeupMessage = "OFF"