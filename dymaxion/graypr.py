# by  Robert W. Gray

# This C program contains the Dymaxion map coordinate
# transformation routines for converting longitude / latitude
# points to (X, Y) points on the Dymaxion map.

# This version uses the exact transformation equations.

import math

def geographic_to_dymaxion(lat, lng):
    # This is the main control procedure.

    # Convert the given (long., lat.) coordinate into spherical
    # polar coordinates (r, theta, phi) with radius=1.
    # Angles are given in radians, NOT degrees.

    theta, phi = geographic_to_spherical(lat, lng)

    # convert the spherical polar coordinates into cartesian
    # (x, y, z) coordinates.

    x, y, z = spherical_to_cartesian(1, theta, phi)

    # determine which of the 20 spherical icosahedron triangles
    # the given point is in and the LCD triangle.

    tri, lcd = s_tri_info(x, y, z)

    # Determine the corresponding Fuller map plane (x, y) point

    h0x, h0y, h0z = black_box(tri, x, y, z)
    gxp, gyp = black_box_trans(h0x, h0y, h0z)
    gx, gy = black_box_p(gxp, gyp)

    return transform(gx, gy, tri, lcd)

def geographic_to_spherical(lat, lng):
    # convert (long., lat.) point into spherical polar coordinates
    # with r=radius=1.  Angles are given in radians.
    return math.radians(90.0 - lat), math.radians(lng + (360.0 if lng < 0.0 else 0.0))

def spherical_to_cartesian(rho, theta, phi):
    # Covert spherical polar coordinates to cartesian coordinates.
    # The angles are given in radians.
    return rho * math.sin(theta) * math.cos(phi), rho * math.sin(theta) * math.sin(phi), rho * math.cos(theta)

def cartesian_to_spherical(x, y, z):
    # convert cartesian coordinates into spherical polar coordinates.
    # The angles are given in radians.
    return math.sqrt(x**2 + y**2 + z**2), math.acos(z / math.sqrt(x**2 + y**2 + z**2)), math.atan2(y, x)

def rotate(angle, x, y):
    # Rotate the point to correct orientation in XY-plane.
    angle = math.radians(angle)
    return x * math.cos(angle) - y * math.sin(angle), x * math.sin(angle) + y * math.cos(angle)

def r2(axis, alpha, x, y, z):
    # Rotate a 3-D point about the specified axis.
    # MRP: Does not conform to normal rotation matrix derived formulae
    if (axis == 'x'):
        return x, y * math.cos(alpha) + z * math.sin(alpha), z * math.cos(alpha) - y * math.sin(alpha)
    elif (axis == 'y'):
        return x * math.cos(alpha) - z * math.sin(alpha), y, x * math.sin(alpha) + z * math.cos(alpha)
    elif (axis == 'z'):
        return x * math.cos(alpha) + y * math.sin(alpha), y * math.cos(alpha) - x * math.sin(alpha), z
    else:
        return x, y, z

def vertices(number):
    # Cartesian coordinates for the 12 vertices of icosahedron
    return {1:  {'x':  0.420152426708710003, 'y':  0.078145249402782959, 'z':  0.904082550615019298},
            2:  {'x':  0.995009439436241649, 'y': -0.091347795276427931, 'z':  0.040147175877166645},
            3:  {'x':  0.518836730327364437, 'y':  0.835420380378235850, 'z':  0.181331837557262454},
            4:  {'x': -0.414682225320335218, 'y':  0.655962405434800777, 'z':  0.630675807891475371},
            5:  {'x': -0.515455959944041808, 'y': -0.381716898287133011, 'z':  0.767200992517747538},
            6:  {'x':  0.355781402532944713, 'y': -0.843580002466178147, 'z':  0.402234226602925571},
            7:  {'x':  0.414682225320335218, 'y': -0.655962405434800777, 'z': -0.630675807891475371},
            8:  {'x':  0.515455959944041808, 'y':  0.381716898287133011, 'z': -0.767200992517747538},
            9:  {'x': -0.355781402532944713, 'y':  0.843580002466178147, 'z': -0.402234226602925571},
            10: {'x': -0.995009439436241649, 'y':  0.091347795276427931, 'z': -0.040147175877166645},
            11: {'x': -0.518836730327364437, 'y': -0.835420380378235850, 'z': -0.181331837557262454},
            12: {'x': -0.420152426708710003, 'y': -0.078145249402782959, 'z': -0.904082550615019298}}[number]

def nodes(face):
    # Vertices defining each face

    return {1:  ( 1,  3,  2),   2:  ( 1,  4,  3),   3:  ( 1,  5,  4),   4:  ( 1,  6,  5),
            5:  ( 1,  2,  6),   6:  ( 2,  3,  8),   7:  ( 3,  9,  8),   8:  ( 3,  4,  9),
            9:  ( 4, 10,  9),   10: ( 4,  5, 10),   11: ( 5, 11, 10),   12: ( 5,  6, 11),
            13: ( 6,  7, 11),   14: ( 2,  7,  6),   15: ( 2,  8,  7),   16: ( 8,  9, 12),
            17: ( 9, 10, 12),   18: (10, 11, 12),   19: (11,  7, 12),   20: ( 8, 12,  7)}[face]

def centers(face):
    old = {'x': 0, 'y': 0, 'z': 0}
    for node in nodes(face):
        for coordinate in old:
            old[coordinate] += vertices(node)[coordinate]
    magnitude = 0
    for coordinate in old:
        magnitude += (old[coordinate])**2
    magnitude = math.sqrt(magnitude)
    center = {}
    for coordinate in old:
        center[coordinate] = old[coordinate] / (3 * magnitude)
    return center

def garc():
    return 2.0 * math.asin(math.sqrt(5 - math.sqrt(5)) / math.sqrt(10))

def gt():
    return garc() / 2.0

def gdve():
    return math.sqrt(3 + math.sqrt(5)) / math.sqrt(5 + math.sqrt(5))

def gel():
    return math.sqrt(8) / math.sqrt(5 + math.sqrt(5))

def s_tri_info(x, y, z):
    # Determine which triangle and LCD triangle the point is in.
    tri = 0
    min_dist = 9999.0

    # Which triangle face center is the closest to the given point
    # is the triangle in which the given point is in.

    for i in range(1, 21):
        h = {'x': centers(i)['x'] - x, 'y': centers(i)['y'] - y, 'z': centers(i)['z'] - z}
        if (math.sqrt(h['x']**2 + h['y']**2 + h['z']**2) < min_dist):
            tri = i
            min_dist = math.sqrt(h['x']**2 + h['y']**2 + h['z']**2)

    # Now the LCD triangle is determined.

    h_dist = {}
    for i in range(3):
        vertex = nodes(tri)[i]
        h = {'x': x - vertices(vertex)['x'], 'y': y - vertices(vertex)['y'], 'z': z - vertices(vertex)['z']}
        h_dist[i] = math.sqrt(h['x']**2 + h['y']**2 + h['z']**2)
    
    if (h_dist[0] <= h_dist[1] and h_dist[1] <= h_dist[2]):
        return tri, 1
    if (h_dist[0] <= h_dist[2] and h_dist[2] <= h_dist[1]):
        return tri, 6
    if (h_dist[1] <= h_dist[0] and h_dist[0] <= h_dist[2]):
        return tri, 2
    if (h_dist[1] <= h_dist[2] and h_dist[2] <= h_dist[0]):
        return tri, 3
    if (h_dist[2] <= h_dist[0] and h_dist[0] <= h_dist[1]):
        return tri, 5
    if (h_dist[2] <= h_dist[1] and h_dist[1] <= h_dist[0]):
        return tri, 4

def black_box(tri, x, y, z):
    # In order to rotate the given point into the template spherical
    # triangle, we need the spherical polar coordinates of the center
    # of the face and one of the face vertices. So set up which vertex
    # to use.
    switchtri = {   1: 1,   2: 1,   3: 1,   4: 1,
                    5: 1,   6: 2,   7: 3,   8: 3,
                    9: 4,   10: 4,  11: 5,  12: 5,
                    13: 6,  14: 2,  15: 2,  16: 8,
                    17: 9,  18: 10, 19: 11, 20: 8}

    radius, hlat, hlng = cartesian_to_spherical(centers(tri)['x'], centers(tri)['y'], centers(tri)['z'])

    h0x, h0y, h0z = r2('z', hlng, x, y, z)
    h1x, h1y, h1z = r2('z', hlng, vertices(switchtri[tri])['x'], vertices(switchtri[tri])['y'], vertices(switchtri[tri])['z'])

    h0x, h0y, h0z = r2('y', hlat, h0x, h0y, h0z)
    h1x, h1y, h1z = r2('y', hlat, h1x, h1y, h1z)

    radius, hlat, hlng = cartesian_to_spherical(h1x, h1y, h1z)
    hlng = hlng - math.radians(90.0)

    h0x, h0y, h0z = r2('z', hlng, h0x, h0y, h0z)

    return h0x, h0y, h0z

def black_box_trans(h0x, h0y, h0z):
    # exact transformation equations
    gs = math.sqrt(5 + 2 * math.sqrt(5)) / (h0z * math.sqrt(15))

    gxp = h0x * gs
    gyp = h0y * gs
    return gxp, gyp

def atan(ap):
    return gt() + math.atan((ap - 0.5 * gel()) / gdve())

def black_box_p(gxp, gyp):
    ga1p =         gyp * ( 2.0 / math.sqrt(3.0)) + (gel() / 3.0)
    ga2p =   gxp + gyp * (-1.0 / math.sqrt(3.0)) + (gel() / 3.0)
    ga3p = - gxp + gyp * (-1.0 / math.sqrt(3.0)) + (gel() / 3.0) 

    ga1, ga2, ga3 = atan(ga1p),atan(ga2p),atan(ga3p)

    gx = 0.5 * (ga2 - ga3)
    gy = (1.0 / (2.0 * math.sqrt(3))) * (2 * ga1 - ga2 - ga3)

    return gx, gy

def transform(gx, gy, tri, lcd):
    # Re-scale so plane triangle edge length is 1.

    x = gx / garc()
    y = gy / garc()

    # rotate and translate to correct position
    switchtri = {   1:  (240.0, 2.0, 3.5),
                    2:  (300.0, 2.0, 2.5),
                    3:  (  0.0, 2.5, 2.0),
                    4:  ( 60.0, 3.0, 2.5),
                    5:  (180.0, 2.5, 4.0),
                    6:  (300.0, 1.5, 4.0),
                    7:  (300.0, 1.0, 2.5),
                    8:  (  0.0, 1.5, 2.0),
                    9:  (300.0, 1.5, 1.0), #if lcd > 2 else (0.0, 2.0, 0.5),
                    10: ( 60.0, 2.5, 1.0),
                    11: ( 60.0, 3.5, 1.0),
                    12: (120.0, 3.5, 2.0),
                    13: ( 60.0, 4.0, 2.5),
                    14: (  0.0, 4.0, 3.5),
                    15: (  0.0, 5.0, 3.5),
                    16: ( 60.0, 0.5, 1.0), #if lcd < 4 else (0.0, 5.5, 2.0),
                    17: (  0.0, 1.0, 0.5),
                    18: (120.0, 4.0, 0.5),
                    19: (120.0, 4.5, 2.0),
                    20: (300.0, 5.0, 2.5)}
    x, y = rotate(switchtri[tri][0], x, y)

    return x + switchtri[tri][1], y + (switchtri[tri][2] / math.sqrt(3.)), tri
