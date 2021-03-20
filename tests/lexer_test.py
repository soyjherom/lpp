from unittest import TestCase
from typing import List
from lpp.token import (Token, TokenType)
from lpp.lexer import Lexer

class LexerTest(TestCase):

    def test_ilegal(self) -> None:
        source: str = '!¿@'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []

        for i in range(len(source)):
            tokens.append(lexer.next_token())

        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '!'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@')
        ]

        self.assertEquals(tokens, expected_tokens)

    def test_one_character_operator(self) -> None:
        source: str = '=+-*/%<>'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] =[
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.MULT, '*'),
            Token(TokenType.DIV, '/'),
            Token(TokenType.MOD, '%'),
            Token(TokenType.LT, '<'),
            Token(TokenType.GT, '>')
        ]
        self.assertEquals(tokens, expected_tokens)

    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(len(source)+1):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, '')
        ]
        self.assertEquals(tokens, expected_tokens)

    def test_delimeters(self) -> None:
        source: str = '(){},;'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(len(source)+1):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),            
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, '')
        ]
        self.assertEquals(tokens, expected_tokens)

    def test_assignment(self) -> None:
        source: str = 'variable cinco = 5;'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(len(source)+1):
            tokens.append(lexer.next_token())
            #print(tokens[-1].token_type.name)
            if tokens[-1].token_type.name == TokenType.EOF.name:
                break
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, '')
        ]
        self.assertEquals(len(tokens), len(expected_tokens))
        self.assertEquals(tokens, expected_tokens)

    def test_function_declaration(self) -> None:
        source: str = '''
            variable suma = procedimiento(x, y){
                x + y;
            };
        '''
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(16):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'), #1
            Token(TokenType.IDENT, 'suma'), #2
            Token(TokenType.ASSIGN, '='), #3
            Token(TokenType.FUNCTION, 'procedimiento'), #4
            Token(TokenType.LPAREN, '('), #5
            Token(TokenType.IDENT, 'x'), #6
            Token(TokenType.COMMA, ','), #7
            Token(TokenType.IDENT, 'y'), #8
            Token(TokenType.RPAREN, ')'), #9
            Token(TokenType.LBRACE, '{'), #10
            Token(TokenType.IDENT, 'x'), #11
            Token(TokenType.PLUS, '+'), #12
            Token(TokenType.IDENT, 'y'), #13
            Token(TokenType.SEMICOLON, ';'), #14
            Token(TokenType.RBRACE, '}'), #15
            Token(TokenType.SEMICOLON, ';'), #16
        ]
        self.assertEquals(len(tokens), len(expected_tokens))
        self.assertEquals(tokens, expected_tokens)

    def test_function_call(self) -> None:
        source: str = 'variable resultado = suma(dos, tres);'
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(11):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'resultado'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.EOF, ''),
        ]
        self.assertEquals(len(tokens), len(expected_tokens))
        self.assertEquals(tokens, expected_tokens)

    def test_control_statement(self) -> None:
        source: str = '''
            si(15 < 10){
                regresa verdadero;
            }si_no{
                regresa falso;
            }
        '''
        lexer: Lexer = Lexer(source)
        tokens: List[Token] = []
        for i in range(18):
            tokens.append(lexer.next_token())
        expected_tokens: List[Token] =[
            Token(TokenType.IF, 'si'), #1
            Token(TokenType.LPAREN, '('), #2
            Token(TokenType.INT, '15'), #3
            Token(TokenType.LT, '<'), #4
            Token(TokenType.INT, '10'), #5
            Token(TokenType.RPAREN, ')'), #6
            Token(TokenType.LBRACE, '{'), #7
            Token(TokenType.RETURN, 'regresa'), #8
            Token(TokenType.TRUE, 'verdadero'), #9
            Token(TokenType.SEMICOLON, ';'), #10
            Token(TokenType.RBRACE, '}'), #11
            Token(TokenType.ELSE, 'si_no'), #12
            Token(TokenType.LBRACE, '{'), #13
            Token(TokenType.RETURN, 'regresa'), #14
            Token(TokenType.FALSE, 'falso'), #15
            Token(TokenType.SEMICOLON, ';'), #16
            Token(TokenType.RBRACE, '}'), #17
            Token(TokenType.EOF, '') #18
        ]
        self.assertEquals(tokens, expected_tokens)