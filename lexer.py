from tokens import Token, Tokens

RESERVED_KEYWORDS = [
    'BEGIN', 'END', 'IF', 'ELSE', 'INTEGER', 'REAL', 'CHAR','CONST',
     'STRING', 'WRITE','WRITELN', 'PROGRAM', 'VAR', 'THEN','BOOLEAN',
     'PROCEDURE', 'FUNCTION', 'EXIT', 'WHILE', 'DO', 'READ', 'READLN',
     'ARRAY', 'OF', 'TYPE', 'STEP', 'CONST', 'AND', 'OR', 'DIV', 'STEP',
     'NOT', 'USES', 'FOR', 'TO'
 ]

SPECIAL_CHARACTERS = {
    '[': Tokens.OPEN_BRA, ']': Tokens.CLOSE_BRA, '+': Tokens.PLUS, '-': Tokens.MINUS,
    '*': Tokens.MULT, '/': Tokens.DIV, ';': Tokens.SEMICOLON, ',': Tokens.COMMA,
    '(': Tokens.OPEN_PAR, ')': Tokens.CLOSE_PAR, '.': Tokens.DOT, '<':Tokens.OP_RELAT,
    '>':Tokens.OP_RELAT, '<=': Tokens.OP_RELAT , '>=': Tokens.OP_RELAT,
    '=': Tokens.OP_RELAT, ':=': Tokens.ASSIGN, ':':Tokens.DECLR,
    '..': Tokens.THROUGH
}

class Lexer:
    def __init__(self):
        self.row = 0

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

    def peek(self, next_char=None):
        next_col = self.col+1
        if next_col < len(self.text) and self.text[next_col] is not None:
            if(next_char):
                return next_char == self.text[next_col]
            else:
                return self.text[next_col]
        else:
            return False

    def build_number(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return number

    def word(self):
        word = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            word += self.current_char
            self.advance()
        return word

    def build_string(self, c):
        literal = ''
        self.advance()
        while self.current_char is not None and self.current_char != c:
            literal += self.current_char
            self.advance()
        if self.current_char == c:
            return literal
        else:
            self.error(msg="Unmatched "+c+" at [{},{}].")

    def get_next_token(self):
        while self.current_char is not None:

            if len(self.text) == 0:
                continue

            if self.current_char.isspace():
                self.skip_ws()
                continue

            if self.current_char.isdigit():
                start_col = self.col
                value = self.build_number()
                if self.current_char == '.':
                    value +=  '.'
                    self.advance()
                    value += self.build_number()
                    return Token(value, Tokens.REAL, start_col, self.row)

                return Token(value, Tokens.INTEGER, start_col, self.row)

            if self.current_char.isalpha():
                ''' reserved keywords recognition '''
                start_col = self.col
                id = self.word()
                if id.upper() in RESERVED_KEYWORDS:
                    return Token(id, Tokens[id.upper()], start_col, self.row)
                else:
                    return Token(id, Tokens.IDENTIFIER, start_col, self.row)

            if self.current_char in ('\"', "\'"):
                ''' string recognition '''
                start_col = self.col
                constant_literal = self.build_string(self.current_char)
                tk = Token(constant_literal, Tokens.STRING, self.col, self.row)
                self.advance()
                return tk

            if self.current_char == '(':
                if self.peek('*'):
                    ''' comment recognition '''
                    self.advance()
                    self.advance()
                    while(self.current_char is not None):
                        if(self.current_char == '*' and self.peek(')')):
                            self.advance()
                            self.advance()
                            return ''
                        self.advance()

                    return self.error(msg="Unmatched comment delimiter at [{},{}]")

            if self.current_char in SPECIAL_CHARACTERS:
                c = self.current_char
                if(self.peek() and c+self.peek() in SPECIAL_CHARACTERS):
                    tk_id = c+self.peek()
                    tk = Token(tk_id, SPECIAL_CHARACTERS[tk_id], self.col, self.row)
                    self.advance()
                else:
                    tk = Token(c, SPECIAL_CHARACTERS[c], self.col, self.row)
                self.advance()
                return tk

            else:
                invalid_tk = Token(self.current_char, Tokens.INVALID, self.col, self.row)
                self.error()
                self.advance()
                return invalid_tk

        return Token('EOF', None, self.col, self.row)
