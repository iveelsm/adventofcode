from functools import reduce

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            line = contents.readline().rstrip("\n")
            ret = list(map(int, line.split(",")))
    except:
        print("Couldn't read the file")
    return ret

def read_file_two(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            line = contents.readline().rstrip("\n")
            ret = list(map(ord, line))
            ret.extend([17, 31, 73, 47, 23])
    except:
        print("Couldn't read the file")
    return ret



def part_one(circular_list, list_mods):
    skip_size = 0
    cursor = 0
    for i in list_mods:
        circular_list = apply_operation(i, cursor, circular_list)
        cursor = cursor + i + skip_size
        skip_size += 1
        cursor = cursor % len(circular_list)
    return circular_list


def part_two(circular_list, list_mods):
    skip_size = 0
    cursor = 0
    ret = []
    
    for i in range(64):
        for j in list_mods:
            apply_operation(j, cursor, circular_list)
            cursor += j + skip_size
            cursor = cursor % len(circular_list)
            skip_size += 1

    for i in range(0, len(circular_list), 16):
        ret.append("%0.2x"%reduce((lambda x, y : x ^ y), circular_list[i: i + 16]))
    return ''.join(ret)


def apply_operation(operation, cursor, circular_list):
    list_slice = []
    if cursor + operation >= len(circular_list):
        pivot = (cursor + operation) % len(circular_list)
        list_slice = circular_list[cursor:] + circular_list[:pivot]
        list_slice = list_slice[::-1]
        circular_list[cursor:] = list_slice[:len(list_slice) - pivot]
        circular_list[:pivot] = list_slice[len(list_slice) - pivot:]
    else:
        list_slice = circular_list[cursor:(cursor + operation)]
        list_slice = list_slice[::-1]
        circular_list[cursor:(cursor + operation)] = list_slice
    return circular_list


def set_cursor(current_cursor, max_size):
    while current_cursor > max_size:
        current_cursor -= max_size
    return current_cursor

def main():
    file_location = "./inputs/input.txt"

    list_mods = read_file(file_location)
    circular_list = list(range(0, 256))
    result = part_one(circular_list, list_mods)
    print(str(result[0] * result[1]))

    file_location = "./inputs/input.txt"
    list2_mods = read_file_two(file_location)
    circular_2list = list(range(0, 256))

    result = part_two(circular_2list, list2_mods)
    print(result)

if "__main__":
    main()
