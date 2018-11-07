__author__ = 'Damon, TheLiving'
__email__ = 'damon.lau@autodesk.com'

import os, sys, json


################################################################################ determine the current geometry platform

def who_am_i():

	print('sys version: ', sys.version)

	if sys.version == '2.7.8 (IronPython 2.7.8 (2.7.8.0) on .NET 4.0.30319.42000 (64-bit))':
		print('i am a rhino')

		return 'Rhino'

	if sys.version == '2.7.3 ()':
		print('i am a dynamo')

		return 'Dynamo'

	else:
		print('i have no idea who i am >< ', sys.version)

		return 'no one'


def point(x, y, z):

	who = who_am_i()

	if who == 'Rhino':

		import Rhino.Geometry as rh
		return rh.Point3d(x, y, z)

	if who == 'Dynamo':
 		return Point.ByCoordinates(x, y, z);




