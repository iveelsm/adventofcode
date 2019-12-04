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
    operations_list = []
    while i < len(instructions):
        [operation, variable, value] = parse_line(instructions[i])
        operations_list.append(operation)
        i += apply_operation(variable_dict, i, [operation, variable, value])
    return operations_list

def part_two():
    h = 0
    b = 57
    c = b
    b = b * 100
    b = b + 100000
    c = b + 17000

    while True:  # E
        f = 1
        d = 2
        e = 2

        while True:  # B
            if b % d == 0:
                f = 0
            d = d + 1
            if d != b:
                continue

            if f == 0:
                h = h + 1

            if b == c:
                return(h)

            b = b + 17
            break

def parse_line(instruction):
    regex = "([a-z]+)\s([-?a-z0-9])\s?([-?a-z0-9]+)?"
    pattern = re.compile(regex)
    match = pattern.search(instruction)
    if match.group(3):
        return [match.group(1), match.group(2), match.group(3)]
    else:
        return [match.group(1), match.group(2), 0]

def apply_operation(variable_dict, index, instruction):
    operation_dict = {
        "sub" : subtract,
        "mul" : multiply,
        "set" : set_value,
        "jnz" : jump
    }
    return operation_dict[instruction[0]](variable_dict, index, instruction[1], instruction[2])


def subtract(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] -= value
    return 1


def multiply(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] = variable_dict[variable] * value
    return 1


def set_value(variable_dict, index, variable, value):
    value = alpha_to_numeric(variable_dict, value)
    variable_dict[variable] = value
    return 1

def jump(variable_dict, index, variable, value):
    if variable.isdigit():
        return int(value) if int(variable) != 0 else 1
    elif variable_dict[variable] != 0:
        return int(value)
    else:
        return 1

def alpha_to_numeric(variable_dict, value):
    if value.isdigit():
        return int(value)
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
    operations_list = part_one(input_instructions)
    print("Number of operations: " + str(len([x for x in operations_list if x == 'mul'])))

    input2_instructions = read_file(file_location)
    h_value = part_two()
    print("Value of h: " + str(h_value))


if "__main__":
    main()
