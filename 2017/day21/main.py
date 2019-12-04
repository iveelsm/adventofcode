from file_reader import read_file
from grid_operator import apply_rule
import time


def part_one(rules):
    grid = [[0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]]
    for i in range(18): # 5 iterations
        grid = apply_rule(grid, rules)
        print("Rule no. " + str(i) + ": " + str(sum(sum(k) for k in grid)))
    return sum(sum(k) for k in grid)

def main():
    file_location = "./inputs/input.txt"
    input_dict = read_file(file_location)
    start_time = time.time()
    ret = part_one(input_dict)
    print("Time: " + str(time.time() - start_time))
    print(ret)

if "__main__":
    main()
