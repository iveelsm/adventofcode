import json

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                values = sorted([int(x) for x in line.rstrip("\n").split("/")])
                ret.append((values[0], values[1]))
    except IOError:
        print("Couldn't read file")
    return ret


def part_one(input_arr):
    start_arr = [x for x in input_arr if 0 in x]
    bridges = {0 : {}}
    for i in start_arr:
        bridges[i[0]][i[1]] = {}
        used_set = set()
        used_set.add(i)
        bridges[i[0]] = build_bridge(input_arr, used_set, bridges.setdefault(i[0], {}), i[1])

    to_file(bridges)

    max_strength = 0
    for i, k in bridges.items():
        test_value = i + max_bridge(k)
        if test_value > max_strength:
            max_strength = test_value

    max_length = 0
    ret = []
    for i, k in bridges.items():
        longest = longest_bridge([], k)
        test_value = 1 + len(longest)
        if test_value > max_length:
            longest.append(i)
            ret = longest
    print(longest)

    return max_strength

def to_file(bridges):
    file_location = "output.txt"
    try:
        with open(file_location, "w") as f:
            print(str(json.dumps(bridges, indent=4)), file=f)
        f.close()
    except IOError:
        print("Problemo")

def max_bridge(next_connect):
    local_max = 0
    for i, k in next_connect.items():
        test = i if not k else (2 * i) + max_bridge(k)
        if test > local_max:
            local_max = test
    return local_max

def longest_bridge(array, next_connect):
    value = 0
    length = 0
    array_to_add = []
    for i, k in next_connect.items():
        array_to_add = [i] if not k else longest_bridge([], k)
        test = len(array_to_add)
        if test > length:
            value = i
    print("Dict: " + str(next_connect))
    print("Value: " + str(value))
    array.extend(array_to_add)
    print("Array to add: " + str(array_to_add))
    print("Array: " + str(array))
    return array


def build_bridge(input_arr, used_set, bridges, to_match):
    for i in input_arr:
        if to_match in i and i not in used_set:
            key = i.index(to_match)
            value = i[key ^ 1]
            bridges[to_match][value] = {}
            bridge_used = set(list(used_set))
            bridge_used.add(i)
            bridges[to_match] = build_bridge(input_arr, bridge_used, bridges.setdefault(to_match, {}), value)
    return bridges


def main():
    file_location = "./inputs/test.txt"
    input_arr = read_file(file_location)
    ret = part_one(input_arr)
    print(ret)


if "__main__":
    main()
