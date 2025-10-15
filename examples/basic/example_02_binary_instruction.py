"""Example 02: BinaryInstruction - Creating and Validating Instructions

This example demonstrates the BinaryInstruction class which encapsulates
operands and operations with automatic validation and state management.
"""

import sys
import pathlib as p_pthl

sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, BinaryInstruction


def inst01_create_arithmetic_instruction() -> None:
    """BinaryInstruction: Create and display arithmetic instruction.
    
    Key: inst01
    Run: python examples/example.py inst01
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:create_instruction]
    # Create instruction with arithmetic operation
    # Input: Two BinaryNumber objects and operation symbol '+'
    # Processing:
    #   1. Validate operand_1 is BinaryNumber instance (setter checks)
    #   2. Validate operand_2 is BinaryNumber instance (setter checks)
    #   3. Convert operation '+' to OperationEnum.ADD
    #   4. Automatically set state to CALCULATE based on operation
    # Expected result: BinaryInstruction with operands and ADD operation
    # Console output: Two-line repr with right-aligned operands
    num1 = BinaryNumber(binary_str='1010')
    num2 = BinaryNumber(binary_str='101')
    
    instruction = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    # --8<-- [end:create_instruction]
    
    # --8<-- [start:display_instruction]
    # Display instruction details
    # Processing:
    #   1. __repr__ calculates indent: len('+') + 1 = 2 spaces
    #   2. Right-aligns operands to max length (4 bits)
    #   3. Formats as two-line representation
    # Expected console output:
    #     1010
    #   +  101
    #   Operation: +
    #   State: calculate
    #   Is calculation: True
    #   Is comparison: False
    print("1. Arithmetic Instruction:")
    print(instruction)
    print(f"   Operation: {instruction.operation.symbol}")
    print(f"   State: {instruction.state.value}")
    print(f"   Is calculation: {instruction.is_calculation()}")
    print(f"   Is comparison: {instruction.is_comparison()}")
    # --8<-- [end:display_instruction]
    print()


def inst02_create_comparison_instruction() -> None:
    """BinaryInstruction: Create and display comparison instruction.
    
    Key: inst02
    Run: python examples/example.py inst02
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:comparison_instruction]
    # Create instruction with comparison operation
    # Input: BinaryNumbers '11010' (26) and '101' (5), operation '>='
    # Processing:
    #   1. Validate operands are BinaryNumber instances
    #   2. Convert operation '>=' to OperationEnum.LARGER_EQUAL
    #   3. Automatically set state to COMPARE (not CALCULATE)
    # Expected result: BinaryInstruction with state=COMPARE
    # Console output: Three-line repr (indent=3 for '>=' operator)
    num3 = BinaryNumber(binary_str='11010')
    num4 = BinaryNumber(binary_str='101')
    
    comparison = BinaryInstruction(
        operand_1=num3,
        operand_2=num4,
        operation='>=')
    # --8<-- [end:comparison_instruction]
    
    # --8<-- [start:display_comparison]
    # Display comparison instruction
    # Processing:
    #   1. __repr__ calculates indent: len('>=') + 1 = 3 spaces
    #   2. Right-aligns to max length (5 bits for '11010')
    #   3. Formats as two-line with 3-space indent
    # Expected console output:
    #      11010
    #   >=   101
    #   Operation: >=
    #   State: compare
    #   Is calculation: False
    #   Is comparison: True
    print("2. Comparison Instruction:")
    print(comparison)
    print(f"   Operation: {comparison.operation.symbol}")
    print(f"   State: {comparison.state.value}")
    print(f"   Is calculation: {comparison.is_calculation()}")
    print(f"   Is comparison: {comparison.is_comparison()}")
    # --8<-- [end:display_comparison]
    print()


def inst03_all_operations() -> None:
    """BinaryInstruction: All supported operations.
    
    Key: inst03
    Run: python examples/example.py inst03
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:all_operations]
    # Demonstrate all supported operations
    # Input: Operation symbols from both categories
    # Processing:
    #   For each operation symbol:
    #     1. Create BinaryInstruction
    #     2. Operation setter converts symbol to OperationEnum
    #     3. State is auto-determined from OperationEnum.op_type
    # Expected result: Each shows operation name and state
    # Console output: List of all 10 operations with their states
    print("3. All Supported Operations:")
    print()
    
    print("   Arithmetic operations:")
    for op in ['+', '-', '*', '/']:
        instr = BinaryInstruction(
            operand_1=num1,
            operand_2=num2,
            operation=op)
        print(f"   {op}: {instr.operation.name} -> {instr.state.value}")
    
    print()
    print("   Comparison operations:")
    for op in ['<', '<=', '>', '>=', '==', '!=']:
        instr = BinaryInstruction(
            operand_1=num1,
            operand_2=num2,
            operation=op)
        print(f"   {op}: {instr.operation.name} -> {instr.state.value}")
    # --8<-- [end:all_operations]
    print()


def inst04_repr_indent() -> None:
    """BinaryInstruction: Representation indentation.
    
    Key: inst04
    Run: python examples/example.py inst04
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:repr_indent]
    # Demonstrate __repr_indent__ method
    # Input: Instructions with different operator lengths
    # Processing:
    #   __repr_indent__() calculates: len(operation.symbol) + 1
    #   Single-char '+': len('+') + 1 = 2
    #   Double-char '>=': len('>=') + 1 = 3
    # Expected results: 2 for '+', 3 for '>='
    # Console output:
    #   Single char op (+):  indent = 2
    #   Double char op (>=): indent = 3
    print("4. Representation Indentation:")
    single_char_op = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    double_char_op = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='>=')
    
    print(f"   Single char op (+):  indent = {single_char_op.__repr_indent__()}")
    print(f"   Double char op (>=): indent = {double_char_op.__repr_indent__()}")
    # --8<-- [end:repr_indent]
    print()


def inst05_error_handling() -> None:
    """BinaryInstruction: Error handling.
    
    Key: inst05
    Run: python examples/example.py inst05
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:error_handling]
    # Error handling demonstrations
    # Two common error scenarios
    # Expected: Both raise appropriate exceptions
    # Console output: Error messages showing validation works
    print("5. Error Handling:")
    
    # Invalid operation symbol
    # Input: Unsupported operation '%'
    # Processing:
    #   1. operation setter calls OperationEnum.from_symbol('%')
    #   2. from_symbol() doesn't find '%' in valid operations
    #   3. Raises ValueError
    # Expected: ValueError with message about unsupported operation
    print("   Invalid operation symbol:")
    try:
        bad_instr = BinaryInstruction(
            operand_1=num1,
            operand_2=num2,
            operation='%')
    except ValueError as e:
        print(f"   [OK] {e}")
    
    print()
    # Invalid operand type
    # Input: String "1010" instead of BinaryNumber object
    # Processing:
    #   1. operand_1 setter checks isinstance(value, BinaryNumber)
    #   2. Check fails (it's a str)
    #   3. Raises TypeError
    # Expected: TypeError with message about type mismatch
    print("   Invalid operand type:")
    try:
        bad_instr = BinaryInstruction(
            operand_1="1010",  # String instead of BinaryNumber
            operand_2=num2,
            operation='+')
    except TypeError as e:
        print(f"   [OK] {e}")
    # --8<-- [end:error_handling]
    print()


def inst06_larger_numbers() -> None:
    """BinaryInstruction: Instructions with larger numbers.
    
    Key: inst06
    Run: python examples/example.py inst06
    """
    print("=" * 70)
    print("Example 02: BinaryInstruction Operations")
    print("=" * 70)
    print()
    
    # --8<-- [start:larger_numbers]
    # Working with larger numbers
    print("6. Instructions with Larger Numbers:")
    
    # Large arithmetic operation
    num_large1 = BinaryNumber.from_int(decimal_num=524288)  # 512 KB
    num_large2 = BinaryNumber.from_int(decimal_num=786432)  # 768 KB
    
    large_instr = BinaryInstruction(
        operand_1=num_large1,
        operand_2=num_large2,
        operation='+')
    
    print(f"   Operand 1: {num_large1.value}")
    print(f"              ({num_large1.to_int():,} = "
          f"{num_large1.to_int() // 1024} KB)")
    print(f"              ({len(num_large1.value)} bits)")
    print()
    print(f"   Operand 2: {num_large2.value}")
    print(f"              ({num_large2.to_int():,} = "
          f"{num_large2.to_int() // 1024} KB)")
    print(f"              ({len(num_large2.value)} bits)")
    print()
    print("   Instruction representation:")
    print(large_instr)
    print()
    
    # Large comparison
    throughput = BinaryNumber.from_int(decimal_num=1048576)  # 1 Mbps
    threshold = BinaryNumber.from_int(decimal_num=500000)    # 500 Kbps
    
    perf_check = BinaryInstruction(
        operand_1=throughput,
        operand_2=threshold,
        operation='>=')
    
    print(f"   Performance check:")
    print(f"   {throughput.to_int():,} >= {threshold.to_int():,}")
    print(perf_check)
    # --8<-- [end:larger_numbers]
    print()


def main() -> None:
    """Run all BinaryInstruction examples."""
    inst01_create_arithmetic_instruction()
    inst02_create_comparison_instruction()
    inst03_all_operations()
    inst04_repr_indent()
    inst05_error_handling()
    inst06_larger_numbers()
    print("=" * 70)


if __name__ == '__main__':
    main()

