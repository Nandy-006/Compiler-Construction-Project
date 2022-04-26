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
        self.size = 0
    
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    
    def pop(self):
        self.size -= 1
        return self.stack.pop()
    
    def print(self):
        print(self.stack)