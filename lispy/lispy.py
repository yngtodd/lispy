from typing import List

import lispy.types as types


def tokenize(chars: str) -> List[str]:
    r"""Convert characters to tokens

    Args:
        chars: program as a string

    Returns:
        tokenized strings by whitespace

    Examples::

        >>> tokenize("(begin (define x 10))")
        ['(', 'begin', '(', 'define', 'x', '10', ')', ')']
    """
    # Add whitespace around braces to split them 
    # from the rest of the tokens
    chars = chars.replace("(", " ( ")
    chars = chars.replace(")", " ) ")
    return chars.split()


def parse(program: str) -> types.Exp:
    """Read a Scheme expression from a string"""
    return read_from_tokens(tokenize(program))


def read_from_tokens(tokens: List) -> types.Exp:
    """Read an expression from a sequence of tokens"""
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF")

    token = tokens.pop(0)
    if token == "(":
        expression = []
        while tokens[0] != ")":
            expression.append(
                read_from_tokens(tokens)
            )
        # pop the final ")"
        tokens.pop(0)
        return expression
    elif token == ")":
        raise SyntaxError("Unexpected )")
    else:
        return atom(token)


def atom(token: str) -> types.Atom:
    """Convert token to proper types

    When parsing, we get all tokens represented as strings.
    Here we convert all integers and floats to their proper
    types, and keep all other types as `types.Symbol` objects.
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return types.Symbol(token)


