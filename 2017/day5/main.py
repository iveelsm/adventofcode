def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = part_one(input_arr)
    print(ret)
    input_two = read_file(file_location)
    ret2 = part_two(input_two)
    print(ret2)

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(int(line.rstrip("\n")))
    except IOError:
        print("Borke")
    return ret


def part_one(input_arr):
    next_location = 0
    num_steps = 0
    while(next_location < len(input_arr) and next_location >= 0):
        temp = input_arr[next_location]
        input_arr[next_location] = temp + 1
        next_location = next_location + temp
        num_steps = num_steps + 1
    return num_steps

def part_two(input_arr):
    next_location = 0
    num_steps = 0
    while(next_location < len(input_arr) and next_location >= 0):
        temp = input_arr[next_location]
        if temp >= 3:
            input_arr[next_location] = temp - 1
        else:
            input_arr[next_location] = temp + 1
        next_location = next_location + temp
        num_steps = num_steps + 1
    return num_steps

if "__main__":
    main()
