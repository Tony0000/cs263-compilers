from lexer import Lexer
from parser import Parser
import sys

def main():
    filename = ''
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        lexer = Lexer(filename)
        while(lexer.has_next() is not None):
            print(lexer.get_next_token())

if __name__ == '__main__':
    main()
