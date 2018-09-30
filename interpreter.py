from lexer import Lexer
from parser import Parser
import sys

def main():
    # filename = ''
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        lexer = Lexer(filename)
        parser = Parser(lexer)
        # token = lexer.get_next_token()
        #
        # while(token.value is not 'EOF'):
        #     print(token)
        #     token = lexer.get_next_token()
        #
        # print(token)

if __name__ == '__main__':
    main()
