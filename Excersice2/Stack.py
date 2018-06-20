class Stack(object):

    def __init__(self):
        self.stack = list()

    def pop(self):
        return self.stack.pop()

    def push(self,item):
        self.stack.append(item)