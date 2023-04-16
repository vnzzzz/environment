"""
This type stub file was generated by pyright.
"""

"""
Preliminary module to handle Fortran formats for IO. Does not use this outside
scipy.sparse io for now, until the API is deemed reasonable.

The *Format classes handle conversion between Fortran and Python format, and
FortranFormatParser can create *Format instances from raw Fortran format
strings (e.g. '(3I4)', '(10I3)', etc...)
"""
__all__ = ["BadFortranFormat", "FortranFormatParser", "IntFormat", "ExpFormat"]
TOKENS = ...
class BadFortranFormat(SyntaxError):
    ...


def number_digits(n): # -> int:
    ...

class IntFormat:
    @classmethod
    def from_number(cls, n, min=...): # -> Self@IntFormat:
        """Given an integer, returns a "reasonable" IntFormat instance to represent
        any number between 0 and n if n > 0, -n and n if n < 0

        Parameters
        ----------
        n : int
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : IntFormat
            IntFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        without losing precision. For example, IntFormat.from_number(1) will
        return an IntFormat instance of width 2, so that any 0 and 1 may be
        represented as 1-character strings without loss of information.
        """
        ...
    
    def __init__(self, width, min=..., repeat=...) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def fortran_format(self): # -> str:
        ...
    
    @property
    def python_format(self): # -> str:
        ...
    


class ExpFormat:
    @classmethod
    def from_number(cls, n, min=...): # -> Self@ExpFormat:
        """Given a float number, returns a "reasonable" ExpFormat instance to
        represent any number between -n and n.

        Parameters
        ----------
        n : float
            max number one wants to be able to represent
        min : int
            minimum number of characters to use for the format

        Returns
        -------
        res : ExpFormat
            ExpFormat instance with reasonable (see Notes) computed width

        Notes
        -----
        Reasonable should be understood as the minimal string length necessary
        to avoid losing precision.
        """
        ...
    
    def __init__(self, width, significand, min=..., repeat=...) -> None:
        """\
        Parameters
        ----------
        width : int
            number of characters taken by the string (includes space).
        """
        ...
    
    def __repr__(self): # -> str:
        ...
    
    @property
    def fortran_format(self): # -> str:
        ...
    
    @property
    def python_format(self): # -> str:
        ...
    


class Token:
    def __init__(self, type, value, pos) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self): # -> str:
        ...
    


class Tokenizer:
    def __init__(self) -> None:
        ...
    
    def input(self, s): # -> None:
        ...
    
    def next_token(self): # -> Token | None:
        ...
    


class FortranFormatParser:
    """Parser for Fortran format strings. The parse method returns a *Format
    instance.

    Notes
    -----
    Only ExpFormat (exponential format for floating values) and IntFormat
    (integer format) for now.
    """
    def __init__(self) -> None:
        ...
    
    def parse(self, s): # -> IntFormat | ExpFormat:
        ...
    


