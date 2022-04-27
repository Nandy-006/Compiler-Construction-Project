# Driver code which calls the lexer to get tokens
import sys
import pandas as pd
from tabulate import tabulate
from Lexer import Lexer
from Utils import checkFile, Stack

TOKEN_HEADERS = ["LINE", "LEXEME", "TOKEN ID", "TOKEN"]
STACK_HEADERS = ["INPUT", "STACK", "ACTION"]

class Parser():

    def __init__(self):
        self.pt = pd.read_csv("parse_table.csv", header=2).fillna(-1)
        self.actions = list(self.pt.columns[:45])
        self.goto = list(self.pt.columns[45:])
        self.stack = Stack([0, ("$", "END")])

        self.tokenTable = []
        self.stackTable = []

        with open("final.cfg", "r") as f:
            self.rules = [x.strip() for x in f.read().split("\n") if len(x.strip()) > 0]
    
    def parse(self, filepath, printTokens=False, printStack=False, writeFiles=False):
        checkFile(filepath)
        lexer = Lexer(filepath)

        nextToken = lexer.getNextToken()
        self.tokenTable.append(nextToken)
        while True:
            if nextToken is not None:
                _, lexeme, _, token = nextToken
            else:
                _, lexeme, _, token = ("_", "$", "_", "END")
                
            if token in self.actions:
                next = (token, lexeme)
            else:
                next = (lexeme, lexeme)
            
            cell = self.pt.loc[self.stack.top()][next[0]]

            if printStack:
                self.stack.print()

            if cell == -1:
                self.parsable = False
                break
            elif cell == "acc":
                self.parsable = True
                break
            elif cell[0] == "s":
                self.stackTable.append((next, self.stack.getStack(), f"SHIFT {int(cell[1:])}"))
                self.shift(int(cell[1:]), next)
                nextToken = lexer.getNextToken()
                if nextToken is not None:
                    self.tokenTable.append(nextToken)
            elif cell[0] == "r":
                self.stackTable.append((next, self.stack.getStack(), f"REDUCE {int(cell[1:])}"))
                self.reduce(int(cell[1:]))
            else:
                raise Exception("Invalid stack")
        
        if printTokens:
            print(tabulate(self.tokenTable, headers=TOKEN_HEADERS))
        with open("parseTokens.txt", "w") as f:
            f.write(tabulate(self.tokenTable, headers=TOKEN_HEADERS))
        
        if printStack:
            print(tabulate(self.stackTable, headers=STACK_HEADERS))
        with open("parseStack.txt", "w") as f:
            f.write(tabulate(self.stackTable, headers=STACK_HEADERS))
            f.write(f"\n\nParsable: {self.parsable}")

        return self.parsable

    def shift(self, index, next):
        self.stack.push(next)
        self.stack.push(index)

    def reduce(self, index):
        rule = self.rules[index].split(" ")
        popCount = len(rule[2:])*2
        for _ in range(popCount):
            self.stack.pop()
        goto = self.stack.top()
        self.stack.push((rule[0], rule[0]))
        self.stack.push(int(self.pt.loc[goto][rule[0]]))

def main():
    filepath = sys.argv[1]
    
    parser = Parser()
    parser.parse(filepath)

if __name__ == "__main__":
    main()