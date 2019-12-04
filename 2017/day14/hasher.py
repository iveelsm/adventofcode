from functools import reduce

def knot_hash(list_mods):
    circular_list = list(range(0, 256))
    skip_size = 0
    cursor = 0
    ret = []

    for i in range(64):
        for j in list_mods:
            apply_operation(j, cursor, circular_list)
            cursor += j + skip_size
            cursor = cursor % len(circular_list)
            skip_size += 1

    for i in range(0, len(circular_list), 16):
        ret.append("%0.2x"%reduce((lambda x, y : x ^ y), circular_list[i: i + 16]))
    return ''.join(ret)

def apply_operation(operation, cursor, circular_list):
    list_slice = []
    if cursor + operation >= len(circular_list):
        pivot = (cursor + operation) % len(circular_list)
        list_slice = circular_list[cursor:] + circular_list[:pivot]
        list_slice = list_slice[::-1]
        circular_list[cursor:] = list_slice[:len(list_slice) - pivot]
        circular_list[:pivot] = list_slice[len(list_slice) - pivot:]
    else:
        list_slice = circular_list[cursor:(cursor + operation)]
        list_slice = list_slice[::-1]
        circular_list[cursor:(cursor + operation)] = list_slice
    return circular_list
