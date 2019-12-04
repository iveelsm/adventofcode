import sys
import operator

UPPER_Y_BOUND = 200
UPPER_X_BOUND = 200
LOWER_X_BOUND = 0
LOWER_Y_BOUND = 0

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(line.rstrip("\n").ljust(UPPER_Y_BOUND))
    except IOError:
        print("Couldn't read the file")
    return ret


def print_grid(grid):
    # print("      ", end="")
    # for i in range(0, len(grid[0])):
    #     print(i % 10, end="")
    # print("")
    for i in range(0, len(grid)):
        print('{:3}'.format(i) + ": " + str(grid[i]))


def part_one(grid, steps):
    ret = []
    location = (0, grid[0].index("|"))
    direction = "d"

    while peek_next_move(location, grid, direction) is not None:
        if peek_next_move(location, grid, direction) is "+":
            location = take_step(direction, location)
            steps += 1
            direction = turn(location, grid, direction)
        if is_letter(peek_next_move(location, grid, direction)):
            ret.append(peek_next_move(location, grid, direction))
        location = take_step(direction, location)
        steps += 1

    return [ret, steps]


def turn(location, grid, direction):
    turned_direction = find_direction(location, grid, direction)
    return turned_direction


def add(a, b):
    return tuple(map(operator.add, a, b))


def peek_next_move(location, grid, direction):
    test = take_step(direction, location)
    if out_of_bounds(test) is True:
        return None
    elif grid[test[0]][test[1]] is " ":
        return None
    else:
        return grid[test[0]][test[1]]


def out_of_bounds(test):
    return test[0] >= UPPER_X_BOUND \
    or test[1] >= UPPER_Y_BOUND \
    or test[0] < LOWER_X_BOUND \
    or test[1] < LOWER_Y_BOUND


def take_step(direction, location):
    step_dict = {
        "d" : ( 1,  0),
        "r" : ( 0,  1),
        "l" : ( 0, -1),
        "u" : (-1,  0)
    }
    return add(location, step_dict[direction])


def is_letter(value):
    return value.isalpha()


def opposite(direction):
    return {
        "d" : "u",
        "l" : "r",
        "r" : "l",
        "u" : "d"
    }[direction]


def find_direction(location, grid, direction):
    potentials = ["d", "u", "r", "l"]
    potentials.remove(opposite(direction))
    value = grid[location[0]][location[1]]
    for i in potentials:
        if peek_next_move(location, grid, i) is not None:
            return i
    return None


def main():
    file_location = "./inputs/input.txt"
    grid = read_file(file_location)
    print_grid(grid)
    [ret, steps] = part_one(grid, 1)
    print(''.join(ret))
    print(steps)

if "__main__":
    main()
