import re
import sys
from threading import Thread
from line_parser import parse_line
from MessageQueue import MessageQueue
from Operator import Operator


class Program(Thread):
    def __init__(self, send_queue, receive_queue, input_arr, pid):
        super(Program, self).__init__()
        self.operator = Operator(send_queue, receive_queue)
        self.pid = pid
        self.instructions = input_arr
        self.variable_dict = self.build_variable_dict(input_arr)

    def run(self):
        operations_list = []
        i = 0
        while i < len(self.instructions):
            [operation, variable, value] = parse_line(self.instructions[i])
            operations_list.append(operation)
            self.print_status("Applying operation: " + str(self.instructions[i]))
            self.print_status("Current dictionary: " + str(self.variable_dict))
            i += self.apply_operation(i, [operation, variable, value])
            self.print_status("Post operation dictionary: " + str(self.variable_dict))
        self.print_status("Total operations length: " + str(len(operations_list)))
        operations_list = list(filter(lambda x: x == "snd", operations_list))
        self.print_status("Sent " + str(len(operations_list)) + " instructions.")

    def apply_operation(self, index, instruction):
        operation_dict = {
            "add" : self.operator.add,
            "mul" : self.operator.multiply,
            "set" : self.operator.set_value,
            "jgz" : self.operator.jump,
            "mod" : self.operator.modulus,
            "snd" : self.operator.send,
            "rcv" : self.operator.receive
        }
        return operation_dict[instruction[0]](self.variable_dict, instruction[1], self.alpha_to_numeric(instruction[2]))

    def build_variable_dict(self, instructions):
        ret = {}
        regex = ".*([a-z]).*"
        pattern = re.compile(regex)
        for i in instructions:
            match = pattern.search(i)
            if not match.group(1) in ret:
                ret[match.group(1)] = 0
        ret['p'] = self.pid
        return ret

    def alpha_to_numeric(self, value):
        if value.isdigit():
            return int(value)
        if value.isalpha():
            return int(self.variable_dict[value])
        return int(value)

    def print_status(self, string):
        print("Program " + str(self.pid) + ": " + str(string))
