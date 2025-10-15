"""Binary number class for encapsulating binary string values."""

import typing as p_typ
from ..comparator.binary_comparator import BinaryComparator


class BinaryNumber:
    """Represents a binary number with encapsulated operations.
    
    This class encapsulates a binary number as a string and provides
    methods for conversion, increment, decrement, and copying operations.
    All binary values are stored as strings containing only '0' and '1'.
    
    Attributes:
        value: Binary number as string (e.g., '1010')
    """
    
    def __init__(self, *, binary_str: str) -> None:
        """Initialize a binary number.
        
        Args:
            binary_str: Binary number as string containing only 0s and 1s
            
        Raises:
            ValueError: If binary_str is not a valid binary string
        """
        self._validate_binary_string(binary_str=binary_str)
        self._value = binary_str
    
    @property
    def value(self) -> str:
        """Get the binary value as string.
        
        Returns:
            Binary number as string
        """
        return self._value
    
    @classmethod
    def from_int(cls, *, decimal_num: int) -> 'BinaryNumber':
        """Create a BinaryNumber from a decimal integer.
        
        Args:
            decimal_num: Decimal integer to convert (must be non-negative)
            
        Returns:
            New BinaryNumber instance
            
        Raises:
            ValueError: If decimal_num is negative
            
        Example:
            >>> num = BinaryNumber.from_int(decimal_num=10)
            >>> num.value
            '1010'
        """
        if decimal_num < 0:
            raise ValueError(
                f"Cannot create BinaryNumber from negative integer: "
                f"{decimal_num}")
        
        binary_str = bin(decimal_num)[2:]
        return cls(binary_str=binary_str)
    
    def to_int(self) -> int:
        """Convert the binary number to a decimal integer.
        
        Returns:
            Decimal representation of the binary number
            
        Example:
            >>> num = BinaryNumber(binary_str='1010')
            >>> num.to_int()
            10
        """
        return int(self._value, 2)
    
    def incr(
            self,
            *,
            increment: p_typ.Optional['BinaryNumber'] = None) -> None:
        """Increment the binary number in place.
        
        Args:
            increment: Optional BinaryNumber to add (defaults to '1')
            
        Example:
            >>> num = BinaryNumber(binary_str='101')
            >>> num.incr()
            >>> num.value
            '110'
        """
        if increment is None:
            increment = BinaryNumber(binary_str='1')
        
        result = self.to_int() + increment.to_int()
        self._value = bin(result)[2:]
    
    def decr(
            self,
            *,
            decrement: p_typ.Optional['BinaryNumber'] = None) -> None:
        """Decrement the binary number in place.
        
        Args:
            decrement: Optional BinaryNumber to subtract (defaults to '1')
            
        Raises:
            ValueError: If result would be less than '0'
            
        Example:
            >>> num = BinaryNumber(binary_str='110')
            >>> num.decr()
            >>> num.value
            '101'
        """
        if decrement is None:
            decrement = BinaryNumber(binary_str='1')
        
        current_val = self.to_int()
        decrement_val = decrement.to_int()
        
        if current_val < decrement_val:
            raise ValueError(
                f"Cannot decrement {self._value} by {decrement.value}: "
                f"result would be negative")
        
        result = current_val - decrement_val
        self._value = bin(result)[2:]
    
    def copy(self) -> 'BinaryNumber':
        """Create a copy of this binary number.
        
        Returns:
            New BinaryNumber instance with the same value
            
        Example:
            >>> num1 = BinaryNumber(binary_str='1010')
            >>> num2 = num1.copy()
            >>> num2.value
            '1010'
        """
        return BinaryNumber(binary_str=self._value)
    
    @staticmethod
    def _validate_binary_string(*, binary_str: str) -> None:
        """Validate that a string contains only binary digits.
        
        Args:
            binary_str: String to validate
            
        Raises:
            ValueError: If string is empty or contains non-binary chars
        """
        if not binary_str:
            raise ValueError("Binary string cannot be empty")
        
        if not all(char in '01' for char in binary_str):
            raise ValueError(
                f"Invalid binary string: '{binary_str}'. "
                f"Must contain only 0 and 1")
    
    def __repr__(self) -> str:
        """Return string representation of the binary number."""
        return f"BinaryNumber(value='{self._value}')"
    
    def __str__(self) -> str:
        """Return the binary value as string."""
        return self._value
    
    def __eq__(self, other: object) -> bool:
        """Compare two BinaryNumber instances for equality.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if values are equal, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.equal(binary_1=self._value, binary_2=other._value)
    
    def __ne__(self, other: object) -> bool:
        """Compare two BinaryNumber instances for inequality.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if values are not equal, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.not_equal(
            binary_1=self._value,
            binary_2=other._value)
    
    def __lt__(self, other: object) -> bool:
        """Compare if this BinaryNumber is less than another.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if this value < other value, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.smaller(
            binary_1=self._value,
            binary_2=other._value)
    
    def __le__(self, other: object) -> bool:
        """Compare if this BinaryNumber is less than or equal to another.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if this value <= other value, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.smaller_equal(
            binary_1=self._value,
            binary_2=other._value)
    
    def __gt__(self, other: object) -> bool:
        """Compare if this BinaryNumber is greater than another.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if this value > other value, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.larger(binary_1=self._value, binary_2=other._value)
    
    def __ge__(self, other: object) -> bool:
        """Compare if this BinaryNumber is greater than or equal to another.
        
        Uses BinaryComparator for accurate binary comparison.
        
        Args:
            other: Object to compare with
            
        Returns:
            True if this value >= other value, False otherwise
        """
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        comparator = BinaryComparator()
        return comparator.larger_equal(
            binary_1=self._value,
            binary_2=other._value)

