# Example 01: BinaryNumber - Creating and Manipulating Binary Numbers

## Overview

This example demonstrates the `BinaryNumber` class, which is the core data structure for encapsulating binary string values. It provides methods for:

- Creating binary numbers from strings or integers
- Converting to integers
- Increment and decrement operations  
- Copying
- Comparing values

## Executable Code

**File:** `examples/basic/example_01_binary_number.py`

**Run it:**
```bash
python examples/basic/example_01_binary_number.py
```

---

## Example 1: Creating from Binary String

**Run this example:**
```bash
python example.py numb01
```

### Code

```python title="Create from binary string"
--8<-- "examples/basic/example_01_binary_number.py:create_from_string"
```

### What This Does

Creates a `BinaryNumber` object from a binary string `'1010'`.

### Input

- **String:** `'1010'` - must contain only `'0'` and `'1'` characters

### Processing Steps

1. **Validation:** The `__init__` method calls `_validate_binary_string()`
2. **Check empty:** Ensures string is not empty
3. **Check characters:** Verifies all characters are either '0' or '1'
4. **Store value:** Saves the validated string as `self._value`

### Expected Console Output

```
1. Created from string: 1010 (decimal: 10)
```

### Return Value

- **Type:** `BinaryNumber` object
- **Internal value:** `'1010'`
- **Accessible via:** `num1.value` property

---

## Example 2: Creating from Integer

**Run this example:**
```bash
python example.py numb02
```

### Code

```python title="Create from integer"
--8<-- "examples/basic/example_01_binary_number.py:create_from_int"
```

### What This Does

Creates a `BinaryNumber` from a decimal integer using the class method `from_int()`.

### Input

- **Integer:** `42` (must be non-negative)

### Processing Steps

1. **Class method called:** `BinaryNumber.from_int(decimal_num=42)`
2. **Validation:** Checks that integer is non-negative
3. **Conversion:** Uses Python's `bin(42)` → returns `'0b101010'`
4. **Strip prefix:** Removes `'0b'` → leaves `'101010'`
5. **Create instance:** Calls `BinaryNumber(binary_str='101010')`

### Character-by-Character Conversion

```
Decimal 42:
  42 ÷ 2 = 21 remainder 0  →  bit 0 = 0
  21 ÷ 2 = 10 remainder 1  →  bit 1 = 1
  10 ÷ 2 = 5  remainder 0  →  bit 2 = 0
   5 ÷ 2 = 2  remainder 1  →  bit 3 = 1
   2 ÷ 2 = 1  remainder 0  →  bit 4 = 0
   1 ÷ 2 = 0  remainder 1  →  bit 5 = 1

Reading bottom to top: 101010
```

### Expected Console Output

```
2. Created from int 42: 101010
```

### Return Value

- **Type:** `BinaryNumber` object
- **Internal value:** `'101010'`
- **Binary representation:** 6 bits

---

## Example 3: Increment Operation

**Run this example:**
```bash
python example.py numb04
```

### Code

```python title="Increment operations"
--8<-- "examples/basic/example_01_binary_number.py:increment"
```

### What This Does

Demonstrates incrementing a binary number, both with default (1) and custom amounts.

### Input

- **Initial value:** `BinaryNumber('1010')` - decimal 10
- **Default increment:** `'1'` (binary)
- **Custom increment:** `BinaryNumber('101')` - decimal 5

### Processing Steps for `incr()`

#### Step 1: Default Increment (by 1)

```
Current value: '1010' (10)
Increment:     '1' (1)

Processing:
  1. Convert current to int:     '1010' → 10
  2. Convert increment to int:   '1' → 1  
  3. Add:                        10 + 1 = 11
  4. Convert result to binary:   bin(11) = '0b1011'
  5. Strip prefix:               '1011'
  6. Update self._value:         self._value = '1011'

Result: '1011' (11)
```

#### Step 2: Custom Increment (by 5)

```
Current value: '1011' (11)
Increment:     '101' (5)

Processing:
  1. Convert current to int:     '1011' → 11
  2. Convert increment to int:   '101' → 5
  3. Add:                        11 + 5 = 16
  4. Convert result to binary:   bin(16) = '0b10000'
  5. Strip prefix:               '10000'
  6. Update self._value:         self._value = '10000'

Result: '10000' (16)
```

### Expected Console Output

```
4. Increment operations:
   Initial: 1010 (10)
   After incr(): 1011 (11)
   After incr(increment='101'): 10000 (16)
```

### Key Points

- **In-place operation:** Modifies the BinaryNumber object directly
- **Default behavior:** Increments by 1 if no argument provided
- **Type safety:** Increment must be a BinaryNumber (not a string or int)

---

## Example 4: Larger Numbers

**Run this example:**
```bash
python example.py numb09
```

### Code

```python title="Working with larger numbers"
--8<-- "examples/basic/example_01_binary_number.py:larger_numbers"
```

### What This Does

Demonstrates the same operations with realistic, larger numbers representing memory addresses and storage sizes.

### Real-World Scenario: Memory Address Calculation

**Context:** Operating system calculating a memory address by adding a base address to an offset.

### Input

- **Base address:** 65,536 bytes (0x10000) - typical 16-bit boundary
- **Offset:** 4,096 bytes (one memory page)

### Processing for Large Numbers

#### Creating 65,536

```
Decimal: 65,536 = 2^16

Binary conversion:
  65536 = 1 × 2^16 + 0 × 2^15 + ... + 0 × 2^0

Result: '10000000000000000' (17 bits)

Note: Exactly 17 bits because 65,536 = 2^16
      Just one '1' followed by sixteen '0's
```

#### Creating 4,096

```
Decimal: 4,096 = 2^12

Binary conversion:
  4096 = 1 × 2^12 + 0 × 2^11 + ... + 0 × 2^0

Result: '1000000000000' (13 bits)

Note: Exactly 13 bits because 4,096 = 2^12
      Just one '1' followed by twelve '0's
```

#### Increment Processing

```
Base:   '10000000000000000' (65,536)
Offset: '1000000000000'     (4,096)

Step-by-step addition:
  1. Convert base to int:    65,536
  2. Convert offset to int:  4,096
  3. Add:                    65,536 + 4,096 = 69,632
  4. Convert to binary:      bin(69,632) = '0b10001000000000000'
  5. Strip prefix:           '10001000000000000'

Result: '10001000000000000' (17 bits, same as base)
```

#### Comparison Processing (1 MB vs 1 KB)

```
Number 1: 1,048,576 (1 MB = 2^20)
Binary:   '100000000000000000000' (21 bits)

Number 2: 1,024 (1 KB = 2^10)
Binary:   '10000000000' (11 bits)

Comparison: mega > kilo
Processing:
  1. Call BinaryComparator.larger()
  2. Remove leading zeros (none in this case)
  3. Compare lengths: 21 > 11
  4. Result: TRUE (longer binary = larger number)

No need to compare actual bits since lengths differ!
```

### Expected Console Output

```
9. Working with Larger Numbers:
   Large number 1: 10000000000000000
                   (65536 in decimal)
                   (17 bits)

   Large number 2: 1000000000000
                   (4096 in decimal)
                   (13 bits)

   Incrementing 65536 by 4096:
   Result: 10001000000000000
           (69632 in decimal)

   Comparing 1 MB vs 1 KB:
   1,048,576 > 1,024: True
   Bit lengths: 21 vs 11 bits
```

### Key Insights

1. **Binary Efficiency:** 65,536 needs only 17 bits (vs 5 decimal digits)
2. **Powers of 2:** Numbers like 2^16 have very sparse binary (just one '1')
3. **Bit Length Growth:** Doubles for each power of 2
   - 2^10 = 11 bits
   - 2^16 = 17 bits  
   - 2^20 = 21 bits
4. **Comparison Speed:** Length comparison is O(1), very fast!

---

## Complete Example Output

When you run `python examples/basic/example_01_binary_number.py`, you'll see:

```
======================================================================
Example 01: BinaryNumber Operations
======================================================================

1. Created from string: 1010 (decimal: 10)
2. Created from int 42: 101010
3. Converted to int: 10

4. Increment operations:
   Initial: 1010 (10)
   After incr(): 1011 (11)
   After incr(increment='101'): 10000 (16)

5. Decrement operations:
   Before decr(): 10000 (16)
   After decr(): 1111 (15)

6. Copy operation:
   Original: 1111
   Copy: 1111
   After incrementing copy:
     Original: 1111 (unchanged)
     Copy: 10000 (changed)

7. Comparison operators:
   num5 = 1010 (10), num6 = 101 (5)
   num5 > num6:  True
   num5 >= num6: True
   num5 < num6:  False
   num5 <= num6: False
   num5 == num6: False
   num5 != num6: True

8. Error handling - decrement below zero:
   [OK] Caught error: Cannot decrement 10 by 101: result would be negative

9. Working with Larger Numbers:
   Large number 1: 10000000000000000
                   (65536 in decimal)
                   (17 bits)

   Large number 2: 1000000000000
                   (4096 in decimal)
                   (13 bits)

   Incrementing 65536 by 4096:
   Result: 10001000000000000
           (69632 in decimal)

   Comparing 1 MB vs 1 KB:
   1,048,576 > 1,024: True
   Bit lengths: 21 vs 11 bits

======================================================================
```

---

## Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `__init__` | O(n) | O(n) |
| `from_int()` | O(log m) | O(log m) |
| `to_int()` | O(n) | O(1) |
| `incr()` | O(n) | O(n) |
| `decr()` | O(n) | O(n) |
| `copy()` | O(n) | O(n) |
| Comparisons | O(n) | O(1) |

Where:
- n = number of bits in binary representation
- m = decimal value of integer

---

## Key Takeaways

1. **Encapsulation:** BinaryNumber wraps string validation and operations
2. **Type Safety:** Forces use of proper binary representations
3. **Immutable with Mutations:** Value property is read-only, but `incr()`/`decr()` modify in-place
4. **Comparison Integration:** Uses BinaryComparator internally for accurate comparisons
5. **Scalability:** Works efficiently with numbers from 1 to millions

---

## Next Steps

- [Example 02: BinaryInstruction](example_02_binary_instruction.md) - Learn how to create instructions
- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - Perform calculations
- [Example 07: InstructionExecutor](example_07_instruction_executor.md) - Execute instructions

---

**All code is executable and tested!** ✓

