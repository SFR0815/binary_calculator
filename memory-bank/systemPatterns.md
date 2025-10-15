# System Patterns: Binary Calculator

## Architecture Overview

### Layer Structure
```
┌─────────────────────────────────────┐
│     User Interface Layer            │
│  (CLI Runner, Example Functions)    │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│     Execution Layer                 │
│  (InstructionExecutor)              │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│     Operation Layer                 │
│  (Calculator, Comparator)           │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│     Core Layer                      │
│  (BinaryNumber, BinaryInstruction)  │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│     Utility Layer                   │
│  (Converter, Normalizer)            │
└─────────────────────────────────────┘
```

## Key Design Patterns

### 1. Encapsulation Pattern (BinaryNumber)
**Purpose**: Wrap binary strings with validation and operations
**Implementation**:
```python
class BinaryNumber:
    def __init__(self, *, binary_str: str) -> None:
        self._validate_binary_string(binary_str)
        self._value: str = binary_str
    
    @property
    def value(self) -> str:
        return self._value
```
**Benefits**: Type safety, validation, clean API

### 2. Strategy Pattern (ArithmeticCalculator)
**Purpose**: Encapsulate different arithmetic algorithms
**Implementation**: Separate methods for add, subtract, multiply, divide
**Benefits**: Each algorithm isolated, easy to test and modify

### 3. Command Pattern (BinaryInstruction + InstructionExecutor)
**Purpose**: Encapsulate operations as objects
**Implementation**:
```python
instruction = BinaryInstruction(operand_1=num1, operand_2=num2, operation='+')
result = executor.calculate(instruction=instruction)
```
**Benefits**: Deferred execution, formatted output, operation history potential

### 4. Factory Method Pattern (BinaryNumber.from_int)
**Purpose**: Alternative constructors for different input types
**Implementation**:
```python
@classmethod
def from_int(cls, *, decimal_num: int) -> 'BinaryNumber':
    binary_str = bin(decimal_num)[2:]
    return cls(binary_str=binary_str)
```
**Benefits**: Multiple creation paths, clear intent

### 5. Facade Pattern (InstructionExecutor)
**Purpose**: Simplified interface to complex subsystems
**Implementation**: Executor routes to appropriate calculator/comparator
**Benefits**: Simple API, centralized control, formatted output

## Component Relationships

### BinaryNumber ← ArithmeticCalculator
- Calculator accepts BinaryNumber objects
- Returns new BinaryNumber results
- Pure functions (no state modification)

### BinaryInstruction → InstructionExecutor
- Instruction holds operands + operation
- Executor dispatches to correct handler
- State-based routing (CALCULATE vs COMPARE)

### BinaryNormalizer ↔ All Operations
- Used internally by calculator and comparator
- Removes leading zeros
- Equalizes operand lengths

## Algorithm Patterns

### Addition (Carry Propagation)
```
Process right to left:
  bit_sum = bit1 + bit2 + carry
  result_bit = sum % 2
  carry = sum // 2
```

### Multiplication (Shift-and-Add)
```
For each bit in multiplier:
  If bit == 1:
    Add shifted multiplicand to result
  Shift multiplicand left
```

### Division (Long Division)
```
For each bit in dividend:
  Bring down bit
  If remainder >= divisor:
    Subtract, append '1' to quotient
  Else:
    Append '0' to quotient
```

## Error Handling Patterns

### Validation at Boundaries
- BinaryNumber validates on construction
- BinaryInstruction validates operand types
- Calculator checks for negative results, division by zero

### Informative Exceptions
```python
raise ValueError(f"Cannot subtract: result would be negative ({op1} - {op2})")
raise ZeroDivisionError("Cannot divide by zero")
raise TypeError(f"operand_1 must be a BinaryNumber instance, got {type(value)}")
```

## Testing Patterns

### Test Class Structure
```python
class TestComponentName(unittest.TestCase):
    def test_01_basic_operation(self) -> None:
        # Setup
        # Execute
        # Assert
        pass
```

### Numbered Test Methods
- Format: `test_##_descriptive_name`
- Ensures consistent execution order
- Makes test identification easier

## Documentation Patterns

### Snippet Markers
```python
# --8<-- [start:operation_name]
# Code here
# --8<-- [end:operation_name]
```
Used with pymdownx.snippets to reference code in docs

### Example Structure
Each example function:
- Prints component header
- Shows section title
- Demonstrates specific feature
- Includes comments explaining processing
- Maintains snippet markers

## CLI Pattern

### Registry-Based Dispatch
```python
EXAMPLES = {
    'numb01': (func, description),
    'calc03': (func, description),
    ...
}
```
Allows dynamic discovery and execution

