"""Complete system demonstration with all components."""

from binary_calculator import (
    BinaryInstruction,
    InstructionExecutor,
    ArithmeticCalculator,
    BinaryConverter,
    BinaryComparator,
    BinaryNormalizer,
    OperationType)


def main() -> None:
    """Demonstrate complete binary calculator system."""
    print("=" * 70)
    print("COMPLETE BINARY CALCULATOR SYSTEM DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Initialize all components
    executor = InstructionExecutor()
    arithmetic = ArithmeticCalculator()
    converter = BinaryConverter()
    comparator = BinaryComparator()
    normalizer = BinaryNormalizer()
    
    # ===== CALCULATION INSTRUCTIONS =====
    print("1. CALCULATION INSTRUCTIONS (state=CALCULATE)")
    print("-" * 70)
    print()
    
    calc_instructions = [
        ('1010', '0101', '+', "10 + 5"),
        ('1111', '0001', '-', "15 - 1"),
        ('101', '11', '*', "5 * 3"),
        ('1010', '10', '/', "10 / 2")]
    
    for op1, op2, operation, desc in calc_instructions:
        instruction = BinaryInstruction(
            operand_1=op1,
            operand_2=op2,
            operation=operation)
        
        result = executor.calculate(instruction=instruction)
        result_decimal = converter.binary_to_decimal(binary_str=result)
        
        print(f"  {desc:>12}")
        print(f"    Instruction state: {instruction.state.value}")
        print(f"    Is calculation?: {instruction.is_calculation()}")
        print(f"    Binary result: {result}")
        print(f"    Decimal result: {result_decimal}")
        print()
    
    # ===== COMPARISON INSTRUCTIONS =====
    print("2. COMPARISON INSTRUCTIONS (state=COMPARE)")
    print("-" * 70)
    print()
    
    comp_instructions = [
        ('10', '101', '<', "2 < 5"),
        ('101', '10', '>', "5 > 2"),
        ('101', '101', '==', "5 == 5"),
        ('101', '110', '!=', "5 != 6"),
        ('10', '101', '<=', "2 <= 5"),
        ('101', '10', '>=', "5 >= 2")]
    
    for op1, op2, operation, desc in comp_instructions:
        instruction = BinaryInstruction(
            operand_1=op1,
            operand_2=op2,
            operation=operation)
        
        result = executor.compare(instruction=instruction)
        
        print(f"  {desc:>12}")
        print(f"    Instruction state: {instruction.state.value}")
        print(f"    Is comparison?: {instruction.is_comparison()}")
        print(f"    Result: {result}")
        print()
    
    # ===== INSTRUCTION STATE CHANGES =====
    print("3. DYNAMIC INSTRUCTION STATE")
    print("-" * 70)
    print()
    
    instruction = BinaryInstruction(
        operand_1='1010',
        operand_2='0101',
        operation='+')
    
    print("  Initial state:")
    print(f"    Operation: {instruction.operation.symbol}")
    print(f"    State: {instruction.state.value}")
    print(f"    Result: {executor.calculate(instruction=instruction)}")
    print()
    
    # Change to comparison
    instruction.operation = '<'
    print("  After changing to '<':")
    print(f"    Operation: {instruction.operation.symbol}")
    print(f"    State: {instruction.state.value}")
    print(f"    Result: {executor.compare(instruction=instruction)}")
    print()
    
    # ===== ERROR HANDLING =====
    print("4. ERROR HANDLING - Wrong Method for Instruction Type")
    print("-" * 70)
    print()
    
    calc_instruction = BinaryInstruction(
        operand_1='1010',
        operand_2='0101',
        operation='+')
    
    print("  Trying to compare() a calculation instruction:")
    try:
        executor.compare(instruction=calc_instruction)
    except ValueError as e:
        print(f"    ERROR: {e}")
    print()
    
    comp_instruction = BinaryInstruction(
        operand_1='10',
        operand_2='101',
        operation='<')
    
    print("  Trying to calculate() a comparison instruction:")
    try:
        executor.calculate(instruction=comp_instruction)
    except ValueError as e:
        print(f"    ERROR: {e}")
    print()
    
    # ===== DIRECT COMPONENT USAGE =====
    print("5. DIRECT COMPONENT USAGE")
    print("-" * 70)
    print()
    
    print("  ArithmeticCalculator (direct arithmetic):")
    result = arithmetic.add(operand_1='1010', operand_2='0101')
    print(f"    1010 + 0101 = {result}")
    print()
    
    print("  BinaryComparator (direct comparison):")
    is_larger = comparator.larger(binary_1='101', binary_2='10')
    print(f"    Is 101 > 10? {is_larger}")
    print()
    
    print("  BinaryConverter (format conversion):")
    decimal = converter.binary_to_decimal(binary_str='1111')
    binary = converter.decimal_to_binary(decimal_num=15)
    print(f"    '1111' to decimal: {decimal}")
    print(f"    15 to binary: '{binary}'")
    print()
    
    print("  BinaryNormalizer (string utilities):")
    b1, b2 = normalizer.normalize_length(binary_1='11', binary_2='1111')
    clean = normalizer.remove_leading_zeros(binary_str='00101')
    print(f"    Normalize '11' and '1111': ('{b1}', '{b2}')")
    print(f"    Remove leading zeros from '00101': '{clean}'")
    print()
    
    # ===== COMPLETE WORKFLOW =====
    print("6. COMPLETE WORKFLOW EXAMPLE")
    print("-" * 70)
    print()
    
    # User input
    user_input_1 = "1010"
    user_input_2 = "0101"
    
    # Create and execute calculation
    calc_inst = BinaryInstruction(
        operand_1=user_input_1,
        operand_2=user_input_2,
        operation='+')
    
    calc_result = executor.calculate(instruction=calc_inst)
    print(f"  Calculation: {user_input_1} + {user_input_2} = {calc_result}")
    print(f"    (decimal: {converter.binary_to_decimal(binary_str=calc_result)})")
    print()
    
    # Create and execute comparison
    comp_inst = BinaryInstruction(
        operand_1=calc_result,
        operand_2='10000',
        operation='<')
    
    comp_result = executor.compare(instruction=comp_inst)
    print(f"  Comparison: {calc_result} < 10000 = {comp_result}")
    print()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("The Binary Calculator system includes:")
    print("  - BinaryInstruction - Encapsulated instructions with enum operations")
    print("  - InstructionExecutor - Execute calculate() or compare()")
    print("  - ArithmeticCalculator - Pure binary arithmetic")
    print("  - BinaryComparator - Binary string comparisons")
    print("  - BinaryConverter - Binary <-> Decimal conversion")
    print("  - BinaryNormalizer - String utilities")
    print()
    print("All components work together seamlessly!")
    print("=" * 70)


if __name__ == '__main__':
    main()

