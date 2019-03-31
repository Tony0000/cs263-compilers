from tokens import Category


class AST(object):
    """Abstract syntax tree"""
    pass


class Program(AST):
    def __init__(self, name, block):
        self.name = name
        self.block = block


class Block(AST):
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class DeclrOp(AST):
    def __init__(self, var, type):
        self.var = var
        self.type = type

    def __str__(self):
        return "{:s} : {:s}".format(self.var, self.type)


class BinaryOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr


class CompoundOp(AST):
    """ BEGIN ... END block """
    def __init__(self):
        self.children = []


class AssignOp(AST):
    """ var_name := expression """
    def __init__(self, left, token, right):
        self.left = left
        self.token = self.op = token
        self.right = right

    def __str__(self):
        return "\t({:10s}, {:10s}) {{{}}}".format(self.left, self.right)


class Numeric(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Variable(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class NoOp(AST):
    """ An empty BEGIN ... END block """
    pass


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax.")

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.lexer.error()

    def program(self):
        """ PROGRAM variable SEMICOLON block DOT """
        self.consume(Category.PROGRAM)
        name = self.variable()
        self.consume(Category.SEMICOLON)
        print('PROGRAM', name)
        node = self.block()

        node = Program(name, node)
        self.consume(Category.DOT)
        return node

    def block(self):
        declr_nodes = self.declarations()
        for node in declr_nodes:
            print(node)
        stmts_nodes = self.compound_statement()
        node = Block(declr_nodes, stmts_nodes)
        return node

    def declarations(self):
        declrs = []
        if(self.current_token.type == Category.VAR):
            self.consume(Category.VAR)
            while(self.current_token.type == Category.IDENTIFIER):
                # concatenates two lists
                declrs.extend(self.variable_declaration())
                self.consume(Category.SEMICOLON)
        return declrs

    def variable_declaration(self):
        node_list = []
        node_list.append(self.variable())
        while(self.current_token.type == Category.COMMA):
            self.consume(Category.COMMA)
            node_list.append(self.variable())

        self.consume(Category.DECLR)
        var_dclrs = []
        type = self.type_specification()
        for node in node_list:
            var_dclrs.append(DeclrOp(var=node, type=type))
        return var_dclrs

    def type_specification(self):
        # Real, Integer and custom data types
        if self.current_token.type in [Category.INTEGER, Category.REAL]:
            node = Type(token=self.current_token)
            self.consume(self.current_token.type)
        else:
            # TODO: conferir se é erro de sintaxe
            self.error()
            #node = Type(token=self.current_token)
        return node

    def compound_statement(self):
        """ BEGIN statement_list END """
        self.consume(Category.BEGIN)
        nodes_list = self.statement_list()
        self.consume(Category.END)

        root = CompoundOp()
        for node in nodes_list:
            root.children.append(node)
        return root

    def statement_list(self):
        """
            statement
            | statement SEMICOLON statement_list
        """
        node = self.statement()
        nodes_list = [node]
        while(self.current_token.type == Category.SEMICOLON):
            self.consume(Category.SEMICOLON)
            nodes_list.append(self.statement())
        return nodes_list

    def assign_statement(self):
        """ variable ASSIGN expression """
        left = self.variable()
        token = self.current_token
        self.consume(Category.ASSIGN)
        right = self.expression()
        node = AssignOp(left, token, right)
        return node

    def statement(self):
        """
                compound_statement
            |   assign_statement
            |   empty_statement
        """
        if self.current_token.type == Category.BEGIN:
            nodes_list = self.compound_statement()
        elif self.current_token.type == Category.IDENTIFIER:
            nodes_list = self.assign_statement()
        else:
            nodes_list = self.empty()
        self.consume(Category.SEMICOLON)
        return nodes_list

    def variable(self):
        """ identifier """
        node = Variable(self.current_token)
        self.consume(Category.IDENTIFIER)
        return node

    def empty(self):
        """ empty production """
        return NoOp()

    def expression(self):
        """ term ((PLUS | MINUS) term)* """
        self.current_token = self.lexer.get_next_token()

        node = self.term()
        while self.current_token.type in (Category.PLUS, Category.MINUS):
            token = self.current_token
            self.consume(Category.PLUS)
            node = BinaryOp(left=node, op=token, right=self.term())
        return node

    def term(self):
        """ factor ((MULT | DIV) factor)* """
        node = self.factor()

        while self.current_token.type in (Category.MULT, Category.DIV):
            token = self.current_token
            self.consume(token.type)
            node = BinaryOp(left=node, op=token, right=self.factor())
        return node

    def factor(self):
        """
                PLUS factor
            |   MINUS factor
            |   INTEGER
            |   REAL
            |   OPEN_PAR expr CLOSE_PAR
            |   variable
        """
        token = self.current_token
        if token.type in (Category.PLUS, Category.MINUS):
            """ Unary operation """
            self.consume(token.type)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type in (Category.REAL, Category.INTEGER):
            """ value derivation """
            self.consume(token.type)
            return Numeric(token)

        elif token.type == Category.OPEN_PAR:
            """ expression derivation """
            self.consume(Category.OPEN_PAR)
            node = self.expression()
            self.consume(Category.CLOSE_PAR)
            return node

        else:
            """ variable derivation """
            node = self.variable()
            return node

    def parse(self):
        """ PROGRAM compound_statement DOT """
        print('hello world')
        node = self.program()
        if self.current_token.type != Category.EOF:
            self.error()
        return node
