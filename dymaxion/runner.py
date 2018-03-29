from __future__ import division
import sys
import math
from rpyarg import dymaxion_to_geographic
from PIL import Image

def rebox(lat, lng, x_max, y_max):
    return (180 + lng) * (x_max / 360), (90 - lat) * (y_max / 180)

def weight(x, y, x0, y0):
    return 1 / ((x - x0)**2 + (y - y0)**2)

def weighted_average(lat, lng, x_max, y_max, image):
    x, y = rebox(lat, lng, x_max, y_max)
    weights = {}
    for x_i in [math.floor(x), math.ceil(x)]:
        for y_i in [math.floor(y), math.ceil(y)]:
            x_0 = x_i % x_max
            y_0 = y_i % y_max
            weights[(x_0, y_0)] = weight(x, y, x_i, y_i)
    total_weight = 0
    r_total = 0
    g_total = 0
    b_total = 0
    for tup in weights:
        x, y = tup
        total_weight += weights[(x, y)]
        r, g, b = image[x, y]
        r_total += r * weights[(x, y)]
        g_total += g * weights[(x, y)]
        b_total += b * weights[(x, y)]
    return int(round(r_total / total_weight)), int(round(g_total / total_weight)), int(round(b_total / total_weight)), 255

if __name__ == '__main__':
    source_image = Image.open(sys.argv[1])
    siarray = source_image.load()
    x_max, y_max = source_image.size
    scale = y_max * math.sqrt(2 * math.sqrt(3) / 15)
    width = int(5.5 * scale)
    height = int(math.ceil(1.5 * math.sqrt(3) * scale))
    sink_image = Image.new('RGBA', (width, height))
    tiarray = sink_image.load()
    for x in xrange(width):
        for y in xrange(height):
            ll = dymaxion_to_geographic((width - x) / scale, y / scale)
            if ll:
                lat, lng = ll
                tiarray[x, y] = weighted_average(lat, lng, x_max, y_max, siarray)
    sink_image.save(sys.argv[2])
