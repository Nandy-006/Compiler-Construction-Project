from curses.ascii import isalnum
import re
from Dictionary import KEYWORDS, SYMBOLS, TOKENS

class Lexer():
    def __init__(self, filepath):
        self.path = filepath
        self.lines = []
        self.eof = False
        self.FLOAT_PATTERN = r"[+-]?[0-9]+([.][0-9]+)?([Ee][+-]?[0-9]+)?"
        self.INTEGER_PATTERN = r"[+-]?[0-9]+"
        self.IDENTIFIER_PATTERN = r"^[_A-Za-z][_A-Za-z0-9]*"
        self.COMMENT_PATTERN = r"(?:\/\*(?:[^*]|[\r\n]|(?:\*+(?:[^*\/]|[\r\n])))*\*+\/)|(?:\/\/.*)"

        self.codeIndex = 0
        self.charIndex = 0
    
    def processFile(self):
        with open(self.path, "r") as f:
            processedFile = re.sub(self.COMMENT_PATTERN, "", f.read()).split("\n")
            self.lines = [line.strip() for line in processedFile]

    def getNextToken(self): # (Line, Lexeme, Token id, Token)
        lexeme = ""
        lexemeLineNum = None
        isString = False
        isChar = False
        
        while self.codeIndex < len(self.code):
            if isChar:
                pass
            elif isString:
                pass
            else:
                code = self.code[self.codeIndex][self.charIndex:]
                lineNum = self.code[self.codeIndex][1]

                if code == "":
                    self.codeIndex += 1
                    self.charIndex = 0
                if code in KEYWORDS or code in SYMBOLS:
                    self.codeIndex += 1
                    return (lineNum, code, TOKENS[code][0], TOKENS[code][1])
                if re.fullmatch(self.FLOAT_PATTERN, code) is not None:
                    self.codeIndex += 1
                    return (lineNum, code, TOKENS["FLOAT"][0], TOKENS["FLOAT"][1])
                if re.fullmatch(self.INTEGER_PATTERN, code) is not None:
                    self.codeIndex += 1
                    return (lineNum, code, TOKENS["INT"][0], TOKENS["INT"][1])
                if re.fullmatch(self.IDENTIFIER_PATTERN, code) is not None:
                    self.codeIndex += 1
                    return (lineNum, code, TOKENS["IDENTIFIER"][0], TOKENS["IDENTIFIER"][1])
                if 2 <= len(self.testString) <= 3 and code[0] =="'" and code[-1] == "'":
                    self.codeIndex += 1
                    return (lineNum, code, TOKENS["CHAR"][0], TOKENS["CHAR"][1])
                if code[0] == "'":
                    self.codeIndex += 1
                    isChar = True
                    lexeme += code
                    lexemeLineNum = lineNum
                elif code[0] == "\"":
                    self.codeIndex += 1
                    if len(code) > 1 and code[-1] == "\"":
                        return (lineNum, code, TOKENS["STRING"][0], TOKENS["STRING"][1])
                    isString = True
                    lexeme += code
                    lexemeLineNum = lineNum
                else:
                    pass
        
        if lexeme == "":
            raise Exception("No more lexemes")
        else:
            raise Exception(f"Invalid Lexeme '{lexeme}' in Line {lexemeLineNum}")

    def hasNextToken(self):
        return self.codeIndex < len(self.code)
