from grid_operator import divide
import numpy

test = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

result = divide(test, 2)

print("Test 1: \n")
for i in result:
    print(numpy.array(i))

test2 = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 0, 1]
]

result2 = divide(test2, 3)

print("Test 2: \n")
for i in result2:
    print(numpy.array(i))

test3 = [
    [1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 1]
]

result3 = divide(test3, 3)
print("Test 3: \n")
for i in result3:
    print(numpy.array(i))
