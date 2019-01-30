from enum import Enum


class Token:
    def __init__(self, value, type, col, row):
        self.value = value
        self.type = type
        self.row = row
        self.col = col

    def __str__(self):
        return "\t[{:04d}, {:04d}] ({:04d}, {:10s}) {{{}}}".format(self.row, self.col+1, self.type.value, self.type.name, self.value)


class Tokens(Enum):
    IDENTIFIER = 1
    CONST_INT = 2
    CONST_REAL = 3
    CONST_BOOL = 4
    CONST_CHAR = 5
    CONST_STR = 6
    INTEGER = 7
    REAL = 8
    CHAR = 9
    STRING = 10
    BOOL = 11
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
    READLN = 26
    WRITE = 27
    WRITELN = 28
    AND = 29
    OR = 30
    NOT = 31
    OPEN_PAR = 32
    CLOSE_PAR = 33
    OPEN_BRA = 34
    CLOSE_BRA = 35
    SEMICOLON = 36
    COLON = 37
    QUOTE = 38
    OPEN_COM = 39
    CLOSE_COM = 40
    MULT = 41
    PLUS = 42
    MINUS = 43
    REAL_DIV = 44
    INT_DIV = 45
    OP_RELAT = 46
    ASSIGN = 47
    UNARY = 48
    BIT_NOT = 49
    BIT_AND = 50
    BIT_NOR = 51
    DOT = 52
    PROGRAM = 53
    DECLR = 54
    VAR = 55
    COMMA = 56
    EXIT = 57
    ARRAY = 58
    OF = 59
    THROUGH = 60
    TYPE = 61
    INVALID = 62
    EOF = 63
