def main():
    file_location = "./inputs/input.txt"
    input_string = read_file(file_location)
    ret = part_one(input_string)
    print(ret)
    input2_string = read_file(file_location)
    ret2 = part_two(input2_string)
    print(ret2)

def read_file(file_location):
    ret = []
    try:
        file = open(file_location, "r")
        lines = file.read().splitlines()
        for line in lines:
            ret.append(list(map(int, line.split())))
    except IOError:
        print("Couldn't read file")
    return ret


def part_one(input_arr):
    ret = 0
    for i in input_arr:
        ret += (max(i) - min(i))
    return ret


def part_two(input_arr):
    ret = 0
    for i in input_arr:
        [numerator, divisor] = find_numerator_divisor(i)
        if divisor != 0:
            ret += int(numerator / divisor)
    return ret

def find_numerator_divisor(arr):
    numerator = 0
    divisor = 0
    for j in arr:
        for k in arr[arr.index(j):]:
            if j > k and j % k == 0:
                [numerator, divisor] = [j, k]
                break
            elif j < k and k % j == 0:
                [numerator, divisor] = [k, j]
                break
    return [numerator, divisor]

if "__main__":
    main()
