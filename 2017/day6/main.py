import copy

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret = list(map(int, line.rstrip("\n").split("\t")))
    except IOError:
        print("Broke")
    return ret


def part2(input_arr):
    combinations = [];
    num_steps = 0
    combination = input_arr
    while combination not in combinations:
        combinations.append(copy.deepcopy(combination))
        combination = generate_new_combination(combination)
        num_steps += 1
    return num_steps - combinations.index(combination)


def part1(input_arr):
    combinations = [];
    num_steps = 0
    combination = input_arr
    while combination not in combinations:
        combinations.append(copy.deepcopy(combination))
        combination = generate_new_combination(combination)
        num_steps += 1
    return num_steps

def get_max_index(arr):
    return [max(arr), arr.index(max(arr))]

def generate_new_combination(combination):
    [max_value, index] = get_max_index(combination)
    combination[index] = 0
    i = 1
    for j in range(max_value, 0, -1):
        if index + i >= len(combination):
            index = 0
            i = 0
        combination[index + i] += 1
        i += 1
    return combination

def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = part1(input_arr)
    print(ret)
    input2_arr = read_file(file_location)
    ret2 = part2(input2_arr)
    print(ret2)

if "__main__":
    main()
