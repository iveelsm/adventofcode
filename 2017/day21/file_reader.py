import re
import numpy
import hashlib

def read_file(file_location):
    ret = {}
    try:
        with open(file_location) as contents:
            for line in contents:
                [key, value] = parse_line(line.rstrip("\n"))
                keys_hashes = construct_permutations(key)
                for i in keys_hashes:
                    ret[i] = value
    except IOError:
        print("Couldn't read file")
    return ret

def parse_line(line):
    regex = "(.*)\s=>\s(.*)"
    pattern = re.compile(regex)
    match = pattern.search(line)
    return [construct_grid(match.group(1)), construct_grid(match.group(2))]

def construct_grid(potential):
    ret = []
    lines = potential.split("/")
    for i in range(len(lines)):
        ret.append([])
        for j in range(len(lines[i])):
            to_add = 1 if lines[i][j] == '#' else 0
            ret[i].append(to_add)
    return ret

def construct_permutations(grid):
    ret = set()
    for axis in range(0, 3):
        for rotation in range(0, 360, 90):
            test = rotate(grid, rotation) if axis == 0 else rotate(flip(grid, axis - 1), rotation)
            test_hash = construct_hash(test.tolist())
            ret.add(test_hash)
    return ret

def rotate(grid, degrees):
    ret = numpy.rot90(grid, int(degrees / 90))
    return ret

def flip(grid, axis):
    ret = numpy.flip(grid, axis)
    return ret

def in_list(values, test):
    for i in values:
        if (numpy.array_equal(numpy.array(i), numpy.array(test))):
            return True
    return False

def construct_hash(test):
    string = []
    for i in test:
        string.append('{0:04b}'.format(int(''.join([str(x) for x in i]))))
    binary_string = ''.join(string).encode('utf-8')
    return hashlib.sha1(binary_string).hexdigest()
