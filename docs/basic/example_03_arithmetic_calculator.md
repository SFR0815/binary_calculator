# Example 03: ArithmeticCalculator - Pure Binary Arithmetic

## Overview

This example demonstrates the `ArithmeticCalculator` class, which performs pure binary arithmetic directly on `BinaryNumber` objects without converting to decimal.

**Operations:**
- Addition - Bit-by-bit with carry propagation
- Subtraction - Bit-by-bit with borrow handling
- Multiplication - Shift-and-add algorithm
- Division - Binary long division

## Executable Code

**File:** `examples/basic/example_03_arithmetic_calculator.py`

**Run it:**
```bash
python examples/basic/example_03_arithmetic_calculator.py
```

---

## Example 1: Addition

**Run this example:**
```bash
python example.py calc01
```

### Code

```python title="Addition operation"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:addition"
```

### What This Does

Adds two binary numbers using bit-by-bit addition with carry.

### Input

- **Operand 1:** `'1010'` (10 in decimal)
- **Operand 2:** `'0101'` (5 in decimal)

### Character-by-Character Processing

#### Step 1: Normalize Lengths

Both operands already have 4 bits - no padding needed.

```
operand_1: 1010
operand_2: 0101
```

#### Step 2: Add Bit-by-Bit (Right to Left)

| Position | Bit 1 | Bit 2 | Carry In | Sum | Result Bit | Carry Out |
|----------|-------|-------|----------|-----|------------|-----------|
| 3 (LSB)  | 0     | 1     | 0        | 1   | 1          | 0         |
| 2        | 1     | 0     | 0        | 1   | 1          | 0         |
| 1        | 0     | 1     | 0        | 1   | 1          | 0         |
| 0 (MSB)  | 1     | 0     | 0        | 1   | 1          | 0         |

#### Step 3: Build Result

Result array (built right to left): `[1, 1, 1, 1]`  
Reversed: `'1111'`

#### Step 4: Remove Leading Zeros

No leading zeros to remove.

**Final Result:** `'1111'` (15 in decimal)

### Expected Console Output

```
1010 + 0101 = 1111
Decimal: 10 + 5 = 15
```

### Return Value

- **Type:** `BinaryNumber`
- **Value:** `'1111'`
- **Decimal:** 15

---

## Example 2: Subtraction

**Run this example:**
```bash
python example.py calc02
```

### Code

```python title="Subtraction operation"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:subtraction"
```

### What This Does

Subtracts the second binary number from the first using borrow propagation.

### Input

- **Operand 1:** `'1111'` (15)
- **Operand 2:** `'0101'` (5)

### Character-by-Character Processing

#### Step 1: Validate Non-Negative

```
Compare '1111' vs '0101':
  Remove leading zeros: '1111', '101'
  Compare lengths: 4 > 3
  Result: '1111' > '0101' ✓ (valid)
```

#### Step 2: Normalize

Already same length (4 bits).

#### Step 3: Subtract Bit-by-Bit

| Position | Bit 1 | Bit 2 | Borrow In | Difference | Result | Borrow Out |
|----------|-------|-------|-----------|------------|--------|------------|
| 3        | 1     | 1     | 0         | 0          | 0      | 0          |
| 2        | 1     | 0     | 0         | 1          | 1      | 0          |
| 1        | 1     | 1     | 0         | 0          | 0      | 0          |
| 0        | 1     | 0     | 0         | 1          | 1      | 0          |

**Result:** `'1010'` (10 in decimal)

### Expected Console Output

```
1111 - 0101 = 1010
Decimal: 15 - 5 = 10
```

---

## Example 3: Multiplication

**Run this example:**
```bash
python example.py calc03
```

### Code

```python title="Multiplication operation"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:multiplication"
```

### What This Does

Multiplies using the shift-and-add algorithm.

### Input

- **Multiplicand:** `'101'` (5)
- **Multiplier:** `'11'` (3)

### Shift-and-Add Algorithm

#### Process Multiplier Right to Left

```
Multiplier: '11'

Iteration 1 (position 1, rightmost bit '1'):
  Bit is 1 → add shifted multiplicand
  Shift amount: len('11') - 1 - 1 = 0
  Shifted value: '101' + '' = '101'
  Partial result: '0' + '101' = '101'

Iteration 2 (position 0, bit '1'):
  Bit is 1 → add shifted multiplicand
  Shift amount: len('11') - 1 - 0 = 1
  Shifted value: '101' + '0' = '1010'
  
  Addition '101' + '1010':
    Normalize: '0101' + '1010'
    Add:
      Position 3: 1+0=1
      Position 2: 0+1=1
      Position 1: 1+0=1
      Position 0: 0+1=1
    Result: '1111'

Final: '1111' (15)
```

### Expected Console Output

```
101 * 11 = 1111
Decimal: 5 * 3 = 15
```

---

## Example 4: Division

**Run this example:**
```bash
python example.py calc04
```

### Code

```python title="Division operation"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:division"
```

### What This Does

Performs binary long division, processing the dividend bit by bit.

### Input

- **Dividend:** `'1010'` (10)
- **Divisor:** `'10'` (2)

### Binary Long Division

```
Dividend: 1010
Divisor:  10

Process left to right:

  Bit 0 ('1'):
    Bring down: remainder = '0' + '1' = '1'
    Compare: '1' < '10'
    Quotient += '0'
  
  Bit 1 ('0'):
    Bring down: remainder = '1' + '0' = '10'
    Compare: '10' >= '10' ✓
    Subtract: '10' - '10' = '0'
    Quotient += '1'
  
  Bit 2 ('1'):
    Bring down: remainder = '0' + '1' = '1'
    Compare: '1' < '10'
    Quotient += '0'
  
  Bit 3 ('0'):
    Bring down: remainder = '1' + '0' = '10'
    Compare: '10' >= '10' ✓
    Subtract: '10' - '10' = '0'
    Quotient += '1'

Quotient: '0101'
Remove leading zero: '101' (5)
```

### Expected Console Output

```
1010 / 10 = 101
Decimal: 10 / 2 = 5
```

---

## Example 5: Chained Operations

**Run this example:**
```bash
python example.py calc05
```

### Code

```python title="Chained operations"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:chained_operations"
```

### What This Does

Demonstrates composing operations: `(12 + 3) * 2`

### Processing

```
Step 1: '1100' + '11' = '1111'
  12 + 3 = 15

Step 2: '1111' * '10'
  Multiplier '10':
    Bit 0 = '0': skip
    Bit 1 = '1': add '1111' shifted 1 = '11110'
  Result: '11110' (30)

Expression value: 30
```

### Expected Console Output

```
Step 1: 1100 + 11 = 1111 (15)
Step 2: 1111 * 10 = 11110 (30)
Expression: (12 + 3) * 2 = 30
```

---

## Example 6: Error Handling

**Run this example:**
```bash
python example.py calc06
```

### Code

```python title="Error handling"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:error_handling"
```

### Validation Scenarios

Both operations properly validate inputs and raise descriptive errors.

### Expected Console Output

```
a) Division by zero:
   [OK] Cannot divide by zero

b) Negative subtraction result:
   [OK] Cannot subtract: result would be negative (101 - 1010)
```

---

## Example 7: Larger Numbers - Real-World Scenarios

**Run this example:**
```bash
python example.py calc07
```

### Code

```python title="Realistic calculations"
--8<-- "examples/basic/example_03_arithmetic_calculator.py:larger_numbers"
```

### Scenarios Demonstrated

#### a) Memory Address: 65,536 + 4,096

**Processing:**
- Base: `'10000000000000000'` (17 bits)
- Offset: `'1000000000000'` (13 bits)
- Normalize to 17 bits, add
- Result: `'10001000000000000'` = 69,632 (0x11000)

#### b) File Storage: 512 KB + 768 KB

**Processing:**
- Both 20 bits (powers of 2)
- Addition creates 21-bit result
- Total: 1,310,720 bytes = 1.25 MB

#### c) Network: 1 Mbps / 8192 bits

**Processing:**
- 21 bits / 14 bits
- Long division yields 8-bit quotient
- Result: 128 packets/second

#### d) Image: 1920 × 1080

**Processing:**
- 11 bits × 11 bits
- Shift-and-add multiplication
- Result: 2,073,600 pixels (21 bits)
- Memory: 6.22 MB for 24-bit RGB

### Expected Console Output

```
a) Memory address calculation:
   Base:   65,536 (0x10000)
   Offset: 4,096 (0x1000)
   Result: 69,632 (0x11000)

b) Total file storage:
   File 1: 524,288 bytes (512 KB)
   File 2: 786,432 bytes (768 KB)
   Total:  1,310,720 bytes = 1280 KB = 1.25 MB

c) Network packets per second:
   Bandwidth:   1,048,576 bits/sec (1 Mbps)
   Packet size: 8,192 bits
   Packets/sec: 128

d) Image pixel count (1920x1080):
   Width:  1,920 pixels
   Height: 1,080 pixels
   Total:  2,073,600 pixels
   Memory: 6,220,800 bytes (5.93 MB for 24-bit RGB)
```

---

## Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Addition | O(n) | O(n) |
| Subtraction | O(n) | O(n) |
| Multiplication | O(n²) | O(n) |
| Division | O(n²) | O(n) |

Where n = number of bits in the larger operand

---

## Key Takeaways

1. **Pure Binary:** No decimal conversion during calculation
2. **Bit-by-Bit:** Operations process one bit at a time
3. **Carry/Borrow:** Addition uses carry, subtraction uses borrow
4. **Shift-and-Add:** Multiplication is repeated addition with shifts
5. **Long Division:** Division mirrors manual binary division
6. **Scalability:** Works efficiently with numbers up to millions

---

## Next Steps

- [Example 04: BinaryComparator](example_04_binary_comparator.md) - Comparison operations
- [Example 07: InstructionExecutor](example_07_instruction_executor.md) - Execution engine
- [Realistic Scenarios](../realistic_scenarios/index.md) - Complete use cases

