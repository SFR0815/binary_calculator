"""Binary calculator package for arithmetic operations on binary strings.

This package provides functionality for:
- Creating binary instructions with operands and operations
- Performing arithmetic operations (+, -, *, /) on binary strings
- Converting between binary strings and decimal integers

Example:
    >>> from binary_calculator import BinaryCalculator, BinaryInstruction, BinaryConverter
    >>> calculator = BinaryCalculator()
    >>> converter = BinaryConverter()
    >>> instruction = BinaryInstruction(
    ...     operand_1='1010',
    ...     operand_2='0101',
    ...     operation='+')
    >>> result = calculator.execute(instruction=instruction)
    >>> print(result)
    '1111'
    >>> decimal = converter.binary_to_decimal(binary_str=result)
    >>> print(decimal)
    15
"""

from .instruction import (
    BinaryInstruction,
    BinaryNumber,
    OperationEnum,
    OperationType)
from .calculator import ArithmeticCalculator
from .converter import BinaryConverter
from .normalizer import BinaryNormalizer
from .comparator import BinaryComparator
from .executor import InstructionExecutor

__all__ = [
    'BinaryInstruction',
    'BinaryNumber',
    'ArithmeticCalculator',
    'InstructionExecutor',
    'BinaryConverter',
    'BinaryNormalizer',
    'BinaryComparator',
    'OperationEnum',
    'OperationType']
__version__ = '1.0.0'

