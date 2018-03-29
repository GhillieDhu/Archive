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

def get_unique(line):
    lineChunks = chunks(line[:-1], 8)
    chunkedLine = []
    for chunk in lineChunks:
        chunkedLine.append(numeric(chunk.strip()))
    try:
        return (chunkedLine[0], chunkedLine[1])
    except IndexError:
        return None

if __name__ == '__main__':
    here = os.getcwd()
    raw_lines = list(open(sys.argv[1], 'r'))
    entities_lines = list(open(sys.argv[2], 'r'))
    processed_lines = []
    entities_dict = {}
    for line in entities_lines:
        entities_dict[get_unique(line)] = line
    for line in raw_lines:
        if get_unique(line) in entities_dict:
            processed_lines.append(entities_dict[get_unique(line)])
        else:
            processed_lines.append(line)
    processed_file = open(sys.argv[3], 'w')
    processed_file.writelines(processed_lines)
    processed_file.close()
