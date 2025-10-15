"""Example 07: InstructionExecutor - Executing Instructions with Formatting

This example demonstrates the InstructionExecutor class which executes
instructions and provides formatted output visualization.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import (
    BinaryNumber,
    BinaryInstruction,
    InstructionExecutor)


def exec01_simple_addition() -> None:
    """InstructionExecutor: Simple addition without formatting.
    
    Key: exec01
    Run: python examples/example.py exec01
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:setup]
    executor = InstructionExecutor()
    # --8<-- [end:setup]
    
    # --8<-- [start:simple_addition]
    # Simple addition without formatted output
    # Input: Instruction with '1011' + '110' and print_result=False
    # Processing:
    #   1. Executor validates instruction is CALCULATE type
    #   2. Routes to ArithmeticCalculator.add()
    #   3. Calculator processes: normalize, add bits, create result
    #   4. Returns BinaryNumber (no formatted output)
    # Expected result: BinaryNumber with value '10001' (17)
    # Console output: "1011 + 110 = 10001" and "Decimal: 11 + 6 = 17"
    print("1. Addition (no formatted output):")
    num1 = BinaryNumber(binary_str='1011')
    num2 = BinaryNumber(binary_str='110')
    
    instruction = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    
    result = executor.calculate(instruction=instruction, print_result=False)
    print(f"   {num1.value} + {num2.value} = {result.value}")
    print(f"   Decimal: {num1.to_int()} + {num2.to_int()} = {result.to_int()}")
    # --8<-- [end:simple_addition]
    print()


def exec02_formatted_addition() -> None:
    """InstructionExecutor: Addition with formatted output.
    
    Key: exec02
    Run: python examples/example.py exec02
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:formatted_addition]
    # Addition with formatted output
    # Input: Same instruction but with print_result=True
    # Processing:
    #   1-3. Same as above (calculate result)
    #   4. Call _print_calculation() before returning
    #   5. Print formatted display:
    #      - Instruction repr (right-aligned operands)
    #      - Separator line of dashes
    #      - Result (right-aligned with indent)
    #      - Separator line of equals
    # Expected console output:
    #     1011
    #   +  110
    #   ------
    #    10001
    #   ======
    #   Result: 10001 (17)
    num1 = BinaryNumber(binary_str='1011')
    num2 = BinaryNumber(binary_str='110')
    instruction = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    print("2. Addition (with formatted output):")
    result = executor.calculate(instruction=instruction, print_result=True)
    print(f"   Result: {result.value} ({result.to_int()})")
    # --8<-- [end:formatted_addition]
    print()


def exec03_subtraction() -> None:
    """InstructionExecutor: Subtraction.
    
    Key: exec03
    Run: python examples/example.py exec03
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:subtraction]
    # Subtraction with formatted output
    # Input: Instruction with '10101' (21) - '1001' (9)
    # Processing:
    #   1. Validate CALCULATE type
    #   2. Route to ArithmeticCalculator.subtract()
    #   3. Subtract bit-by-bit with borrow handling
    #   4. Result: '1100' (12)
    #   5. Display formatted output
    # Expected console output:
    #   10101
    # -  1001
    # -------
    #    1100
    # =======
    #   Result: 1100 (12)
    print("3. Subtraction:")
    num3 = BinaryNumber(binary_str='10101')
    num4 = BinaryNumber(binary_str='1001')
    
    sub_instr = BinaryInstruction(
        operand_1=num3,
        operand_2=num4,
        operation='-')
    
    result_sub = executor.calculate(instruction=sub_instr, print_result=True)
    print(f"   Result: {result_sub.value} ({result_sub.to_int()})")
    # --8<-- [end:subtraction]
    print()


def exec04_multiplication() -> None:
    """InstructionExecutor: Multiplication.
    
    Key: exec04
    Run: python examples/example.py exec04
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:multiplication]
    # Multiplication with shift-and-add algorithm
    # Input: '101' (5) * '11' (3)
    # Processing:
    #   1. Validate and route to multiply()
    #   2. Shift-and-add: Process multiplier bits, add shifted values
    #   3. Result: '1111' (15)
    # Expected console output:
    #   101
    # *  11
    # -----
    #  1111
    # =====
    #   Result: 1111 (15)
    print("4. Multiplication:")
    num5 = BinaryNumber(binary_str='101')
    num6 = BinaryNumber(binary_str='11')
    
    mul_instr = BinaryInstruction(
        operand_1=num5,
        operand_2=num6,
        operation='*')
    
    result_mul = executor.calculate(instruction=mul_instr, print_result=True)
    print(f"   Result: {result_mul.value} ({result_mul.to_int()})")
    # --8<-- [end:multiplication]
    print()


def exec05_division() -> None:
    """InstructionExecutor: Division.
    
    Key: exec05
    Run: python examples/example.py exec05
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:division]
    # Division using binary long division algorithm
    # Input: '1101' (13) / '11' (3)
    # Processing:
    #   1. Validate and route to divide()
    #   2. Binary long division processes dividend bit-by-bit
    #   3. Result: '100' (4, with remainder discarded)
    # Expected console output:
    #   1101
    # /   11
    # ------
    #    100
    # ======
    #   Result: 100 (4)
    print("5. Division:")
    num7 = BinaryNumber(binary_str='1101')
    num8 = BinaryNumber(binary_str='11')
    
    div_instr = BinaryInstruction(
        operand_1=num7,
        operand_2=num8,
        operation='/')
    
    result_div = executor.calculate(instruction=div_instr, print_result=True)
    print(f"   Result: {result_div.value} ({result_div.to_int()})")
    # --8<-- [end:division]
    print()


def exec06_comparison() -> None:
    """InstructionExecutor: Comparison operation.
    
    Key: exec06
    Run: python examples/example.py exec06
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:comparison]
    # Comparison demonstration
    # Input: Comparison instruction '1010' >= '101'
    # Processing:
    #   1. Validate COMPARE type
    #   2. Route to BinaryComparator.larger_equal()
    #   3. Compare: lengths 4 > 3, return 1
    #   4. Check 1 >= 0: True
    #   5. Display formatted output
    # Expected console output:
    #    1010
    # >=  101
    # -------
    #    True
    # =======
    #   Result: True
    print("6. Comparison (>=):")
    num9 = BinaryNumber(binary_str='1010')
    num10 = BinaryNumber(binary_str='101')
    
    cmp_instr = BinaryInstruction(
        operand_1=num9,
        operand_2=num10,
        operation='>=')
    
    result_cmp = executor.compare(instruction=cmp_instr, print_result=True)
    print(f"   Result: {result_cmp}")
    # --8<-- [end:comparison]
    print()


def exec07_all_comparisons() -> None:
    """InstructionExecutor: All comparison operations.
    
    Key: exec07
    Run: python examples/example.py exec07
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:all_comparisons]
    # All comparison operations on same operands
    # Input: '1010' (10) and '101' (5) with all 6 operators
    # Processing: Each routes to appropriate comparator method
    #   All use same compare() result (1 = first > second)
    # Expected results: True for >, >=, !=; False for <, <=, ==
    # Console output: Six lines showing boolean results
    print("7. All Comparison Operations:")
    comp_ops = ['<', '<=', '>', '>=', '==', '!=']
    for op in comp_ops:
        instr = BinaryInstruction(
            operand_1=num9,
            operand_2=num10,
            operation=op)
        result_bool = executor.compare(instruction=instr, print_result=False)
        print(f"   {num9.value} {op} {num10.value} = {result_bool}")
    # --8<-- [end:all_comparisons]
    print()


def exec08_error_handling() -> None:
    """InstructionExecutor: Error handling.
    
    Key: exec08
    Run: python examples/example.py exec08
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:error_handling]
    # Error handling for common mistakes
    # Input: Various invalid operations
    # Processing: Each validates and raises appropriate exception
    # Expected: All errors caught with informative messages
    # Console output: Three error messages showing validation works
    print("8. Error Handling:")
    
    # Wrong method for instruction type
    # Input: Comparison instruction ('<') passed to calculate()
    # Processing:
    #   1. calculate() checks is_calculation()
    #   2. Returns False (it's COMPARE type)
    #   3. Raises ValueError with helpful message
    # Expected: ValueError explaining to use compare() instead
    print("   a) Wrong method for instruction type:")
    try:
        calc_instr = BinaryInstruction(
            operand_1=num1,
            operand_2=num2,
            operation='<')
        # Using calculate() instead of compare()
        wrong = executor.calculate(instruction=calc_instr)
    except ValueError as e:
        print(f"      [OK] {e}")
    
    print()
    # Division by zero
    # Input: Valid dividend, zero divisor
    # Processing: ArithmeticCalculator detects zero, raises exception
    # Expected: ZeroDivisionError
    print("   b) Division by zero:")
    try:
        zero = BinaryNumber(binary_str='0')
        nonzero = BinaryNumber(binary_str='1010')
        div_zero = BinaryInstruction(
            operand_1=nonzero,
            operand_2=zero,
            operation='/')
        result_err = executor.calculate(instruction=div_zero)
    except ZeroDivisionError as e:
        print(f"      [OK] {e}")
    
    print()
    # Negative subtraction result
    # Input: '101' (5) - '1010' (10)
    # Processing: Subtraction detects result would be negative
    # Expected: ValueError
    print("   c) Negative subtraction result:")
    try:
        small = BinaryNumber(binary_str='101')
        large = BinaryNumber(binary_str='1010')
        sub_neg = BinaryInstruction(
            operand_1=small,
            operand_2=large,
            operation='-')
        result_neg = executor.calculate(instruction=sub_neg)
    except ValueError as e:
        print(f"      [OK] {e}")
    # --8<-- [end:error_handling]
    print()


def exec09_larger_numbers() -> None:
    """InstructionExecutor: Realistic scenarios with larger numbers.
    
    Key: exec09
    Run: python examples/example.py exec09
    """
    print("=" * 70)
    print("Example 07: InstructionExecutor Operations")
    print("=" * 70)
    print()
    
    executor = InstructionExecutor()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    print("9. Realistic Scenarios with Larger Numbers:")
    
    # Memory allocation
    print("   a) Memory address calculation:")
    base = BinaryNumber.from_int(decimal_num=65536)
    offset = BinaryNumber.from_int(decimal_num=4096)
    
    mem_instr = BinaryInstruction(
        operand_1=base,
        operand_2=offset,
        operation='+')
    
    print(f"      Base + Offset:")
    result_mem = executor.calculate(instruction=mem_instr, print_result=True)
    print(f"      Final address: {result_mem.to_int():,} bytes "
          f"(0x{result_mem.to_int():X})")
    print()
    
    # File storage
    print("   b) Total file storage:")
    file1_large = BinaryNumber.from_int(decimal_num=524288)
    file2_large = BinaryNumber.from_int(decimal_num=786432)
    
    storage_instr = BinaryInstruction(
        operand_1=file1_large,
        operand_2=file2_large,
        operation='+')
    
    result_storage = executor.calculate(
        instruction=storage_instr,
        print_result=True)
    total_kb = result_storage.to_int() // 1024
    print(f"      Total: {result_storage.to_int():,} bytes = {total_kb} KB")
    print()
    
    # Network throughput
    print("   c) Network packets per second:")
    throughput = BinaryNumber.from_int(decimal_num=1048576)
    pkt_size = BinaryNumber.from_int(decimal_num=8192)
    
    net_instr = BinaryInstruction(
        operand_1=throughput,
        operand_2=pkt_size,
        operation='/')
    
    result_net = executor.calculate(instruction=net_instr, print_result=True)
    print(f"      Packets/sec: {result_net.to_int():,}")
    print()
    
    # Performance check
    print("   d) Performance threshold check:")
    actual = BinaryNumber.from_int(decimal_num=750000)
    threshold = BinaryNumber.from_int(decimal_num=500000)
    
    perf_instr = BinaryInstruction(
        operand_1=actual,
        operand_2=threshold,
        operation='>=')
    
    result_perf = executor.compare(instruction=perf_instr, print_result=True)
    status = "PASS" if result_perf else "FAIL"
    print(f"      Performance check: {status}")
    print(f"      ({actual.to_int():,} >= {threshold.to_int():,})")
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all InstructionExecutor examples."""
    exec01_simple_addition()
    exec02_formatted_addition()
    exec03_subtraction()
    exec04_multiplication()
    exec05_division()
    exec06_comparison()
    exec07_all_comparisons()
    exec08_error_handling()
    exec09_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

