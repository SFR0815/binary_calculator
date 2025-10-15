"""Binary converter class for converting between binary and decimal."""


class BinaryConverter:
    """Converter for binary-decimal transformations.
    
    This class provides utility methods for converting between binary string
    representations and decimal integer values. These conversions are separate
    from the arithmetic operations performed by BinaryCalculator.
    """
    
    @staticmethod
    def binary_to_decimal(*, binary_str: str) -> int:
        """Convert binary string to decimal integer.
        
        This is a convenience method that uses Python's built-in int()
        function with base 2. It is NOT used internally for arithmetic
        operations, which work directly on binary strings.
        
        Args:
            binary_str: Binary number as string (e.g., '1010')
            
        Returns:
            Decimal representation of the binary number
            
        Example:
            >>> converter = BinaryConverter()
            >>> converter.binary_to_decimal(binary_str='1010')
            10
        """
        return int(binary_str, 2)
    
    @staticmethod
    def decimal_to_binary(*, decimal_num: int) -> str:
        """Convert decimal integer to binary string.
        
        This is a convenience method that uses Python's built-in bin()
        function. It is NOT used internally for arithmetic operations,
        which work directly on binary strings.
        
        Args:
            decimal_num: Decimal integer to convert
            
        Returns:
            Binary representation as string (without '0b' prefix)
            
        Example:
            >>> converter = BinaryConverter()
            >>> converter.decimal_to_binary(decimal_num=10)
            '1010'
            
        Note:
            Negative numbers are represented with a '-' prefix
        """
        if decimal_num >= 0:
            return bin(decimal_num)[2:]
        else:
            # For negative numbers, use '-' prefix for simplicity
            return '-' + bin(decimal_num)[3:]

