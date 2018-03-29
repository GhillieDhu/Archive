from random import random
from time import sleep

if __name__ == '__main__':
    while True:
        print(random() / random())
        sleep(10 * random())
