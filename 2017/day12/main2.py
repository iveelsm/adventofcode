def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(line.rstrip("\n"))
    except IOError:
        print("Couldn't read the file")
    return ret

def part_one(input_arr):
    ret = set()
    ret.add(0)
    arrays = []
    for i in input_arr:
        array_to_add = []
        array_to_add.append(int(i.split(" <-> ")[0]))
        array_to_add.extend(list(map(int, i.split(" <-> ")[1].split(", "))))
        arrays.append(sorted(array_to_add))

    arrays = sorted(arrays)
    values_added = 1
    while values_added < 100:
        values_added += 1
        for array in arrays:
            for j in array:
                if j in ret:
                    [ret.add(x) for x in array]
                    break

    return len(returnval)



def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    result = part_one(input_arr)
    print(result)

if "__main__":
    main()
