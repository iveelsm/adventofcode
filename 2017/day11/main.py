
def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            line = contents.readline().rstrip("\n")
            ret = line.split(",")
    except:
        print("Couldn't read the file")
    return ret

def part_one(steps):
    ret = [0, 0, 0]
    for i in steps:
        [x, y, z] = find_coordinates(i)
        ret[0] += x
        ret[1] += y
        ret[2] += z
    return (abs(ret[0]) + abs(ret[1]) + abs(ret[2])) / 2

def part_two(steps):
    ret = []
    x = 0
    y = 0
    z = 0
    for i in steps:
        [x_delta, y_delta, z_delta] = find_coordinates(i)
        x += x_delta
        y += y_delta
        z += z_delta
        ret.append((abs(x) + abs(y) + abs(z)) / 2)
    return max(ret)

def find_coordinates(i):
    movement_dict = {
        "sw" : [-1, 0, 1],
        "se" : [1, -1, 0],
        "s"  : [0, -1, 1],
        "n"  : [0, 1, -1],
        "ne" : [1, 0, -1],
        "nw" : [-1, 1, 0]
    }
    return movement_dict[i]


def main():
    file_location = "./inputs/input.txt"

    steps = read_file(file_location)
    result = part_one(steps)
    print(result)

    file_location = "./inputs/input.txt"
    steps2 = read_file(file_location)

    result2 = part_two(steps2)
    print(result2)

if "__main__":
    main()
