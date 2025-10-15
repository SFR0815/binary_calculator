"""Example usage of the binary calculator with comprehensive comments.

This example demonstrates:
- Creating BinaryNumber objects from strings and integers
- Creating BinaryInstruction objects for arithmetic and comparison operations
- Using InstructionExecutor to execute instructions
- Printing formatted results with the print_result parameter
- Converting between binary and decimal representations
- Error handling for invalid operations
"""

from binary_calculator import (
    BinaryNumber,
    BinaryInstruction,
    InstructionExecutor,
    BinaryConverter)


def main() -> None:
    """Demonstrate comprehensive binary calculator functionality."""
    # =========================================================================
    # SETUP: Create executor and converter instances
    # =========================================================================
    # Input: None (initialization only)
    # Processing: Initialize the InstructionExecutor for executing instructions
    # Console output: None
    # Return value: None (instances stored in local variables)
    executor = InstructionExecutor()
    converter = BinaryConverter()
    
    print("=" * 70)
    print("Binary Calculator Examples - Comprehensive Demonstration")
    print("=" * 70)
    print()
    
    # =========================================================================
    # EXAMPLE 1: Basic Addition with BinaryNumber Objects
    # =========================================================================
    # Input: Two binary strings '11010' (26) and '101' (5)
    # Processing: 
    #   1. Create BinaryNumber objects from binary strings
    #   2. Create BinaryInstruction with '+' operation
    #   3. Execute instruction using executor.calculate()
    #   4. Print formatted result with print_result=True
    # Console output: Formatted calculation display with operands and result
    # Return value: BinaryNumber object containing '11111' (31)
    print("EXAMPLE 1: Basic Addition")
    print("-" * 70)
    
    # Create BinaryNumber objects (encapsulate binary string values)
    num1 = BinaryNumber(binary_str='11010')  # 26 in decimal
    num2 = BinaryNumber(binary_str='101')     # 5 in decimal
    
    # Create instruction (validates operation and stores operands)
    instruction_add = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    
    # Execute and print formatted result
    # The print_result=True parameter triggers console output
    result_add = executor.calculate(
        instruction=instruction_add,
        print_result=True)
    
    # Display decimal equivalent for verification
    decimal_result = converter.binary_to_decimal(binary_str=result_add.value)
    print(f"Decimal equivalent: 26 + 5 = {decimal_result}")
    print()
    
    # =========================================================================
    # EXAMPLE 2: Subtraction with Right-Aligned Display
    # =========================================================================
    # Input: Binary strings '1111' (15) and '101' (5)
    # Processing:
    #   1. Create BinaryNumber objects
    #   2. Create BinaryInstruction with '-' operation
    #   3. Execute with formatted output
    # Console output: Right-aligned operands with separator lines
    # Return value: BinaryNumber object containing '1010' (10)
    print("EXAMPLE 2: Subtraction (demonstrates right-alignment)")
    print("-" * 70)
    
    num3 = BinaryNumber(binary_str='1111')    # 15 in decimal
    num4 = BinaryNumber(binary_str='101')     # 5 in decimal
    
    instruction_sub = BinaryInstruction(
        operand_1=num3,
        operand_2=num4,
        operation='-')
    
    result_sub = executor.calculate(
        instruction=instruction_sub,
        print_result=True)
    
    print(f"Decimal: 15 - 5 = "
          f"{converter.binary_to_decimal(binary_str=result_sub.value)}")
    print()
    
    # =========================================================================
    # EXAMPLE 3: Multiplication with Different Length Operands
    # =========================================================================
    # Input: '1010' (10) and '11' (3)
    # Processing: Binary multiplication using shift-and-add algorithm
    # Console output: Formatted with proper alignment for different lengths
    # Return value: BinaryNumber object containing '11110' (30)
    print("EXAMPLE 3: Multiplication")
    print("-" * 70)
    
    num5 = BinaryNumber(binary_str='1010')    # 10 in decimal
    num6 = BinaryNumber(binary_str='11')      # 3 in decimal
    
    instruction_mul = BinaryInstruction(
        operand_1=num5,
        operand_2=num6,
        operation='*')
    
    result_mul = executor.calculate(
        instruction=instruction_mul,
        print_result=True)
    
    print(f"Decimal: 10 * 3 = "
          f"{converter.binary_to_decimal(binary_str=result_mul.value)}")
    print()
    
    # =========================================================================
    # EXAMPLE 4: Division (Integer Division)
    # =========================================================================
    # Input: '11010' (26) and '101' (5)
    # Processing: Binary long division algorithm
    # Console output: Formatted division display
    # Return value: BinaryNumber object with quotient '101' (5)
    #               Note: Remainder is discarded (integer division)
    print("EXAMPLE 4: Division (integer division)")
    print("-" * 70)
    
    num7 = BinaryNumber(binary_str='11010')   # 26 in decimal
    num8 = BinaryNumber(binary_str='101')     # 5 in decimal
    
    instruction_div = BinaryInstruction(
        operand_1=num7,
        operand_2=num8,
        operation='/')
    
    result_div = executor.calculate(
        instruction=instruction_div,
        print_result=True)
    
    print(f"Decimal: 26 // 5 = "
          f"{converter.binary_to_decimal(binary_str=result_div.value)} "
          f"(remainder discarded)")
    print()
    
    # =========================================================================
    # EXAMPLE 5: Creating BinaryNumber from Integer
    # =========================================================================
    # Input: Integer 42
    # Processing: Use BinaryNumber.from_int() class method to convert
    # Console output: Binary representation display
    # Return value: BinaryNumber object containing '101010'
    print("EXAMPLE 5: Creating BinaryNumber from Integer")
    print("-" * 70)
    
    # Create BinaryNumber from decimal integer using class method
    num_from_int = BinaryNumber.from_int(decimal_num=42)
    print(f"Created from integer 42: {num_from_int.value}")
    print(f"Verification: "
          f"{converter.binary_to_decimal(binary_str=num_from_int.value)}")
    print()
    
    # =========================================================================
    # EXAMPLE 6: Comparison Operations with >= Operator
    # =========================================================================
    # Input: '1010' (10) and '101' (5)
    # Processing:
    #   1. Create comparison instruction with '>=' operation
    #   2. Execute using executor.compare() method
    #   3. Print formatted comparison with boolean result
    # Console output: Formatted comparison display showing True/False
    # Return value: Boolean (True in this case)
    print("EXAMPLE 6: Comparison Operation (>=)")
    print("-" * 70)
    
    num9 = BinaryNumber(binary_str='1010')    # 10 in decimal
    num10 = BinaryNumber(binary_str='101')    # 5 in decimal
    
    instruction_cmp = BinaryInstruction(
        operand_1=num9,
        operand_2=num10,
        operation='>=')
    
    # Note: Use compare() method for comparison operations
    result_cmp = executor.compare(
        instruction=instruction_cmp,
        print_result=True)
    
    print(f"Result: {result_cmp} (10 >= 5)")
    print()
    
    # =========================================================================
    # EXAMPLE 7: Equality Comparison
    # =========================================================================
    # Input: '1010' and '01010' (both represent 10)
    # Processing: Comparison ignores leading zeros
    # Console output: Formatted comparison showing True
    # Return value: Boolean (True - values are equal)
    print("EXAMPLE 7: Equality Comparison (leading zeros ignored)")
    print("-" * 70)
    
    num11 = BinaryNumber(binary_str='1010')   # 10 in decimal
    num12 = BinaryNumber(binary_str='01010')  # Also 10 (leading zero)
    
    instruction_eq = BinaryInstruction(
        operand_1=num11,
        operand_2=num12,
        operation='==')
    
    result_eq = executor.compare(
        instruction=instruction_eq,
        print_result=True)
    
    print(f"Result: {result_eq} (leading zeros are handled correctly)")
    print()
    
    # =========================================================================
    # EXAMPLE 8: All Arithmetic Operations on Same Operands
    # =========================================================================
    # Input: '1100' (12) and '11' (3)
    # Processing: Loop through all arithmetic operations
    # Console output: Four formatted calculations
    # Return value: None (demonstrates iteration over operations)
    print("EXAMPLE 8: All Arithmetic Operations (1100 vs 11)")
    print("-" * 70)
    
    operand_a = BinaryNumber(binary_str='1100')  # 12 in decimal
    operand_b = BinaryNumber(binary_str='11')    # 3 in decimal
    
    print(f"Operands: {operand_a.value} (12) and {operand_b.value} (3)")
    print()
    
    # Iterate through all arithmetic operations
    operations = ['+', '-', '*', '/']
    for op in operations:
        print(f"Operation: {op}")
        instr = BinaryInstruction(
            operand_1=operand_a,
            operand_2=operand_b,
            operation=op)
        
        # Execute and display formatted result
        result = executor.calculate(instruction=instr, print_result=True)
        
        # Show decimal verification
        dec_result = converter.binary_to_decimal(binary_str=result.value)
        print(f"Decimal verification: {dec_result}")
        print()
    
    # =========================================================================
    # EXAMPLE 9: All Comparison Operations
    # =========================================================================
    # Input: '1010' (10) and '101' (5)
    # Processing: Execute all six comparison operators
    # Console output: Six formatted comparisons with boolean results
    # Return value: None (demonstrates all comparison types)
    print("EXAMPLE 9: All Comparison Operations (1010 vs 101)")
    print("-" * 70)
    
    comp_a = BinaryNumber(binary_str='1010')  # 10 in decimal
    comp_b = BinaryNumber(binary_str='101')   # 5 in decimal
    
    print(f"Operands: {comp_a.value} (10) and {comp_b.value} (5)")
    print()
    
    # Iterate through all comparison operations
    comparisons = ['<', '<=', '>', '>=', '==', '!=']
    for cmp_op in comparisons:
        print(f"Comparison: {cmp_op}")
        instr_cmp = BinaryInstruction(
            operand_1=comp_a,
            operand_2=comp_b,
            operation=cmp_op)
        
        # Execute and display formatted result
        result_bool = executor.compare(
            instruction=instr_cmp,
            print_result=True)
        
        print(f"Result: {result_bool}")
        print()
    
    # =========================================================================
    # EXAMPLE 10: BinaryNumber Operations (incr, decr, copy)
    # =========================================================================
    # Input: BinaryNumber with value '1010' (10)
    # Processing: Demonstrate increment, decrement, and copy operations
    # Console output: Values at each step
    # Return value: None (demonstrates BinaryNumber methods)
    print("EXAMPLE 10: BinaryNumber Operations (incr, decr, copy)")
    print("-" * 70)
    
    num_ops = BinaryNumber(binary_str='1010')  # 10 in decimal
    print(f"Initial value: {num_ops.value} ({num_ops.to_int()})")
    
    # Increment by 1 (default)
    num_ops.incr()
    print(f"After incr(): {num_ops.value} ({num_ops.to_int()})")
    
    # Increment by custom amount
    increment = BinaryNumber(binary_str='101')  # 5
    num_ops.incr(increment=increment)
    print(f"After incr(increment='101'): {num_ops.value} "
          f"({num_ops.to_int()})")
    
    # Decrement by 1 (default)
    num_ops.decr()
    print(f"After decr(): {num_ops.value} ({num_ops.to_int()})")
    
    # Create a copy
    num_copy = num_ops.copy()
    print(f"Copy created: {num_copy.value} (independent object)")
    print()
    
    # =========================================================================
    # EXAMPLE 11: Error Handling - Invalid Binary String
    # =========================================================================
    # Input: String '1012' containing invalid character '2'
    # Processing: BinaryNumber validation rejects non-binary characters
    # Console output: Error message from caught exception
    # Return value: None (demonstrates error handling)
    print("EXAMPLE 11: Error Handling - Invalid Binary String")
    print("-" * 70)
    
    print("Attempting to create BinaryNumber with invalid character '2':")
    try:
        invalid_num = BinaryNumber(binary_str='1012')
    except ValueError as e:
        print(f"  [OK] Caught ValueError: {e}")
    print()
    
    # =========================================================================
    # EXAMPLE 12: Error Handling - Division by Zero
    # =========================================================================
    # Input: Valid operands but divisor is '0'
    # Processing: Division operation detects zero divisor
    # Console output: Error message from caught exception
    # Return value: None (demonstrates error handling)
    print("EXAMPLE 12: Error Handling - Division by Zero")
    print("-" * 70)
    
    print("Attempting division by zero:")
    try:
        zero = BinaryNumber(binary_str='0')
        nonzero = BinaryNumber(binary_str='1010')
        div_zero_instr = BinaryInstruction(
            operand_1=nonzero,
            operand_2=zero,
            operation='/')
        result_error = executor.calculate(instruction=div_zero_instr)
    except ZeroDivisionError as e:
        print(f"  [OK] Caught ZeroDivisionError: {e}")
    print()
    
    # =========================================================================
    # EXAMPLE 13: Error Handling - Negative Subtraction Result
    # =========================================================================
    # Input: Smaller value minus larger value (5 - 10)
    # Processing: Subtraction detects result would be negative
    # Console output: Error message from caught exception
    # Return value: None (demonstrates error handling)
    print("EXAMPLE 13: Error Handling - Negative Subtraction Result")
    print("-" * 70)
    
    print("Attempting subtraction that would result in negative:")
    try:
        small = BinaryNumber(binary_str='101')   # 5
        large = BinaryNumber(binary_str='1010')  # 10
        sub_neg_instr = BinaryInstruction(
            operand_1=small,
            operand_2=large,
            operation='-')
        result_neg = executor.calculate(instruction=sub_neg_instr)
    except ValueError as e:
        print(f"  [OK] Caught ValueError: {e}")
    print()
    
    # =========================================================================
    # EXAMPLE 14: Error Handling - Wrong Executor Method
    # =========================================================================
    # Input: Comparison instruction passed to calculate() method
    # Processing: Executor validates instruction type
    # Console output: Error message from caught exception
    # Return value: None (demonstrates type checking)
    print("EXAMPLE 14: Error Handling - Wrong Executor Method")
    print("-" * 70)
    
    print("Attempting to use calculate() with comparison instruction:")
    try:
        cmp_instr_wrong = BinaryInstruction(
            operand_1=BinaryNumber(binary_str='101'),
            operand_2=BinaryNumber(binary_str='11'),
            operation='<')
        # Should use compare(), not calculate()
        wrong_result = executor.calculate(instruction=cmp_instr_wrong)
    except ValueError as e:
        print(f"  [OK] Caught ValueError: {e}")
    print()
    
    # =========================================================================
    # EXAMPLE 15: BinaryNumber Comparison Operators
    # =========================================================================
    # Input: Two BinaryNumber objects
    # Processing: Use Python comparison operators directly on BinaryNumber
    # Console output: Results of using <, <=, >, >=, ==, != operators
    # Return value: None (demonstrates operator overloading)
    print("EXAMPLE 15: Using Python Operators on BinaryNumber Objects")
    print("-" * 70)
    
    num_x = BinaryNumber(binary_str='1010')  # 10
    num_y = BinaryNumber(binary_str='101')   # 5
    
    print(f"num_x = {num_x.value} (10)")
    print(f"num_y = {num_y.value} (5)")
    print()
    print(f"num_x > num_y:  {num_x > num_y}")
    print(f"num_x >= num_y: {num_x >= num_y}")
    print(f"num_x < num_y:  {num_x < num_y}")
    print(f"num_x <= num_y: {num_x <= num_y}")
    print(f"num_x == num_y: {num_x == num_y}")
    print(f"num_x != num_y: {num_x != num_y}")
    print()
    
    # =========================================================================
    # CONCLUSION
    # =========================================================================
    print("=" * 70)
    print("All examples completed successfully!")
    print()
    print("Key Takeaways:")
    print("  1. BinaryNumber encapsulates binary string values")
    print("  2. BinaryInstruction validates and stores operation details")
    print("  3. InstructionExecutor.calculate() for arithmetic operations")
    print("  4. InstructionExecutor.compare() for comparison operations")
    print("  5. print_result=True shows formatted calculation display")
    print("  6. All operations use pure binary algorithms")
    print("  7. Comprehensive error handling for invalid inputs")
    print("=" * 70)


if __name__ == '__main__':
    main()
