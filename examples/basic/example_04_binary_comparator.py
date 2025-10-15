"""Example 04: BinaryComparator - Comparing Binary Values

This example demonstrates the BinaryComparator class which performs
comparisons on binary strings without converting to decimal.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryComparator


def comp01_basic_compare() -> None:
    """BinaryComparator: Basic compare method.
    
    Key: comp01
    Run: python examples/example.py comp01
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:setup]
    comparator = BinaryComparator()
    # --8<-- [end:setup]
    
    # --8<-- [start:basic_compare]
    # Basic compare method returns -1, 0, or 1
    # Input: Binary strings '101' (5) and '11' (3)
    # Processing:
    #   1. Remove leading zeros: '101'->'101', '11'->'11'
    #   2. Compare lengths: len('101')=3 > len('11')=2
    #   3. First is longer, so it's larger
    #   4. Return 1
    # Expected result: 1 (first > second)
    # Console output:
    #   compare('101', '11') = 1
    #   (-1 if first < second, 0 if equal, 1 if first > second)
    print("1. Basic compare() method:")
    binary_1 = '101'   # 5
    binary_2 = '11'    # 3
    
    result = comparator.compare(binary_1=binary_1, binary_2=binary_2)
    print(f"   compare('{binary_1}', '{binary_2}') = {result}")
    print(f"   (-1 if first < second, 0 if equal, 1 if first > second)")
    # --8<-- [end:basic_compare]
    print()


def comp02_smaller() -> None:
    """BinaryComparator: Less than comparison.
    
    Key: comp02
    Run: python examples/example.py comp02
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:smaller]
    # Less than comparison
    # Input: Binary strings '10' (2) and '101' (5)
    # Processing:
    #   1. Call compare('10', '101')
    #   2. Remove leading zeros: no change
    #   3. Compare lengths: len('10')=2 < len('101')=3
    #   4. First is shorter, return -1
    #   5. Check if -1 < 0: True
    # Expected result: True
    # Console output: "'10' < '101' = True"
    print("2. smaller() - Less than:")
    bin_a = '10'     # 2
    bin_b = '101'    # 5
    
    is_smaller = comparator.smaller(binary_1=bin_a, binary_2=bin_b)
    print(f"   '{bin_a}' < '{bin_b}' = {is_smaller}")
    # --8<-- [end:smaller]
    print()


def comp03_smaller_equal() -> None:
    """BinaryComparator: Less than or equal comparison.
    
    Key: comp03
    Run: python examples/example.py comp03
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:smaller_equal]
    # Less than or equal comparison
    # Input: '101' (5) and '101' (5) - same value
    # Processing: compare() returns 0, check 0 <= 0: True
    # Expected result: True
    # Console output: "'101' <= '101' = True"
    print("3. smaller_equal() - Less than or equal:")
    bin_c = '101'    # 5
    bin_d = '101'    # 5
    
    is_smaller_eq = comparator.smaller_equal(binary_1=bin_c, binary_2=bin_d)
    print(f"   '{bin_c}' <= '{bin_d}' = {is_smaller_eq}")
    # --8<-- [end:smaller_equal]
    print()


def comp04_larger() -> None:
    """BinaryComparator: Greater than comparison.
    
    Key: comp04
    Run: python examples/example.py comp04
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:larger]
    # Greater than comparison
    # Input: '1010' (10) and '101' (5)
    # Processing: Lengths 4 > 3, return 1, check 1 > 0: True
    # Expected result: True
    # Console output: "'1010' > '101' = True"
    print("4. larger() - Greater than:")
    bin_e = '1010'   # 10
    bin_f = '101'    # 5
    
    is_larger = comparator.larger(binary_1=bin_e, binary_2=bin_f)
    print(f"   '{bin_e}' > '{bin_f}' = {is_larger}")
    # --8<-- [end:larger]
    print()


def comp05_larger_equal() -> None:
    """BinaryComparator: Greater than or equal comparison.
    
    Key: comp05
    Run: python examples/example.py comp05
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:larger_equal]
    # Greater than or equal comparison
    # Input: '1010' (10) and '1010' (10) - same value
    # Processing: compare() returns 0, check 0 >= 0: True
    # Expected result: True
    # Console output: "'1010' >= '1010' = True"
    print("5. larger_equal() - Greater than or equal:")
    bin_g = '1010'   # 10
    bin_h = '1010'   # 10
    
    is_larger_eq = comparator.larger_equal(binary_1=bin_g, binary_2=bin_h)
    print(f"   '{bin_g}' >= '{bin_h}' = {is_larger_eq}")
    # --8<-- [end:larger_equal]
    print()


def comp06_equal() -> None:
    """BinaryComparator: Equality comparison.
    
    Key: comp06
    Run: python examples/example.py comp06
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:equal]
    # Equality comparison with leading zeros
    # Input: '101' (5) and '0101' (also 5, with leading zero)
    # Processing:
    #   1. Remove leading zeros: '101'->'101', '0101'->'101'
    #   2. Compare lengths: 3 == 3
    #   3. Compare lexicographically: '101' == '101'
    #   4. Return 0, check 0 == 0: True
    # Expected result: True (leading zeros handled correctly)
    # Console output: "'101' == '0101' = True"
    print("6. equal() - Equality:")
    bin_i = '101'      # 5
    bin_j = '0101'     # Also 5 (leading zero)
    
    is_equal = comparator.equal(binary_1=bin_i, binary_2=bin_j)
    print(f"   '{bin_i}' == '{bin_j}' = {is_equal}")
    print(f"   (Leading zeros are ignored)")
    # --8<-- [end:equal]
    print()


def comp07_not_equal() -> None:
    """BinaryComparator: Inequality comparison.
    
    Key: comp07
    Run: python examples/example.py comp07
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:not_equal]
    # Inequality comparison
    # Input: '101' (5) and '110' (6)
    # Processing:
    #   1. Lengths equal (3), compare lexicographically
    #   2. '101' < '110', return -1
    #   3. Check -1 != 0: True
    # Expected result: True
    # Console output: "'101' != '110' = True"
    print("7. not_equal() - Inequality:")
    bin_k = '101'    # 5
    bin_l = '110'    # 6
    
    is_not_equal = comparator.not_equal(binary_1=bin_k, binary_2=bin_l)
    print(f"   '{bin_k}' != '{bin_l}' = {is_not_equal}")
    # --8<-- [end:not_equal]
    print()


def comp08_all_comparisons() -> None:
    """BinaryComparator: All comparison operations.
    
    Key: comp08
    Run: python examples/example.py comp08
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:all_comparisons]
    # Demonstrate all comparisons with same pair
    # Input: '1010' (10) and '101' (5) for all 6 operators
    # Processing: Each calls compare() which returns 1 (first > second)
    #   <:  check 1 < 0 = False
    #   <=: check 1 <= 0 = False
    #   >:  check 1 > 0 = True
    #   >=: check 1 >= 0 = True
    #   ==: check 1 == 0 = False
    #   !=: check 1 != 0 = True
    # Expected results: True for >, >=, !=; False for <, <=, ==
    # Console output: Six lines showing all comparison results
    print("8. All Comparisons (1010 vs 101):")
    val_1 = '1010'  # 10
    val_2 = '101'   # 5
    
    print(f"   '{val_1}' < '{val_2}':  "
          f"{comparator.smaller(binary_1=val_1, binary_2=val_2)}")
    print(f"   '{val_1}' <= '{val_2}': "
          f"{comparator.smaller_equal(binary_1=val_1, binary_2=val_2)}")
    print(f"   '{val_1}' > '{val_2}':  "
          f"{comparator.larger(binary_1=val_1, binary_2=val_2)}")
    print(f"   '{val_1}' >= '{val_2}': "
          f"{comparator.larger_equal(binary_1=val_1, binary_2=val_2)}")
    print(f"   '{val_1}' == '{val_2}': "
          f"{comparator.equal(binary_1=val_1, binary_2=val_2)}")
    print(f"   '{val_1}' != '{val_2}': "
          f"{comparator.not_equal(binary_1=val_1, binary_2=val_2)}")
    # --8<-- [end:all_comparisons]
    print()


def comp09_larger_numbers() -> None:
    """BinaryComparator: Comparisons with larger numbers.
    
    Key: comp09
    Run: python examples/example.py comp09
    """
    print("=" * 70)
    print("Example 04: BinaryComparator Operations")
    print("=" * 70)
    print()
    
    comparator = BinaryComparator()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    print("9. Comparisons with Larger Numbers:")
    
    # Performance threshold check
    print("   a) Performance threshold check:")
    actual_ops = '10110111001001110000'      # 750,000 ops/sec
    threshold_ops = '1111010000100100000'    # 500,000 ops/sec
    
    meets_threshold = comparator.larger_equal(
        binary_1=actual_ops,
        binary_2=threshold_ops)
    
    actual_decimal = int(actual_ops, 2)
    threshold_decimal = int(threshold_ops, 2)
    
    print(f"      Actual:    {actual_ops}")
    print(f"                 ({actual_decimal:,} ops/sec)")
    print(f"      Threshold: {threshold_ops}")
    print(f"                 ({threshold_decimal:,} ops/sec)")
    print(f"      Meets requirement: {meets_threshold}")
    print()
    
    # Memory capacity check
    print("   b) Memory capacity check:")
    available = '100000000000000000000000'  # 8 MB
    required = '10000000000000000000'       # 512 KB
    
    has_enough = comparator.larger(binary_1=available, binary_2=required)
    
    avail_decimal = int(available, 2)
    req_decimal = int(required, 2)
    
    print(f"      Available: {available}")
    print(f"                 ({avail_decimal:,} bytes = "
          f"{avail_decimal // (1024*1024)} MB)")
    print(f"      Required:  {required}")
    print(f"                 ({req_decimal:,} bytes = "
          f"{req_decimal // 1024} KB)")
    print(f"      Sufficient: {has_enough}")
    print()
    
    # Time comparison
    print("   c) Time duration comparison:")
    elapsed = '1001001001111100000'    # 300,000 ms (5 min)
    limit = '1110101001100000'         # 60,000 ms (1 min)
    
    exceeds_limit = comparator.larger(binary_1=elapsed, binary_2=limit)
    
    elapsed_decimal = int(elapsed, 2)
    limit_decimal = int(limit, 2)
    
    print(f"      Elapsed: {elapsed}")
    print(f"               ({elapsed_decimal:,} ms = "
          f"{elapsed_decimal // 60000} minutes)")
    print(f"      Limit:   {limit}")
    print(f"               ({limit_decimal:,} ms = "
          f"{limit_decimal // 60000} minute)")
    print(f"      Exceeds limit: {exceeds_limit}")
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all BinaryComparator examples."""
    comp01_basic_compare()
    comp02_smaller()
    comp03_smaller_equal()
    comp04_larger()
    comp05_larger_equal()
    comp06_equal()
    comp07_not_equal()
    comp08_all_comparisons()
    comp09_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

