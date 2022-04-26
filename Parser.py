# Driver code which calls the lexer to get tokens

import sys
from Lexer import Lexer
from Utils import checkFile

class Parser():

    def __init__(self):
        pass
    
    def parse(self, filepath):
        pass

    def shift(self):
        pass

    def reduce(self):
        pass

def main():
    filepath = sys.argv[1]
    checkFile(filepath)
    lexer = Lexer(filepath)

    print(f"{'LINE':<8}{'LEXEME':<24}{'TOKEN ID':<12}{'TOKEN':<16}\n")
    while True:
        token = lexer.getNextToken()
        if token is not None:
            print(f"{token[0]:<8}{token[1]:<24}{token[2]:<12}{token[3]:<16}")
        else:
            break

if __name__ == "__main__":
    main()