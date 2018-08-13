from tokens import Token, Tokens

RESERVED_KEYWORDS = [
                    'BEGIN', 'END', 'IF', 'ELSE', 'INTEGER', 'REAL', 'CHAR','CONST',
                     'STRING', 'WRITE','WRITELN', 'PROGRAM', 'VAR', 'THEN','BOOLEAN',
                     'PROCEDURE', 'FUNCTION', 'EXIT', 'WHILE', 'DO', 'READ', 'READLN',
                     'ARRAY', 'OF', 'TYPE', 'STEP', 'CONST', 'AND', 'OR', 'DIV', 'STEP',
                     'NOT', 'USES', 'FOR', 'TO'
                     ]

class Lexer:
    def __init__(self):
        self.row = -1

    def feed(self, text):
        self.text = text.rstrip()
        self.col = 0
        self.row += 1
        if len(self.text) > 0:
            self.current_char = self.text[self.col]

    def is_readable(self):
        return self.col < len(self.text)

    def error(self, token=None, msg=None):
        if msg:
            print(msg.format(self.row, self.col))
        elif token:
            print("Invalid syntax {} at [{},{}]".format(token, self.row, self.col))
        else:
            print("Invalid character {} at [{},{}]".format(self.current_char, self.row, self.col))

    def advance(self):
        self.col += 1
        if self.col > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.col]

    def skip_ws(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def peek(self, next_char):
        next_col = self.col+1
        if next_col < len(self.text) and self.text[next_col] is not None:
            return next_char == self.text[next_col]
        else:
            return False


    def integer(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        if not self.current_char.isalpha():
            return int(number)
        else:
            while self.current_char.isalnum():
                number += self.current_char
                self.advance()
            self.error(token=number)

    def word(self):
        word = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            word += self.current_char
            self.advance()
        return word

    def build_string(self):
        literal = ''
        self.advance()
        while self.current_char is not None and self.current_char is not '\"' and self.current_char is not '\'':
            literal += self.current_char
            self.advance()
        if self.current_char in ('\"', '\''):
            return literal
        else:
            self.error(msg="Unmatched single or double quotes missing at [{},{}].")

    def get_next_token(self):
        while self.current_char is not None:
            # print(self.current_char)
            if len(self.text) == 0:
                continue

            if self.current_char.isspace():
                self.skip_ws()
                continue

            if self.current_char.isdigit():
                start_col = self.col
                value = self.integer()
                return Token(value, Tokens.INTEGER, start_col, self.row)

            if self.current_char.isalpha():
                start_col = self.col
                id = self.word()
                if id.upper() in RESERVED_KEYWORDS:
                    return Token(id, Tokens[id.upper()], start_col, self.row)
                else:
                    return Token(id, Tokens.IDENTIFIER, start_col, self.row)

            if self.current_char in ('\"', "\'"):
                start_col = self.col
                constant_literal = self.build_string()
                tk = Token(constant_literal, Tokens.STRING, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '(':
                if self.peek('*'):
                    ''' comment handler '''
                    self.advance()
                    self.advance()
                    while(self.current_char is not None):
                        if(self.current_char == '*' and self.peek(')')):
                            self.advance()
                            self.advance()
                            return ''
                        self.advance()

                    return self.error(msg="Unmatched closing comment delimiter at [{},{}]")
                else:
                    tk = Token('(', Tokens.OPEN_PAR, self.col, self.row)
                    self.advance()
                    return tk

            if self.current_char == ')':
                tk = Token(')', Tokens.CLOSE_PAR, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '[':
                tk = Token('[', Tokens.OPEN_BRA, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == ']':
                tk = Token(']', Tokens.CLOSE_BRA, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '+':
                tk = Token('+', Tokens.PLUS, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '-':
                tk = Token('-', Tokens.MINUS, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '*':
                tk = Token('*', Tokens.MULT, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '/':
                tk = Token('/', Tokens.DIV, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == ';':
                tk = Token(';', Tokens.SEMICOLON, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == ',':
                tk = Token(',', Tokens.COMMA, self.col, self.row)
                self.advance()
                return tk

            if self.current_char in ('=', '<', '>'):
                if self.peek('=') and self.current_char != '=':
                    tk = Token(self.current_char+'=', Tokens.OP_RELAT, self.col, self.row)
                    self.advance()
                    # self.advance()
                elif self.current_char == '<' and self.peek('>'):
                    tk = Token('<>', Tokens.OP_RELAT, self.col, self.row)
                    self.advance()
                    # self.advance()
                else:
                    tk = Token(self.current_char, Tokens.OP_RELAT, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == ':':
                if self.peek('='):
                    tk = Token(':=', Tokens.ASSIGN, self.col, self.row)
                    self.advance()
                    self.advance()
                    return tk
                else:
                    tk = Token(self.current_char, Tokens.DECLR, self.col, self.row)
                    self.advance()
                    return tk

            if self.current_char == '.':
                if self.peek('.'):
                    tk = Token('..', Tokens.THROUGH, self.col, self.row)
                    self.advance()
                    self.advance()
                else:
                    tk = Token('.', Tokens.DOT, self.col, self.row)
                    self.advance()
                return tk

            else:
                invalid_tk = Token(self.current_char, Tokens.INVALID, self.col, self.row)
                self.error()
                self.advance()
                return invalid_tk

        return Token('EOF', None, self.col, self.row)
