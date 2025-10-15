# Binary Calculator Architecture

## Project Structure

```
binary_cals/
├── binary_calculator/                    # Main package
│   ├── __init__.py                      # Package exports
│   ├── instruction/                     # Instruction module
│   │   ├── __init__.py
│   │   └── binary_instruction.py        # BinaryInstruction class
│   └── calculator/                      # Calculator module
│       ├── __init__.py
│       └── binary_calculator.py         # BinaryCalculator class
├── test_binary_calculator.py            # 27 basic tests
├── test_conversions.py                  # 48 conversion tests
├── test_instruction_properties.py       # 20 property tests
├── test_instruction_advanced.py         # 34 advanced tests
├── example.py                           # Usage examples
├── example_conversions.py               # Conversion examples
├── requirements.txt                     # Dependencies (none)
├── README.md                            # Documentation
├── ARCHITECTURE.md                      # This file
└── TEST_COVERAGE.md                     # Test coverage details
```

## Design Principles

### 1. Separation of Concerns

Each class has a single, well-defined responsibility:

- **`BinaryInstruction`**: Encapsulates binary operands and operations with validation
- **`BinaryCalculator`**: Performs arithmetic operations and conversions

### 2. Encapsulation

The `BinaryInstruction` class uses proper encapsulation:

```python
class BinaryInstruction:
    def __init__(self, *, operand_1: str, operand_2: str, operation: str):
        # Uses property setters for validation
        self.operand_1 = operand_1  # Calls @operand_1.setter
        self.operand_2 = operand_2  # Calls @operand_2.setter
        self.operation = operation  # Calls @operation.setter
    
    @property
    def operand_1(self) -> str:
        return self._operand_1  # Private attribute
    
    @operand_1.setter
    def operand_1(self, value: str) -> None:
        self._validate_binary_string(binary_str=value)  # Validation
        self._operand_1 = value
```

**Benefits:**
- Controlled access to internal state
- Automatic validation on every change
- Prevents invalid state
- Clean public API

### 3. One Class Per Module

Each class lives in its own file within an organized package structure:

```
binary_calculator/
├── instruction/
│   └── binary_instruction.py    # BinaryInstruction class only
└── calculator/
    └── binary_calculator.py     # BinaryCalculator class only
```

**Benefits:**
- Easy to locate specific functionality
- Reduces merge conflicts
- Improves code organization
- Follows single responsibility principle

### 4. Type Safety

All functions and methods have complete type hints:

```python
def binary_to_decimal(*, binary_str: str) -> int:
    """Convert binary string to decimal integer."""
    return int(binary_str, 2)

def decimal_to_binary(*, decimal_num: int) -> str:
    """Convert decimal integer to binary string."""
    if decimal_num >= 0:
        return bin(decimal_num)[2:]
    else:
        return '-' + bin(decimal_num)[3:]
```

### 5. Validation at Boundaries

Input validation occurs at system boundaries:

- Constructor validates initial values
- Property setters validate changes
- Clear error messages guide users

```python
@staticmethod
def _validate_binary_string(*, binary_str: str) -> None:
    if not binary_str:
        raise ValueError("Binary string cannot be empty")
    
    if not all(char in '01' for char in binary_str):
        raise ValueError(
            f"Invalid binary string: '{binary_str}'. "
            f"Must contain only 0 and 1")
```

## Class Responsibilities

### BinaryInstruction

**Purpose**: Encapsulate a binary operation instruction

**Responsibilities:**
- Store two binary operands (as strings)
- Store one operation (+, -, *, /)
- Validate operands and operation
- Provide controlled access via properties
- Prevent invalid state

**Public Interface:**
```python
instruction = BinaryInstruction(
    operand_1='1010',
    operand_2='0101',
    operation='+')

# Property access
value = instruction.operand_1
instruction.operand_1 = '1111'  # Validated

# String representation
print(instruction)  # BinaryInstruction(operand_1='1111', ...)
```

### BinaryCalculator

**Purpose**: Perform arithmetic operations on binary strings using pure binary algorithms

**Responsibilities:**
- Execute binary arithmetic operations directly on binary strings (NO decimal conversion)
- Implement classical binary algorithms:
  - Binary addition with carry
  - Binary subtraction with borrow
  - Binary multiplication (shift-and-add)
  - Binary division (long division)
- Convert between binary and decimal (for convenience only)
- Process BinaryInstruction objects
- Return results as binary strings

**Public Interface:**
```python
calculator = BinaryCalculator()

# Direct operations
result = calculator.add(operand_1='1010', operand_2='0101')

# Instruction execution
result = calculator.execute(instruction=instruction)

# Conversions
decimal = calculator.binary_to_decimal(binary_str='1010')
binary = calculator.decimal_to_binary(decimal_num=10)
```

## Data Flow

```
User Input (Strings)
        ↓
[Validation via Properties]
        ↓
BinaryInstruction Object
        ↓
BinaryCalculator.execute()
        ↓
[Pure Binary Algorithm]
- Addition: Bit-by-bit with carry
- Subtraction: Bit-by-bit with borrow
- Multiplication: Shift-and-add
- Division: Binary long division
        ↓
Result (String)

NO DECIMAL CONVERSION IN ARITHMETIC!
```

## Error Handling Strategy

### Fail Fast

Validation occurs immediately at input boundaries:

1. **Construction Time**: Invalid operands/operations rejected in constructor
2. **Modification Time**: Invalid changes rejected by property setters
3. **Execution Time**: Division by zero detected before operation

### Clear Error Messages

All errors include:
- What went wrong
- What value caused the problem
- What is expected

Example:
```
ValueError: Invalid binary string: '1012'. Must contain only 0 and 1
```

## Testing Strategy

### Test Pyramid

```
        /\
       /34\     Advanced Tests (encapsulation, edge cases, integration)
      /____\
     /  20  \   Property Tests (getters, setters, validation)
    /________\
   /    48    \ Conversion Tests (comprehensive binary-decimal)
  /____________\
 /      27      \ Basic Tests (operations, instructions, errors)
/________________\
```

**Total: 129 Tests**

### Test Categories

1. **Unit Tests**: Individual methods and functions
2. **Integration Tests**: Interaction between classes
3. **Property Tests**: Encapsulation behavior
4. **Edge Case Tests**: Boundary conditions, special inputs
5. **Validation Tests**: Error handling and messages
6. **Stress Tests**: Large numbers, long strings

## Package Import Strategy

### Clean Public API

Users import from the package root:

```python
from binary_calculator import BinaryCalculator, BinaryInstruction
```

### Internal Organization

The `__init__.py` file manages exports:

```python
# binary_calculator/__init__.py
from .instruction import BinaryInstruction
from .calculator import BinaryCalculator

__all__ = ['BinaryInstruction', 'BinaryCalculator']
__version__ = '1.0.0'
```

### Module Independence

Submodules are independent:
- `instruction/` has no dependencies on `calculator/`
- `calculator/` imports `BinaryInstruction` for type hints only (TYPE_CHECKING)

## Design Patterns Used

### 1. Value Object Pattern

`BinaryInstruction` is a value object representing an immutable operation specification (though properties allow controlled mutation).

### 2. Strategy Pattern

Different operations (+, -, *, /) are mapped to methods in `BinaryCalculator`:

```python
operation_map = {
    '+': self.add,
    '-': self.subtract,
    '*': self.multiply,
    '/': self.divide}
```

### 3. Property Pattern

Properties provide controlled access to private attributes with automatic validation.

### 4. Static Method Pattern

Validation and conversion methods are static when they don't need instance state.

## Extension Points

The architecture supports easy extension:

### Adding New Operations

1. Add validation to `BinaryInstruction._validate_operation()`
2. Add method to `BinaryCalculator`
3. Update operation map in `execute()`

### Adding New Instruction Types

Create a new class in `instruction/` following the same pattern:
- Use properties for encapsulation
- Validate in setters
- Provide clear `__repr__`

### Adding New Calculators

Create a new class in `calculator/` that can process instructions.

## Performance Considerations

### String Immutability

Binary strings are immutable, preventing accidental modification and enabling safe sharing.

### Lazy Evaluation

Operations are only performed when `execute()` is called, not when the instruction is created.

### No Premature Optimization

The implementation prioritizes clarity and correctness over performance. Python's built-in `int()` and `bin()` are used for conversions.

## Coding Standards

- **Type Hints**: All parameters and return values have type hints
- **Keyword Arguments**: All methods use keyword-only arguments (`*`)
- **Docstrings**: All public classes and methods have docstrings
- **Validation**: All inputs validated at boundaries
- **Error Messages**: Clear, descriptive error messages
- **Line Length**: Maximum 80 characters per line
- **Import Aliases**: Standard library imports use `p_` prefix

## Future Enhancements

Potential improvements while maintaining architecture:

1. **Bitwise Operations**: AND, OR, XOR, NOT, shifts
2. **Floating Point**: Binary fractions
3. **Multiple Operands**: N-ary operations
4. **Instruction History**: Undo/redo capability
5. **Asynchronous Operations**: For very large numbers
6. **Binary String Optimization**: Custom binary string class

## Conclusion

The binary calculator follows clean architecture principles:

- ✅ Separation of concerns
- ✅ Encapsulation with properties
- ✅ One class per module
- ✅ Type safety
- ✅ Comprehensive validation
- ✅ Extensive testing
- ✅ Clear error handling
- ✅ Easy to extend

This architecture supports long-term maintainability and evolution while keeping the codebase clean and understandable.

