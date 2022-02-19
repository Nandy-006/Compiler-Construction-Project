# Lexer reads the source code character by character
# It tokenizes the source code by traversing the DFA (refer Langwej-DFA.png)

import re
from Dictionary import DELIMITERS, KEYWORDS, SYMBOLS, TOKENS, STATES

class Lexer():
    def __init__(self, filepath):
        self.path = filepath
        self.eof = False
        self.lineNum = 0
        self.charIndex = -1
        self.newLine = True

        with open(self.path, "r") as f:
            self.code = f.read()
        self.code += '\n'

    # Gets the next character from the input stream
    def getChar(self):
        if self.newLine:
            self.lineNum += 1
            self.newLine = False
        if self.charIndex+1 < len(self.code):
            self.charIndex += 1
            if self.code[self.charIndex] == "\n":
                self.newLine = True
            return self.code[self.charIndex]
        return None

    # Adds the last read character back to the input stream
    def retract(self):
        self.charIndex -= 1
        self.newLine = False
        if self.charIndex < -1:
            raise Exception("Invalid retract")

    # Returns the next token in the format: (Line, Lexeme, Token id, Token)
    def getNextToken(self): 
        lexeme = ""
        state = STATES.EMPTY_LEXEME

        while True:
            char = self.getChar()
            if char is None:
                if lexeme != "":
                    raise Exception(f"Invalid lexeme {lexeme} on line {self.lineNum}")
                else:
                    return None
            
            if state == STATES.EMPTY_LEXEME:
                lexeme = ""
                if char.isspace():
                    pass
                elif char in SYMBOLS:
                    return (self.lineNum, char, TOKENS[char][0], TOKENS[char][1])
                elif char == "#":
                    state = STATES.MIDDLE_SINGLE_COMMENT
                elif char == "`":
                    state = STATES.MIDDLE_MULTIPLE_COMMENT
                elif char.isalpha() or char == "_":
                    lexeme += char
                    state = STATES.ALPHABET
                elif char.isdecimal():
                    lexeme += char
                    state = STATES.NUMBER
                elif char == "'":
                    lexeme += char
                    state = STATES.OPEN_CHAR
                elif char == "\"":
                    lexeme += char
                    state = STATES.OPEN_STRING
                elif char == ">":
                    lexeme += char
                    state = STATES.GREATER_THAN
                elif char == "<":
                    lexeme += char
                    state = STATES.LESS_THAN
                elif char == "=":
                    lexeme += char
                    state = STATES.EQUAL_HALF
                elif char == "!":
                    lexeme += char
                    state = STATES.NOT_EQUAL_HALF
                elif char == "|":
                    lexeme += char
                    state = STATES.OR_HALF
                elif char == "&":
                    lexeme += char
                    state = STATES.AND_HALF
                else:
                    raise Exception(f"Invalid character {char} in line {self.lineNum}")

            
            elif state == STATES.MIDDLE_SINGLE_COMMENT:
                if char == "\n":
                    state = STATES.EMPTY_LEXEME
                else:
                    state = STATES.MIDDLE_SINGLE_COMMENT

            
            elif state == STATES.MIDDLE_MULTIPLE_COMMENT:
                if char == "`":
                    state = STATES.EMPTY_LEXEME
                else:
                    state = STATES.MIDDLE_MULTIPLE_COMMENT

            
            elif state == STATES.ALPHABET:
                if char.isalpha() or char == "_":
                    lexeme += char
                    state = STATES.ALPHABET
                elif char.isdecimal():
                    lexeme += char
                    state = STATES.ALNUM
                elif char in DELIMITERS or char.isspace():
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    if lexeme in KEYWORDS:
                        return (self.lineNum, lexeme, TOKENS[lexeme][0], TOKENS[lexeme][1])
                    else:
                        return (self.lineNum, lexeme, TOKENS["IDENTIFIER"][0], TOKENS["IDENTIFIER"][1])
                else:
                    raise Exception(f"Invalid character {char} in line {self.lineNum}")

            elif state == STATES.ALNUM:
                if char.isalnum() or char == "_":
                    lexeme += char
                    state = STATES.ALNUM
                elif char in DELIMITERS or char.isspace():
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["IDENTIFIER"][0], TOKENS["IDENTIFIER"][1])
                else:
                    raise Exception(f"Invalid character {char} in line {self.lineNum}")

            elif state == STATES.NUMBER:
                if char.isdecimal():
                    lexeme += char
                    state = STATES.NUMBER
                elif char == '.':
                    lexeme += char
                    state = STATES.POINT
                elif char in DELIMITERS or char.isspace():
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["INT"][0], TOKENS["INT"][1])
                else:
                    raise Exception(f"Invalid lexeme {lexeme+char} in line {self.lineNum}")

            elif state == STATES.POINT:
                if char.isdecimal():
                    lexeme += char
                    state = STATES.FLOAT
                else:
                    raise Exception(f"Expected a decimal to follow {lexeme} in line {self.lineNum}, found {char} instead")

            elif state == STATES.FLOAT:
                if char.isdecimal():
                    lexeme += char
                    state = STATES.FLOAT
                elif char == 'e' or char == 'E':
                    lexeme += char
                    state = STATES.EXPONENT
                elif char in DELIMITERS or char.isspace():
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["FLOAT"][0], TOKENS["FLOAT"][1])
                else:
                    raise Exception(f"Invalid lexeme {lexeme+char} in line {self.lineNum}")

            elif state == STATES.EXPONENT:
                if char.isdecimal():
                    lexeme += char
                    state = STATES.FLOAT
                elif char == '+' or char == '-':
                    lexeme += char
                    state = STATES.EXPONENT_SIGN
                else:
                    raise Exception(f"Expected a sign or a decimal to follow {lexeme+char} in line {self.lineNum}, found {char} instead")

            elif state == STATES.EXPONENT_SIGN:
                if char.isdecimal():
                    lexeme += char
                    state = STATES.FLOAT
                else:
                    raise Exception(f"Expected a decimal to follow {lexeme} in line {self.lineNum}, found {char} instead")

            elif state == STATES.OPEN_CHAR:
                if char == "'":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["CHAR"][0], TOKENS["CHAR"][1])                    
                elif char == "\\":
                    lexeme += char
                    state = STATES.SLASH_CHAR
                elif char == "\n":
                    raise Exception(f"Expected a closing ' in line {self.lineNum}, not found")
                else:
                    lexeme += char
                    state = STATES.CHAR

            elif state == STATES.SLASH_CHAR:
                if char in ["n","t","\"","r","\\"]:
                    lexeme += char
                    state = STATES.CHAR
                else:
                    raise Exception(f"Expected an escape sequence character in line {self.lineNum}, found {char}")

            elif state == STATES.CHAR:
                if char == "'":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["CHAR"][0], TOKENS["CHAR"][1])
                elif char == "\n":
                    raise Exception(f"Expected a closing ' in line {self.lineNum}, not found")
                else:
                    raise Exception(f"Expected char to contain a single character in line {self.lineNum}, found {lexeme+char} instead")

            elif state == STATES.OPEN_STRING:
                if char == "\"":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["STRING"][0], TOKENS["STRING"][1])
                elif char == "\n":
                    raise Exception(f"Expected a closing \" in line {self.lineNum}, not found")
                else:
                    lexeme += char

            elif state == STATES.GREATER_THAN:
                if char == "=":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS[">="][0], TOKENS[">="][1])
                else:
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS[">"][0], TOKENS[">"][1])
            
            elif state == STATES.LESS_THAN:
                if char == "=":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["<="][0], TOKENS["<="][1])
                else:
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["<"][0], TOKENS["<"][1])

            elif state == STATES.EQUAL_HALF:
                if char == "=":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["=="][0], TOKENS["=="][1])
                else:
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["="][0], TOKENS["="][1])

            elif state == STATES.NOT_EQUAL_HALF:
                if char == "=":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["!="][0], TOKENS["!="][1])
                else:
                    self.retract()
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["!"][0], TOKENS["!"][1])

            elif state == STATES.OR_HALF:
                if char == "|":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["||"][0], TOKENS["||"][1])
                else:
                    raise Exception(f"Invalid lexeme {lexeme+char} in line {self.lineNum}")
            
            elif state == STATES.AND_HALF:
                if char == "&":
                    lexeme += char
                    state = STATES.EMPTY_LEXEME
                    return (self.lineNum, lexeme, TOKENS["&&"][0], TOKENS["&&"][1])
                else:
                    raise Exception(f"Invalid lexeme {lexeme+char} in line {self.lineNum}")