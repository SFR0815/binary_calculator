"""Example 05: BinaryConverter - Converting Between Binary and Decimal

This example demonstrates the BinaryConverter class which provides utility
methods for converting between binary strings and decimal integers.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryConverter


def conv01_binary_to_decimal() -> None:
    """BinaryConverter: Binary to decimal conversion.
    
    Key: conv01
    Run: python examples/example.py conv01
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:setup]
    converter = BinaryConverter()
    # --8<-- [end:setup]
    
    # --8<-- [start:binary_to_decimal]
    # Converting binary to decimal
    # Input: Binary strings ['1010', '1111', '10000', '11111111']
    # Processing for each:
    #   Uses Python's int(binary_str, 2) to convert
    #   Example: int('1010', 2) = 1×8 + 0×4 + 1×2 + 0×1 = 10
    # Expected results: [10, 15, 16, 255]
    # Console output: Four lines showing binary -> decimal conversions
    print("1. Binary to Decimal Conversion:")
    binary_values = ['1010', '1111', '10000', '11111111']
    
    for binary in binary_values:
        decimal = converter.binary_to_decimal(binary_str=binary)
        print(f"   {binary:>10} (binary) = {decimal:>5} (decimal)")
    # --8<-- [end:binary_to_decimal]
    print()


def conv02_decimal_to_binary() -> None:
    """BinaryConverter: Decimal to binary conversion.
    
    Key: conv02
    Run: python examples/example.py conv02
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:decimal_to_binary]
    # Converting decimal to binary
    # Input: Integers [10, 15, 16, 255]
    # Processing for each:
    #   Uses Python's bin(decimal) then strips '0b' prefix
    #   Example: bin(10) = '0b1010', strip to '1010'
    # Expected results: ['1010', '1111', '10000', '11111111']
    # Console output: Four lines showing decimal -> binary conversions
    print("2. Decimal to Binary Conversion:")
    decimal_values = [10, 15, 16, 255]
    
    for decimal in decimal_values:
        binary = converter.decimal_to_binary(decimal_num=decimal)
        print(f"   {decimal:>5} (decimal) = {binary:>10} (binary)")
    # --8<-- [end:decimal_to_binary]
    print()


def conv03_round_trip() -> None:
    """BinaryConverter: Round-trip conversion.
    
    Key: conv03
    Run: python examples/example.py conv03
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:round_trip]
    # Round-trip conversion verifies no data loss
    # Input: Integer 42
    # Processing:
    #   1. decimal_to_binary(42): bin(42)[2:] = '101010'
    #   2. binary_to_decimal('101010'): int('101010', 2) = 42
    # Expected result: 42 == 42 (True)
    # Console output:
    #   Original decimal:   42
    #   Converted to binary: 101010
    #   Back to decimal:    42
    #   Match: True
    print("3. Round-Trip Conversion:")
    original = 42
    
    # Decimal -> Binary -> Decimal
    binary = converter.decimal_to_binary(decimal_num=original)
    back_to_decimal = converter.binary_to_decimal(binary_str=binary)
    
    print(f"   Original decimal:   {original}")
    print(f"   Converted to binary: {binary}")
    print(f"   Back to decimal:    {back_to_decimal}")
    print(f"   Match: {original == back_to_decimal}")
    # --8<-- [end:round_trip]
    print()


def conv04_powers_of_two() -> None:
    """BinaryConverter: Powers of 2.
    
    Key: conv04
    Run: python examples/example.py conv04
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:powers_of_two]
    # Powers of 2 show sparse binary representations
    # Input: Powers from 2^0 to 2^10
    # Processing: Each power of 2 has only ONE bit set
    #   2^0 = 1 = '1' (1 bit set)
    #   2^1 = 2 = '10' (1 bit set)
    #   2^2 = 4 = '100' (1 bit set)
    #   etc.
    # Expected: All show exactly 1 bit set
    # Console output: 11 lines showing power of 2 binary patterns
    print("4. Powers of 2:")
    for power in range(0, 11):
        decimal_val = 2 ** power
        binary_val = converter.decimal_to_binary(decimal_num=decimal_val)
        bit_count = binary_val.count('1')
        print(f"   2^{power:2} = {decimal_val:5} = {binary_val:>12} "
              f"({bit_count} bit set)")
    # --8<-- [end:powers_of_two]
    print()


def conv05_large_numbers() -> None:
    """BinaryConverter: Larger numbers.
    
    Key: conv05
    Run: python examples/example.py conv05
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:large_numbers]
    # Larger numbers demonstrate bit length growth
    # Input: [1024, 4096, 65536, 1048576] - all powers of 2
    # Processing: Convert each to binary
    #   1024 = 2^10: '10000000000' (11 bits)
    #   4096 = 2^12: '1000000000000' (13 bits)
    #   65536 = 2^16: '10000000000000000' (17 bits)
    #   1048576 = 2^20: '100000000000000000000' (21 bits)
    # Expected: Bit length = power + 1
    # Console output: Shows binary and bit length for each
    print("5. Larger Numbers:")
    large_values = [1024, 4096, 65536, 1048576]
    
    for val in large_values:
        binary = converter.decimal_to_binary(decimal_num=val)
        bit_length = len(binary)
        print(f"   {val:>10} = {binary}")
        print(f"   {' ' * 14} ({bit_length} bits)")
    # --8<-- [end:large_numbers]
    print()


def conv06_comparison() -> None:
    """BinaryConverter: Representation comparison.
    
    Key: conv06
    Run: python examples/example.py conv06
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:comparison]
    # Comparing decimal and binary representation efficiency
    # Input: [1, 10, 100, 1000]
    # Processing: Count digits in each representation
    #   1: 1 decimal digit, 1 binary bit (ratio 1.0)
    #   10: 2 decimal digits, 4 binary bits (ratio 2.0)
    #   100: 3 decimal digits, 7 binary bits (ratio 2.33)
    #   1000: 4 decimal digits, 10 binary bits (ratio 2.5)
    # Expected: Binary grows ~log2(n), decimal grows ~log10(n)
    # Console output: Shows efficiency comparison for each value
    print("6. Representation Comparison:")
    test_values = [1, 10, 100, 1000]
    
    for val in test_values:
        binary = converter.decimal_to_binary(decimal_num=val)
        decimal_digits = len(str(val))
        binary_bits = len(binary)
        ratio = binary_bits / decimal_digits
        
        print(f"   {val:>6}: {decimal_digits} decimal digits vs "
              f"{binary_bits} binary bits (ratio: {ratio:.2f})")
    # --8<-- [end:comparison]
    print()


def conv07_realistic_conversions() -> None:
    """BinaryConverter: Realistic use cases.
    
    Key: conv07
    Run: python examples/example.py conv07
    """
    print("=" * 70)
    print("Example 05: BinaryConverter Operations")
    print("=" * 70)
    print()
    
    converter = BinaryConverter()
    
    # --8<-- [start:realistic_conversions]
    # Realistic use cases with larger numbers
    print("7. Realistic Use Cases:")
    
    print("   a) Memory sizes:")
    memory_sizes = [
        (1024, "1 KB"),
        (65536, "64 KB"),
        (524288, "512 KB"),
        (1048576, "1 MB"),
        (8388608, "8 MB")]
    
    for decimal, label in memory_sizes:
        binary = converter.decimal_to_binary(decimal_num=decimal)
        print(f"      {label:>8} = {decimal:>10,} = {binary}")
        print(f"                                    ({len(binary)} bits)")
    print()
    
    print("   b) Network throughput:")
    network_speeds = [
        (128000, "128 Kbps"),
        (1048576, "1 Mbps"),
        (10485760, "10 Mbps")]
    
    for bits_per_sec, label in network_speeds:
        binary = converter.decimal_to_binary(decimal_num=bits_per_sec)
        print(f"      {label:>10} = {bits_per_sec:>10,} bits/sec")
        print(f"                     Binary: {binary}")
        print(f"                     ({len(binary)} bits)")
    print()
    
    print("   c) Time durations:")
    time_values = [
        (1000, "1 second"),
        (60000, "1 minute"),
        (300000, "5 minutes"),
        (3600000, "1 hour")]
    
    for milliseconds, label in time_values:
        binary = converter.decimal_to_binary(decimal_num=milliseconds)
        print(f"      {label:>10} = {milliseconds:>10,} ms = {binary}")
    print()
    
    print("   d) Image dimensions:")
    dimensions = [
        (1920 * 1080, "Full HD (1920x1080)"),
        (2560 * 1440, "2K (2560x1440)"),
        (3840 * 2160, "4K (3840x2160)")]
    
    for pixels, label in dimensions:
        binary = converter.decimal_to_binary(decimal_num=pixels)
        print(f"      {label:>25}: {pixels:>10,} pixels")
        print(f"                                  {binary}")
        print(f"                                  ({len(binary)} bits)")
    # --8<-- [end:realistic_conversions]
    print()


def main() -> None:
    """Run all BinaryConverter examples."""
    conv01_binary_to_decimal()
    conv02_decimal_to_binary()
    conv03_round_trip()
    conv04_powers_of_two()
    conv05_large_numbers()
    conv06_comparison()
    conv07_realistic_conversions()
    print("=" * 70)


if __name__ == '__main__':
    main()

