"""Example 03: ArithmeticCalculator - Direct Arithmetic Operations

This example demonstrates the ArithmeticCalculator class which performs
pure binary arithmetic directly on BinaryNumber objects.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, ArithmeticCalculator


def calc01_addition() -> None:
    """ArithmeticCalculator: Addition operation.
    
    Key: calc01
    Run: python examples/example.py calc01
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:setup]
    calculator = ArithmeticCalculator()
    # --8<-- [end:setup]
    
    # --8<-- [start:addition]
    # Addition operation
    # Input: BinaryNumbers '1010' (10) and '0101' (5)
    # Processing:
    #   1. Normalize lengths: '1010' and '0101' already 4 bits
    #   2. Add bit-by-bit from right to left with carry:
    #      Position 3: 0+1+carry(0)=1, result='1', carry=0
    #      Position 2: 1+0+carry(0)=1, result='1', carry=0
    #      Position 1: 0+1+carry(0)=1, result='1', carry=0
    #      Position 0: 1+0+carry(0)=1, result='1', carry=0
    #   3. Reverse result array: '1111'
    #   4. Create BinaryNumber('1111')
    # Expected result: BinaryNumber with value '1111' (15)
    # Console output: "1010 + 0101 = 1111" and "Decimal: 10 + 5 = 15"
    print("1. Addition:")
    num1 = BinaryNumber(binary_str='1010')  # 10
    num2 = BinaryNumber(binary_str='0101')  # 5
    
    result_add = calculator.add(operand_1=num1, operand_2=num2)
    print(f"   {num1.value} + {num2.value} = {result_add.value}")
    print(f"   Decimal: {num1.to_int()} + {num2.to_int()} = "
          f"{result_add.to_int()}")
    # --8<-- [end:addition]
    print()


def calc02_subtraction() -> None:
    """ArithmeticCalculator: Subtraction operation.
    
    Key: calc02
    Run: python examples/example.py calc02
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:subtraction]
    # Subtraction operation
    # Input: BinaryNumbers '1111' (15) and '0101' (5)
    # Processing:
    #   1. Check if result would be negative: 15 >= 5 ✓
    #   2. Normalize lengths: both already 4 bits
    #   3. Subtract bit-by-bit right to left with borrow:
    #      Position 3: 1-1-borrow(0)=0, result='0', borrow=0
    #      Position 2: 1-0-borrow(0)=1, result='1', borrow=0
    #      Position 1: 1-1-borrow(0)=0, result='0', borrow=0
    #      Position 0: 1-0-borrow(0)=1, result='1', borrow=0
    #   4. Reverse: '1010'
    #   5. Create BinaryNumber('1010')
    # Expected result: BinaryNumber with value '1010' (10)
    # Console output: "1111 - 0101 = 1010" and "Decimal: 15 - 5 = 10"
    print("2. Subtraction:")
    num3 = BinaryNumber(binary_str='1111')  # 15
    num4 = BinaryNumber(binary_str='0101')  # 5
    
    result_sub = calculator.subtract(operand_1=num3, operand_2=num4)
    print(f"   {num3.value} - {num4.value} = {result_sub.value}")
    print(f"   Decimal: {num3.to_int()} - {num4.to_int()} = "
          f"{result_sub.to_int()}")
    # --8<-- [end:subtraction]
    print()


def calc03_multiplication() -> None:
    """ArithmeticCalculator: Multiplication operation.
    
    Key: calc03
    Run: python examples/example.py calc03
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:multiplication]
    # Multiplication operation using shift-and-add algorithm
    # Input: BinaryNumbers '101' (5) and '11' (3)
    # Processing:
    #   1. Check for zeros: none
    #   2. Process multiplier '11' right to left:
    #      Bit 1 (rightmost): '1' -> add '101' shifted 0: result='101'
    #      Bit 0: '1' -> add '101' shifted 1: '101'+'1010'='1111'
    #   3. Create BinaryNumber('1111')
    # Expected result: BinaryNumber with value '1111' (15)
    # Console output: "101 * 11 = 1111" and "Decimal: 5 * 3 = 15"
    print("3. Multiplication:")
    num5 = BinaryNumber(binary_str='101')   # 5
    num6 = BinaryNumber(binary_str='11')    # 3
    
    result_mul = calculator.multiply(operand_1=num5, operand_2=num6)
    print(f"   {num5.value} * {num6.value} = {result_mul.value}")
    print(f"   Decimal: {num5.to_int()} * {num6.to_int()} = "
          f"{result_mul.to_int()}")
    # --8<-- [end:multiplication]
    print()


def calc04_division() -> None:
    """ArithmeticCalculator: Division operation.
    
    Key: calc04
    Run: python examples/example.py calc04
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:division]
    # Division operation using binary long division
    # Input: BinaryNumbers '1010' (10) and '10' (2)
    # Processing:
    #   1. Check for zero divisor: '10' != '0' ✓
    #   2. Check if dividend < divisor: '1010' >= '10' ✓
    #   3. Binary long division:
    #      Process '1010' bit by bit (left to right):
    #      - Bit '1': remainder='1', 1<10, quotient+='0'
    #      - Bit '0': remainder='10', 10>=10, subtract, quotient+='1'
    #      - Bit '1': remainder='01', 01<10, quotient+='0'
    #      - Bit '0': remainder='010', 010>=10, subtract, quotient+='1'
    #      Result quotient: '0101' -> remove leading zero -> '101'
    #   4. Create BinaryNumber('101')
    # Expected result: BinaryNumber with value '101' (5)
    # Console output: "1010 / 10 = 101" and "Decimal: 10 / 2 = 5"
    print("4. Division:")
    num7 = BinaryNumber(binary_str='1010')  # 10
    num8 = BinaryNumber(binary_str='10')    # 2
    
    result_div = calculator.divide(operand_1=num7, operand_2=num8)
    print(f"   {num7.value} / {num8.value} = {result_div.value}")
    print(f"   Decimal: {num7.to_int()} / {num8.to_int()} = "
          f"{result_div.to_int()}")
    # --8<-- [end:division]
    print()


def calc05_chained_operations() -> None:
    """ArithmeticCalculator: Chained operations.
    
    Key: calc05
    Run: python examples/example.py calc05
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:chained_operations]
    # Chained operations demonstrate composing results
    # Expression: (12 + 3) * 2
    # Input: BinaryNumbers '1100' (12), '11' (3), '10' (2)
    # Processing:
    #   Step 1 - Addition:
    #     1100 + 11 = 1111 (15)
    #   Step 2 - Multiplication:
    #     1111 * 10:
    #       - Multiplier bit 0='0': skip
    #       - Multiplier bit 1='1': add '1111' shifted 1 = '11110'
    #     Result: '11110' (30)
    # Expected result: BinaryNumber '11110' (30)
    # Console output:
    #   Step 1: 1100 + 11 = 1111 (15)
    #   Step 2: 1111 * 10 = 11110 (30)
    #   Expression: (12 + 3) * 2 = 30
    print("5. Chained Operations:")
    a = BinaryNumber(binary_str='1100')  # 12
    b = BinaryNumber(binary_str='11')    # 3
    
    # (12 + 3) * 2
    step1 = calculator.add(operand_1=a, operand_2=b)
    print(f"   Step 1: {a.value} + {b.value} = {step1.value} ({step1.to_int()})")
    
    two = BinaryNumber(binary_str='10')
    step2 = calculator.multiply(operand_1=step1, operand_2=two)
    print(f"   Step 2: {step1.value} * {two.value} = {step2.value} "
          f"({step2.to_int()})")
    print(f"   Expression: (12 + 3) * 2 = {step2.to_int()}")
    # --8<-- [end:chained_operations]
    print()


def calc06_error_handling() -> None:
    """ArithmeticCalculator: Error handling.
    
    Key: calc06
    Run: python examples/example.py calc06
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:error_handling]
    # Error handling demonstrations
    # Expected: Both operations raise appropriate exceptions
    # Console output: Error messages showing validation
    print("6. Error Handling:")
    
    # Division by zero
    # Input: Dividend '1010', divisor '0'
    # Processing:
    #   1. normalize_leading_zeros('0') = '0'
    #   2. Check if divisor == '0': True
    #   3. Raise ZeroDivisionError
    # Expected: ZeroDivisionError raised
    print("   a) Division by zero:")
    try:
        zero = BinaryNumber(binary_str='0')
        nonzero = BinaryNumber(binary_str='1010')
        result_err = calculator.divide(operand_1=nonzero, operand_2=zero)
    except ZeroDivisionError as e:
        print(f"      [OK] {e}")
    
    print()
    # Negative subtraction result
    # Input: '101' (5) - '1010' (10)
    # Processing:
    #   1. Compare: '101' < '1010' ✓ (would be negative)
    #   2. Raise ValueError before attempting subtraction
    # Expected: ValueError raised
    print("   b) Negative subtraction result:")
    try:
        small = BinaryNumber(binary_str='101')   # 5
        large = BinaryNumber(binary_str='1010')  # 10
        result_neg = calculator.subtract(operand_1=small, operand_2=large)
    except ValueError as e:
        print(f"      [OK] {e}")
    # --8<-- [end:error_handling]
    print()


def calc07_larger_numbers() -> None:
    """ArithmeticCalculator: Operations with larger numbers.
    
    Key: calc07
    Run: python examples/example.py calc07
    """
    print("=" * 70)
    print("Example 03: ArithmeticCalculator Operations")
    print("=" * 70)
    print()
    
    calculator = ArithmeticCalculator()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    # Real-world scenarios demonstrating practical use cases
    # Numbers in range 1,000 to 1,000,000
    # Expected console output shows memory addresses, file sizes, network
    # calculations, and image dimensions with both binary and decimal values
    print("7. Operations with Larger Numbers:")
    
    # Memory address calculation
    # Real-world: OS memory management, adding offset to base address
    # Input: 65,536 bytes (16-bit boundary) + 4,096 bytes (one page)
    # Processing: Same add algorithm, just with 17-bit and 13-bit numbers
    # Expected: 69,632 bytes (0x11000)
    # Console output: Shows hex addresses for OS context
    print("   a) Memory address calculation:")
    base_addr = BinaryNumber.from_int(decimal_num=65536)  # Base: 0x10000
    offset = BinaryNumber.from_int(decimal_num=4096)      # Offset: 0x1000
    
    addr_result = calculator.add(operand_1=base_addr, operand_2=offset)
    print(f"      Base:   {base_addr.to_int():,} (0x{base_addr.to_int():X})")
    print(f"      Offset: {offset.to_int():,} (0x{offset.to_int():X})")
    print(f"      Result: {addr_result.to_int():,} (0x{addr_result.to_int():X})")
    print()
    
    # File size calculation
    print("   b) Total file storage:")
    file1 = BinaryNumber.from_int(decimal_num=524288)   # 512 KB
    file2 = BinaryNumber.from_int(decimal_num=786432)   # 768 KB
    
    total = calculator.add(operand_1=file1, operand_2=file2)
    total_kb = total.to_int() // 1024
    total_mb = total.to_int() / (1024 * 1024)
    print(f"      File 1: {file1.to_int():,} bytes (512 KB)")
    print(f"      File 2: {file2.to_int():,} bytes (768 KB)")
    print(f"      Total:  {total.to_int():,} bytes = {total_kb} KB = "
          f"{total_mb:.2f} MB")
    print()
    
    # Network calculation
    print("   c) Network packets per second:")
    bandwidth = BinaryNumber.from_int(decimal_num=1048576)  # 1 Mbps
    packet_size = BinaryNumber.from_int(decimal_num=8192)   # 1 KB packets
    
    packets = calculator.divide(operand_1=bandwidth, operand_2=packet_size)
    print(f"      Bandwidth:   {bandwidth.to_int():,} bits/sec (1 Mbps)")
    print(f"      Packet size: {packet_size.to_int():,} bits")
    print(f"      Packets/sec: {packets.to_int():,}")
    print()
    
    # Image dimensions
    print("   d) Image pixel count (1920x1080):")
    width = BinaryNumber.from_int(decimal_num=1920)
    height = BinaryNumber.from_int(decimal_num=1080)
    
    pixels = calculator.multiply(operand_1=width, operand_2=height)
    print(f"      Width:  {width.to_int():,} pixels")
    print(f"      Height: {height.to_int():,} pixels")
    print(f"      Total:  {pixels.to_int():,} pixels")
    memory_bytes = pixels.to_int() * 3  # RGB
    print(f"      Memory: {memory_bytes:,} bytes "
          f"({memory_bytes / (1024*1024):.2f} MB for 24-bit RGB)")
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all ArithmeticCalculator examples."""
    calc01_addition()
    calc02_subtraction()
    calc03_multiplication()
    calc04_division()
    calc05_chained_operations()
    calc06_error_handling()
    calc07_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

