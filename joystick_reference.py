#!/usr/bin/python

"""
  Brian Smith
  7.25.2014
  Test_Joystick
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    - Preliminary tests for final project.  Attempting to access bindings for
    microsoft multi-channel joystick
"""
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#                         O P E R A B L E  C O D E
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class ModuleInitializationError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class MissingJoystickError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def getJoystickInfo():
    try:
        import pygame as pygame #FIXME: pygame wont work... make it!
    except ImportError:
        print "Missing pygame module!!  Make sure to install pygame"

    try:
        assert pygame.init() == (6,0) # initialize joystick module
        assert pygame.joystick.get_init() == 1 # check that it initialized (bool)
    else:
        raise ModuleInitializationError("The Joystick Module did not load")

    print "\nJoystick Reference Information"
    print "::::::::::::::::::::::::::::::::"
    print "Joystick Module Loaded"

    # Get the number of connected joysticks
    joystickCount = pygame.joystick.get_count() # returns the number of joysticks connected
    print "Joystick Count           = %d" % joystickCount

    # initialize new Joystick Objects
    for i in xrange(joystickCount):
        sideWinder2 = pygame.joystick.Joystick(i)
        sideWinder2.init()

    # check that the Joystick objects initialized
    if sideWinder2.get_init() == True:
        print "Initialization Status    = Success"
    else:
        print "Initialization Status    = Failed"

    # Get desired joystick id number
    joystickId = sideWinder2.get_id()
    print "SideWinder 2 ID          = %d" % joystickId

    # Get desired joystick name
    joystickName = sideWinder2.get_name()
    print "Joystick Name            = %s" % joystickName

    # Get the total number of axis
    numAxes = sideWinder2.get_numaxes()
    print "Number of Axes           = %d" % numAxes


    # Get the number of trackballs on joystick
    numBalls = sideWinder2.get_numballs()
    print "Number of TrackBalls     = %d" % numBalls

    # Get the number of buttons on joystick
    numButtons = sideWinder2.get_numbuttons()
    print "Number of Buttons        = %d" % numButtons

    # Get number of hat controls
    numHats = sideWinder2.get_numhats()
    print "Number of Hat Controls   = %d" % numHats


# getJoystickInfo()

def getCurrStates():
    # Get the current position of a specified axis
    """
    Gets the current Axis locations, or button states, or hat values and
    returns then in a corresponding format
    """
    currAxis = 0
    currAxisPos = sideWinder2.get_axis(currAxis)
    print "Current Axis Pos(%d)      = %d" % (currAxis, currAxisPos)

    # Get specified button state
    currButton = 2
    buttonState = sideWinder2.get_button(currButton)
    print "Button_%d State           = %d" % (currButton, buttonState)

    # Get value of hat control
    currHat = 0
    hatVal = sideWinder2.get_hat(currHat)
    print "Hat Control Value        = (%d, %d)" % hatVal

# get getCurrPosition()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#                         T E S T  F U N C T I O N S
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::