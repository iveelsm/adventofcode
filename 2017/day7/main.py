import sys
import re
import json

def read_file(file_location):
    ret = []
    regex_bottom = "(.*)[\s*](\(\d+\))[\s*](->)(.*)"
    regex_top = "(.*)[\s*](\(\d+\))"
    pattern_bottom = re.compile(regex_bottom)
    pattern_top = re.compile(regex_top)
    try:
        with open(file_location) as contents:
            for line in contents:
                line = line.rstrip("\n")
                retToAdd = {}
                if pattern_bottom.search(line):
                    match = pattern_bottom.match(line)
                    weight = int(match.group(2)[1:-1])
                    retToAdd = { weight : { match.group(1) : [x.strip() for x in match.group(4).split(", ")] } }
                elif pattern_top.search(line):
                    match = pattern_top.match(line)
                    weight = int(match.group(2)[1:-1])
                    retToAdd = { weight : { match.group(1) : [] } }
                else:
                    print("No match?")
                ret.append(retToAdd)
    except IOError:
        print("Broke")
    return ret

def read_file_two(file_location):
    ret = {}
    regex_bottom = "(.*)[\s*](\(\d+\))[\s*](->)(.*)"
    regex_top = "(.*)[\s*](\(\d+\))"
    pattern_bottom = re.compile(regex_bottom)
    pattern_top = re.compile(regex_top)
    try:
        with open(file_location) as contents:
            for line in contents:
                line = line.rstrip("\n")
                retToAdd = {}
                if pattern_bottom.search(line):
                    match = pattern_bottom.match(line)
                    weight = int(match.group(2)[1:-1])
                    ret[match.group(1)] = { "weight": weight, "children" : [x.strip() for x in match.group(4).split(", ")] }
                elif pattern_top.search(line):
                    match = pattern_top.match(line)
                    weight = int(match.group(2)[1:-1])
                    ret[match.group(1)] = { "weight": weight, "children" : [] }
                else:
                    print("No match?")
    except IOError:
        print("Broke")
    return ret

def part_one(input_arr):
    test_value = None
    for i in input_arr:
        for key, value in i.items():
            [holder, holdees] = (list(value.items())[0])
            if test_value is None or test_value in holdees:
                test_value = holder
    return test_value

def part_two(input_arr, start):
    weight = input_arr[start]['weight']
    children = input_arr[start]["children"]
    full_programs = {start : {"weight" : weight }}
    full_programs[start]["weight"] = weight
    for i in children:
        ret = full_programs[start].setdefault(i, {})
        full_programs[start][i] = add_program(ret, i, input_arr)
    #print(json.dumps(full_programs, indent=4))
    for i in children:
        ret = full_programs[start].setdefault(i, {})
        full_programs[start][i]["total_weight"] = get_weight(ret, i, input_arr)
    print(json.dumps(full_programs, indent=4))

def add_program(ret, program, input_arr):
    ret["weight"] = input_arr[program]["weight"]
    children = input_arr[program]["children"]
    for child in children:
        ret = ret.setdefault(child, {})
        add_program(ret, child, input_arr)
    return ret

def get_weight(ret, program, input_arr):
    ret["weight"] = input_arr[program]["weight"]
    children = input_arr[program]["children"]
    weight = ret["weight"]
    for child in children:
        ret = ret.setdefault(child, {})
        weight += get_weight(ret, child, input_arr)
    ret["total_weight"] = weight
    return weight

def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = part_one(input_arr)
    #print(ret)
    input2_arr = read_file_two(file_location)
    ret2 = part_two(input2_arr, ret)
    #print(ret2)

if "__main__":
    main()
