import re

def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
            for line in contents:
                ret.append(line.rstrip("\n"))
    except IOError:
        print("Couldn't read the file")
    return ret

def parse_line(instruction):
    regex = "([a-z]+)\s([-?a-z0-9])\s?([-?a-z0-9]+)?"
    pattern = re.compile(regex)
    match = pattern.search(instruction)
    if match.group(3):
        return [match.group(1), match.group(2), match.group(3)]
    else:
        return [match.group(1), match.group(2), '0']
