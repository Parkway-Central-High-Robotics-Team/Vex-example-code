#LINK TO SOURCE: https://www.robotmesh.com/studio/5be40c6ec8f17a1f5795f517
# VEX V5 Python Project
import sys
import vex
from vex import *

#region config
brain       = vex.Brain();
motor_right = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT16, vex.GearSetting.RATIO18_1, False)
con         = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

while True:
  # Left motor, vertical axis of left joystick
  motor_left.spin(vex.DirectionType.FWD, (con.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
  # Right motor, vertical axis of right joystick
  motor_right.spin(vex.DirectionType.FWD, (con.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)