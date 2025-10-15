# Example 07: InstructionExecutor - Executing Instructions

## Overview

This example demonstrates the `InstructionExecutor` class, which executes `BinaryInstruction` objects and provides optional formatted output visualization.

**Key Features:**
- Routes instructions to appropriate calculators
- Validates instruction types
- Provides formatted output display
- Handles both calculation and comparison operations

## Executable Code

**File:** `examples/basic/example_07_instruction_executor.py`

**Run it:**
```bash
python examples/basic/example_07_instruction_executor.py
```

---

## Example 1: Simple Addition (No Formatted Output)

**Run this example:**

```bash
python example.py exec01
```

### Code

```python title="Addition without formatting"
--8<-- "examples/basic/example_07_instruction_executor.py:simple_addition"
```

### What This Does

Executes an addition instruction and returns the result without formatted display.

### Input

- **Operand 1:** `'1011'` (11)
- **Operand 2:** `'110'` (6)
- **Operation:** `'+'`
- **print_result:** `False`

### Processing Pipeline

```
1. User creates BinaryInstruction
   ↓
2. Pass to executor.calculate()
   ↓
3. Executor validates: is_calculation() == True ✓
   ↓
4. Map operation: OperationEnum.ADD → calculator.add
   ↓
5. Call calculator.add(operand_1, operand_2)
   ↓
6. Arithmetic processing (normalize, add bits)
   ↓
7. Return BinaryNumber('10001')
```

### Expected Console Output

```
1011 + 110 = 10001
Decimal: 11 + 6 = 17
```

### Return Value

- **Type:** `BinaryNumber`
- **Value:** `'10001'`
- **Decimal:** 17

---

## Example 2: Addition with Formatted Output

**Run this example:**

```bash
python example.py exec02
```

### Code

```python title="Addition with formatting"
--8<-- "examples/basic/example_07_instruction_executor.py:formatted_addition"
```

### What This Does

Same calculation but displays formatted visual output.

### Processing for Formatted Output

#### Step 1-3: Calculate (Same as Above)

Calculate the result `'10001'`.

#### Step 4: Call _print_calculation()

```python
def _print_calculation(self, *, instruction, result):
    # 1. Print instruction repr
    print(instruction)
    
    # 2. Calculate separator width
    max_operand_width = max(len('1011'), len('110')) = 4
    result_width = len('10001') = 5
    total_width = max(2 + 4, 2 + 5) = 7
    
    # 3. Print dashes
    print('-' * 7)
    
    # 4. Print result (right-aligned with indent)
    indent = ' ' * 2
    print(f"{indent}{'10001'.rjust(5)}")
    
    # 5. Print equals
    print('=' * 7)
```

### Expected Console Output

```
  1011
+  110
------
 10001
======
Result: 10001 (17)
```

### Visual Explanation

```
Line 1:   "  1011"     (2 spaces + '1011')
Line 2:   "+  110"     ('+' + space + '110' right-aligned to 4)
Line 3:   "------"     (7 dashes)
Line 4:   " 10001"     (2 spaces + '10001' right-aligned to 5)
Line 5:   "======"     (7 equals)
```

---

## Example 3-5: Other Operations

**Run these examples:**

- **Subtraction:** `python example.py exec03`
- **Multiplication:** `python example.py exec04`
- **Division:** `python example.py exec05`

### Subtraction

```python title="Subtraction"
--8<-- "examples/basic/example_07_instruction_executor.py:subtraction"
```

**Output:**
```
  10101
-  1001
-------
   1100
=======
Result: 1100 (12)
```

### Multiplication

```python title="Multiplication"
--8<-- "examples/basic/example_07_instruction_executor.py:multiplication"
```

**Output:**
```
  101
*  11
-----
 1111
=====
Result: 1111 (15)
```

### Division

```python title="Division"
--8<-- "examples/basic/example_07_instruction_executor.py:division"
```

**Output:**
```
  1101
/   11
------
   100
======
Result: 100 (4)
```

---

## Example 6: Comparison Operations

**Run this example:**

```bash
python example.py exec06
```

### Code

```python title="Comparison with formatting"
--8<-- "examples/basic/example_07_instruction_executor.py:comparison"
```

### What This Does

Executes a comparison instruction with formatted output.

### Processing

```
1. Validate: is_comparison() == True ✓
2. Route to: BinaryComparator.larger_equal()
3. Compare:
   - Remove leading zeros (none)
   - Compare lengths: 4 > 3
   - Return 1
4. Check: 1 >= 0 → True
5. Format and display
```

### Expected Console Output

```
   1010
>=  101
-------
   True
=======
Result: True
```

---

## Example 7: All Comparisons

**Run this example:**

```bash
python example.py exec07
```

### Code

```python title="All comparison operations"
--8<-- "examples/basic/example_07_instruction_executor.py:all_comparisons"
```

### Expected Console Output

```
1010 < 101 = False
1010 <= 101 = False
1010 > 101 = True
1010 >= 101 = True
1010 == 101 = False
1010 != 101 = True
```

---

## Example 8: Error Handling

**Run this example:**

```bash
python example.py exec08
```

### Code

```python title="Error handling"
--8<-- "examples/basic/example_07_instruction_executor.py:error_handling"
```

### Errors Demonstrated

1. **Wrong method:** Using `calculate()` for comparison instruction
2. **Division by zero:** Attempting to divide by `'0'`
3. **Negative result:** Subtracting larger from smaller

### Expected Console Output

```
a) Wrong method for instruction type:
   [OK] Cannot calculate comparison instruction...

b) Division by zero:
   [OK] Cannot divide by zero

c) Negative subtraction result:
   [OK] Cannot subtract: result would be negative (101 - 1010)
```

---

## Example 9: Larger Numbers

**Run this example:**

```bash
python example.py exec09
```

### Code

```python title="Realistic scenarios"
--8<-- "examples/basic/example_07_instruction_executor.py:larger_numbers"
```

### Scenarios

Four realistic use cases with formatted output:

1. **Memory:** 65,536 + 4,096 bytes
2. **Storage:** 512 KB + 768 KB  
3. **Network:** 1 Mbps / 8192 bits
4. **Performance:** 750,000 >= 500,000 check

### Expected Output Examples

#### Memory Address
```
  10000000000000000
+     1000000000000
-------------------
  10001000000000000
===================
Final address: 69,632 bytes (0x11000)
```

#### Performance Check
```
    100000000000000000000
>=   1111010000100100000
------------------------
                    True
========================
Performance check: PASS
(750,000 >= 500,000)
```

---

## Algorithm Complexity

| Method | Time | Space |
|--------|------|-------|
| `calculate()` | O(f(n)) | O(n) |
| `compare()` | O(n) | O(1) |
| `_print_calculation()` | O(n) | O(n) |
| `_print_comparison()` | O(n) | O(n) |

Where:
- n = bit length
- f(n) = complexity of delegated operation

---

## Key Takeaways

1. **Routing:** Automatically delegates to correct calculator
2. **Validation:** Type-checks instructions before execution
3. **Formatted Output:** `print_result=True` shows visual representation
4. **Flexibility:** Same executor handles all operations
5. **Error Messages:** Helpful guidance when methods misused

---

## Next Steps

- [Example 01: BinaryNumber](example_01_binary_number.md) - Core data structure
- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - Arithmetic details
- [Realistic Scenarios](../realistic_scenarios/index.md) - Complete use cases

