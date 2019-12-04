import operator
import re

def read_file(file_location):
    ret = {}
    particle_no = 0
    try:
        with open(file_location) as contents:
            for line in contents:
                ret[particle_no] = parse_line(line.rstrip("\n"))
                particle_no += 1
    except IOError:
        print("Couldn't read file!")
    return ret


def parse_line(line):
    ret = {}

    regex_component = "(p=.*),\s(v=.*),\s(a=.*)"
    component = re.compile(regex_component)

    regex_individual = "([a-z])=<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>"
    individual = re.compile(regex_individual)

    component_match = component.search(line)
    for i in range(1, 4):
        individual_match = individual.search(component_match.group(i))
        ret[individual_match.group(1)] = ( \
                                        int(individual_match.group(2)), \
                                        int(individual_match.group(3)), \
                                        int(individual_match.group(4)))
    return ret

def part_one(input_arr):
    for j in range(1000):
        for value, key in input_arr.items():
            input_arr[value]['v'] = add(key['v'], key['a'])
            input_arr[value]['p'] = add(key['p'], key['v'])
    return find_closest(input_arr)

def part_two(input_arr):
    for j in range(1000):
        for value, key in input_arr.items():
            input_arr[value]['v'] = add(key['v'], key['a'])
            input_arr[value]['p'] = add(key['p'], key['v'])
        input_arr = find_and_filter_collisions(input_arr)
    return len(input_arr)


def initialize_collisions_dict(keys):
    collisions_dict = {}
    for i in keys:
        collisions_dict[i] = False
    return collisions_dict


def find_and_filter_collisions(input_arr):
    collisions_dict = initialize_collisions_dict(input_arr.keys())

    for control_key, control_value in input_arr.items():
        slice_dict = {key : input_arr[key] for key in filter(lambda x: x > control_key, input_arr.keys())}
        for test_key, test_value in slice_dict.items():
            if collisions_dict[control_key] == False or collisions_dict[test_key] == False:
                if control_value['p'] == test_value['p']:
                    collisions_dict[control_key] = True
                    collisions_dict[test_key] = True

    return filter_collisions(input_arr, collisions_dict)

def filter_collisions(input_arr, collisions_dict):
    return {key: input_arr[key] for key in filter(lambda x: collisions_dict[x] == False, collisions_dict.keys())}

def find_closest(particles):
    closest_particle = 0
    closest_distance = (1000000, 1000000, 1000000)
    for key, value in particles.items():
        if is_closer(value['p'], closest_distance):
            closest_distance = value['p']
            closest_particle = key
    return closest_particle


def add(tuple_one, tuple_two):
    return tuple(map(operator.add, tuple_one, tuple_two))


def is_closer(tuple_one, tuple_two):
    return sum([abs(x) for x in tuple_one]) < sum([abs(x) for x in tuple_two])


def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = part_one(input_arr)
    print("Closest particle: " + str(ret))

    input2_arr = read_file(file_location)
    ret2 = part_two(input2_arr)
    print("Length after collisions removal: " + str(ret2))

if "__main__":
    main()
