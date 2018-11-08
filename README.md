## The Living.Geometry

Geometry library for use in GD projects, with connctions with mulitple general purpose geometry, optimization, and simulation packages.



### Geometry Creation:


```python
import theliving_geo as tl

# 3D point: [x, y, z]
p1 = tl.point(0, 0, 0)
p2 = tl.point(1, 2, 3)
p3 = tl.point(x, y, z)

# Line: [[p1, p2, p3], [p4, p5, p6]]
tl.line(p1, p3).draw()
m
# Polyline: [[[p1, p2, p3], [p4, p5, p6], [p7, p8, p9]], closed]
tl.polyline([p1, p2, p3], 0).draw()


# Vector:
vec = tl.vector([0,0,1])
vec_rotate = vec.rotate(vec, [1,0,0], 90)
vec_add = vec.add([vec, vec_rotate])

# Mesh
tl.mesh(verts)

```

**3D point:** [x, y, z]

**Line:** [ [p0, p1, p2], [p3, p4, p5] ]

**Polyline:** [ [p0, p1, p2], [p3, p4, p5], [p6, p7, p8] ]

**Mesh** { vertex:[p0, p1, p2], edge:[1,2,3] }


This library will automatically detect which environment it is running in (Dynamo, Nastran, GH, or NumPy) in and produce the corresponding geometry for. If script is running outside any geometry library, data will be left in native TheLiving_Geo format. Additional attributes can be attached to base geometry for

**DesignScript:** Autodesk.Point.ByCoordinates(x, y, z);

**Rhino Commons:** point(x, y, z)

**NumPy / Matplotlib:** ax.scatter(xs, ys, zs, c=c, marker=m)

**Nastran:**		GRID eid x y z


### Geometry Functions:



```python
import theliving_geo as tl

# Intersection
intersection_point = tl.intersection(crv0, crv1)

# Distance to Point
dist = tl.distance(p0, p1)

# Point Move
pt_move = tl.point.move(point, vector)

# Polyline Curve Rotate
pline_rotate = tl.polyline.rotate(center, axis, angle)

```



### Polygon Boolean Operations
```python
import theliving_geo as tl

# Boolean Union
bool_union = tl.bool.union(crv0, crv1)

# Boolean Intersection
bool_intersection = tl.bool.intersection(crv0, crv1)

# Boolean Difference
bool_diff = tl.bool.difference(crv0, crv1)

# Boolean XOR
bool_xor = tl.bool.xor(crv0, crv1)

```




### Simulation Functions
```python
import theliving_geo as tl

# GRID

# BEAM

# MESH

# TET

# FORCE

# MASS

```
