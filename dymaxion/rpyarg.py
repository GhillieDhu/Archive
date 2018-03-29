from math import sqrt, radians, degrees, sin, cos, tan, asin, acos, atan2
import sys

def rotate(angle, x, y):
    # Rotate the point to correct orientation in XY-plane.
    angle = radians(angle)
    return x * cos(angle) - y * sin(angle), x * sin(angle) + y * cos(angle)

def r2(axis, alpha, x, y, z):
    # Rotate a 3-D point about the specified axis.
    # MRP: Does not conform to normal rotation matrix derived formulae
    if (axis == 'x'):
        return x, y * cos(alpha) + z * sin(alpha), z * cos(alpha) - y * sin(alpha)
    elif (axis == 'y'):
        return x * cos(alpha) - z * sin(alpha), y, x * sin(alpha) + z * cos(alpha)
    elif (axis == 'z'):
        return x * cos(alpha) + y * sin(alpha), y * cos(alpha) - x * sin(alpha), z
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
    magnitude = sqrt(magnitude)
    center = {}
    for coordinate in old:
        center[coordinate] = old[coordinate] / (3 * magnitude)
    return center

def garc():
    return 2.0 * asin(sqrt(5 - sqrt(5)) / sqrt(10))

def gt():
    return garc() / 2.0

def gdve():
    return sqrt(3 + sqrt(5)) / sqrt(5 + sqrt(5))

def gel():
    return sqrt(8) / sqrt(5 + sqrt(5))

def same_side(p1, p2, a, b):
    return 0 <= ((p1[1] - a[1]) * (b[0] - a[0]) - (p1[0] - a[0]) * (b[1] - a[1])) * ((p2[1] - a[1]) * (b[0] - a[0]) - (p2[0] - a[0]) * (b[1] - a[1]))

def point_in_triangle(p, a, b, c):
    return (same_side(p, a, b, c) and same_side(p, b, a, c) and same_side(p, c, a, b))

def dymaxion_to_geographic(x, y): #MASTER
    tri = point_to_face(x, y)
    if not tri:
        return False
    gx, gy = cartesian_point(x, y, tri)
    tri = int(float(tri))
    gxp, gyp = white_box_p(gx, gy)
    h0x, h0y, h0z = white_box_trans(gxp, gyp)
    x, y, z = white_box(tri, h0x, h0y, h0z)
    rho, theta, phi = cartesian_to_spherical(x, y, z)
    return spherical_to_geographic(theta, phi)

def white_box(tri, h0x, h0y, h0z):
    switchtri = {   1: 1,   2: 1,   3: 1,   4: 1,
                    5: 1,   6: 2,   7: 3,   8: 3,
                    9: 4,   10: 4,  11: 5,  12: 5,
                    13: 6,  14: 2,  15: 2,  16: 8,
                    17: 9,  18: 10, 19: 11, 20: 8}

    radius0, hlat0, hlng0 = cartesian_to_spherical(centers(tri)['x'], centers(tri)['y'], centers(tri)['z'])
    h1x, h1y, h1z = r2('z', hlng0, vertices(switchtri[tri])['x'], vertices(switchtri[tri])['y'], vertices(switchtri[tri])['z'])
    h1x, h1y, h1z = r2('y', hlat0, h1x, h1y, h1z)
    radius1, hlat1, hlng1 = cartesian_to_spherical(h1x, h1y, h1z)
    hlng1 = hlng1 - radians(90.0)
    h0x, h0y, h0z = r2('z', -hlng1, h0x, h0y, h0z)
    h0x, h0y, h0z = r2('y', -hlat0, h0x, h0y, h0z)
    return r2('z', -hlng0, h0x, h0y, h0z)

def cartesian_to_spherical(x, y, z):
    # convert cartesian coordinates into spherical polar coordinates.
    # The angles are given in radians.
    return sqrt(x**2 + y**2 + z**2), acos(z / sqrt(x**2 + y**2 + z**2)), atan2(y, x)

def spherical_to_geographic(theta, phi):
    lat = 90.0 - degrees(theta)
    lng = degrees(phi)
    while lng < -180:
        lng += 360
    while lng > 180:
        lng -= 360
    return lat, lng

def point_to_face(x, y): #validated
    nodes = {   1:      [(2.5, 3.0), (1.5, 3.0), (2.0, 4.5)],
                2:      [(2.5, 3.0), (2.0, 1.5), (1.5, 3.0)],
                3:      [(2.5, 3.0), (3.0, 1.5), (2.0, 1.5)],
                4:      [(2.5, 3.0), (3.5, 3.0), (3.0, 1.5)],
                5:      [(2.5, 3.0), (2.0, 4.5), (3.0, 4.5)],
                6:      [(2.0, 4.5), (1.5, 3.0), (1.0, 4.5)],
                7:      [(1.5, 3.0), (1.0, 1.5), (0.5, 3.0)],
                8:      [(1.5, 3.0), (2.0, 1.5), (1.0, 1.5)],
                9:      [(2.0, 1.5), (2.5, 0.0), (2.0, 0.5)],
                '9':    [(1.5, 1.0), (1.5, 0.0), (1.0, 1.5)],
                '9.0':  [(2.0, 1.5), (1.5, 1.0), (1.0, 1.5)],
                10:     [(2.0, 1.5), (3.0, 1.5), (2.5, 0.0)],
                11:     [(3.0, 1.5), (4.0, 1.5), (3.5, 0.0)],
                12:     [(3.0, 1.5), (3.5, 3.0), (4.0, 1.5)],
                13:     [(3.5, 3.0), (4.5, 3.0), (4.0, 1.5)],
                14:     [(4.0, 4.5), (4.5, 3.0), (3.5, 3.0)],
                15:     [(5.0, 4.5), (5.5, 3.0), (4.5, 3.0)],
                16:     [(0.0, 1.5), (1.0, 1.5), (0.75, 0.75)],
                '16':   [(5.5, 3.0), (6.0, 1.5), (5.0, 1.5)],
                17:     [(1.0, 1.5), (1.5, 0.0), (0.5, 0.0)],
                18:     [(3.5, 0.0), (4.0, 1.5), (4.5, 0.0)],
                19:     [(4.0, 1.5), (4.5, 3.0), (5.0, 1.5)],
                20:     [(5.5, 3.0), (5.0, 1.5), (4.5, 3.0)]}
    point = (x, y)
    for face in nodes:
        [a, b, c] = nodes[face]
        a = (a[0], a[1] / sqrt(3))
        b = (b[0], b[1] / sqrt(3))
        c = (c[0], c[1] / sqrt(3))
        if point_in_triangle(point, a, b, c):
            return face
    return False

def tann(a): #??? pi problem, possibly tolerable
    return 0.5 * gel() + gdve() * tan(a - gt())

def white_box_trans(gxp, gyp):
    # exact transformation equations
    q = (5 + 2 * sqrt(5)) / 15

    gs = sqrt(gxp**2 + gyp**2 + q)

    h0x = gxp / gs
    h0y = gyp / gs
    h0z = sqrt(1 - h0x**2 - h0y**2)

    return h0x, h0y, h0z

def white_box_p(gx, gy):
    ga1 =        gy * ( 2.0 / sqrt(3.0)) + (gel() / 3.0)
    ga2 =   gx + gy * (-1.0 / sqrt(3.0)) + (gel() / 3.0)
    ga3 = - gx + gy * (-1.0 / sqrt(3.0)) + (gel() / 3.0)

    ga1p, ga2p, ga3p = tann(ga1), tann(ga2), tann(ga3)
    
    gxp = 0.5 * (ga2p - ga3p)
    gyp = (1.0 / (2.0 * sqrt(3))) * (2 * ga1p - ga2p - ga3p)

    return gxp, gyp

def cartesian_point(x, y, tri):
    unpeel = {  1:      (240.0, 2.0, 3.5),
                2:      (300.0, 2.0, 2.5),
                3:      (  0.0, 2.5, 2.0),
                4:      ( 60.0, 3.0, 2.5),
                5:      (180.0, 2.5, 4.0),
                6:      (300.0, 1.5, 4.0),
                7:      (300.0, 1.0, 2.5),
                8:      (  0.0, 1.5, 2.0),
                '9':    (300.0, 1.5, 1.0),
                '9.0':  (300.0, 1.5, 1.0),
                9:      (  0.0, 2.0, 0.5),
                10:     ( 60.0, 2.5, 1.0),
                11:     ( 60.0, 3.5, 1.0),
                12:     (120.0, 3.5, 2.0),
                13:     ( 60.0, 4.0, 2.5),
                14:     (  0.0, 4.0, 3.5),
                15:     (  0.0, 5.0, 3.5),
                16:     ( 60.0, 0.5, 1.0),
                '16':   (  0.0, 5.5, 2.0),
                17:     (  0.0, 1.0, 0.5),
                18:     (120.0, 4.0, 0.5),
                19:     (120.0, 4.5, 2.0),
                20:     (300.0, 5.0, 2.5)}
    x, y = rotate(-unpeel[tri][0], x - unpeel[tri][1], y - (unpeel[tri][2] / sqrt(3.0)))
    return x * garc(), y * garc()
