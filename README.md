# Binary Calculator

A professional-grade Python calculator for performing arithmetic operations on binary numbers represented as strings of zeros and ones.

## Features

- **Pure Binary Arithmetic**: True binary operations on string patterns—NO decimal conversion! ✨
- **Binary Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (*), and Division (/)
  - Addition: Bit-by-bit with carry propagation
  - Subtraction: Bit-by-bit with borrow handling
  - Multiplication: Shift-and-add algorithm
  - Division: Binary long division
- **Instruction-Based Interface**: Use `BinaryInstruction` objects to encapsulate operations
- **Full Encapsulation**: Properties with validated getters and setters
- **Modular Architecture**: One class per module, organized in subdirectories
- **String-Based Binary Representation**: Work with binary numbers as intuitive string representations
- **Bidirectional Conversion**: Binary ↔ Decimal conversion utilities (for convenience)
- **Input Validation**: Automatic validation of binary strings and operations
- **Comprehensive Error Handling**: Clear error messages for invalid inputs
- **Extensive Testing**: 129 comprehensive tests covering all functionality

## Installation

No external dependencies required. Simply clone the repository:

```bash
git clone <repository-url>
cd binary_cals
```

## Usage

### Basic Usage

```python
from binary_calculator import BinaryCalculator, BinaryInstruction

# Create calculator instance
calculator = BinaryCalculator()

# Create an instruction
instruction = BinaryInstruction(
    operand_1='1010',  # Binary for 10
    operand_2='0101',  # Binary for 5
    operation='+')

# Execute the instruction
result = calculator.execute(instruction=instruction)
print(result)  # Output: '1111' (Binary for 15)
```

### Direct Operations

```python
from binary_calculator import BinaryCalculator

calculator = BinaryCalculator()

# Addition
result = calculator.add(operand_1='1010', operand_2='0101')
print(f"1010 + 0101 = {result}")  # Output: 1111

# Subtraction
result = calculator.subtract(operand_1='1010', operand_2='0101')
print(f"1010 - 0101 = {result}")  # Output: 101

# Multiplication
result = calculator.multiply(operand_1='101', operand_2='11')
print(f"101 * 11 = {result}")  # Output: 1111

# Division (integer division)
result = calculator.divide(operand_1='1010', operand_2='10')
print(f"1010 / 10 = {result}")  # Output: 101
```

### Conversion Utilities

```python
from binary_calculator import BinaryCalculator

calculator = BinaryCalculator()

# Convert binary to decimal
decimal = calculator.binary_to_decimal(binary_str='1010')
print(decimal)  # Output: 10

# Convert decimal to binary
binary = calculator.decimal_to_binary(decimal_num=10)
print(binary)  # Output: 1010
```

## API Reference

### BinaryInstruction

An instruction object that contains two binary operands and an operation type.

**Constructor Parameters:**
- `operand_1` (str): First binary number as string (keyword-only)
- `operand_2` (str): Second binary number as string (keyword-only)
- `operation` (str): Operation type (+, -, *, /) (keyword-only)

**Raises:**
- `ValueError`: If operands are not valid binary strings or operation is not supported

### BinaryCalculator

Calculator class for performing arithmetic operations on binary strings.

**Methods:**

#### `add(*, operand_1: str, operand_2: str) -> str`
Add two binary numbers.

#### `subtract(*, operand_1: str, operand_2: str) -> str`
Subtract second binary number from first.

#### `multiply(*, operand_1: str, operand_2: str) -> str`
Multiply two binary numbers.

#### `divide(*, operand_1: str, operand_2: str) -> str`
Divide first binary number by second (integer division).
Raises `ZeroDivisionError` if operand_2 is zero.

#### `execute(*, instruction: BinaryInstruction) -> str`
Execute a binary instruction and return the result.

#### `binary_to_decimal(*, binary_str: str) -> int`
Convert binary string to decimal integer.

#### `decimal_to_binary(*, decimal_num: int) -> str`
Convert decimal integer to binary string.

## Examples

### Addition Example
```python
instruction = BinaryInstruction(
    operand_1='1111',  # 15 in decimal
    operand_2='1',     # 1 in decimal
    operation='+')

result = calculator.execute(instruction=instruction)
# Result: '10000' (16 in decimal)
```

### Division Example
```python
instruction = BinaryInstruction(
    operand_1='1010',  # 10 in decimal
    operand_2='11',    # 3 in decimal
    operation='/')

result = calculator.execute(instruction=instruction)
# Result: '11' (3 in decimal, integer division)
```

## Running Tests

The project includes **four comprehensive test suites with 129 tests**:

### Basic Calculator Tests (27 tests)
Tests all calculator operations, instruction handling, and basic conversions:

```bash
python test_binary_calculator.py -v
```

### Comprehensive Conversion Tests (48 tests)
Extensive in-depth testing of binary-decimal conversions:

```bash
python test_conversions.py -v
```

### Property Encapsulation Tests (20 tests)
Tests for property getters/setters and validation:

```bash
python test_instruction_properties.py -v
```

### Advanced Instruction Tests (34 tests)
Advanced encapsulation, edge cases, integration, and validation tests:

```bash
python test_instruction_advanced.py -v
```

### Run All Tests (129 total tests)
Run the complete test suite:

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

The comprehensive test suite includes:
- **Encapsulation Testing**: Property access, validation, atomicity
- **Edge Cases**: Zero handling, leading zeros, empty inputs, special characters
- **Boundary Testing**: 8-bit, 16-bit, 32-bit, and 64-bit boundaries
- **Sequential Testing**: All values 0-1000, boundary ranges
- **Pattern Testing**: Alternating bits, walking ones/zeros
- **Large Number Testing**: Up to 2^1000 and beyond
- **Mathematical Sequences**: Fibonacci, Mersenne numbers, primes
- **Random Testing**: 200+ random values across bit ranges
- **Round-Trip Testing**: Verify conversions are reversible
- **Stress Testing**: Very large numbers (100+ decimal digits)
- **Integration Testing**: Instruction reuse, chaining, calculator interaction
- **Validation Testing**: Comprehensive input validation and error handling

## Error Handling

The calculator includes comprehensive error handling:

- **Invalid Binary Strings**: Strings containing characters other than '0' and '1' raise `ValueError`
- **Empty Strings**: Empty operands raise `ValueError`
- **Invalid Operations**: Operations other than +, -, *, / raise `ValueError`
- **Division by Zero**: Attempting to divide by '0' raises `ZeroDivisionError`

## Technical Details

- **Pure Binary Operations**: All arithmetic operations work directly on binary string patterns without converting to decimal
  - Addition uses carry propagation
  - Subtraction uses borrow handling
  - Multiplication uses shift-and-add algorithm
  - Division uses binary long division algorithm
- **Division Behavior**: Division performs integer division (floor division)
- **Negative Results**: Negative results are represented with a '-' prefix (e.g., '-101')
- **No Leading Zeros**: Results do not include unnecessary leading zeros (except for zero itself)
- **Conversion Functions**: `binary_to_decimal()` and `decimal_to_binary()` are provided for convenience but are NOT used internally for arithmetic

## Requirements

- Python 3.10 or higher
- No external dependencies (uses standard library only)

## License

This project is provided as-is for educational and practical use.

