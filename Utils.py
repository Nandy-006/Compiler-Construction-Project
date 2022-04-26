import os

# Checks if the file has .lwj extension
def checkFile(filepath):
    if os.path.isfile(filepath) and os.path.splitext(os.path.basename(filepath))[1] == ".lwj":
        return None
    else:
        raise Exception("Not a Langwej file")

class Stack:
    def __init__(self, stack = []):
        self.stack = stack
        self.size = len(stack)
    
    def top(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        return self.stack[0]
    
    def push(self, item):
        self.stack.insert(0, item)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise Exception("Stack is empty")
        self.size -= 1
        return self.stack.pop(0)
    
    def getStack(self, single=True):
        if not single:
            return self.stack
        else:
            return [x[0] if isinstance(x, tuple) else x for x in self.stack]
    
    def print(self, single=True):
        print(self.getStack(single))