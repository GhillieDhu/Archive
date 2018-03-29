import win32api
import win32con
import sys
import pixel
from time import sleep
from SendKeys import SendKeys
from subprocess import Popen
from str2tuple import str2tuple

class homunculus:

    def dispatch(self, t):
        print(t)
        try:
            {
            'LD': lambda cdr: self.mouse(cdr, win32con.MOUSEEVENTF_LEFTDOWN),
            'LU': lambda cdr: self.mouse(cdr, win32con.MOUSEEVENTF_LEFTUP),
            'RD': lambda cdr: self.mouse(cdr, win32con.MOUSEEVENTF_RIGHTDOWN),
            'RU': lambda cdr: self.mouse(cdr, win32con.MOUSEEVENTF_RIGHTUP),
            'KD': lambda cdr: self.keyboard(cdr, 0),
            'KU': lambda cdr: self.keyboard(cdr, 2),
            'pixel': lambda cdr: self.pixel(cdr),
            'type': lambda cdr: self.type(cdr),
            'wait': lambda cdr: sleep(cdr[0]),
            'if': lambda cdr: self.varpix(cdr),
            'call': lambda cdr: Popen(cdr)
            }[t[0]](t[1:])
        except KeyError:
            print('Unknown tag in tuple '+str(t))

    def mouse(self, xy, event):
        try:
            x, y = xy[0]
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(event, x, y, 0, 0)
        except ValueError:
            print('Malformed mouse tuple '+str(xy))

    def keyboard(self, key, event):
        try:
            keyCode = int(key[0])
            win32api.keybd_event(keyCode, 0, event, 0)
        except ValueError:
            print('Malformed key tuple '+str(key))

    def type(self, s):
        try:
            if s[0] == 'exit':
                raise NameError
            SendKeys(eval(s[0]))
        except NameError:
            SendKeys(s[0])
        finally:
            self.keyboard((13,), 0)
            self.keyboard((13,), 2)

    def pixel(self, t):
        try:
            xy, rgb = t
            if len(rgb) == 3:
                x, y = xy
                while pixel.color(x, y) != rgb:
                    pass
            else:
                print('Malformed pixel color subtuple')
        except ValueError:
            print('Malformed pixel tuple '+str(t))

    def varpix(self, cdr):
        try:
            ifs = cdr[0]
            t = cdr[1]
            throwaway, xy, rgb = t
            if len(rgb) == 3:
                x, y = xy
                while pixel.color(x, y) != rgb:
                    for j in range(0, len(ifs)):
                        cond, act = ifs[j]
                        condthrow, condxy, condrgb = cond
                        condx, condy = condxy
                        if pixel.color(condx, condy) == condrgb:
                            for i in range(0, len(act)):
                                self.dispatch(act[i])
            else:
                print('Malformed pixel color subtuple')
        except ValueError:
            print('Malformed pixel tuple '+str(t))

    def sequence(self, filename):
        file = open(filename, 'r')
        command = ('wait', 0)
        while command != ():
            self.dispatch(command)
            command = str2tuple(file.readline())
        file.close()

    def fileseq(self, metafilename):
        metafile = open(metafilename, 'r')
        filename = file.readline()[:-1]
        while filename != '':
            self.sequence(filename)
            filename = file.readline()[:-1]
        file.close()

if __name__ == '__main__':
    h = homunculus()
    if sys.argv[1] == '-f':
        for i in range(1, len(sys.argv) - 1):
            h.fileseq(sys.argv[i + 1])
    else:
        for i in range(0, len(sys.argv) - 1):
            h.sequence(sys.argv[i + 1])
