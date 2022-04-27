# Driver code for the compilation process
 
import argparse
from Parser import Parser
 
def main():
    argparser = argparse.ArgumentParser(description = "Langwej frontend compiler.")
    
    argparser.add_argument("filepath", type=str, help="Specifies the path to the .lwj file to be compiled")
    argparser.add_argument("--tokenize", action="store_true", default=False, help="Specify this flag if the program needs to be tokenized only, defaults to False")
    argparser.add_argument("--parseOnly", action="store_true", default=False, help="Specify this flag if intermediate code should not be generated, defaults to False")
    argparser.add_argument("--tokenPath", type=str, default="parseTokens.txt", help="Specifies the file where tokens are written, defaults to parseTokens.txt")
    argparser.add_argument("--stackPath", type=str, default="parseStack.txt", help="Specifies the file where parse stack traces are written, defaults to parseStack.txt")
    argparser.add_argument("--ICPath", type=str, default="parseIC.txt", help="Specifies the path where intermediate code generated is written, defaults to parseIC.txt")
 
    args = argparser.parse_args()
    
    parser = Parser(tokenPath=args.tokenPath, stackPath=args.stackPath, ICPath=args.ICPath)
    if args.tokenize:
        parser.tokenize(args.filepath)
    else:
        parser.parse(args.filepath, parseOnly=args.parseOnly)
 
if __name__ == "__main__":
    main()