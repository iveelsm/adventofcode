
NUM_STEPS = 12172063

# def read_file(file_location):
#     ret = []
#     try:
#         with open(file_location) as contents:
#             for line in contents:
#
#     except IOError:
#         print("Couldn't read file")
#     return ret

def manual():
    return {
        'A' : {
            0 : {
                "value" : 1,
                "move"  : 1,
                "state" : 'B'
            },
            1 : {
                "value" : 0,
                "move"  : -1,
                "state" : 'C'
            }
        },
        'B' : {
            0 : {
                "value" : 1,
                "move"  : -1,
                "state" : 'A'
            },
            1 : {
                "value" : 1,
                "move"  : -1,
                "state" : 'D'
            }
        },
        'C' : {
            0 : {
                "value" : 1,
                "move"  : 1,
                "state" : 'D'
            },
            1 : {
                "value" : 0,
                "move"  : 1,
                "state" : 'C'
            }
        },
        'D' : {
            0 : {
                "value" : 0,
                "move"  : -1,
                "state" : 'B'
            },
            1 : {
                "value" : 0,
                "move"  : 1,
                "state" : 'E'
            }
        },
        'E' : {
            0 : {
                "value" : 1,
                "move"  : 1,
                "state" : 'C'
            },
            1 : {
                "value" : 1,
                "move"  : -1,
                "state" : 'F'
            }
        },
        'F' : {
            0 : {
                "value" : 1,
                "move"  : -1,
                "state" : 'E'
            },
            1 : {
                "value" : 1,
                "move"  : 1,
                "state" : 'A'
            }
        }
}

def part_one(input_steps, num_steps):
    ret = {}
    index = 0
    ret[index] = 0
    state = 'A'

    i = 0
    while i < num_steps:
        current_val = get_next(ret, index)
        ret[index] = input_steps[state][current_val]["value"]
        index += input_steps[state][current_val]["move"]
        state = input_steps[state][current_val]["state"]
        i += 1
    return [ret, sum(ret.values())]

def get_next(ret, index):
    if not index in ret:
        ret[index] = 0
    return ret[index]

def main():
    file_location = "./inputs/input.txt"
    input_arr = manual()
    # input_arr = read_file(file_location)
    ret, checksum = part_one(input_arr, NUM_STEPS)
    print(ret)
    print(checksum)

if "__main__":
    main()
