import math

def main():
    file_location = "./inputs/input.txt"
    digits_1 = read_file(file_location)
    ret = part_one(digits_1)
    print(ret)
    digits_2 = read_file(file_location)
    ret2 = part_two(digits_2)
    print(ret2)

def read_file(file_location):
    ret = []
    try:
        file = open(file_location, "r")
        ret = list(file.read())
    except IOError:
        print("Couldn't read file")
    return ret

def part_one(digits):
  return sum(int(digits[i]) 
    for i in range(len(digits)) 
      if digits[i] == digits[(i + 1) % len(digits)])

def part_two(digits):
  return sum(int(digits[i])
    for i in range(len(digits))
      if digits[i] == digits[math.floor(i + len(digits) / 2) % len(digits)])  

if "__main__":
    main()
