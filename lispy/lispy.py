from typing import List


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
