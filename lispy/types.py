from typing import Union, List, Dict


Symbol = str
Number = Union[int, float]
Atom = Union[Symbol, Number]
Exp = Union[Atom, List]
Env = Dict
