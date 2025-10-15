"""Arithmetic calculator class for binary arithmetic operations."""

from ..normalizer import BinaryNormalizer
from ..comparator import BinaryComparator
from ..instruction import BinaryNumber


class ArithmeticCalculator:
    """Calculator for performing arithmetic operations on binary strings.
    
    This calculator performs pure binary arithmetic directly on binary strings
    without converting to decimal, following the patterns of 0 and 1.
    
    Operations:
        - Addition: Bit-by-bit with carry propagation
        - Subtraction: Bit-by-bit with borrow handling
        - Multiplication: Shift-and-add algorithm
        - Division: Binary long division
    """
    
    def __init__(self) -> None:
        """Initialize the arithmetic calculator with helper objects."""
        self._normalizer = BinaryNormalizer()
        self._comparator = BinaryComparator()
    
    def add(
            self,
            *,
            operand_1: BinaryNumber,
            operand_2: BinaryNumber) -> BinaryNumber:
        """Add two binary numbers using binary addition algorithm.
        
        Performs bit-by-bit addition with carry, following the rules:
        - 0 + 0 = 0 (carry 0)
        - 0 + 1 = 1 (carry 0)
        - 1 + 0 = 1 (carry 0)
        - 1 + 1 = 0 (carry 1)
        
        Args:
            operand_1: First binary number as BinaryNumber object
            operand_2: Second binary number as BinaryNumber object
            
        Returns:
            Sum as BinaryNumber object
        """
        # Normalize lengths
        bin_1, bin_2 = self._normalizer.normalize_length(
            binary_1=operand_1.value,
            binary_2=operand_2.value)
        
        result = []
        carry = 0
        
        # Process from right to left (least significant bit first)
        for i in range(len(bin_1) - 1, -1, -1):
            bit_1 = int(bin_1[i])
            bit_2 = int(bin_2[i])
            
            # Add bits and carry
            total = bit_1 + bit_2 + carry
            
            # Determine result bit and new carry
            result.append(str(total % 2))
            carry = total // 2
        
        # Add final carry if present
        if carry:
            result.append('1')
        
        # Reverse to get correct order and remove leading zeros
        result_str = ''.join(reversed(result))
        result_binary = self._normalizer.remove_leading_zeros(
            binary_str=result_str)
        return BinaryNumber(binary_str=result_binary)
    
    def subtract(
            self,
            *,
            operand_1: BinaryNumber,
            operand_2: BinaryNumber) -> BinaryNumber:
        """Subtract second binary number from first using binary subtraction.
        
        Performs bit-by-bit subtraction with borrow, following the rules:
        - 0 - 0 = 0 (borrow 0)
        - 1 - 0 = 1 (borrow 0)
        - 1 - 1 = 0 (borrow 0)
        - 0 - 1 = 1 (borrow 1, from next higher bit)
        
        Args:
            operand_1: First binary number as BinaryNumber object (minuend)
            operand_2: Second binary number as BinaryNumber object (subtrahend)
            
        Returns:
            Difference as BinaryNumber object
            
        Raises:
            ValueError: If result would be negative (operand_1 < operand_2)
        """
        # Check if result will be negative
        if self._comparator.smaller(
                binary_1=operand_1.value,
                binary_2=operand_2.value):
            raise ValueError(
                f"Cannot subtract: result would be negative "
                f"({operand_1.value} - {operand_2.value})")
        
        # Normalize lengths
        bin_1, bin_2 = self._normalizer.normalize_length(
            binary_1=operand_1.value,
            binary_2=operand_2.value)
        
        result = []
        borrow = 0
        
        # Process from right to left
        for i in range(len(bin_1) - 1, -1, -1):
            bit_1 = int(bin_1[i])
            bit_2 = int(bin_2[i])
            
            # Subtract with borrow
            diff = bit_1 - bit_2 - borrow
            
            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0
            
            result.append(str(diff))
        
        # Reverse and remove leading zeros
        result_str = ''.join(reversed(result))
        result_binary = self._normalizer.remove_leading_zeros(
            binary_str=result_str)
        return BinaryNumber(binary_str=result_binary)
    
    def multiply(
            self,
            *,
            operand_1: BinaryNumber,
            operand_2: BinaryNumber) -> BinaryNumber:
        """Multiply two binary numbers using shift-and-add algorithm.
        
        Performs binary multiplication by:
        1. For each bit in operand_2 (from right to left):
        2. If bit is 1, add operand_1 (shifted appropriately) to result
        3. Shift operand_1 left for next iteration
        
        Args:
            operand_1: First binary number as BinaryNumber (multiplicand)
            operand_2: Second binary number as BinaryNumber (multiplier)
            
        Returns:
            Product as BinaryNumber object
        """
        # Handle zero cases
        if operand_1.value == '0' or operand_2.value == '0':
            return BinaryNumber(binary_str='0')
        
        result = BinaryNumber(binary_str='0')
        operand_2_val = operand_2.value
        
        # Process multiplier from right to left
        for i in range(len(operand_2_val) - 1, -1, -1):
            if operand_2_val[i] == '1':
                # Shift operand_1 left by (len - 1 - i) positions
                shift_amount = len(operand_2_val) - 1 - i
                shifted = operand_1.value + ('0' * shift_amount)
                
                # Add to result
                result = self.add(
                    operand_1=result,
                    operand_2=BinaryNumber(binary_str=shifted))
        
        return result
    
    def divide(
            self,
            *,
            operand_1: BinaryNumber,
            operand_2: BinaryNumber) -> BinaryNumber:
        """Divide first binary number by second using long division algorithm.
        
        Performs binary long division:
        1. Start with most significant bit of dividend
        2. If current value >= divisor, subtract and add '1' to quotient
        3. Otherwise add '0' to quotient
        4. Bring down next bit and repeat
        
        Args:
            operand_1: First binary number as BinaryNumber (dividend)
            operand_2: Second binary number as BinaryNumber (divisor)
            
        Returns:
            Quotient as BinaryNumber object (integer division)
            
        Raises:
            ZeroDivisionError: If operand_2 is zero
        """
        # Check for division by zero
        if self._normalizer.remove_leading_zeros(
                binary_str=operand_2.value) == '0':
            raise ZeroDivisionError("Cannot divide by zero")
        
        # If dividend is less than divisor, result is 0
        if self._comparator.smaller(
                binary_1=operand_1.value,
                binary_2=operand_2.value):
            return BinaryNumber(binary_str='0')
        
        # If equal, result is 1
        if self._comparator.equal(
                binary_1=operand_1.value,
                binary_2=operand_2.value):
            return BinaryNumber(binary_str='1')
        
        quotient = []
        remainder = BinaryNumber(binary_str='0')
        
        # Process each bit of dividend from left to right
        for bit in operand_1.value:
            # Bring down next bit
            remainder_str = self._normalizer.remove_leading_zeros(
                binary_str=remainder.value + bit)
            remainder = BinaryNumber(binary_str=remainder_str)
            
            # Check if remainder >= divisor
            if self._comparator.larger_equal(
                    binary_1=remainder.value,
                    binary_2=operand_2.value):
                # Subtract divisor from remainder
                remainder = self.subtract(
                    operand_1=remainder,
                    operand_2=operand_2)
                quotient.append('1')
            else:
                quotient.append('0')
        
        result = ''.join(quotient)
        result_binary = self._normalizer.remove_leading_zeros(
            binary_str=result)
        return BinaryNumber(binary_str=result_binary)

