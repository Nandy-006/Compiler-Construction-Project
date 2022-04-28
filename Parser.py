import pandas as pd
from tabulate import tabulate

from Lexer import Lexer
from IC import ICVar, getICVar
from Utils import checkFile, Stack

TOKEN_HEADERS = ["LINE", "LEXEME", "TOKEN ID", "TOKEN"]
STACK_HEADERS = ["INPUT", "STACK", "ACTION"]
IC_HEADERS = ["OPERATOR", "ARG1", "ARG2", "RESULT"]

# Parser class to parse the langwej program
class Parser():
    def __init__(self, tokenPath, stackPath, ICPath):
        self.pt = pd.read_csv("parse_table.csv")
        self.actions = list(self.pt.columns[:45])
        self.goto = list(self.pt.columns[45:])
        self.stack = Stack([0, ("$", "END")])
        self.ICStack = Stack([ICVar("$")])

        self.tokenTable = []
        self.stackTable = []
        self.ICTable = []

        self.tokenPath = tokenPath
        self.stackPath = stackPath
        self.ICPath = ICPath

        self.parsable = None

        with open("langwej.cfg", "r") as f:
            self.rules = [x.strip() for x in f.read().split("\n") if len(x.strip()) > 0]
    
    def tokenize(self, filepath):
        checkFile(filepath)
        lexer = Lexer(filepath)
        nextToken = lexer.getNextToken()
        while nextToken is not None:
            self.tokenTable.append(nextToken)
            nextToken = lexer.getNextToken()
        with open(self.tokenPath, "w") as f:
            f.write(tabulate(self.tokenTable, headers=TOKEN_HEADERS))
    
    def parse(self, filepath, parseOnly=False):
        checkFile(filepath)
        lexer = Lexer(filepath)

        nextToken = lexer.getNextToken()
        self.tokenTable.append(nextToken)

        while True:
            # import pdb; pdb.set_trace()
            if nextToken is not None:
                lineNum, lexeme, _, token = nextToken
            else:
                _, lexeme, _, token = ("_", "$", "_", "END")
                
            if token in self.actions:
                next = (token, lexeme)
            else:
                next = (lexeme, lexeme)
            
            cell = self.pt.loc[self.stack.top()][next[0]]

            if cell[0] == "e":
                self.parsable = False
                if cell == "e0":
                    print(f"[SYNTAX ERROR: {lineNum}]: Unexpected closing parenthesis ')'")
                    nextToken = lexer.getNextToken()
                    if nextToken is not None:
                        self.tokenTable.append(nextToken)
                elif cell == "e1":
                    print(f"[SYNTAX ERROR: {lineNum}]: Unexpected closing braces '}}'")
                    nextToken = lexer.getNextToken()
                    if nextToken is not None:
                        self.tokenTable.append(nextToken)
                elif cell == "ee":
                    print(f"[SYNTAX ERROR: {lineNum}]: PANIK MODE INITIATED")
                    nextToken = lexer.getNextToken()
                    while nextToken is not None:
                        self.tokenTable.append(nextToken)
                        if nextToken[1] in [';','}']:  
                            break
                        nextToken = lexer.getNextToken()

                    if nextToken is None:
                        break

                    while self.stack.top() != 0 and self.pt.loc[self.stack.top()][nextToken[0]] != "e":
                        self.stack.pop()
                        self.stack.pop()
                    if self.stack.top() == 0:
                        nextToken = lexer.getNextToken()
                        if nextToken is not None:
                            self.tokenTable.append(nextToken)
                else:
                    raise Exception("Invalid error")
            elif cell == "acc":
                if self.parsable is None:
                    self.parsable = True
                break
            elif cell[0] == "s":
                self.stackTable.append((next, self.stack.getStack(), f"SHIFT {int(float(cell[1:]))}"))
                self.shift(int(float(cell[1:])), next)
                nextToken = lexer.getNextToken()
                if nextToken is not None:
                    self.tokenTable.append(nextToken)
            elif cell[0] == "r":
                self.stackTable.append((next, self.stack.getStack(), f"REDUCE {int(float(cell[1:]))}"))
                self.reduce(int(float(cell[1:])), parseOnly)
            else:
                raise Exception("Invalid stack")
        
        with open(self.tokenPath, "w") as f:
            f.write(tabulate(self.tokenTable, headers=TOKEN_HEADERS))

        with open(self.stackPath, "w") as f:
            f.write(tabulate(self.stackTable, headers=STACK_HEADERS))
            f.write(f"\n\nValid: {self.parsable}")

        if not parseOnly:
            self.ICTable = self.ICStack.top().code
            with open(self.ICPath, "w") as f:
                if not self.parsable:
                    f.write("Note: Syntax errors were found. Intermediate code maybe unreliable.\n\n")
                f.write(tabulate(self.ICTable, headers=IC_HEADERS))

        return self.parsable

    def shift(self, index, next):
        self.stack.push(next)
        self.ICStack.push(ICVar(next[1]))
        self.stack.push(index)

    def reduce(self, index, parseOnly):
        rule = self.rules[index].split(" ")
        if index == 1 or index == 4:
            popCount = 0
        else: 
            popCount = len(rule[2:])
        for _ in range(2*popCount):
            self.stack.pop()
        if not parseOnly:
            popped = []
            for _ in range(popCount):
                popped.insert(0, self.ICStack.pop())
        goto = self.stack.top()
        self.stack.push((rule[0], rule[0]))
        if not parseOnly:
            self.ICStack.push(getICVar(index, popped))
        self.stack.push(int(float(self.pt.loc[goto][rule[0]])))