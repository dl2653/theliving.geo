# Enable Python support and load DesignScript library
import clr, sys
sys.path.append("C:\\Program Files (x86)\\IronPython 2.7\\Lib")


sys.path.append("C:\\Users\\Damon\\Documents\\GitHub\\theliving.geo\\python")

import theliving_geo as tl

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *


# The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

x = IN[0]
y = IN[1]
z = IN[2]

# Place your code below this line

# Assign your output to the OUT variable.
OUT = tl.who_am_i(), point(x, y, z)