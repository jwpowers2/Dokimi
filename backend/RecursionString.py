class RecursionString(object):
    def __init__(self):
        self.messages = []

    def rec_string(self, message, num):
        if (num == 0):
            return self.messages
        else:
            self.messages.append(message)
            return self.rec_string(message, num - 1)
