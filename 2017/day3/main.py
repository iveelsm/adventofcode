import math
import sys
from Square import Square

def read_file(file_location):
    ret = 0
    try:
        with open(file_location) as contents:
            ret = contents.readline().rstrip("\n")
    except IOError:
        print("Coudln't read file")

    return int(ret)


def part_one(input_number):
    square = construct_square(input_number)
    height = 0
    length = 0
    print(square.square_dict)
    [height, length] = square.get_value(input_number)

    return abs(height) + abs(length)


def part_two(input_number):
    for x in sum_spiral():
        if x > n:
            return x


def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]


def construct_square(number):
    square = Square()
    square_size = 3
    i = 2
    current_x = 1
    current_y = 0
    while i < number + 1:
        while current_y < 0 :
            square.add_value(current_x, current_y, i)
            current_y += 1
            i += 1
        for j in range(0, int(square_size / 2)):
            square.add_value(current_x, current_y, i)
            current_y += 1
            i += 1
        for j in range(0, int(square_size) - 1):
            square.add_value(current_x, current_y, i)
            current_x -= 1
            i += 1
        for j in range(0, int(square_size) - 1):
            square.add_value(current_x, current_y, i)
            current_y -= 1
            i += 1
        for j in range(0, int(square_size)):
            square.add_value(current_x, current_y, i)
            current_x += 1
            i += 1
        square_size += 2
    return square


def get_corner(square_size):
    return [-1 * int(square_size / 2), -1 * int(square_size / 2)]


def main():
    file_location = "./inputs/input.txt"

    input_number = read_file(file_location)
    # input_number = 1024
    ret = part_one(input_number)
    print(ret)


    input2_number = read_file(file_location)
    # input_number = 1024
    ret2 = part_two(input_number)
    print(ret2)

if "__main__":
    main()
