from tokens import Token, Category

RESERVED_KEYWORDS = [
    'BEGIN', 'END', 'IF', 'ELSE', 'INTEGER', 'REAL', 'CHAR', 'CONST',
     'STRING', 'WRITE', 'PROGRAM', 'VAR', 'THEN', 'BOOLEAN',
     'PROCEDURE', 'FUNCTION', 'EXIT', 'WHILE', 'DO', 'READ',
     'ARRAY', 'OF', 'TYPE', 'STEP', 'CONST', 'AND', 'OR', 'STEP',
     'NOT', 'USES', 'FOR', 'TO', 'WRITELN', 'CONST', 'BREAK', 'CONTINUE'
 ]

SPECIAL_CHARACTERS = {
    '[': Category.OPEN_BRA, ']': Category.CLOSE_BRA, '+': Category.PLUS,
    '-': Category.MINUS, '*': Category.MULT, '/': Category.DIV,
    ';': Category.SEMICOLON, ',': Category.COMMA,
    '(': Category.OPEN_PAR, ')': Category.CLOSE_PAR, '.': Category.DOT,
    '<': Category.OP_RELAT, '>': Category.OP_RELAT, '<=': Category.OP_RELAT,
    '>=': Category.OP_RELAT, '=': Category.OP_RELAT, ':=': Category.ASSIGN,
    ':': Category.DECLR, '..': Category.THROUGH
}


class Lexer:
    def __init__(self, filename):
        self.row = 1
        self.col = 0
        self.file = open(filename, 'r')
        self.text = self.file.readline().rstrip()
        print("%4d  %s" % (self.row, self.text.rstrip()) )
        self.current_char = self.text[self.col]

    def error(self, token=None, msg=None):
        if msg:
            print(msg.format(self.row, self.col))
        elif token:
            print("Invalid syntax {} at [{},{}]".format(token, self.row, self.col))
        else:
            print("Invalid character {} at [{},{}]".format(self.current_char, self.row, self.col))

    def advance(self, comment=None):
        self.col += 1
        if self.col > len(self.text):
            self.col = 0
            self.row += 1
            self.text = self.file.readline()
            while self.text == '\n':
                self.row += 1
                self.text = self.file.readline()

            self.current_char = self.text[self.col] if len(self.text) > 0 else None
            if(len(self.text) > 0 and self.current_char != '(' and not comment):
                print("%4d  %s" % (self.row, self.text.rstrip()) )

        elif self.col == len(self.text):
            self.current_char = ' '
            return
        else:
            self.current_char = self.text[self.col]

    def skip_ws(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def peek(self, next_char=None):
        next_col = self.col+1
        if next_col < len(self.text) and self.text[next_col] is not None:
            if next_char:
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

    def build_potency(self):
        potency = ''
        if self.current_char == 'e' and self.peek() in ('+', '-'):
            potency += self.current_char
            self.advance()
            potency += self.current_char
            self.advance()
            potency += self.build_number()
        return potency

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
                if self.current_char in ('.') and self.peek() != '.':
                    value += self.current_char
                    self.advance()
                    value += self.build_number()
                    value += self.build_potency()
                    return Token(value, Category.CONST_REAL, start_col, self.row)

                potency = self.build_potency()
                if potency:
                    return Token(value+potency, Category.CONST_REAL, start_col, self.row)
                else:
                    return Token(value, Category.CONST_INT, start_col, self.row)

            if self.current_char.isalpha():
                ''' reserved keywords recognition '''
                start_col = self.col
                id = self.word()
                if id.upper() in ('TRUE', 'FALSE'):
                    return Token(id, Category.CONST_BOOL, start_col, self.row)
                if id.upper() in RESERVED_KEYWORDS:
                    return Token(id, Category[id.upper()], start_col, self.row)
                else:
                    return Token(id, Category.IDENTIFIER, start_col, self.row)

            if self.current_char in ('\"', "\'"):
                ''' string recognition '''
                start_col = self.col + 1
                constant_literal = self.build_string(self.current_char)
                tk = Token(constant_literal, Category.CONST_STR, start_col, self.row)
                self.advance()
                return tk

            if self.current_char == '/' and self.peek('/'):
                ''' single line comment '''
                self.text = self.file.readline()
                self.row += 1
                self.col = 0
                print("%4d  %s" % (self.row, self.text.rstrip()))
                self.current_char = self.text[self.col]
                return self.get_next_token()

            if self.current_char == '(' and self.peek('*'):
                ''' multi line comment '''
                self.advance(comment=True)
                self.advance(comment=True)
                while self.current_char != '*':
                    self.advance(comment=True)
                self.advance(comment=True)
                self.advance(comment=True)
                return self.get_next_token()

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
                invalid_tk = Token(self.current_char, Category.INVALID, self.col, self.row)
                self.error()
                self.advance()
                return invalid_tk

        return Token('EOF', Category.EOF, self.col, self.row)
