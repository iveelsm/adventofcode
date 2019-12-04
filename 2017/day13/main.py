import time

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(list(map(int, line.rstrip("\n").split(":"))))
    except IOError:
        print("Couldn't read the file")
    return ret


def part_one(game_dict):
    frog = 0
    ret = []
    while frog < max(game_dict.keys()):
        if has_been_hit(frog, game_dict):
            dict_to_add = {}
            dict_to_add["range"] = game_dict[frog]["size"]
            dict_to_add["depth"] = frog
            ret.append(dict_to_add)
        frog += 1
        game_dict = increment_game(game_dict)
    return ret


def part_two(input_arr):
    delay = 0
    start_time = time.time()
    while not can_complete(input_arr, delay):
        delay += 1
    print(time.time() - start_time)
    return delay


def can_complete(input_arr, delay):
    step = 0 + delay
    for i in input_arr:
        if (step + i[0]) % ((2 * i[1]) - 2) == 0:
            return False
    return True


def calculate_severity(hit_dict):
    severity = 0
    for i in hit_dict:
        to_add = i["range"] * i["depth"]
        severity += to_add
    return severity


def increment_game(game):
    for i, j in game.items():
        if j["location"] == j["size"] and j["direction"] == 1:
            j["direction"] = -1
        elif j["location"] == 1 and j["direction"] == -1:
            j["direction"] = 1
        j["location"] += j["direction"]
        game[i] = j
    return game


def has_been_hit(frog, road):
    if road.get(frog, {"location" : 0})["location"] == 1:
        return True
    return False


def initialize_dict(input_arr):
    ret = {}
    for i in input_arr:
        key                         = i[0]
        dict_to_insert              = ret.setdefault(key, {})
        dict_to_insert["size"]      = i[1]
        dict_to_insert["location"]  = 1
        dict_to_insert["direction"] = 1
        ret[key]                    = dict_to_insert
    return ret


def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    game_dict = initialize_dict(input_arr)
    ret = part_one(game_dict)
    severity = calculate_severity(ret)
    print("Part One Severity: %s" % severity)

    input2_arr = read_file(file_location)
    delay = part_two(input2_arr)
    print("Part Two Delay: %s" % delay)

if "__main__":
    main()
