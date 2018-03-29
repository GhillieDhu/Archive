import sys
import math

def get_lines(input_file):
    raw = open(input_file, 'r')
    mod = raw.readlines()
    raw.close()
    return mod

def collimate(lines):
    cells = []
    for line in lines:
        cells.append(line.split())
    return cells

def sect(full):
    column_headers = []
    for i in range(len(full)):
        if (full[i][:6] == ' PLATE'):
            column_headers.append(i)
    for j in range(len(column_headers)):
        section = []
        start = column_headers[j]+1
        if j < len(column_headers)-1:
            end = column_headers[j+1]
        else:
            end = len(full)
        for k in range(start, end):
            section.append(full[k])
        columns = collimate(section)
        for i in range(start, end):
            if (len(columns[i-start]) == 9):
                full[i] = columns[i-start]
    return full

def merge(cells, divisor):
    strung = cells[0]
    for i in range(1, len(cells)):
        strung += str('%11.4E' % (cells[i] / divisor)).rjust(12)
    return strung+'\n'

if __name__ == '__main__':
    lines = get_lines(sys.argv[1])
    sected = sect(lines)
    replaced = []
    aggregate = []
    count = 0
    for i in range(len(sected)):
        if (isinstance(sected[i], basestring)):
            if (len(aggregate) > 0):
                replaced.append(merge(aggregate, count))
            replaced.append(sected[i])
            aggregate = []
            count = 0
        else:
            count += 1
            if len(aggregate) == 0:
                for j in range(len(sected[i])):
                    aggregate.append(float(sected[i][j]))
                aggregate[0] = ' AVERAGE  '
            else:
                for j in range(1, len(sected[i])):
                    aggregate[j] += float(sected[i][j])
    if (len(aggregate) > 0):
        replaced.append(merge(aggregate, count))
    dump = open(sys.argv[2], 'w')
    dump.writelines(replaced)
    dump.close()
