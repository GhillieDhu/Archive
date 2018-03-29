from PIL import Image

def diff(before, after):
    bpa = before.load()
    apa = after.load()
    diff = Image.new("RGB", after.size, (0, 0, 0))
    dpa = diff.load()
    for i in range(0, after.size[0]):
        for j in range(0, after.size[1]):
            if (apa[i,j] != bpa[i,j]):
                dpa[i,j] = apa[i,j]
    return diff
