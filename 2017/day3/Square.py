class Square(object):
    def __init__(self):
        self.square_dict = {(0,0) : 1}

    def add_value(self, x, y, value):
        if (x, y) in self.square_dict:
            return 0
        else:
            self.square_dict[(x,y)] = value
            return 1

    def get_value(self, value):
        for key, test in self.square_dict.items():
            if value == test:
                print(key)
                return key
        raise Exception("No value found in dictionary!")
