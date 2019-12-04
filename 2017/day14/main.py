from hasher import knot_hash
import sys

def read_file(file_location):
    ret = ""
    try:
        with open(file_location) as contents:
            ret = contents.readline().rstrip("\n")
    except IOError:
        print("Couldn't read file")
    return ret


def part_one(input_str):
    hash_board = create_board(input_str)
    ret = 0
    for i in hash_board:
        for j in i:
            if j == '1':
                ret += 1
    return ret


def part_two(input_str):
    hash_board = create_board(input_str)
    print_board(hash_board)
    hash_board = regionize(hash_board)
    print_board(hash_board)
    return max([max(k) for k in hash_board]) - 1

def regionize(hash_board):
    current_group = 1
    for i in range(len(hash_board)):
        for j in range(len(hash_board[0])):
            if hash_board[i][j] == 1:
                current_group += 1
                hash_board[i][j] = current_group
                connected_values = get_connections(hash_board, [i, j])
                while len(connected_values) != 0:
                    new_values = []
                    for k in connected_values:
                        hash_board[k[0]][k[1]] = current_group
                        new_values.extend(get_connections(hash_board, [k[0], k[1]]))
                    connected_values = new_values
    return hash_board

def get_connections(hash_board, location):
    connections = []
    x = location[0]
    y = location[1]
    for i in range((-1 + x), (x + 2), 2):
        if in_bounds(i, y) and hash_board[i][y] == 1:
            connections.append((i, y))
    for j in range((-1 + y), (y + 2), 2):
        if in_bounds(x, j) and hash_board[x][j] == 1:
            connections.append((x, j))
    return connections

def in_bounds(x, y):
    return x >= 0 \
    and x < 128 \
    and y >= 0 \
    and y < 128

def create_board(input_str):
    ret = []
    for i in range(0, 128):
        ret.append(build_line(input_str, i))
    return ret

def build_line(input_str, i):
    knot_hash = hash_string(input_str + "-" + str(i))
    ret = '{0:0128b}'.format(int(knot_hash, 16))
    return list(map(int, list(ret)))

def hash_string(input_str):
    ascii_string = list(map(ord, input_str))
    ascii_string.extend([17, 31, 73, 47, 23])
    return knot_hash(ascii_string)

def main():
    file_location = "./inputs/input.txt"
    input_str = read_file(file_location)
    ret = part_one(input_str)
    print(ret)

    input2_str = read_file(file_location)
    ret2 = part_two(input2_str)
    print(ret2)

if "__main__":
    main()
