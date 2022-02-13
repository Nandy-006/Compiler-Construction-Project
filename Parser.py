import sys
from tabnanny import check
from Lexer import Lexer
from Utils import checkFile

def main():
    filepath = sys.argv[1]
    checkFile(filepath)
    lexer = Lexer(filepath)

    print(f"{'LINE':<8}{'LEXEME':<24}{'TOKEN ID':<12}{'TOKEN':<16}\n")
    while lexer.hasNextToken():
        token = lexer.getNextToken()
        print(f"{token[0]:<8}{token[1]:<24}{token[2]:<12}{token[3]:<16}")

if __name__ == "__main__":
    main()