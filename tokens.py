class Token:
    def __init__(self, value, type, col, row):
        self.value = value
        self.type = type
        self.row = row
        self.col = col

    def __str__(self):
        return "[{:4d}, {:4d}] ({:4d}, {:10s}) {{ {} }}".format(self.row, self.col, self.type.value, self.type.name, self.value)


from enum import Enum
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
    DIV = 32
    OPEN_PAR = 33
    CLOSE_PAR = 34
    OPEN_BRA = 35
    CLOSE_BRA = 36
    SEMICOLON = 37
    COLON = 38
    QUOTE = 39
    OPEN_COM = 40
    CLOSE_COM = 41
    MULT = 42
    PLUS = 43
    MINUS = 44
    OP_RELAT = 45
    ASSIGN = 46
    UNARY = 47
    BIT_NOT = 48
    BIT_AND = 49
    BIT_NOR = 50
    DOT = 51
    PROGRAM = 52
    DECLR = 53
    VAR = 54
    COMMA = 55
    EXIT = 56
    ARRAY = 57
    OF = 58
    THROUGH = 59
    TYPE = 60
    INVALID = 61
