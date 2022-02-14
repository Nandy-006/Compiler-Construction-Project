from curses.ascii import isalnum, isalpha
from os import stat
import re
from Dictionary import KEYWORDS, SYMBOLS, TOKENS, STATES

class Lexer():
    def __init__(self, filepath):
        self.path = filepath
        self.processed = None
        self.eof = False
        self.COMMENT_PATTERN = r"(?:\/\*(?:[^*]|[\r\n]|(?:\*+(?:[^*\/]|[\r\n])))*\*+\/)|(?:\/\/.*)"

        self.lineNum = 0
        self.charIndex = -1
        self.newLine = True
    
    def processFile(self):
        with open(self.path, "r") as f:
            self.processed = re.sub(self.COMMENT_PATTERN, "", f.read())
    
    def getChar(self):
        if self.newLine:
            self.lineNum += 1
            self.newLine = False
        if self.charIndex+1 < len(self.processed):
            self.charIndex += 1
            if self.processed[self.charIndex] == "\n":
                self.newLine = True
            return self.processed[self.charIndex]
        return None

    def retract(self):
        self.charIndex -= 1
        if self.charIndex < -1:
            raise Exception("Invalid retract")

    def getNextToken(self): # (Line, Lexeme, Token id, Token)
        lexeme = ""
        state = STATES.EMPTY_LEXEME

        while True:
            char = self.getChar()
            if char is None and lexeme != "":
                raise Exception(f"Invalid lexeme {lexeme} on line {self.lineNum}")
            
            if state == STATES.EMPTY_LEXEME:
                if char in SYMBOLS:
                    return (self.lineNum, char, TOKENS[char][0], TOKENS[char][1])
                elif char.isalpha() or char == "_":
                    state = STATES.ALPHABET
                elif char.isdecimal():
                    state = STATES.NUMBER
                elif char == "'":
                    state = STATES.OPEN_CHAR
                elif char == "\"":
                    state = STATES.OPEN_STRING
                elif char == ">":
                    state = STATES.GREATER_THAN
                elif char == "<":
                    state = STATES.LESS_THAN
                elif char == "=":
                    state = STATES.EQUAL_HALF
                elif char == "!":
                    state = STATES.NOT_EQUAL_HALF
                elif char == "|":
                    state = STATES.OR_HALF
                elif char == "&":
                    state = STATES.AND_HALF
                else:
                    raise Exception(f"Invalid character {char} in line {self.lineNum}s")
            elif state == STATES.ALPHABET:
                pass

