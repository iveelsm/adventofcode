from file_reader import construct_hash
import numpy
import sys

def apply_rule(grid, rules):
    size = len(grid)
    grids = divide(grid, 2) if size % 2 == 0 else divide(grid, 3)
    for i in range(len(grids)):
        grids[i] = enhance(grids[i], rules)

    ret = combine_grids(grids, size)
    return ret

def divide(grid, amount):
    ret = []
    for index in range(0, len(grid), amount):
        for j in range(0, len(grid), amount):
            ret.append([grid[index + x][j : j + amount] for x in range(amount)])
    return ret

def enhance(grid, rules):
    control = construct_hash(grid)
    return rules[control]

def combine_grids(grids, size):
    ret = []
    num_grids = int(size / 2) if size % 2 == 0 else int(size / 3)
    stacked_grids = []
    for i in range(0, len(grids), num_grids):
        stacked_grids.append(numpy.hstack(grids[i : i + num_grids]))
    ret = numpy.vstack(stacked_grids)
    return ret.tolist()
