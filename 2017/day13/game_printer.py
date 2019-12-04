def print_game(frog, road):
    statement_arr = []
    j = 1
    max_size = get_max_size({k: road.get(k, {}) for k in range(frog - 5, frog + 5)})
    while j < max_size:
        statement = ""
        iter_range = range(frog - 5, frog + 5)
        if (frog <= 5):
            iter_range = range(0, frog + 5)
        for i in iter_range:
            if i == frog and j == 1:
                if road.get(i, {"location" : 0})["location"] == j:
                    statement += "(S ) "
                else:
                    statement += "(. ) "
            elif road.get(i, {"location" : 0})["location"] == j:
                arrow = "+" if road.get(i, {"direction" : 1})["direction"] == 1 else "-"
                statement += "[S" + arrow + "] "
            elif road.get(i, {"size" : 0})["size"] < j:
                statement += "     "
            else:
                statement += "[  ] "
        j += 1
        statement_arr.append(statement)

    for i in statement_arr:
        print(i)


def get_max_size(subset):
    ret = 0
    for i in subset.values():
        if i.get("size", 0) > ret:
            ret = i["size"]
    return ret
