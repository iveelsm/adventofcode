import re

def read_file(file_location, regex):
    instructions_match_arr = []
    variable_set = set()
    pattern = re.compile(regex)

    try:
        with open(file_location) as contents:
            for line in contents:
                match = pattern.match(line)
                instructions_match_arr.append(match)
                variable_set.add(match.group(1))
                variable_set.add(match.group(5))
    except IOError:
        print("Couldn't read the file!")

    variable_dict = {}
    for i in variable_set:
        variable_dict[i] = 0

    return [instructions_match_arr, variable_dict]

def part_one(input_arr, variable_dict):
    for i in input_arr:
        if is_valid(variable_dict[i.group(5)], i.group(6), int(i.group(7))):
            variable_dict = apply_operation(variable_dict, [i.group(1), i.group(2), i.group(3)])

    return max(variable_dict.values())

def is_valid(value, boolean, test):
    boolean_operators = {
        ">=" : value >= test,
        ">"  : value > test,
        "==" : value == test,
        "<"  : value < test,
        "<=" : value <= test,
        "!=" : value != test
    }
    return boolean_operators[boolean]

def apply_operation(dict_var, operations):
    operatee = operations[0]
    operation = operations[1]
    value = int(operations[2])

    if operation == "inc":
        dict_var[operatee] += value
    elif operation == "dec":
        dict_var[operatee] -= value
    return dict_var

def part_two(input_arr, variable_dict):
    max_ret = 0
    for i in input_arr:
        if is_valid(variable_dict[i.group(5)], i.group(6), int(i.group(7))):
            variable_dict = apply_operation(variable_dict, [i.group(1), i.group(2), i.group(3)])
            if variable_dict[i.group(1)] > max_ret:
                max_ret = variable_dict[i.group(1)]

    return max_ret

def main():
    regex = "([a-zA-Z]*)[\s+]([a-zA-Z]*)[\s+]([-0-9]+)[\s+]([a-zA-Z]*)[\s+]([a-zA-Z]*)[\s+](.*)[\s+]([-0-9]+)"
    file_location = "./inputs/input.txt"

    [input_arr, var_set] = read_file(file_location, regex)
    ret = part_one(input_arr, var_set)
    print(ret)

    [input2_arr, var2_set] = read_file(file_location, regex)
    ret2 = part_two(input2_arr, var2_set)
    print(ret2)

if "__main__":
    main()
