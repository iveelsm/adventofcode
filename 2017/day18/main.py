import re

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(line.rstrip("\n"))
    except IOError:
        print("Couldn't read the file")
    return ret


def part_one(instructions):
    variable_dict = build_variable_dict(instructions)
    i = 0
    latest_sound = {'a' : '0'}
    operations_list = []
    while i < len(instructions):
        [operation, variable, value] = parse_line(instructions[i])
        operations_list.append(operation)
        if operation == "snd":
            latest_sound = {}
            latest_sound[variable] = variable_dict[variable]
            i += 1
        elif operation == "rcv":
            if variable_dict[variable] != 0:
                return [latest_sound, operations_list]
            i += 1
        else:
            [variable_dict, i] = apply_operation(variable_dict, i, [operation, variable, value])

    return [latest_sound, operations_list]

def parse_line(instruction):
    regex = "([a-z]+)\s([a-z])\s?([-?a-z0-9]+)?"
    pattern = re.compile(regex)
    match = pattern.search(instruction)
    if match.group(3):
        return [match.group(1), match.group(2), match.group(3)]
    else:
        return [match.group(1), match.group(2), 0]

def apply_operation(variable_dict, index, instruction):
    operation_dict = {
        "add" : add,
        "mul" : multiply,
        "set" : set_value,
        "jgz" : jump,
        "mod" : modulus
    }
    return operation_dict[instruction[0]](variable_dict, index, instruction[1], instruction[2])

def add(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] += value
    index += 1
    return[variable_dict, index]

def multiply(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] = variable_dict[variable] * value
    index += 1
    return[variable_dict, index]

def set_value(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] = value
    index += 1
    return [variable_dict, index]

def jump(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    if variable_dict[variable] > 0:
        index += value
    else:
        index += 1
    return[variable_dict, index]

def modulus(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] = variable_dict[variable] % value
    index += 1
    return[variable_dict, index]


def alpha_to_numeric(variable_dict, value):
    if value.isalpha():
        return int(variable_dict[value])
    return int(value)

def build_variable_dict(instructions):
    ret = {}
    regex = ".*([a-z]).*"
    pattern = re.compile(regex)
    for i in instructions:
        match = pattern.search(i)
        if not match.group(1) in ret:
            ret[match.group(1)] = 0
    return ret


def main():
    file_location = "./inputs/input.txt"
    input_instructions = read_file(file_location)
    [ret, operations_list] = part_one(input_instructions)
    print(ret)
    print("Number of operations: " + str(len(operations_list)))

if "__main__":
    main()
