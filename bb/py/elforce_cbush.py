import csv
import math
import sys

def parse_force_lines(force_lines):
    hook = ' BUSH  #         F-X         F-Y         F-Z         M-X         M-Y        M-Z  \n'
    offset = -1
    loadcase_tag = (-1, 'LOAD:', 8)
    content = 2
    release = 'LOAD' #contains
    loadcase_dict = parse_lines(force_lines, hook, offset, loadcase_tag, content, release)
    return split_dict(loadcase_dict, 0)

def parse_f06_lines(f06_lines):
    hook = '                                 F O R C E S   I N   B U S H   E L E M E N T S        ( C B U S H )\n'
    offset = -4
    loadcase_tag = (-2, 'SUBCASE', 5)
    content = 7
    release = 'PAGE' #contains
    loadcase_dict = parse_lines(f06_lines, hook, offset, loadcase_tag, content, release)
    return split_dict(loadcase_dict, 1)

def parse_lines(lines, hook, offset, loadcase_tag, content, release):
    breaks = {}
    on = False
    for i in range(len(lines)):
        if lines[i] == hook:
            start = i
            loadcase = int(lines[i + loadcase_tag[0]][lines[i + loadcase_tag[0]].find(loadcase_tag[1]) + len(loadcase_tag[1]):lines[i + loadcase_tag[0]].find(loadcase_tag[1]) + len(loadcase_tag[1]) + loadcase_tag[2]])
            on = True
        if on and release in lines[i]:
            on = False
            breaks[loadcase] = (start + offset, i - 1)
    if on:
        breaks[loadcase] = (start + offset, len(lines) - 1)
    excerpt = {}
    for loadcase in breaks:
        excerpt[loadcase] = lines[breaks[loadcase][0] + content:breaks[loadcase][1] + 1]
    return excerpt

def split_dict(loadcase_dict, offset):
    loadcase_elem_dict = {}
    for loadcase in loadcase_dict:
        for line in loadcase_dict[loadcase]:
            split_line = line[offset:].split()
            loadcase_elem_dict[(loadcase, int(split_line[0]))] = (float(split_line[1]), float(split_line[2]), float(split_line[3]), float(split_line[4]), float(split_line[5]), float(split_line[6]))
    return loadcase_elem_dict

if __name__ == '__main__':
    # f_x, f_y, f_z, m_x, m_y, m_z = elforce(source, loadcase, eid)
    force_file = open(sys.argv[1])
    force_lines = force_file.readlines()
    force_dict = parse_force_lines(force_lines)
    f06_file = open(sys.argv[2])
    f06_lines = f06_file.readlines()
    f06_dict = parse_f06_lines(f06_lines)
    dict_writer = csv.writer(open(sys.argv[3], 'w', newline=''))
    dict_writer.writerow(['Subcase', 'EID', 'F_x(f06)', 'F_y(f06)', 'F_z(f06)', 'F_x', 'F_y', 'F_z'])
    for lc, eid in force_dict:
        fx, fy, fz, mx, my, mz = force_dict[(lc, eid)]
        fx6, fy6, fz6, mx6, my6, mz6 = f06_dict[(lc, eid)]
        dict_writer.writerow([lc, eid, fx6, fy6, fz6, fx, fy, fz])
