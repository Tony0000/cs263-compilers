from tokens import Tokens

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # self.current_token = self.lexer.get_next_token()

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.lexer.error()

    def term(self):
        token = self.current_token
        self.consume(Tokens.INTEGER)
        return token.value

    def expression(self):
        self.current_token = self.lexer.get_next_token()

        result = self.term()
        while self.current_token.type in (Tokens.PLUS, Tokens.MINUS):
            token = self.current_token
            if token.type == Tokens.PLUS:
                self.consume(Tokens.PLUS)
                result = result + self.term()
            elif token.type == Tokens.MINUS:
                self.consume(Tokens.MINUS)
                result = result - self.term()

        return result
