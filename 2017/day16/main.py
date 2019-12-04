import time

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            line = contents.readline().rstrip("\n")
            ret = line.split(",")
    except IOError:
        print("Couldn't read file")
    return ret


def part_one(input_arr, programs):
    for i in input_arr:
        programs = apply_operation(i, programs)
    return programs

def part_two(input_arr, programs):
    repititions = 1000000000
    seen_dances = []
    for i in range(repititions):
        string = ''.join(programs)
        if string in seen_dances:
            return (seen_dances[(repititions % i) - 1])
        seen_dances.append(string)
        programs = part_one(input_arr, programs)

    return programs

def apply_operation(operation, programs):
    return {
        "s" : spin,
        "x" : swap,
        "p" : partner
    }[operation[0]](operation, programs)

def spin(operation, programs):
    spin_size = int(operation[1:])
    programs = programs[-spin_size:] + programs[:-spin_size]
    return programs

def swap(operation, programs):
    programs_to_swap = list(map(int, operation[1:].split("/")))
    programs[programs_to_swap[1]], programs[programs_to_swap[0]] = programs[programs_to_swap[0]], programs[programs_to_swap[1]]
    return programs

def partner(operation, programs):
    programs_to_swap = operation[1:].split("/")
    a, b = programs.index(programs_to_swap[0]), programs.index(programs_to_swap[1])
    programs[b], programs[a] = programs[a], programs[b]
    return programs


def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    programs = list('abcdefghijklmnop')
    ret = part_one(input_arr, programs)
    print(''.join(ret))

    ret2 = part_two(input_arr, ret)
    print(''.join(ret2))

if "__main__":
    main()
