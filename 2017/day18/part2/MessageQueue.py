import time

class MessageQueue(object):
    def __init__(self):
        self.queue = []
        self.max_retry = 60

    def send(self, value):
        self.queue.insert(0, value)

    def receive(self):
        for i in range(self.max_retry):
            try:
                return self.queue.pop()
            except:
                print("Nothing to receive...")
                time.sleep(1)
                print("Finished waiting...")
        print("Gave up?")
        return None
