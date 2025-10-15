"""Example 06: BinaryNormalizer - Normalizing Binary Strings

This example demonstrates the BinaryNormalizer class which provides utility
methods for normalizing binary string representations.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNormalizer


def norm01_remove_leading_zeros() -> None:
    """BinaryNormalizer: Remove leading zeros.
    
    Key: norm01
    Run: python examples/example.py norm01
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:setup]
    normalizer = BinaryNormalizer()
    # --8<-- [end:setup]
    
    # --8<-- [start:remove_leading_zeros]
    # Removing leading zeros using lstrip('0') or '0'
    # Input: Binary strings with various leading zero patterns
    # Processing for each:
    #   Uses binary_str.lstrip('0') or '0' (prevents empty string)
    #   '0101' -> '101', '00001010' -> '1010', '000' -> '0'
    # Expected: Normalized strings without leading zeros
    # Console output:
    #   '0101' -> '101'
    #   '00001010' -> '1010'
    #   '000' -> '0'
    #   '1010' -> '1010'
    #   '0' -> '0'
    print("1. Removing Leading Zeros:")
    test_cases = ['0101', '00001010', '000', '1010', '0']
    
    for binary in test_cases:
        normalized = normalizer.remove_leading_zeros(binary_str=binary)
        print(f"   '{binary:>10}' -> '{normalized}'")
    # --8<-- [end:remove_leading_zeros]
    print()


def norm02_normalize_length() -> None:
    """BinaryNormalizer: Normalize length.
    
    Key: norm02
    Run: python examples/example.py norm02
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    normalizer = BinaryNormalizer()
    
    # --8<-- [start:normalize_length]
    # Normalizing length prepends zeros to shorter string
    # Input: Pairs of binary strings with different lengths
    # Processing for each pair:
    #   1. Find max length
    #   2. Pad shorter string with leading zeros using zfill()
    #   Example: '101' (3 bits) and '11' (2 bits)
    #     max_len = 3
    #     '101'.zfill(3) = '101'
    #     '11'.zfill(3) = '011'
    # Expected: Both strings same length
    # Console output: Shows original and normalized pairs
    print("2. Normalizing Length:")
    pairs = [
        ('101', '11'),
        ('1010', '101010'),
        ('1', '1111')]
    
    for bin1, bin2 in pairs:
        norm1, norm2 = normalizer.normalize_length(
            binary_1=bin1,
            binary_2=bin2)
        print(f"   '{bin1}' and '{bin2}'")
        print(f"   -> '{norm1}' and '{norm2}'")
        print(f"      (both {len(norm1)} bits)")
        print()
    # --8<-- [end:normalize_length]
    print()


def norm03_practical_use() -> None:
    """BinaryNormalizer: Practical use case.
    
    Key: norm03
    Run: python examples/example.py norm03
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    normalizer = BinaryNormalizer()
    
    # --8<-- [start:practical_use]
    # Practical use case - preparing operands for addition
    # Input: '1010' (4 bits) and '101' (3 bits)
    # Processing:
    #   1. Before: Cannot add bit-by-bit (different lengths)
    #   2. Normalize: '1010' and '0101' (both 4 bits)
    #   3. After: Can add position-by-position
    # Expected: Both operands are 4 bits
    # Console output:
    #   Original: 1010 (4 bits), 101 (3 bits)
    #   After: 1010 (4 bits), 0101 (4 bits)
    #   Now ready for bit-by-bit addition!
    print("3. Practical Use Case - Preparing for Addition:")
    binary_a = '1010'  # 10
    binary_b = '101'   # 5
    
    print(f"   Original operands:")
    print(f"     {binary_a} ({len(binary_a)} bits)")
    print(f"     {binary_b} ({len(binary_b)} bits)")
    print()
    
    # Normalize for bit-by-bit operation
    norm_a, norm_b = normalizer.normalize_length(
        binary_1=binary_a,
        binary_2=binary_b)
    
    print(f"   After normalization:")
    print(f"     {norm_a} ({len(norm_a)} bits)")
    print(f"     {norm_b} ({len(norm_b)} bits)")
    print(f"   Now ready for bit-by-bit addition!")
    # --8<-- [end:practical_use]
    print()


def norm04_edge_cases() -> None:
    """BinaryNormalizer: Edge cases.
    
    Key: norm04
    Run: python examples/example.py norm04
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    normalizer = BinaryNormalizer()
    
    # --8<-- [start:edge_cases]
    # Edge cases demonstrate robust handling
    # Input: Various edge case scenarios
    # Processing:
    #   All zeros: '0000'.lstrip('0') = '', fallback to '0'
    #   Single vs multiple: normalize '1' and '1111' to both 4 bits
    #   Already normalized: '101' has no leading zeros, unchanged
    # Expected: Handles all cases correctly
    # Console output:
    #   All zeros: '0000' -> '0'
    #   Single vs multiple: '1', '1111' -> '0001', '1111'
    #   Already normalized: '101' -> '101'
    print("4. Edge Cases:")
    
    # All zeros
    all_zeros = normalizer.remove_leading_zeros(binary_str='0000')
    print(f"   All zeros: '0000' -> '{all_zeros}'")
    
    # Single bit
    single = '1'
    multi = '1111'
    n1, n2 = normalizer.normalize_length(binary_1=single, binary_2=multi)
    print(f"   Single vs multiple: '{single}', '{multi}'")
    print(f"   -> '{n1}', '{n2}'")
    
    # Already normalized
    already_norm = '101'
    result = normalizer.remove_leading_zeros(binary_str=already_norm)
    print(f"   Already normalized: '{already_norm}' -> '{result}'")
    # --8<-- [end:edge_cases]
    print()


def norm05_comparison_demo() -> None:
    """BinaryNormalizer: Why normalization matters.
    
    Key: norm05
    Run: python examples/example.py norm05
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    normalizer = BinaryNormalizer()
    
    # --8<-- [start:comparison_demo]
    # Why normalization matters for comparisons
    # Input: Three representations of decimal 5
    #   '101' (3 bits), '0101' (4 bits), '00101' (5 bits)
    # Processing:
    #   Without normalization: String comparison would say they differ
    #   With normalization: All strip to '101'
    # Expected: All normalize to '101' and are equal
    # Console output:
    #   Different representations: 101, 0101, 00101
    #   After removing leading zeros: all become '101'
    #   All equal: True
    print("5. Why Normalization Matters:")
    
    # These represent the same value
    value1 = '101'
    value2 = '0101'
    value3 = '00101'
    
    print(f"   Different representations of same value (5):")
    print(f"     '{value1}' ({len(value1)} bits)")
    print(f"     '{value2}' ({len(value2)} bits)")
    print(f"     '{value3}' ({len(value3)} bits)")
    print()
    
    print(f"   After removing leading zeros:")
    norm1 = normalizer.remove_leading_zeros(binary_str=value1)
    norm2 = normalizer.remove_leading_zeros(binary_str=value2)
    norm3 = normalizer.remove_leading_zeros(binary_str=value3)
    
    print(f"     '{norm1}'")
    print(f"     '{norm2}'")
    print(f"     '{norm3}'")
    print(f"   All equal: {norm1 == norm2 == norm3}")
    # --8<-- [end:comparison_demo]
    print()


def norm06_larger_numbers() -> None:
    """BinaryNormalizer: Normalizing larger numbers.
    
    Key: norm06
    Run: python examples/example.py norm06
    """
    print("=" * 70)
    print("Example 06: BinaryNormalizer Operations")
    print("=" * 70)
    print()
    
    normalizer = BinaryNormalizer()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    print("6. Normalizing Larger Numbers:")
    
    # Memory addresses with different representations
    print("   a) Memory address normalization:")
    addr1 = '10000000000000000'      # 65536 (no leading zeros)
    addr2 = '00001000000000000'      # 4096 (leading zeros)
    
    print(f"      Address 1: {addr1} ({len(addr1)} bits)")
    print(f"      Address 2: {addr2} ({len(addr2)} bits)")
    
    # Remove leading zeros from addr2
    addr2_clean = normalizer.remove_leading_zeros(binary_str=addr2)
    print(f"      After removing leading zeros from addr2:")
    print(f"                 {addr2_clean} ({len(addr2_clean)} bits)")
    print()
    
    # Normalize both for addition
    n_addr1, n_addr2 = normalizer.normalize_length(
        binary_1=addr1,
        binary_2=addr2)
    print(f"      After normalizing lengths:")
    print(f"      Address 1: {n_addr1}")
    print(f"      Address 2: {n_addr2}")
    print(f"      (both {len(n_addr1)} bits, ready for addition)")
    print()
    
    # File sizes
    print("   b) File size normalization:")
    file_kb = '10000000000000000000'    # 524,288 bytes (512 KB)
    file_mb = '11000000000000000000'    # 786,432 bytes (768 KB)
    
    print(f"      File 1: {file_kb}")
    print(f"              ({int(file_kb, 2):,} bytes = "
          f"{int(file_kb, 2) // 1024} KB)")
    print(f"      File 2: {file_mb}")
    print(f"              ({int(file_mb, 2):,} bytes = "
          f"{int(file_mb, 2) // 1024} KB)")
    print()
    
    # Already same length, but demonstrate
    nf1, nf2 = normalizer.normalize_length(
        binary_1=file_kb,
        binary_2=file_mb)
    print(f"      After normalization (already same length):")
    print(f"      File 1: {nf1}")
    print(f"      File 2: {nf2}")
    print()
    
    # Network packets
    print("   c) Different magnitude numbers:")
    bandwidth = '100000000000000000000'    # 1,048,576 (1 Mbps)
    packet = '10000000000000'              # 8,192 bits
    
    print(f"      Bandwidth:   {bandwidth}")
    print(f"                   ({int(bandwidth, 2):,} bits/sec)")
    print(f"      Packet size: {packet}")
    print(f"                   ({int(packet, 2):,} bits)")
    print()
    
    nb, np = normalizer.normalize_length(
        binary_1=bandwidth,
        binary_2=packet)
    print(f"      After normalization:")
    print(f"      Bandwidth:   {nb}")
    print(f"      Packet size: {np}")
    print(f"      Length difference handled: {len(bandwidth)} and "
          f"{len(packet)} -> both {len(nb)} bits")
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all BinaryNormalizer examples."""
    norm01_remove_leading_zeros()
    norm02_normalize_length()
    norm03_practical_use()
    norm04_edge_cases()
    norm05_comparison_demo()
    norm06_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

