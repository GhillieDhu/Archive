import controlPanel
import pyHook
import sys
import os
from collections import deque
from PIL import ImageGrab
from imageDiff import diff

class taskmaster():
    hm = pyHook.HookManager()
    lf = '.\\tm.hom'
    lp = '.'
    imgq = deque()
    uiq = deque()

    def __init__(self, logpath):
        if not(os.path.exists(logpath)):
            os.makedirs(logpath)
        self.lp = logpath
        self.lf = os.path.join(self.lp, self.lf)
        self.hm.SubscribeMouseLeftDown(self.LeftDown)
        self.hm.SubscribeMouseLeftUp(self.LeftUp)
        self.hm.SubscribeMouseRightDown(self.RightDown)
        self.hm.SubscribeMouseRightUp(self.RightUp)
        self.hm.SubscribeKeyDown(self.KeyDown)
        self.hm.SubscribeKeyUp(self.KeyUp)
        frame = controlPanel.new(self.start, self.stop)

    def LeftUp(self, event):
        self.uiq.append(("LU", event.Position))
        return True

    def LeftDown(self, event):
        self.uiq.append(("LD", event.Position))
        self.imgq.append(ImageGrab.grab())
        return True

    def RightUp(self, event):
        self.uiq.append(("RU", event.Position))
        return True

    def RightDown(self, event):
        self.uiq.append(("RD", event.Position))
        self.imgq.append(ImageGrab.grab())
        return True

    def KeyDown(self, event):
        self.uiq.append(("KD", event.KeyID))
        return True

    def KeyUp(self, event):
        self.uiq.append(("KU", event.KeyID))
        return True

    def start(self, event):
        self.hm.HookMouse()
        self.hm.HookKeyboard()
        self.log = open(self.lf, 'w')

    def stop(self, event):
        self.hm.UnhookMouse()
        self.hm.UnhookKeyboard()
        self.write()
        self.log.close()

    def write(self):
        while len(self.uiq) > 2:
            self.log.write(str(self.uiq.popleft()))
            self.log.write('\n')

if __name__ == '__main__':
    ch = taskmaster(sys.argv[1])
    ch.imgq.append(ImageGrab.grab())
    b = ch.imgq.popleft()
    for i in range(0, len(ch.imgq)):
        a = ch.imgq.popleft()
        diffname = os.path.join(ch.lp, "diff"+str(i)+".png")
        diff(b,a).save(diffname, "PNG")
        b = a
