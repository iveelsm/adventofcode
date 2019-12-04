import time


def read_file(file_location):
    ret = 0
    try:
        with open(file_location) as contents:
            ret = int(contents.readline().rstrip("\n"))
    except IOError:
        print("Couldn't read file")
    return ret

def part_one(input_int):
    ret = []
    current_index = 0
    ret.insert(0, 0)
    for i in range(1, 2018):
        current_index = ((current_index + input_int) % len(ret)) + 1
        ret.insert(current_index, i)
    index = ret.index(2017)
    return ret[index - 3: index + 3]

def part_two(input_int):
    ret = 0
    current_index = 0
    for i in range(1, 50000001):
        current_index = ((current_index + input_int) % i) + 1
        if current_index == 1:
            ret = i
    return ret


def main():
    file_location = "./inputs/input.txt"

    start_time = time.time()
    input_int = read_file(file_location)
    ret = part_one(input_int)
    print(ret)
    print("Time: " + str(time.time() - start_time))

    input2_int = read_file(file_location)
    ret2 = part_two(input2_int)
    print(ret2)

if "__main__":
    main()
