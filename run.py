# Driver code which calls the lexer to get tokens
import sys
from Parser import Parser

def main():
    filepath = sys.argv[1]
    
    parser = Parser()
    # parser.tokenize(filepath)
    parser.parse(filepath)

if __name__ == "__main__":
    main()