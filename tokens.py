from enum import Enum


class Token:
    def __init__(self, value, categ, col, row):
        self.value = value
        self.categ = categ
        self.row = row
        self.col = col

    def __str__(self):
        return "              [{:04d}, {:04d}] ({:04d}, {:10s}) {{{}}}".format(self.row,
                    self.col+1, self.categ.value, self.categ.name, self.value)


class Category(Enum):
    IDENTIFIER = 1
    CONST_INT = 2
    CONST_REAL = 3
    CONST_BOOL = 4
    CONST_CHAR = 5
    CONST_STR = 6
    INTEGER = 7
    REAL = 8
    BOOL = 9
    CHAR = 10
    STRING = 11
    USES = 12
    FUNCTION = 13
    PROCEDURE = 14
    BEGIN = 15
    END = 16
    IF = 17
    THEN = 18
    ELSE = 19
    FOR = 20
    TO = 21
    STEP = 22
    WHILE = 23
    DO = 24
    READ = 25
    WRITE = 26
    TYPE = 27
    OF = 28
    ARRAY = 29
    EXIT = 30
    PROGRAM = 31
    VAR = 32
    OPEN_PAR = 33
    CLOSE_PAR = 34
    OPEN_BRA = 35
    CLOSE_BRA = 36
    SEMICOLON = 37
    DECLR = 38
    QUOTE = 39
    OPEN_COM = 40
    CLOSE_COM = 41
    COMMA = 42
    THROUGH = 43
    MINUS_UNAR = 44
    DOT = 45
    NOT = 46
    MULOP = 47
    ADDOP = 48
    MINUS = 49
    PLUS = 50
    OP_RELAT = 51
    ASSIGN = 52
    INVALID = 53
    EOF = 54
    WRITELN = 55
    CONST = 56
    AND = 57
    OR = 58
    BREAK = 59
    CONTINUE = 60
