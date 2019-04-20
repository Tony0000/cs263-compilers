from tokens import Category
STD_TYPE = [Category.INTEGER, Category.REAL,
            Category.STRING, Category.BOOL,
            Category.CHAR]

CONST_VALUES = [Category.CONST_INT, Category.CONST_REAL,
                Category.CONST_STR, Category.CONST_BOOL,
                Category.CONST_CHAR]

STMT_OPTIONS = [Category.WHILE, Category.IF, Category.FOR, Category.BEGIN,
                Category.WRITE, Category.WRITELN, Category.READ,
                Category.IDENTIFIER]

FACTOR_OPTIONS = [Category.CONST_INT, Category.CONST_REAL, Category.OPEN_PAR,
                  Category.NOT, Category.IDENTIFIER, Category.MINUS,
                  Category.PLUS]


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.list_sub_pgm = []
        self.user_defined_type = []

    def error(self, expected):
        raise Exception("Invalid syntax. Expected ", expected,
                        "and found ", self.current_token.categ, " at line ",
                         self.current_token.row,
                         "and  column.", self.current_token.col)

    def consume(self, token_categ):
        if self.current_token.categ == token_categ:
            print(self.current_token)
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_categ)

    def empty(self):
        pass

    def program(self):
        """
            program id semicolon
            LIBRARIES
            DECLRS
            SUB_PGM_DECLRS
            COMPOUND_STMT
            dot
        """
        print('           PROGRAM = program id semicolon LIBRARIES DECLRS SUB_PGM_DECLRS COMPOUND_STMT dot')
        self.consume(Category.PROGRAM)
        self.identifier()
        self.consume(Category.SEMICOLON)
        self.libraries()
        self.declarations()
        self.sub_program_declrs()
        self.compound_statement()
        self.consume(Category.DOT)

    def libraries(self):
        if self.current_token.categ == Category.USES:
            print('           LIBRARIES = uses ID_LIST semicolon')
            self.consume(Category.USES)
            self.id_list()
            self.consume(Category.SEMICOLON)
        else:
            print('           LIBRARIES = epsilon')
            self.empty()

    def identifier(self):
        self.consume(Category.IDENTIFIER)

    def identifier_list(self):
        print('           ID_LIST = id ID_LISTR')
        self.consume(Category.IDENTIFIER)
        self.identifier_listr()

    def identifier_listr(self):
        ''' ID_LISTR = comma id ID_LISTR | epsilon '''
        if self.current_token.categ == Category.COMMA:
            print('           ID_LISTR = comma id ID_LISTR')
            self.consume(Category.COMMA)
            self.identifier()
            self.identifier_listr()
        else:
            print('           ID_LISTR = epsilon')
            self.empty()

    def declarations(self):
        """
            var VAR_DECLR DECLRSR |
            const CONST_DECLR DECLRSR
            type id TYPE
            | epsilon
        """
        if self.current_token.categ == Category.VAR:
            print('           DECLRS = var VAR_DECLRS')
            self.consume(Category.VAR)
            self.var_declarations()
            self.declarations()
        elif self.current_token.categ == Category.CONST:
            print('           DECLRS = const CONST_DECLRS')
            self.consume(Category.CONST)
            self.const_declarations()
            self.declarations()
        elif self.current_token.categ == Category.TYPE:
            print('           DECLRS = type NEW_TYPE DECLRSR')
            self.consume(Category.TYPE)
            self.new_type()
            self.declarations()
        else:
            print('           DECLRS = epsilon')
            self.empty()

    def const_declarations(self):
        ''' id assignop CONST_VALUES semicolon CONST_DECLR | epsilon '''
        if self.current_token.categ == Category.IDENTIFIER:
            print('           CONST_DECLRS = id assignop CONST_VALUES semicolon CONST_DECLR')
            self.consume(Category.IDENTIFIER)
            self.consume(Category.ASSIGN)
            if self.current_token.categ in CONST_VALUES:
                self.consume(self.current_token.categ)
            self.consume(Category.SEMICOLON)
            self.const_declarations()
        else:
            print('           CONST_DECLRS = epsilon')
            self.empty()

    def var_declarations(self):
        ''' ID_LIST dp TYPE semicolon VAR_DECLR | epsilon'''
        if self.current_token.categ == Category.IDENTIFIER:
            print('           VAR_DECLRS = ID_LIST dp TYPE semicolon VAR_DECLRS')
            self.identifier_list()
            self.consume(Category.DECLR)
            self.type_specification()
            self.consume(Category.SEMICOLON)
            self.var_declarations()
        else:
            print('           VAR_DECLRS = epsilon')
            self.empty()

    def type_specification(self):
        ''' STD_TYPE
        | array lbrkt CTRL_VALUE through CTRL_VALUE rbrkt of STD_TYPE '''
        if self.current_token.categ in STD_TYPE or self.current_token.value in self.user_defined_type:
            print('           TYPE = STD_TYPE')
            print('           STD_TYPE = ', self.current_token.value)
            self.consume(self.current_token.categ)
        elif self.current_token.categ == Category.ARRAY:
            print('           TYPE = array lbrkt CTRL_VALUE through CTRL_VALUE rbrkt of STD_TYPE')
            self.consume(Category.ARRAY)
            self.consume(Category.OPEN_BRA)
            self.ctrl_value()
            self.consume(Category.THROUGH)
            self.ctrl_value()
            self.consume(Category.CLOSE_BRA)
            self.consume(Category.OF)
            if self.current_token.categ in STD_TYPE or self.current_token.categ in self.user_defined_type:
                print('           STD_TYPE = ', str(self.current_token.value))
                self.consume(self.current_token.categ)
        else:
            self.error("standard type, user defined type or array")

    def new_type(self):
        if self.current_token.categ == Category.IDENTIFIER:
            print('           NEW_TYPE = id assignop TYPE semicolon NEW_TYPE')
            self.user_defined_type.append(self.current_token.value)
            self.consume(Category.IDENTIFIER)
            self.consume(Category.ASSIGN)
            self.type_specification()
            self.consume(Category.SEMICOLON)
            self.new_type()
        else:
            print('new_type = epsilon')
            self.empty()

    def sub_program_declrs(self):
        ''' SUB_PGM_DECLR semicolon SUB_PGM_DECLRS | epsilon '''
        if self.current_token.categ in [Category.FUNCTION, Category.PROCEDURE]:
            print('           SUB_PGM_DECLRS = SUB_PGM_DECLR semicolon SUB_PGM_DECLRS')
            self.sub_program_declr()
            self.consume(Category.SEMICOLON)
            self.sub_program_declrs()
        else:
            print('           SUB_PGM_DECLRS = epsilon')
            self.empty()

    def sub_program_declr(self):
        ''' SUB_PGM_HEAD DECLRS COMPOUND_STMT '''
        print('           SUB_PGM_DECLR = SUB_PGM_HEAD DECLRS COMPOUND_STMT')
        self.sub_program_head()
        self.declarations()
        self.compound_statement()

    def sub_program_head(self):
        '''
            function SUB_PGM_HEAD_PARAM declr STD_TYPE semicolon
            | procedure SUB_PGM_HEAD_PARAM semicolon
        '''
        if self.current_token.categ == Category.FUNCTION:
            print('           SUB_PGM_HEAD = function SUB_PGM_HEAD_PARAM declr STD_TYPE semicolon')
            self.consume(Category.FUNCTION)
            self.sub_program_head_param()
            self.consume(Category.DECLR)
            self.type_specification()
            self.consume(Category.SEMICOLON)
        elif self.current_token.categ == Category.PROCEDURE:
            print('           SUB_PGM_HEAD = procedure SUB_PGM_HEAD_PARAM semicolon')
            self.consume(Category.PROCEDURE)
            self.sub_program_head_param()
            self.consume(Category.SEMICOLON)

    def sub_program_head_param(self):
        print('           SUB_PGM_HEAD_PARAM = id lparen PARAM_LIST rparen')
        self.list_sub_pgm.append(self.current_token.value)
        self.consume(Category.IDENTIFIER)
        self.consume(Category.OPEN_PAR)
        self.parameter_list()
        self.consume(Category.CLOSE_PAR)

    def parameter_list(self):
        ''' ID_LIST dp TYPE PARAM_LISTR | epsilon '''
        if self.current_token.categ == Category.IDENTIFIER:
            print('           PARAM_LIST = ID_LIST dp TYPE PARAM_LISTR')
            self.identifier_list()
            self.consume(Category.DECLR)
            self.type_specification()
            self.parameter_listr()
        else:
            print('           PARAM_LIST = epsilon')
            self.empty()

    def parameter_listr(self):
        ''' semicolon ID_LIST dp TYPE PARAM_LIST | epsilon '''
        if self.current_token.categ == Category.SEMICOLON:
            print('           PARAM_LISTR = semicolon ID_LIST dp TYPE PARAM_LIST')
            self.consume(Category.SEMICOLON)
            self.identifier_list()
            self.consume(Category.DECLR)
            self.type_specification()
            self.parameter_listr()
        else:
            print('           PARAM_LIST = epsilon')
            self.empty()

    def compound_statement(self):
        ''' begin OPT_STMT end '''
        print('           COMPOUND_STMT = begin OPT_STMT end')
        self.consume(Category.BEGIN)
        self.opt_statement()
        self.consume(Category.END)

    def opt_statement(self):
        if self.current_token.categ in STMT_OPTIONS:
            print('           OPT_STMT = STMT_LIST')
            self.statement_list()
        else:
            print('           OPT_STMT = epsilon')
            self.empty()

    def statement_list(self):
        print('           STMT_LIST = STMT STMT_LISTR')
        self.statement()
        self.statement_listr()

    def statement_listr(self):
        ''' STMT_LISTR -> semicolon STMT STMT_LISTR | epsilon '''
        if self.current_token.categ == Category.SEMICOLON:
            print('           STMT_LISTR = semicolon STMT STMT_LISTR')
            self.consume(Category.SEMICOLON)
            self.statement()
            self.statement_listr()
        else:
            print('           STMT_LISTR = epsilon')
            self.empty()

    def statement(self):
        '''
            VARIABLE assignop EXPRESSION
            | COMPOUND_STMT
            | PROCEDURE_STMT
            | if EXPRESSION then STMT OPT_CONDITIONAL_STMT
            | while EXPRESSION do STMT
            | for id assignop const_int to const_int OPT_FOR_STEP do COMPOUND_STMT
        '''
        if self.current_token.categ == Category.IDENTIFIER and self.current_token.value not in self.list_sub_pgm:
            print('           STMT = VARIABLE assignop EXPRESSION')
            self.variable()
            self.consume(Category.ASSIGN)
            self.expression()
        elif self.current_token.categ == Category.BEGIN:
            print('           STMT = COMPOUND_STMT')
            self.compound_statement()
        elif self.current_token.categ == Category.FOR:
            print('           STMT = for id assignop CTRL_VALUE to CTRL_VALUE OPT_FOR_STEP do COMPOUND_STMT')
            self.consume(Category.FOR)
            self.consume(Category.IDENTIFIER)
            self.consume(Category.ASSIGN)
            self.ctrl_value()
            self.consume(Category.TO)
            self.ctrl_value()
            self.opt_for_step()
            self.consume(Category.DO)
            self.compound_statement()
        elif self.current_token.categ == Category.IF:
            print('           STMT = if EXPRESSION then STMT OPT_CONDITIONAL_STMT')
            self.consume(Category.IF)
            self.expression_list()
            self.consume(Category.THEN)
            self.statement()
            self.opt_conditional_statement()
        elif self.current_token.categ == Category.WHILE:
            print('           STMT = while EXPRESSION do STMT')
            self.consume(Category.WHILE)
            self.expression_list()
            self.consume(Category.DO)
            self.statement()
        else:
            print('           STMT = PROCEDURE_STMT')
            self.procedure_statement()

    def opt_conditional_statement(self):
        ''' else STMT | epsilon '''
        if self.current_token.categ == Category.ELSE:
            print('           OPT_CONDITIONAL_STMT = else STMT')
            self.consume(Category.ELSE)
            self.statement()
        else:
            print('           OPT_CONDITIONAL_STMT = epsilon')
            self.empty()

    def opt_for_step(self):
        ''' step const_int | epsilon '''
        if self.current_token.categ == Category.STEP:
            print('           OPT_FOR_STEP = step const_int')
            self.consume(Category.ELSE)
            self.statement()
        else:
            print('           OPT_FOR_STEP = epsilon')
            self.empty()

    def ctrl_value(self):
        if self.current_token.categ == Category.IDENTIFIER:
            print('           CTRL_VALUE = id')
            self.consume(Category.IDENTIFIER)
        else:
            print('           CTRL_VALUE = const_int')
            self.consume(Category.CONST_INT)

    def procedure_statement(self):
        '''
            read lparen ID_LIST rparen
            | write lparen WRITE_PARAM_LIST
            | writeln lparen WRITE_PARAM_LIST
            | id lparen ID_LIST rparen .
        '''
        if self.current_token.categ == Category.READ:
            print('           PROCEDURE_STMT = read lparen VAR_LIST rparen')
            self.consume(Category.READ)
            self.consume(Category.OPEN_PAR)
            self.variable_list()
            self.consume(Category.CLOSE_PAR)
        elif self.current_token.categ == Category.WRITE:
            print('           PROCEDURE_STMT = write lparen WRITE_PARAM_LIST')
            self.consume(Category.WRITE)
            self.consume(Category.OPEN_PAR)
            self.write_param_list()
        elif self.current_token.categ == Category.WRITELN:
            print('           PROCEDURE_STMT = writeln lparen WRITE_PARAM_LIST')
            self.consume(Category.WRITELN)
            self.consume(Category.OPEN_PAR)
            self.write_param_list()
        else:
            print('           PROCEDURE_STMT = id lparen ID_LIST rparen')
            self.identifier()
            self.consume(Category.OPEN_PAR)
            self.identifier_list()
            self.consume(Category.CLOSE_PAR)

    def write_param_list(self):
        if self.current_token.categ == Category.CONST_STR:
            print('           WRITE_PARAM_LIST = const_string FIELD_WIDTH WRITE_PARAM_LISTR')
            self.consume(Category.CONST_STR)
            self.field_width()
            self.write_param_listr()
        else:
            print('           WRITE_PARAM_LIST = VARIABLE FIELD_WIDTH WRITE_PARAM_LISTR')
            self.variable()
            self.field_width()
            self.write_param_listr()

    def write_param_listr(self):
        if self.current_token.categ == Category.COMMA:
            print('           WRITE_PARAM_LISTR = comma WRITE_PARAM_LIST')
            self.consume(Category.COMMA)
            self.write_param_list()
        else:
            print('           WRITE_PARAM_LISTR = rparen')
            self.consume(Category.CLOSE_PAR)

    def field_width(self):
        if self.current_token.categ == Category.DECLR:
            print('           FIELD_WIDTH = dp const_int PRECISION')
            self.consume(Category.DECLR)
            self.consume(Category.CONST_INT)
            self.precision()
        else:
            print('           FIELD_WIDTH = epsilon')
            self.empty()

    def precision(self):
        if self.current_token.categ == Category.DECLR:
            print('           PRECISION = dp const_int')
            self.consume(Category.DECLR)
            self.consume(Category.CONST_INT)
        else:
            print('           PRECISION = epsilon')
            self.empty()

    def variable(self):
        print('           VARIABLE = id INDEX')
        self.consume(Category.IDENTIFIER)
        self.index()

    def variable_list(self):
        ''' VAR_LIST =  VARIABLE VARIABLE_LISTR '''
        self.variable()
        self.variable_listr()

    def variable_listr(self):
        ''' VAR_LIST =  comma VARIABLE_LIST | epsilon '''
        if self.current_token.categ == Category.COMMA:
            print('           VAR_LISTR = comma VARIABLE_LIST')
            self.consume(Category.COMMA)
            self.variable_list()
        else:
            print('           VAR_LISTR = epsilon')
            self.empty()

    def index(self):
        if self.current_token.categ == Category.OPEN_BRA:
            print('           INDEX = lbrkt SIMPLE_EXPRESSION rbrkt')
            self.consume(Category.OPEN_BRA)
            self.simple_expression()
            self.consume(Category.CLOSE_BRA)
        else:
            print('           INDEX = epsilon')
            self.empty()

    def expression_list(self):
        print('           EXPRESSION_LIST = EXPRESSION EXPRESSION_LISTR')
        self.expression()
        self.expression_listr()

    def expression_listr(self):
        if self.current_token.categ in [Category.AND, Category.OR]:
            print('           EXPRESSION_LISTR = logicop EXPRESSION_LIST')
            self.consume(self.current_token.categ)
            self.expression_list()
        else:
            print('           EXPRESSION_LISTR = epsilon')
            self.empty()

    def expression(self):
        print('           EXPRESSION = SIMPLE_EXPRESSION EXPRESSIONR')
        self.simple_expression()
        self.expressionr()

    def expressionr(self):
        if self.current_token.categ == Category.OP_RELAT:
            print('           EXPRESSIONR = relop SIMPLE_EXPRESSION')
            self.consume(Category.OP_RELAT)
            self.simple_expression()
        else:
            print('           EXPRESSIONR = epsilon')
            self.empty()

    def simple_expression(self):
        ''' TERM SIMPLE_EXPRESSIONR
            | SIGN TERM SIMPLE_EXPRESSIONR '''
        if self.current_token.categ in FACTOR_OPTIONS:
            print('           SIMPLE_EXPRESSION = TERM SIMPLE_EXPRESSIONR')
            self.term()
            self.simple_expressionr()
        else:
            print('           SIMPLE_EXPRESSION = SIGN TERM SIMPLE_EXPRESSIONR')
            self.sign()
            self.term()
            self.simple_expressionr()

    def simple_expressionr(self):
        if self.current_token.categ == Category.ADDOP:
            print('           SIMPLE_EXPRESSIONR = addop SIMPLE_EXPRESSION')
            self.consume(Category.ADDOP)
            self.simple_expression()
        else:
            print('           SIMPLE_EXPRESSIONR = epsilon')
            self.empty()

    def term(self):
        print('           TERM = FACTOR TERMR')
        self.factor()
        self.termr()

    def termr(self):
        if self.current_token.categ == Category.MULOP:
            print('           TERMR = mulop FACTOR TERMR')
            self.consume(Category.MULOP)
            self.factor()
            self.termr()
        else:
            print('           TERMR = epsilon')
            self.empty()

    def factor(self):
        if self.current_token.categ == Category.IDENTIFIER:
            print('           FACTOR = VARIABLE')
            self.variable()
        elif self.current_token.categ == Category.CONST_INT:
            print('           FACTOR = const_int')
            self.consume(Category.CONST_INT)
        elif self.current_token.categ == Category.CONST_REAL:
            print('           FACTOR = const_real')
            self.consume(Category.CONST_REAL)
        elif self.current_token.categ == Category.NOT:
            print('           FACTOR = not FACTOR')
            self.consume(Category.NOT)
            self.factor()
        else:
            print('           TERMR = epsilon')
            self.empty()

    def sign(self):
        if self.current_token.categ == Category.PLUS:
            print('           SIGN = +')
            self.consume(Category.PLUS)
        elif self.current_token.categ == Category.MINUS:
            print('           SIGN = -')
            self.consume(Category.MINUS)

    def parse(self):
        self.program()
        if self.current_token.categ != Category.EOF:
            self.error("Expected end of file")
