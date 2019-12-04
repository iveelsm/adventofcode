import re


def read_file(file_location):
    ret = {}
    regex = ".*([A-B]).*(\\b[\\d]+)"
    pattern = re.compile(regex)
    try:
        with open(file_location) as contents:
            for line in contents:
                matcher = pattern.search(line.rstrip("\n"))
                ret[matcher.group(1)] = {}
                ret[matcher.group(1)]["value"] = int(matcher.group(2))
    except IOError:
        print("Couldn't read file")
    ret['A']["factor"] = 16807
    ret['B']["factor"] = 48271
    return ret

def part_two(input_arr):
    modulo_divisor = 2147483647
    max_value = 5000000
    i = 0
    judge_count = 0
    a_results = []
    b_results = []
    while i < max_value:
        for j in input_arr.values():
            j["value"] = int(j["value"] * j["factor"] % modulo_divisor)

        if input_arr['A']["value"] % 4 == 0:
            a_results.append(input_arr['A']["value"])
        if input_arr['B']["value"] % 8 == 0:
            b_results.append(input_arr['B']["value"])
            
        i = min(len(a_results), len(b_results))

    i = 0
    j = 0
    while i < len(a_results) and j < len(b_results):
        if positive_match(a_results[i], b_results[j]):
            judge_count += 1
        i += 1
        j += 1

    return judge_count

def part_one(input_arr):
    modulo_divisor = 2147483647
    max_value = 40000000
    i = 0
    judge_count = 0
    while i < max_value:
        for j in input_arr.values():
            j["value"] = int(j["value"] * j["factor"] % modulo_divisor)

        if positive_match(input_arr['A']["value"], input_arr['B']["value"]):
            judge_count += 1
        i += 1
    return judge_count

def positive_match(a, b):
    mask = 0b1111111111111111
    if (a & mask) == (b & mask):
        return True
    return False


def main():
    file_location = "./inputs/input.txt"
    # input_arr = read_file(file_location)
    # ret = part_one(input_arr)
    # print(ret)

    input2_arr = read_file(file_location)
    ret2 = part_two(input2_arr)
    print(ret2)

if "__main__":
    main()
