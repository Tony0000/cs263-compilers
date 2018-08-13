from lexer import Lexer
from parser import Parser
import sys

def main():
    filename = ''
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        f = open(filename, 'r+')
        lexer = Lexer()
        for line in f:
            lexer.feed(line)
            while lexer.is_readable():
                token = lexer.get_next_token()
                if token is not None:
                    print(token)

if __name__ == '__main__':
    main()
