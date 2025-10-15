"""Demonstration of pure binary arithmetic (no decimal conversion)."""

from binary_calculator import BinaryCalculator, BinaryInstruction


def demonstrate_binary_addition() -> None:
    """Demonstrate pure binary addition."""
    print("=" * 70)
    print("BINARY ADDITION (No Decimal Conversion)")
    print("=" * 70)
    print()
    print("Algorithm: Bit-by-bit addition with carry")
    print("Rules:")
    print("  0 + 0 = 0 (carry 0)")
    print("  0 + 1 = 1 (carry 0)")
    print("  1 + 0 = 1 (carry 0)")
    print("  1 + 1 = 0 (carry 1)")
    print()
    
    calculator = BinaryCalculator()
    
    examples = [
        ('1010', '0101', "10 + 5"),
        ('1111', '1', "15 + 1"),
        ('11', '11', "3 + 3"),
        ('10101', '1010', "21 + 10")]
    
    for operand_1, operand_2, description in examples:
        result = calculator.add(operand_1=operand_1, operand_2=operand_2)
        print(f"  {operand_1:>8} ({description})")
        print(f"+ {operand_2:>8}")
        print(f"  {'-' * 8}")
        print(f"  {result:>8}")
        print()


def demonstrate_binary_subtraction() -> None:
    """Demonstrate pure binary subtraction."""
    print("=" * 70)
    print("BINARY SUBTRACTION (No Decimal Conversion)")
    print("=" * 70)
    print()
    print("Algorithm: Bit-by-bit subtraction with borrow")
    print("Rules:")
    print("  0 - 0 = 0 (borrow 0)")
    print("  1 - 0 = 1 (borrow 0)")
    print("  1 - 1 = 0 (borrow 0)")
    print("  0 - 1 = 1 (borrow 1)")
    print()
    
    calculator = BinaryCalculator()
    
    examples = [
        ('1010', '0101', "10 - 5"),
        ('1111', '0001', "15 - 1"),
        ('10000', '1', "16 - 1"),
        ('0101', '1010', "5 - 10 (negative)")]
    
    for operand_1, operand_2, description in examples:
        result = calculator.subtract(operand_1=operand_1, operand_2=operand_2)
        print(f"  {operand_1:>8} ({description})")
        print(f"- {operand_2:>8}")
        print(f"  {'-' * 8}")
        print(f"  {result:>8}")
        print()


def demonstrate_binary_multiplication() -> None:
    """Demonstrate pure binary multiplication."""
    print("=" * 70)
    print("BINARY MULTIPLICATION (No Decimal Conversion)")
    print("=" * 70)
    print()
    print("Algorithm: Shift-and-add (like long multiplication)")
    print("Process:")
    print("  1. For each '1' bit in multiplier (right to left)")
    print("  2. Add multiplicand shifted by bit position")
    print("  3. Sum all shifted values")
    print()
    
    calculator = BinaryCalculator()
    
    examples = [
        ('101', '11', "5 * 3"),
        ('1010', '10', "10 * 2"),
        ('11', '11', "3 * 3"),
        ('1111', '10', "15 * 2")]
    
    for operand_1, operand_2, description in examples:
        result = calculator.multiply(operand_1=operand_1, operand_2=operand_2)
        print(f"  {operand_1:>8} ({description})")
        print(f"* {operand_2:>8}")
        print(f"  {'-' * 8}")
        print(f"  {result:>8}")
        print()


def demonstrate_binary_division() -> None:
    """Demonstrate pure binary division."""
    print("=" * 70)
    print("BINARY DIVISION (No Decimal Conversion)")
    print("=" * 70)
    print()
    print("Algorithm: Binary long division")
    print("Process:")
    print("  1. Process dividend bits left to right")
    print("  2. If current remainder >= divisor:")
    print("     - Subtract divisor, add '1' to quotient")
    print("  3. Otherwise add '0' to quotient")
    print()
    
    calculator = BinaryCalculator()
    
    examples = [
        ('1010', '10', "10 / 2"),
        ('1111', '11', "15 / 3"),
        ('10100', '101', "20 / 5"),
        ('1010', '11', "10 / 3 (integer division)")]
    
    for operand_1, operand_2, description in examples:
        result = calculator.divide(operand_1=operand_1, operand_2=operand_2)
        print(f"  {operand_1:>8} ({description})")
        print(f"/ {operand_2:>8}")
        print(f"  {'-' * 8}")
        print(f"  {result:>8}")
        print()


def demonstrate_step_by_step_addition() -> None:
    """Show step-by-step binary addition."""
    print("=" * 70)
    print("STEP-BY-STEP BINARY ADDITION: 1011 + 0110")
    print("=" * 70)
    print()
    print("Working from right to left:")
    print()
    print("Position:   3   2   1   0")
    print("Operand 1:  1   0   1   1")
    print("Operand 2:  0   1   1   0")
    print("           ---------------")
    print()
    print("Step 1 (pos 0): 1 + 0 + carry(0) = 1, new carry = 0")
    print("Step 2 (pos 1): 1 + 1 + carry(0) = 0, new carry = 1")
    print("Step 3 (pos 2): 0 + 1 + carry(1) = 0, new carry = 1")
    print("Step 4 (pos 3): 1 + 0 + carry(1) = 0, new carry = 1")
    print("Final carry:    1")
    print()
    print("Result:    1   0   0   0   1  =  10001")
    print()
    
    calculator = BinaryCalculator()
    result = calculator.add(operand_1='1011', operand_2='0110')
    print(f"Verified: {result}")
    print()


def main() -> None:
    """Run all demonstrations."""
    demonstrate_binary_addition()
    demonstrate_binary_subtraction()
    demonstrate_binary_multiplication()
    demonstrate_binary_division()
    demonstrate_step_by_step_addition()
    
    print("=" * 70)
    print("KEY POINT: No Conversion to Decimal!")
    print("=" * 70)
    print()
    print("All operations work directly on the binary string patterns.")
    print("The calculator manipulates 0s and 1s following binary arithmetic rules.")
    print("No intermediate decimal representation is used.")
    print()
    print("This demonstrates true binary computation!")
    print("=" * 70)


if __name__ == '__main__':
    main()

