import operator
import sys
import time

NUMBER_ACTIVITY_BURSTS = 10000000

def read_file(file_location):
    ret = {}
    index = 0 # start
    try:
        with open(file_location) as contents:
            for line in contents:
                for j in range(len(line.rstrip("\n"))):
                    ret[(index, j)] = 2 if line[j] == '#' else 0
                index += 1
    except IOError:
        print("Couldn't read file")
    return [ret, index]


def part_one(board, size):
    current = (int(size / 2), int(size / 2), 0)
    print("Start: " + str(current))
    infected = 0
    for i in range(NUMBER_ACTIVITY_BURSTS):
        [x, y, _] = current
        current = turn_and_move(board, current)
        board[(x, y)] = (board[(x, y)] + 1) % 4
        if board[(x, y)] == 2:
            infected += 1
    return infected


def turn_and_move(board, current):
    operation_dict = {
        0 : 'l',
        1 : 'x',
        2 : 'r',
        3 : 'f'
    }

    direction = int((360 \
        + current[2] \
        + turn(operation_dict[board[(current[0], current[1])]]) \
        ) % 360)

    x, y = move({
        'x' : current[0],
        'y' : current[1],
        'd' : direction })

    expand_board(board, {'x' : x, 'y': y})

    return (x, y, direction)

def expand_board(board, locations):
    if not (locations['x'], locations['y']) in board:
        board[(locations['x'], locations['y'])] = 0

def turn(direction):
    return {
        'l' : -90,
        'x' : 0,
        'r' : 90,
        'f' : 180
    }[direction]


def move(current):
    move_dict = {
        0   : (-1,  0),
        90  : ( 0,  1),
        180 : ( 1,  0),
        270 : ( 0, -1)
    }
    return add((current['x'], current['y']), move_dict[current['d']])


def add(a, b):
    return tuple(map(operator.add, a, b))


def main():
    file_location = "./inputs/input.txt"
    [input_arr, size] = read_file(file_location)
    start_time = time.time()
    ret = part_one(input_arr, size)
    print("Number of infected nodes: " + str(ret))
    print("Time: " + str(time.time() - start_time))

if "__main__":
    main()
