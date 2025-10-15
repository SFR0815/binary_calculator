# Example 02: BinaryInstruction - Instruction Validation and Formatting

## Overview

This example demonstrates the `BinaryInstruction` class, which encapsulates operands and operations with automatic validation and state management.

**Key Features:**
- Validates operands are BinaryNumber instances
- Converts operation symbols to enums
- Automatically determines state (CALCULATE vs COMPARE)
- Provides formatted two-line representation

## Executable Code

**File:** `examples/basic/example_02_binary_instruction.py`

**Run it:**
```bash
python examples/basic/example_02_binary_instruction.py
```

---

## Example 1: Creating an Arithmetic Instruction

**Run this example:**
```bash
python example.py inst01
```

### Code

```python title="Create arithmetic instruction"
--8<-- "examples/basic/example_02_binary_instruction.py:create_instruction"
```

### What This Does

Creates a `BinaryInstruction` for an addition operation.

### Input

- **Operand 1:** `BinaryNumber('1010')` - decimal 10
- **Operand 2:** `BinaryNumber('101')` - decimal 5
- **Operation:** `'+'` - addition symbol

### Processing Steps

1. **Operand 1 setter:**
   - Checks `isinstance(value, BinaryNumber)`
   - If not, raises `TypeError`
   - Stores as `self._operand_1`

2. **Operand 2 setter:**
   - Same validation as operand 1
   - Stores as `self._operand_2`

3. **Operation setter:**
   - Calls `OperationEnum.from_symbol(symbol='+')`
   - Looks up '+' in operation mapping
   - Finds `OperationEnum.ADD`
   - Stores enum (not string)

4. **State auto-determination:**
   - Accessed via `self._operation.op_type`
   - `OperationEnum.ADD` has `op_type=OperationType.CALCULATE`
   - State automatically set to CALCULATE

### Expected Console Output

```
   1010
+   101
Operation: +
State: calculate
Is calculation: True
Is comparison: False
```

### Return Value

- **Type:** `BinaryInstruction` object
- **Operands:** Stored as BinaryNumber objects
- **Operation:** `OperationEnum.ADD`
- **State:** `OperationType.CALCULATE`

---

## Example 2: Comparison Instructions

**Run this example:**
```bash
python example.py inst02
```

### Code

```python title="Create comparison instruction"
--8<-- "examples/basic/example_02_binary_instruction.py:comparison_instruction"
```

```python title="Display comparison"
--8<-- "examples/basic/example_02_binary_instruction.py:display_comparison"
```

### What This Does

Creates and displays a comparison instruction with the `>=` operator.

### Representation Details

#### Indent Calculation

The `__repr_indent__()` method calculates:
```
len(operation.symbol) + 1
```

For `'>='`:
```
len('>=') + 1 = 2 + 1 = 3 spaces
```

#### Right-Alignment

Both operands are right-aligned to the maximum length:
```
max_width = max(len('11010'), len('101')) = 5

'11010'.rjust(5) = '11010'
'101'.rjust(5) = '  101'

Result:
   11010
>=   101
```

### Expected Console Output

```
   11010
>=   101
Operation: >=
State: compare
Is calculation: False
Is comparison: True
```

---

## Example 3: All Supported Operations

**Run this example:**
```bash
python example.py inst03
```

### Code

```python title="All operations"
--8<-- "examples/basic/example_02_binary_instruction.py:all_operations"
```

### What This Does

Demonstrates all 10 supported operations and their automatic state assignment.

### Operation Mapping

| Symbol | Enum Name | State |
|--------|-----------|-------|
| `+` | ADD | calculate |
| `-` | SUBTRACT | calculate |
| `*` | MULTIPLY | calculate |
| `/` | DIVIDE | calculate |
| `<` | SMALLER | compare |
| `<=` | SMALLER_EQUAL | compare |
| `>` | LARGER | compare |
| `>=` | LARGER_EQUAL | compare |
| `==` | EQUAL | compare |
| `!=` | NOT_EQUAL | compare |

### Expected Console Output

```
Arithmetic operations:
   +: ADD -> calculate
   -: SUBTRACT -> calculate
   *: MULTIPLY -> calculate
   /: DIVIDE -> calculate

Comparison operations:
   <: SMALLER -> compare
   <=: SMALLER_EQUAL -> compare
   >: LARGER -> compare
   >=: LARGER_EQUAL -> compare
   ==: EQUAL -> compare
   !=: NOT_EQUAL -> compare
```

---

## Example 4: Representation Indentation

**Run this example:**
```bash
python example.py inst04
```

### Code

```python title="Indent calculation"
--8<-- "examples/basic/example_02_binary_instruction.py:repr_indent"
```

### What This Does

Shows how indentation adapts to operator length.

### Processing

```python
def __repr_indent__(self) -> int:
    return len(self.operation.symbol) + 1
```

**Examples:**
- `'+'` → `len('+') + 1` = 2
- `'>='` → `len('>=') + 1` = 3

This ensures proper alignment regardless of operator length.

### Expected Console Output

```
Single char op (+):  indent = 2
Double char op (>=): indent = 3
```

---

## Example 5: Error Handling

**Run this example:**
```bash
python example.py inst05
```

### Code

```python title="Error handling"
--8<-- "examples/basic/example_02_binary_instruction.py:error_handling"
```

### What This Does

Demonstrates validation for invalid inputs.

### Validation Errors

#### Invalid Operation Symbol

**Input:** `'%'` (modulo - not supported)

**Processing:**
1. Operation setter calls `OperationEnum.from_symbol('%')`
2. Symbol not in valid operations dictionary
3. Raises `ValueError`

**Error Message:**
```
Unsupported operation: '%'
```

#### Invalid Operand Type

**Input:** String `"1010"` instead of `BinaryNumber`

**Processing:**
1. Operand setter checks `isinstance(value, BinaryNumber)`
2. Check fails (it's a `str`)
3. Raises `TypeError`

**Error Message:**
```
operand_1 must be a BinaryNumber instance, got str
```

### Expected Console Output

```
Invalid operation symbol:
   [OK] Unsupported operation: '%'

Invalid operand type:
   [OK] operand_1 must be a BinaryNumber instance, got str
```

---

## Example 6: Larger Numbers

**Run this example:**
```bash
python example.py inst06
```

### Code

```python title="Large number instructions"
--8<-- "examples/basic/example_02_binary_instruction.py:larger_numbers"
```

### What This Does

Creates instructions with realistic, larger numbers representing file sizes and performance metrics.

### Real-World Scenarios

#### File Storage Addition

**Numbers:**
- File 1: 524,288 bytes (512 KB = 2^19)
- File 2: 786,432 bytes (768 KB = 3 × 2^18)

**Binary Representations:**
```
524,288 = 10000000000000000000  (20 bits)
786,432 = 11000000000000000000  (20 bits)
```

#### Performance Threshold Check

**Numbers:**
- Throughput: 1,048,576 bps (1 Mbps = 2^20)
- Threshold: 500,000 bps

**Binary Representations:**
```
1,048,576 = 100000000000000000000  (21 bits)
  500,000 = 1111010000100100000     (19 bits)
```

### Expected Console Output

```
Operand 1: 10000000000000000000
           (524,288 = 512 KB)
           (20 bits)

Operand 2: 11000000000000000000
           (786,432 = 768 KB)
           (20 bits)

Instruction representation:
   10000000000000000000
+  11000000000000000000

Performance check:
1,048,576 >= 500,000
    100000000000000000000
>=   1111010000100100000
```

---

## Complete Example Output

```
======================================================================
Example 02: BinaryInstruction Operations
======================================================================

1. Arithmetic Instruction:
   1010
+   101
   Operation: +
   State: calculate
   Is calculation: True
   Is comparison: False

2. Comparison Instruction:
   11010
>=   101
   Operation: >=
   State: compare
   Is calculation: False
   Is comparison: True

3. All Supported Operations:

   Arithmetic operations:
   +: ADD -> calculate
   -: SUBTRACT -> calculate
   *: MULTIPLY -> calculate
   /: DIVIDE -> calculate

   Comparison operations:
   <: SMALLER -> compare
   <=: SMALLER_EQUAL -> compare
   >: LARGER -> compare
   >=: LARGER_EQUAL -> compare
   ==: EQUAL -> compare
   !=: NOT_EQUAL -> compare

4. Representation Indentation:
   Single char op (+):  indent = 2
   Double char op (>=): indent = 3

5. Error Handling:
   Invalid operation symbol:
   [OK] Unsupported operation: '%'

   Invalid operand type:
   [OK] operand_1 must be a BinaryNumber instance, got str

6. Instructions with Larger Numbers:
   [... large number output ...]
======================================================================
```

---

## Algorithm Complexity

| Operation | Time | Space |
|-----------|------|-------|
| `__init__` | O(1) | O(1) |
| Property access | O(1) | O(1) |
| `__repr__` | O(n) | O(n) |
| `__repr_indent__` | O(1) | O(1) |

Where n = max length of operand binary strings

---

## Key Takeaways

1. **Type Safety:** Enforces BinaryNumber operands at creation
2. **Automatic State:** State determined from operation type
3. **Clean Representation:** Two-line format with proper alignment
4. **Adaptive Indentation:** Handles different operator lengths
5. **Early Validation:** Catches errors before execution

---

## Next Steps

- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - Perform calculations
- [Example 07: InstructionExecutor](example_07_instruction_executor.md) - Execute instructions
- [Basic Examples Index](index.md) - Back to overview

