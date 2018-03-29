def color(x,y):
    from PIL import ImageGrab
    return ImageGrab.grab().load()[x,y]
