Geometry library for use in GD projects


Data types (with constructors)

Point(x, y, z)
p = Autodesk.Point.ByCoordinates(x, y, z);

Vector(x, y, z)
v = Vector.ByCoordinates(x, y, z);

Line(PointA, PointB)
l = Line.ByStartPointEndPoint(p1, p2);

PolylineCurve([Point(s)])
 pts = [p0,p1,p2];
 polyCurve = PolyCurve.ByPoints(pts, 0);
// specify True for closed polycurve, False for open polyline

Functions

rh.Intersect.Intersection.CurveCurve(LineA, LineB) → [intersection Point(s)]
			intersection = Autodesk.Geometry.Intersect(line1, line2);

Point.DistanceTo(PointA) → distance
			dist  = Autodesk.Geometry.DistanceTo(p0, p1);


rh.Curve.CreateBooleanIntersection(PolylineCurveA, PolylineCurveB) → [PolylineCurve(s)]
			// this should be the boolean intersect region shared by both closed polylines

 p = Autodesk.Point.ByCoordinates(x, y, z); // point on the side of curve you want to keep. Not in intersection region.
geo_1 = Autodesk.Geometry.Trim(polyCurve1, polyCurve2, p);
geo_2 = Autodesk.Geometry.Trim(polyCurve2, polyCurve1, p);

intersection_region = PolyCurve.ByJoinedCurves([geo_1, geo_2], 0.001);



rh.Curve.CreateBooleanUnion([PolylineCurves(s)]) → [PolylineCurve(s)]
			// not easy using polycurves
// possible as solids, but slow
// possible using series of trims

 p = Autodesk.Point.ByCoordinates(x, y, z); // point on the side of polyCurve_1 you want to keep. Not in intersection region.
p2 = Autodesk.Point.ByCoordinates(x, y, z);  // point on the side of polyCurve_2 you want to keep. Not in intersection region.

geo_1 = Autodesk.Geometry.Trim(polyCurve1, polyCurve2, p);
geo_2 = Autodesk.Geometry.Trim(polyCurve2, polyCurve1, p2);

union_region = PolyCurve.ByJoinedCurves([geo_1, geo_2], 0.001);


rh.Curve.CreateBooleanDifference(PolylineCurveA, PolylineCurveB) → [PolylineCurve(s)]



PolylineCurve.Rotate(angle, Vector(normal axis), Point(center)) → PolylineCurve

				point = Autodesk.Point.ByCoordinates(x, y, z);
vector = Vector.ByCoordinates(0, 0, 1); //z axis
angle = 45
geo_rotated = Autodesk.Geometry.Rotate(geo, point, vector, angle);


Point.Move(Vector) → Point
Autodesk.Geometry.Translate(geo, x, y, z)


