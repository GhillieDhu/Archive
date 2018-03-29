if __name__ == '__main__':
    from imageDiff import diff
    from PIL import Image
    import sys
    b = Image.open(sys.argv[1])
    a = Image.open(sys.argv[2])
    diff(b,a).save(sys.argv[3], "PNG")
