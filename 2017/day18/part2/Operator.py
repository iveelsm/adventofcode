class Operator(object):
    def __init__(self, send_queue, receive_queue):
        self.send_queue = send_queue
        self.receive_queue = receive_queue

    def add(self, variable_dict, variable, value):
        variable_dict[variable] += value
        return 1

    def multiply(self, variable_dict, variable, value):
        variable_dict[variable] *= value
        return 1

    def set_value(self, variable_dict, variable, value):
        variable_dict[variable] = value
        return 1

    def jump(self, variable_dict, variable, value):
        if variable.isdigit():
            if int(variable) > 0:
                return value
            else:
                return 1
        elif variable_dict[variable] > 0:
            return value
        else:
            return 1

    def modulus(self, variable_dict, variable, value):
        variable_dict[variable] = variable_dict[variable] % value
        return 1

    def send(self, variable_dict, variable, value):
        self.send_queue.send(variable_dict[variable])
        return 1

    def receive(self, variable_dict, variable, value):
        value = self.receive_queue.receive()
        if not value is None:
            variable_dict[variable] = value
            return 1
        else:
            return 100000
