def read_file(file_location):
    ret = ""
    try:
        with open(file_location) as contents:
            ret = contents.readline().rstrip("\n")
    except IOError:
        print("Couldn't read the file!")
    return ret


def part_one(input_str):
    char_list = []
    ret = 0
    i = 0
    in_garbage = False
    while i < len(input_str):
        if input_str[i] == "!":
            i += 1
        else:
            if in_garbage:
                if input_str[i] == ">":
                    in_garbage = False
            elif input_str[i] == "<":
                in_garbage = True
            else:
                [char_list, inc] = apply_operation(char_list, input_str[i])
                ret += inc
        i += 1

    return ret


def part_two(input_str):
    char_list = []
    ret = 0
    i = 0
    number_chars_garbage = 0
    in_garbage = False
    while i < len(input_str):
        if input_str[i] == "!":
            i += 1
        else:
            if in_garbage:
                if input_str[i] == ">":
                    in_garbage = False
                else:
                    number_chars_garbage += 1
            elif input_str[i] == "<":
                in_garbage = True
            else:
                [char_list, inc] = apply_operation(char_list, input_str[i])
                ret += inc
        i += 1

    return number_chars_garbage


def apply_operation(char_list, i):
    if i == '{':
        return add_value(char_list, i)
    elif i == '}':
        return remove_until_last(char_list, '{')
    else:
        return [char_list, 0]


def add_value(char_list, i):
    char_list.append(i)
    return [char_list, 0]


def remove_until_last(char_list, char):
    slice_index = ''.join(char_list).rfind(char)
    ret = number_of_left_braces(char_list)
    return [char_list[:slice_index], ret]


def number_of_left_braces(char_list):
    return char_list.count("{")


def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = part_one(input_arr)
    print(ret)

    input2_arr = read_file(file_location)
    ret2 = part_two(input2_arr)
    print(ret2)


if "__main__":
    main()