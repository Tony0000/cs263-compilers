from tokens import Tokens


class AST(object):
    """Abstract syntax tree"""
    pass


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
        self.children = list()


class AssignOp(AST):
    """ var_name := expression """
    def __init__(self, left, token, right):
        self.left = left
        self.token = self.op = token
        self.right = right


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
        """ compound statement DOT """
        node = self.compound_statement()
        self.eat(Tokens.DOT)
        return node

    def compound_statement(self):
        """ BEGIN statement_list END """
        self.eat(Tokens.BEGIN)
        nodes_list = self.statement_list()
        self.eat(Tokens.END)

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
        while(self.current_token.type == Tokens.SEMICOLON):
            self.eat(Tokens.SEMICOLON)
            nodes_list.append(self.statement())
        return nodes_list

    def assign_statement(self):
        """ variable ASSIGN expression """
        left = self.variable()
        token = self.current_token
        self.eat(Tokens.ASSIGN)
        right = self.expression()
        node = AssignOp(left, token, right)
        return node

    def statement(self):
        """
                compound_statement
            |   assign_statement
            |   empty_statement
        """
        if self.current_token.type == Tokens.BEGIN:
            nodes_list = self.compound_statement()
        elif self.current_token.type == Tokens.IDENTIFIER:
            nodes_list = self.assign_statement()
        else:
            nodes_list = self.empty()
        return nodes_list

    def variable(self):
        """ identifier """
        node = Variable(self.current_token)
        self.eat(Tokens.IDENTIFIER)
        return node

    def empty(self):
        """ empty production """
        return NoOp()

    def expression(self):
        """ term ((PLUS | MINUS) term)* """
        self.current_token = self.lexer.get_next_token()

        node = self.term()
        while self.current_token.type in (Tokens.PLUS, Tokens.MINUS):
            token = self.current_token
            self.consume(Tokens.PLUS)
            node = BinaryOp(left=node, op=token, right=self.term())
        return node

    def term(self):
        """ factor ((MULT | DIV) factor)* """
        node = self.factor()

        while self.current_token.type in (Tokens.MULT, Tokens.DIV):
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
        if token.type in (Tokens.PLUS, Tokens.MINUS):
            """ Unary operation """
            self.consume(token.type)
            node = UnaryOp(token, self.factor())
            return node

        elif token.type in (Tokens.REAL, Tokens.INTEGER):
            """ value derivation """
            self.consume(token.type)
            return Numeric(token)

        elif token.type == Tokens.OPEN_PAR:
            """ expression derivation """
            self.consume(Tokens.OPEN_PAR)
            node = self.expression()
            self.consume(Tokens.CLOSE_PAR)
            return node

        else:
            """ variable derivation """
            node = self.variable()
            return node

    def parse(self):
        """ PROGRAM compound_statement DOT """
        node = self.program()
        if self.current_token.type != Tokens.EOF:
            self.error()
        return node
