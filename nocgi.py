import sys
import os

if __name__ == '__main__':
    a = sys.argv[1].split("%2F%2F")[1].split("%3F")[0].replace("%2F","/")
    os.system('"C://Program Files (x86)//Google//Chrome//Application//chrome.exe" --incognito '+a+'')
