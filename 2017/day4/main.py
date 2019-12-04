def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    ret = count_valid_inputs(input_arr)
    print(ret)

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(line.rstrip("\n"))
    except IOError:
        print("Broke")
    return ret

def count_valid_inputs(input_arr):
    ret = 0
    for line in input_arr:
        line_arr = line.split(" ")
        if part_one(line_arr):
            ret = ret + 1
    return ret

def part_one(line_arr):
    for i in range(0, len(line_arr)):
        for j in range(i + 1, len(line_arr)):
            if line_arr[i] == line[j]:
                return False
    return True

def part_two(line_arr):
    for i in range(0, len(line_arr)):
        for j in range(i + 1, len(line_arr)):
            if sorted(line_arr[i]) == sorted(line_arr[j]):
                return False
    return True

if "__main__":
    main()
