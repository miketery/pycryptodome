from typing import Union, List, Tuple, Optional

def _mult_gf2(f1: int, f2: int) -> int : ...
def _div_gf2(a: int, b: int) -> int : ...

class _Element(object):
    irr_poly: int
    def __init__(self, encoded_value: Union[int, bytes]) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __int__(self) -> int: ...
    def encode(self) -> bytes: ...
    def __mul__(self, factor: int) -> _Element: ...
    def __add__(self, term: _Element) -> _Element: ...
    def inverse(self) -> _Element: ...
    def __pow__(self, exponent) -> _Element: ...

class Shamir(object):
    @staticmethod
    def split(k: int, n: int, secret: bytes, ssss: Optional[bool]) -> List[Tuple[int, bytes]]: ...
    @staticmethod
    def combine(shares: List[Tuple[int, bytes]], ssss: Optional[bool]) -> bytes: ...
    @staticmethod
    def split_large(k: int, n: int, secret: bytes, ssss: Optional[bool]) -> List[Tuple[int, bytes]]: ...
    @staticmethod
    def combine_large(shares: List[Tuple[int, bytes]], ssss: Optional[bool]) -> bytes: ...

