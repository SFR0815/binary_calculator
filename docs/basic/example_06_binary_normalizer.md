# Example 06: BinaryNormalizer - Normalizing Binary Strings

## Overview

This example demonstrates the `BinaryNormalizer` class, which provides utility methods for normalizing binary string representations to prepare them for bit-wise operations.

**Key Features:**
- Removing leading zeros
- Normalizing string lengths (padding)
- Preparing operands for binary operations

## Executable Code

**File:** `examples/basic/example_06_binary_normalizer.py`

**Run it:**
```bash
python examples/basic/example_06_binary_normalizer.py
```

---

## Example 1: Removing Leading Zeros

**Run this example:**

```bash
python example.py norm01
```

### Code

```python title="Remove leading zeros"
--8<-- "examples/basic/example_06_binary_normalizer.py:remove_leading_zeros"
```

### What This Does

Strips leading zeros from binary strings to get canonical representation.

### Input

Strings with various leading zero patterns:
- `'0101'` - one leading zero
- `'00001010'` - four leading zeros
- `'000'` - all zeros
- `'1010'` - no leading zeros
- `'0'` - single zero

### Processing

Uses Python's `lstrip('0') or '0'`:

```python
'0101'.lstrip('0') or '0' = '101'
'00001010'.lstrip('0') or '0' = '1010'
'000'.lstrip('0') or '0' = '' or '0' = '0'  # Prevents empty string
'1010'.lstrip('0') or '0' = '1010'
'0'.lstrip('0') or '0' = '' or '0' = '0'
```

### Why `or '0'` is Important

Without it, `'000'.lstrip('0')` would return empty string `''`, which is invalid for binary representation. The `or '0'` ensures we always get at least `'0'`.

### Expected Console Output

```
     '0101' -> '101'
 '00001010' -> '1010'
      '000' -> '0'
     '1010' -> '1010'
        '0' -> '0'
```

---

## Example 2: Normalizing Length

**Run this example:**

```bash
python example.py norm02
```

### Code

```python title="Normalize lengths"
--8<-- "examples/basic/example_06_binary_normalizer.py:normalize_length"
```

### What This Does

Pads both strings to the same length by prepending zeros to the shorter one.

### Input / Processing / Output

#### Pair 1: `'101'` and `'11'`

```
Lengths: 3 and 2
Max length: 3

'101'.zfill(3) = '101'  (no padding needed)
'11'.zfill(3) = '011'   (prepend one zero)

Result: Both 3 bits
```

#### Pair 2: `'1010'` and `'101010'`

```
Lengths: 4 and 6
Max length: 6

'1010'.zfill(6) = '001010'  (prepend two zeros)
'101010'.zfill(6) = '101010'  (no padding)

Result: Both 6 bits
```

### Why This Matters

Bit-wise operations require aligned positions:

```
Cannot add:
  1010
   101

Can add (after normalization):
  1010
  0101
```

### Expected Console Output

```
'101' and '11'
-> '101' and '011'
   (both 3 bits)

'1010' and '101010'
-> '001010' and '101010'
   (both 6 bits)

'1' and '1111'
-> '0001' and '1111'
   (both 4 bits)
```

---

## Example 3: Practical Use Case

**Run this example:**

```bash
python example.py norm03
```

### Code

```python title="Preparing for addition"
--8<-- "examples/basic/example_06_binary_normalizer.py:practical_use"
```

### What This Does

Shows how normalization prepares operands for bit-by-bit addition.

### Processing

```
Before normalization:
  1010  (4 bits)
   101  (3 bits)
  Cannot align for bit-wise addition!

After normalization:
  1010  (4 bits)
  0101  (4 bits, prepended zero)
  Now can add position-by-position:
    Position 3: 0 + 1
    Position 2: 1 + 0
    Position 1: 0 + 1
    Position 0: 1 + 0
```

### Expected Console Output

```
Original operands:
  1010 (4 bits)
  101 (3 bits)

After normalization:
  1010 (4 bits)
  0101 (4 bits)
Now ready for bit-by-bit addition!
```

---

## Example 4: Edge Cases

**Run this example:**

```bash
python example.py norm04
```

### Code

```python title="Edge cases"
--8<-- "examples/basic/example_06_binary_normalizer.py:edge_cases"
```

### What This Does

Demonstrates robust handling of special cases.

### Cases

1. **All zeros:** `'0000'` → `'0'`
2. **Single vs multiple:** `'1'` and `'1111'` → both 4 bits
3. **Already normalized:** `'101'` → `'101'` (unchanged)

### Expected Console Output

```
All zeros: '0000' -> '0'
Single vs multiple: '1', '1111' -> '0001', '1111'
Already normalized: '101' -> '101'
```

---

## Example 5: Why Normalization Matters

**Run this example:**

```bash
python example.py norm05
```

### Code

```python title="Importance of normalization"
--8<-- "examples/basic/example_06_binary_normalizer.py:comparison_demo"
```

### What This Does

Shows how different representations of the same value normalize to identical strings.

### Processing

```
Three representations of decimal 5:
  '101'   (3 bits, canonical)
  '0101'  (4 bits, one leading zero)
  '00101' (5 bits, two leading zeros)

After normalization:
  All become '101'

String equality: '101' == '101' == '101' ✓
```

**Without normalization:**
```
'101' == '0101' → False (different strings)
```

**With normalization:**
```
'101' == '101' → True (same value)
```

### Expected Console Output

```
Different representations of same value (5):
  '101' (3 bits)
  '0101' (4 bits)
  '00101' (5 bits)

After removing leading zeros:
  '101'
  '101'
  '101'
All equal: True
```

---

## Example 6: Larger Numbers

**Run this example:**

```bash
python example.py norm06
```

### Code

```python title="Large number normalization"
--8<-- "examples/basic/example_06_binary_normalizer.py:larger_numbers"
```

### Real-World Scenarios

#### a) Memory Addresses

**Numbers:**
- Address 1: 65,536 (17 bits, no zeros)
- Address 2: 4,096 (with leading zeros to 17 bits)

**Processing:**
```
Original:
  10000000000000000 (17 bits)
  00001000000000000 (17 bits, 4 leading zeros)

After normalize_length():
  10000000000000000
  00001000000000000
  (both already 17 bits)

For addition, the leading zeros in addr2 don't affect the result.
```

#### b) File Sizes

**Numbers:**
- 524,288 bytes (512 KB, 20 bits)
- 786,432 bytes (768 KB, 20 bits)

Both already same length - demonstrates that normalization handles equal lengths gracefully.

#### c) Network (Different Magnitudes)

**Numbers:**
- Bandwidth: 1,048,576 (21 bits)
- Packet: 8,192 (14 bits)

**Normalization:**
```
Before:
  100000000000000000000 (21 bits)
  10000000000000        (14 bits)

After:
  100000000000000000000
  000000010000000000000  (7 zeros prepended)
  (both 21 bits)
```

### Expected Console Output

```
a) Memory address normalization:
   Address 1: 10000000000000000 (17 bits)
   Address 2: 00001000000000000 (17 bits)
   After removing leading zeros from addr2:
              1000000000000 (13 bits)
   After normalizing lengths:
   Address 1: 10000000000000000
   Address 2: 00001000000000000
   (both 17 bits, ready for addition)

b) File size normalization:
   File 1: 10000000000000000000 (524,288 bytes = 512 KB)
   File 2: 11000000000000000000 (786,432 bytes = 768 KB)
   After normalization (already same length):
   File 1: 10000000000000000000
   File 2: 11000000000000000000

c) Different magnitude numbers:
   Bandwidth:   100000000000000000000 (1,048,576 bits/sec)
   Packet size: 10000000000000 (8,192 bits)
   After normalization:
   Bandwidth:   100000000000000000000
   Packet size: 000000010000000000000
   Length difference handled: 21 and 14 -> both 21 bits
```

---

## Algorithm Complexity

| Operation | Time | Space |
|-----------|------|-------|
| `remove_leading_zeros()` | O(n) | O(n) |
| `normalize_length()` | O(max(n₁, n₂)) | O(max(n₁, n₂)) |

Where n = string length

---

## Key Takeaways

1. **Leading Zeros:** Removed for canonical form
2. **Length Matching:** Critical for bit-wise operations
3. **Zero Padding:** Prepended to shorter operand
4. **Comparison:** Normalization enables accurate equality checks
5. **Internal Use:** Used by ArithmeticCalculator and BinaryComparator

---

## Next Steps

- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - See normalization in action
- [Example 04: BinaryComparator](example_04_binary_comparator.md) - Comparison with normalization
- [Back to Index](index.md)

