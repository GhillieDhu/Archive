import math
import sys

if __name__ == '__main__':
    before = open(sys.argv[1], 'r')
    primelist = before.readlines()
    before.close()
    for i in range(len(primelist)):
        primelist[i] = int(primelist[i][:-1])
    prior_max = primelist[-1]
    for candidate in range(prior_max, prior_max + int(sys.argv[2])):
        for prime in primelist:
            if candidate % prime == 0:
                break
        else:
            primelist.append(candidate)
            print(candidate)
    for i in range(len(primelist)):
        primelist[i] = str(primelist[i])+'\n'
    after = open(sys.argv[1], 'w')
    after.writelines(primelist)
    after.close()
