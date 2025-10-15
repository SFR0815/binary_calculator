"""Example 01: BinaryNumber - Creating and Manipulating Binary Numbers

This example demonstrates the BinaryNumber class which encapsulates binary
string values and provides methods for conversion and manipulation.
"""

import sys
import pathlib as p_pthl

# Add parent directory to path for imports
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber


def numb01_create_from_string() -> None:
    """BinaryNumber: Create from binary string.
    
    Key: numb01
    Run: python examples/example.py numb01
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:create_from_string]
    # Create BinaryNumber from binary string
    # Input: String '1010' containing only '0' and '1' characters
    # Processing: 
    #   1. Validates string contains only binary digits
    #   2. Stores value internally as string
    # Expected result: BinaryNumber object representing decimal 10
    # Console output: "1. Created from string: 1010 (decimal: 10)"
    num1 = BinaryNumber(binary_str='1010')
    print(f"1. Created from string: {num1.value} (decimal: {num1.to_int()})")
    # --8<-- [end:create_from_string]
    print()


def numb02_create_from_int() -> None:
    """BinaryNumber: Create from integer.
    
    Key: numb02
    Run: python examples/example.py numb02
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:create_from_int]
    # Create BinaryNumber from integer using class method
    # Input: Integer 42
    # Processing:
    #   1. Python's bin(42) converts to '0b101010'
    #   2. Strip '0b' prefix to get '101010'
    #   3. Create BinaryNumber with result
    # Expected result: BinaryNumber with value '101010'
    # Console output: "2. Created from int 42: 101010"
    num2 = BinaryNumber.from_int(decimal_num=42)
    print(f"2. Created from int 42: {num2.value}")
    # --8<-- [end:create_from_int]
    print()


def numb03_convert_to_int() -> None:
    """BinaryNumber: Convert to integer.
    
    Key: numb03
    Run: python examples/example.py numb03
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:convert_to_int]
    # Convert BinaryNumber to integer
    # Input: BinaryNumber with value '1010'
    # Processing:
    #   1. Call to_int() method
    #   2. Uses int(self._value, 2) to convert binary string to decimal
    #   3. Returns integer value
    # Expected result: Integer 10
    # Console output: "3. Converted to int: 10"
    num1 = BinaryNumber(binary_str='1010')
    decimal_value = num1.to_int()
    print(f"3. Converted to int: {decimal_value}")
    # --8<-- [end:convert_to_int]
    print()


def numb04_increment() -> None:
    """BinaryNumber: Increment operations.
    
    Key: numb04
    Run: python examples/example.py numb04
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:increment]
    # Increment operations
    # Input: BinaryNumber with value '1010' (10)
    # Processing for incr():
    #   1. Convert '1010' to int: 10
    #   2. Convert default increment '1' to int: 1
    #   3. Add: 10 + 1 = 11
    #   4. Convert 11 back to binary: '1011'
    #   5. Update internal value in-place
    # Expected result: Value changes from '1010' -> '1011'
    # Console output:
    #   Initial: 1010 (10)
    #   After incr(): 1011 (11)
    #   After incr(increment='101'): 10000 (16)
    print("4. Increment operations:")
    num3 = BinaryNumber(binary_str='1010')
    print(f"   Initial: {num3.value} ({num3.to_int()})")
    
    # Default increment by 1
    num3.incr()
    print(f"   After incr(): {num3.value} ({num3.to_int()})")
    
    # Custom increment
    # Processing: 11 + 5 = 16 -> '10000'
    increment = BinaryNumber(binary_str='101')
    num3.incr(increment=increment)
    print(f"   After incr(increment='101'): {num3.value} ({num3.to_int()})")
    # --8<-- [end:increment]
    print()


def numb05_decrement() -> None:
    """BinaryNumber: Decrement operations.
    
    Key: numb05
    Run: python examples/example.py numb05
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:decrement]
    # Decrement operations
    # Input: BinaryNumber with value '10000' (16)
    # Processing for decr():
    #   1. Convert current value '10000' to int: 16
    #   2. Convert default decrement '1' to int: 1
    #   3. Check validity: 16 >= 1 ✓
    #   4. Subtract: 16 - 1 = 15
    #   5. Convert to binary: bin(15) = '0b1111'
    #   6. Strip prefix and update: '1111'
    # Expected result: Value changes from '10000' -> '1111'
    # Console output:
    #   Before decr(): 10000 (16)
    #   After decr(): 1111 (15)
    num3 = BinaryNumber(binary_str='10000')
    print("5. Decrement operations:")
    print(f"   Before decr(): {num3.value} ({num3.to_int()})")
    num3.decr()
    print(f"   After decr(): {num3.value} ({num3.to_int()})")
    # --8<-- [end:decrement]
    print()


def numb06_copy() -> None:
    """BinaryNumber: Copy operation.
    
    Key: numb06
    Run: python examples/example.py numb06
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:copy]
    # Copy operation creates independent object
    # Input: BinaryNumber with value '1111' (15)
    # Processing:
    #   1. Call copy() method
    #   2. Create new BinaryNumber with same binary string value
    #   3. Return independent object (not a reference)
    # Expected result: New BinaryNumber with value '1111'
    # Console output:
    #   Original: 1111
    #   Copy: 1111
    #   After incrementing copy:
    #     Original: 1111 (unchanged)
    #     Copy: 10000 (changed)
    num3 = BinaryNumber(binary_str='1111')
    print("6. Copy operation:")
    num4 = num3.copy()
    print(f"   Original: {num3.value}")
    print(f"   Copy: {num4.value}")
    num4.incr()  # Modify copy only
    print(f"   After incrementing copy:")
    print(f"     Original: {num3.value} (unchanged)")
    print(f"     Copy: {num4.value} (changed)")
    # --8<-- [end:copy]
    print()


def numb07_comparisons() -> None:
    """BinaryNumber: Comparison operators.
    
    Key: numb07
    Run: python examples/example.py numb07
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:comparisons]
    # Comparison operations using Python operators
    # Input: Two BinaryNumbers '1010' (10) and '101' (5)
    # Processing for each operator:
    #   __gt__ (>):  Calls BinaryComparator.larger()
    #   __ge__ (>=): Calls BinaryComparator.larger_equal()
    #   __lt__ (<):  Calls BinaryComparator.smaller()
    #   __le__ (<=): Calls BinaryComparator.smaller_equal()
    #   __eq__ (==): Calls BinaryComparator.equal()
    #   __ne__ (!=): Calls BinaryComparator.not_equal()
    # Expected results: True for >, >=, !=; False for <, <=, ==
    # Console output: Shows all 6 comparison results
    print("7. Comparison operators:")
    num5 = BinaryNumber(binary_str='1010')  # 10
    num6 = BinaryNumber(binary_str='101')   # 5
    print(f"   num5 = {num5.value} (10), num6 = {num6.value} (5)")
    print(f"   num5 > num6:  {num5 > num6}")
    print(f"   num5 >= num6: {num5 >= num6}")
    print(f"   num5 < num6:  {num5 < num6}")
    print(f"   num5 <= num6: {num5 <= num6}")
    print(f"   num5 == num6: {num5 == num6}")
    print(f"   num5 != num6: {num5 != num6}")
    # --8<-- [end:comparisons]
    print()


def numb08_error_handling() -> None:
    """BinaryNumber: Error handling.
    
    Key: numb08
    Run: python examples/example.py numb08
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:error_handling]
    # Error handling - attempt to decrement below zero
    # Input: BinaryNumber '10' (2), decrement by '101' (5)
    # Processing:
    #   1. Convert current: '10' -> 2
    #   2. Convert decrement: '101' -> 5
    #   3. Check validity: 2 < 5 ❌
    #   4. Raise ValueError before attempting subtraction
    # Expected result: ValueError raised
    # Console output: "[OK] Caught error: Cannot decrement 10 by 101..."
    print("8. Error handling - decrement below zero:")
    try:
        small = BinaryNumber(binary_str='10')  # 2
        decrement_large = BinaryNumber(binary_str='101')  # 5
        small.decr(decrement=decrement_large)
    except ValueError as e:
        print(f"   [OK] Caught error: {e}")
    # --8<-- [end:error_handling]
    print()


def numb09_larger_numbers() -> None:
    """BinaryNumber: Working with larger numbers.
    
    Key: numb09
    Run: python examples/example.py numb09
    """
    print("=" * 70)
    print("Example 01: BinaryNumber Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    # Real-world scenario: Memory address calculation
    # Input: Large integers 65536 (0x10000) and 4096 (one page)
    # Processing:
    #   1. Convert 65536 to binary: '10000000000000000' (17 bits)
    #   2. Convert 4096 to binary: '1000000000000' (13 bits)
    #   3. Increment uses same algorithm but with larger numbers
    #   4. Result: 69632 in binary
    # Expected console output:
    #   Large number 1: 10000000000000000 (65536) (17 bits)
    #   Large number 2: 1000000000000 (4096) (13 bits)
    #   Incrementing 65536 by 4096:
    #   Result: 10001000000000000 (69632)
    #   Comparing 1,048,576 > 1,024: True
    #   Bit lengths: 21 vs 11 bits
    print("9. Working with Larger Numbers:")
    
    # Create from large integers
    large1 = BinaryNumber.from_int(decimal_num=65536)  # 2^16
    large2 = BinaryNumber.from_int(decimal_num=4096)   # 2^12
    
    print(f"   Large number 1: {large1.value}")
    print(f"                   ({large1.to_int()} in decimal)")
    print(f"                   ({len(large1.value)} bits)")
    print()
    print(f"   Large number 2: {large2.value}")
    print(f"                   ({large2.to_int()} in decimal)")
    print(f"                   ({len(large2.value)} bits)")
    print()
    
    # Increment by large amount
    print(f"   Incrementing {large1.to_int()} by {large2.to_int()}:")
    large1.incr(increment=large2)
    print(f"   Result: {large1.value}")
    print(f"           ({large1.to_int()} in decimal)")
    print()
    
    # Compare large numbers
    # Comparison processing:
    #   1. Delegates to BinaryComparator.larger()
    #   2. Compare lengths: 21 bits > 11 bits
    #   3. Result: True (first is larger)
    mega = BinaryNumber.from_int(decimal_num=1048576)  # 2^20 (1 MB)
    kilo = BinaryNumber.from_int(decimal_num=1024)     # 2^10 (1 KB)
    
    print(f"   Comparing 1 MB vs 1 KB:")
    print(f"   {mega.to_int():,} > {kilo.to_int():,}: {mega > kilo}")
    print(f"   Bit lengths: {len(mega.value)} vs {len(kilo.value)} bits")
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all BinaryNumber examples."""
    numb01_create_from_string()
    numb02_create_from_int()
    numb03_convert_to_int()
    numb04_increment()
    numb05_decrement()
    numb06_copy()
    numb07_comparisons()
    numb08_error_handling()
    numb09_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

