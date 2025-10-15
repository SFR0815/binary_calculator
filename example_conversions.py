"""Example usage of binary-decimal conversion functions."""

from binary_calculator import BinaryCalculator, BinaryInstruction


def main() -> None:
    """Demonstrate binary-decimal conversion functionality."""
    calculator = BinaryCalculator()
    
    print("=" * 70)
    print("Binary-Decimal Conversion Examples")
    print("=" * 70)
    print()
    
    # Example 1: Binary to Decimal
    print("Example 1: Binary to Decimal Conversion")
    print("-" * 70)
    binary_numbers = ['1010', '11111111', '10000000', '101010',
                      '11001100', '1111']
    
    for binary in binary_numbers:
        decimal = calculator.binary_to_decimal(binary_str=binary)
        print(f"  Binary: {binary:>12} -> Decimal: {decimal}")
    print()
    
    # Example 2: Decimal to Binary
    print("Example 2: Decimal to Binary Conversion")
    print("-" * 70)
    decimal_numbers = [0, 1, 10, 42, 100, 255, 1024, 65535]
    
    for decimal in decimal_numbers:
        binary = calculator.decimal_to_binary(decimal_num=decimal)
        print(f"  Decimal: {decimal:>6} -> Binary: {binary}")
    print()
    
    # Example 3: Round-trip conversion
    print("Example 3: Round-Trip Conversion")
    print("-" * 70)
    original_binary = '110110101'
    print(f"  Original binary: {original_binary}")
    
    decimal = calculator.binary_to_decimal(binary_str=original_binary)
    print(f"  Converted to decimal: {decimal}")
    
    result_binary = calculator.decimal_to_binary(decimal_num=decimal)
    print(f"  Converted back to binary: {result_binary}")
    print(f"  Match: {original_binary == result_binary}")
    print()
    
    # Example 4: Powers of 2
    print("Example 4: Powers of Two")
    print("-" * 70)
    for power in [0, 1, 2, 4, 8, 10, 16]:
        decimal = 2 ** power
        binary = calculator.decimal_to_binary(decimal_num=decimal)
        print(f"  2^{power:>2} = {decimal:>6} = {binary}")
    print()
    
    # Example 5: Large numbers
    print("Example 5: Large Number Conversions")
    print("-" * 70)
    large_decimals = [
        1000000,
        2 ** 20,
        2 ** 32,
        2 ** 50]
    
    for decimal in large_decimals:
        binary = calculator.decimal_to_binary(decimal_num=decimal)
        print(f"  Decimal: {decimal:>20}")
        print(f"  Binary:  {binary}")
        print(f"  Bits:    {len(binary)}")
        print()
    
    # Example 6: Very large numbers (stress test)
    print("Example 6: Very Large Number Support")
    print("-" * 70)
    huge_number = 2 ** 100
    print(f"  Decimal: 2^100")
    print(f"  Value: {huge_number}")
    binary = calculator.decimal_to_binary(decimal_num=huge_number)
    print(f"  Binary bits: {len(binary)}")
    print(f"  Binary (first 50 bits): {binary[:50]}...")
    
    # Verify round-trip
    back_to_decimal = calculator.binary_to_decimal(binary_str=binary)
    print(f"  Round-trip verification: {back_to_decimal == huge_number}")
    print()
    
    # Example 7: Using conversions in calculator operations
    print("Example 7: Conversions in Calculator Operations")
    print("-" * 70)
    
    # User provides numbers in different formats
    binary_num = '1010'
    decimal_num = 5
    
    # Convert decimal to binary for calculation
    binary_num_2 = calculator.decimal_to_binary(decimal_num=decimal_num)
    
    print(f"  Binary operand 1: {binary_num} "
          f"(decimal: "
          f"{calculator.binary_to_decimal(binary_str=binary_num)})")
    print(f"  Decimal operand 2: {decimal_num} "
          f"(binary: {binary_num_2})")
    
    # Perform calculation
    instruction = BinaryInstruction(
        operand_1=binary_num,
        operand_2=binary_num_2,
        operation='+')
    
    result_binary = calculator.execute(instruction=instruction)
    result_decimal = calculator.binary_to_decimal(
        binary_str=result_binary)
    
    print(f"  Result binary: {result_binary}")
    print(f"  Result decimal: {result_decimal}")
    print()
    
    # Example 8: Bit patterns
    print("Example 8: Common Bit Patterns")
    print("-" * 70)
    patterns = {
        'Alternating 1': '10101010',
        'Alternating 2': '01010101',
        'High nibble': '11110000',
        'Low nibble': '00001111',
        'All ones': '11111111',
        'MSB set': '10000000',
        'LSB set': '00000001'}
    
    for name, pattern in patterns.items():
        decimal = calculator.binary_to_decimal(binary_str=pattern)
        print(f"  {name:>14}: {pattern} = {decimal:>3}")
    print()
    
    # Example 9: Negative numbers
    print("Example 9: Negative Number Handling")
    print("-" * 70)
    negative_numbers = [-1, -10, -100, -255]
    
    for decimal in negative_numbers:
        binary = calculator.decimal_to_binary(decimal_num=decimal)
        print(f"  Decimal: {decimal:>5} -> Binary: {binary}")
    print()
    
    # Example 10: Performance with many conversions
    print("Example 10: Batch Conversion Performance")
    print("-" * 70)
    print("  Converting 1000 sequential numbers...")
    
    for i in range(1000):
        binary = calculator.decimal_to_binary(decimal_num=i)
        decimal = calculator.binary_to_decimal(binary_str=binary)
        if decimal != i:
            print(f"  ERROR at {i}")
            break
    else:
        print("  ✓ All 1000 conversions successful!")
    print()
    
    print("=" * 70)
    print("All conversion examples completed successfully!")
    print("=" * 70)


if __name__ == '__main__':
    main()

