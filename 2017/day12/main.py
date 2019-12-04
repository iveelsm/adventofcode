<<<<<<< Updated upstream
class Node:
    def __init__(self, node_value, next_node):
        self.node_value = node_value
        self.next_node = next_node

    def __str__(self):
        return str(self.node_value)

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.current = head
        self.next = None


    def insert_nodes(self, linked_list):
        print("Attempting to insert: " + str(linked_list))
        linked_list.reset_current()
        self.reset_current()
        while linked_list.current is not None:
            self.insert_node(linked_list.current)
            linked_list.to_next()


    def insert_node(self, node_value):
        if node_value < self.head.node_value: # set new head node
            new_node = Node(node_value, self.head)
            self.head = new_node
            self.next = self.head.next_node
        elif self.current.node_value == node_value: # we already have it
            return
        elif self.has_next():
            if self.next.node_value > node_value and self.current.node_value < node_value: # insert and modify list
                new_node = Node(node_value, self.next)
                self.next.previous_node = new_node
                self.current.next_node = new_node
            else:
                if self.current.node_value < node_value: # keep progressing
                    self.to_next()
                    self.insert_node(node_value)
                else:
                    return
        else:
            if self.current.node_value < node_value: # set new tail node
                new_node = Node(node_value, None)
                self.next = new_node



    def has_next(self):
        return (self.next is not None)


    def has_node(self, node_value):
        if self.current.node_value == node_value:
            return True
        else:
            if self.next is None:
                return False
            else:
                self.to_next()


    def reset_current(self):
        self.current = self.head
        self.next = self.head.next_node


    def to_next(self):
        self.current = self.next
        if self.current is not None:
            self.next = self.current.next_node
        else:
            self.next = None


    def __len__(self):
        length = 0
        self.current = self.head
        while (self.next is not None):
            length += 1
            self.to_next()
        return length


    def __lt__(self, other):
        return self.head.node_value < other.head.node_value


    def __gt__(self, other):
        return self.head.node_value > other.head.node_value


    def __eq__(self, other):
        return self.head.node_value == other.head.node_value


    def __str__(self):
        ret = str(self.head)
        self.current = self.head.next_node
        while self.current is not None:
            ret += " -> %s" % (self.current)
            self.to_next()
        self.reset_current()
        return ret

=======
>>>>>>> Stashed changes
def read_file(file_location):
    ret = []
    try:
        with open(file_location) as contents:
<<<<<<< Updated upstream
            for line in contents:
                ret.append(line.rstrip("\n"))
    except IOError:
        print("Couldn't read the file")
    return ret

def part_one(input_arr):
    zero_node = Node(0, None)
    ret = LinkedList(zero_node)
    linked_lists = []
    for i in input_arr:
        primary = int(i.split(" <-> ")[0])
        secondaries = list(map(int, i.split(" <-> ")[1].split(", ")))
        primary_node = Node(primary, None)
        linked_list_to_add = LinkedList(primary_node)
        for i in secondaries:
            linked_list_to_add.reset_current()
            linked_list_to_add.insert_node(i)
        linked_lists.append(linked_list_to_add)


    linked_lists = sorted(linked_lists)
    ret = collapse_lists(ret, linked_lists)
    return len(ret)

def collapse_lists(ret, linked_lists):
    print("\nCollapsing lists\n")
    for i in linked_lists:
        i.reset_current()
        while i.current is not None:
            if ret.has_node(i.current.node_value):
                ret.insert_nodes(i)
                print("Current ret: " + str(ret))
                break
            else:
                i.to_next()
    return ret

def main():
    file_location = "./inputs/input.txt"
    input_arr = read_file(file_location)
    result = part_one(input_arr)
    print(result)

if "__main__":
    main()

## Steps:
# Construct n linked lists (O(nm)) m<<<n -> O(n)
# Sort n linked lists by head (O(nlog(n)))
# If master list contains any node in list i O(nm), add all elements to the list  O(1)
# Return length of list O(n)

# O(nlog(n))
=======
            line = contents.readline().rstrip("\n")
            ret = line.split(",")
    except:
        print("Couldn't read the file")
    return ret


def main():
    file_location = "./inputs/input.txt"

    steps = read_file(file_location)
    result = part_one(steps)
    print(result)

    file_location = "./inputs/input.txt"
    steps2 = read_file(file_location)

    result2 = part_two(steps2)
    print(result2)

if "__main__":
    main()
>>>>>>> Stashed changes
