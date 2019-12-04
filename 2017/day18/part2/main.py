from Program import Program
from line_parser import read_file
from MessageQueue import MessageQueue

FILE_LOCATION = "./inputs/input.txt"

def main():
    input_instructions = read_file(FILE_LOCATION)

    Queue_1_2 = MessageQueue()
    Queue_2_1 = MessageQueue()

    Program_1 = Program(Queue_1_2, Queue_2_1, input_instructions, 0)
    Program_2 = Program(Queue_2_1, Queue_1_2, input_instructions, 1)

    Program_1.start()
    Program_2.start()

if "__main__":
    main()
