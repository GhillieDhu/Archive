import os
import sys
from math import copysign, floor, log10

def round_sig(x, sig):
    if x == 0.0:
        return 0.0
    else:
        return copysign(round(abs(x), sig - int(floor(log10(abs(x)))) - 1), x)

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def get_includes(focalFile, includeFiles):
    for line in list(focalFile):
        try:
            if 'INCLUDE' == line[:7].upper():
                includeFile = open(line[9:-2], 'r')
                includeFiles.append(includeFile)
                includeFiles = get_includes(includeFile, includeFiles)
        except IndexError:
            pass
    return includeFiles

def numeric(s):
    try:
        return int(s)
    except ValueError:
        try:
            return round_sig(float(s), 3)
        except ValueError:
            try:
                if s[0] == '-':
                    return round_sig(float('-'+s[1:].replace('-', 'e-')), 3)
                else:
                    return round_sig(float(s.replace('-', 'e-').replace('+', 'e+')), 3)
            except (ValueError, IndexError) as e:
                return s

def parse_model(modelFilePath):
    modelMasterFile = open(modelFilePath, 'r')
    os.chdir(os.path.dirname(modelMasterFile.name))
    
    model = get_includes(modelMasterFile, [modelMasterFile])
    modelDict = {}
    for modelFile in model:
        modelFile.seek(0)
        modelLines = list(modelFile)
        for line in modelLines:
            if not '$' == line[0]:
                lineChunks = chunks(line[:-1], 8)
                chunkedLine = []
                for chunk in lineChunks:
                    chunkedLine.append(numeric(chunk.strip()))
                try:
                    modelDict[chunkedLine[0], chunkedLine[1]] = chunkedLine
                except IndexError:
                    pass
    return modelDict

if __name__ == '__main__':
    here = os.getcwd()
    masterDict = parse_model(sys.argv[1])
    os.chdir(here)
    slaveDict = parse_model(sys.argv[2])
    os.chdir(here)
    masterOnly = set(masterDict.keys()).difference(slaveDict.keys())
    slaveOnly = set(slaveDict.keys()).difference(masterDict.keys())
    both = set(masterDict.keys()).intersection(slaveDict.keys())
    print(len(masterOnly))
    print(len(slaveOnly))
    print(len(both))
    for entity in both:
        m = masterDict[entity]
        s = slaveDict[entity]
        comparison = [(i, j) for i, j in zip(m, s) if i != j]
        if len(comparison) > 0:
            print(str(masterDict[entity])+' '+str(slaveDict[entity]))
    print('-------------------------------')
    for entity in masterOnly:
        print(masterDict[entity])
    print('-------------------------------')
    for entity in slaveOnly:
        print(slaveDict[entity])
    # for files included in the master file, compare to the analogous file in the slave directory
