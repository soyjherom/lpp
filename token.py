from enum import(
    auto,
    Enum,
    unique
)
from typing import (
    Dict, NamedTuple)
@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    ELSE = auto()
    EOF = auto()
    DIV = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    MINUS = auto()
    MOD = auto()
    MULT = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str
    def __str__(self) -> str:
        return f'Type:{self.token_type}, Literal: {self.literal}'

def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'variable': TokenType.LET,
        'procedimiento': TokenType.FUNCTION, 
        'si': TokenType.IF, 
        'si_no': TokenType.ELSE, 
        'regresa': TokenType.RETURN,
        'verdadero': TokenType.TRUE,
        'falso': TokenType.FALSE
    }
    return keywords.get(literal, TokenType.IDENT)