# Example 04: BinaryComparator - Comparing Binary Values

## Overview

This example demonstrates the `BinaryComparator` class, which performs comparisons on binary strings without converting to decimal, using length-based and lexicographic comparison.

**Key Features:**
- Length-based comparison (longer = larger)
- Lexicographic comparison (same length)
- Leading zero normalization
- All 6 comparison operators

## Executable Code

**File:** `examples/basic/example_04_binary_comparator.py`

**Run it:**
```bash
python examples/basic/example_04_binary_comparator.py
```

---

## Example 1: Basic compare() Method

**Run this example:**
```bash
python example.py comp01
```

### Code

```python title="Basic compare"
--8<-- "examples/basic/example_04_binary_comparator.py:basic_compare"
```

### What This Does

The `compare()` method returns `-1`, `0`, or `1` indicating the relationship between two binary strings.

### Input

- **Binary 1:** `'101'` (5 in decimal)
- **Binary 2:** `'11'` (3 in decimal)

### Processing Steps

```
Step 1: Remove leading zeros
  '101'.lstrip('0') or '0' = '101'
  '11'.lstrip('0') or '0' = '11'

Step 2: Compare lengths
  len('101') = 3
  len('11') = 2
  3 > 2 → first is larger

Step 3: Return
  return 1 (first > second)
```

### Why Length Comparison Works

In binary, a number with more bits is **always** larger (assuming no leading zeros):
- 3 bits: maximum value = 111₂ = 7₁₀
- 2 bits: maximum value = 11₂ = 3₁₀

Any 3-bit number (minimum 100₂ = 4₁₀) is larger than any 2-bit number (maximum 11₂ = 3₁₀).

### Expected Console Output

```
compare('101', '11') = 1
(-1 if first < second, 0 if equal, 1 if first > second)
```

### Return Value

- **Type:** `int`
- **Value:** `1`
- **Meaning:** First > Second

---

## Examples 2-7: Specific Comparison Methods

**Run individual examples:**
- `python example.py comp02` - Example 2: Less than
- `python example.py comp03` - Example 3: Less than or equal
- `python example.py comp04` - Example 4: Greater than
- `python example.py comp05` - Example 5: Greater than or equal
- `python example.py comp06` - Example 6: Equality
- `python example.py comp07` - Example 7: Inequality

### smaller() - Less Than

```python
--8<-- "examples/basic/example_04_binary_comparator.py:smaller"
```

**Processing:** `compare() < 0` → `-1 < 0` → `True`

### equal() - Equality with Leading Zeros

```python
--8<-- "examples/basic/example_04_binary_comparator.py:equal"
```

**Special Feature:** Leading zeros are normalized!
```
'101' == '0101' → both strip to '101' → True
```

---

## Example 8: All Comparisons

**Run this example:**
```bash
python example.py comp08
```

### Code

```python title="All comparison operations"
--8<-- "examples/basic/example_04_binary_comparator.py:all_comparisons"
```

### Processing for `'1010'` vs `'101'`

```
compare('1010', '101'):
  1. Strip: '1010', '101' (no leading zeros)
  2. Lengths: 4 > 3
  3. Return: 1

Results:
  <:  1 < 0  = False
  <=: 1 <= 0 = False
  >:  1 > 0  = True
  >=: 1 >= 0 = True
  ==: 1 == 0 = False
  !=: 1 != 0 = True
```

### Expected Console Output

```
'1010' < '101':  False
'1010' <= '101': False
'1010' > '101':  True
'1010' >= '101': True
'1010' == '101': False
'1010' != '101': True
```

---

## Example 9: Larger Numbers - Real-World Comparisons

**Run this example:**
```bash
python example.py comp09
```

### Code

```python title="Large number comparisons"
--8<-- "examples/basic/example_04_binary_comparator.py:larger_numbers"
```

### Scenario a: Performance Threshold Check

**Numbers:**
- Actual: 750,000 ops/sec (`'10110111001001110000'` - 20 bits)
- Threshold: 500,000 ops/sec (`'1111010000100100000'` - 19 bits)

**Processing:**
```
compare('10110111001001110000', '1111010000100100000'):
  Lengths: 20 > 19
  Return: 1 (actual > threshold)

larger_equal(): 1 >= 0 → True
```

**Output:**
```
Actual:    10110111001001110000 (750,000 ops/sec)
Threshold: 1111010000100100000 (500,000 ops/sec)
Meets requirement: True
```

### Scenario b: Memory Capacity Check

**Numbers:**
- Available: 8,388,608 bytes (8 MB, 24 bits)
- Required: 524,288 bytes (512 KB, 20 bits)

**Processing:**
```
Lengths: 24 > 20
Result: Available > Required ✓
```

**Output:**
```
Available: 100000000000000000000000 (8,388,608 bytes = 8 MB)
Required:  10000000000000000000 (524,288 bytes = 512 KB)
Sufficient: True
```

### Scenario c: Time Duration Check

**Numbers:**
- Elapsed: 300,000 ms (5 minutes, 19 bits)
- Limit: 60,000 ms (1 minute, 16 bits)

**Processing:**
```
Lengths: 19 > 16
Result: Elapsed > Limit ✓
```

---

## Complete Example Output

```
======================================================================
Example 04: BinaryComparator Operations
======================================================================

1. Basic compare() method:
   compare('101', '11') = 1
   (-1 if first < second, 0 if equal, 1 if first > second)

2. smaller() - Less than:
   '10' < '101' = True

3. smaller_equal() - Less than or equal:
   '101' <= '101' = True

4. larger() - Greater than:
   '1010' > '101' = True

5. larger_equal() - Greater than or equal:
   '1010' >= '1010' = True

6. equal() - Equality:
   '101' == '0101' = True
   (Leading zeros are ignored)

7. not_equal() - Inequality:
   '101' != '110' = True

8. All Comparisons (1010 vs 101):
   '1010' < '101':  False
   '1010' <= '101': False
   '1010' > '101':  True
   '1010' >= '101': True
   '1010' == '101': False
   '1010' != '101': True

9. Comparisons with Larger Numbers:
   [... large number output ...]
======================================================================
```

---

## Comparison Algorithm

### Pseudocode

```
function compare(binary_1, binary_2):
    b1 = binary_1.lstrip('0') or '0'
    b2 = binary_2.lstrip('0') or '0'
    
    if len(b1) < len(b2):
        return -1
    elif len(b1) > len(b2):
        return 1
    
    # Same length - lexicographic
    if b1 < b2:
        return -1
    elif b1 > b2:
        return 1
    else:
        return 0
```

### Why This Works

1. **Leading zeros removed:** `'0101'` → `'101'`
2. **Length comparison:** More bits = larger number
3. **Lexicographic comparison:** For same length, compare string-wise

**Lexicographic works because:** In same-length binary strings, left-to-right comparison is correct:
- `'1010'` > `'1001'` (comparing left to right: 1=1, 0=0, 1>0)

---

## Algorithm Complexity

| Operation | Time | Space |
|-----------|------|-------|
| `compare()` | O(n) | O(n) |
| `smaller()` | O(n) | O(n) |
| `larger()` | O(n) | O(n) |
| `equal()` | O(n) | O(n) |
| All others | O(n) | O(n) |

Where n = max length of binary strings

**Note:** Often faster than O(n) due to early exit on length difference!

---

## Key Takeaways

1. **No Decimal Conversion:** Pure binary comparison
2. **Length First:** Most comparisons resolve with length check
3. **Leading Zeros:** Automatically normalized
4. **Efficient:** O(1) for different lengths, O(n) for same length
5. **Accurate:** Handles all edge cases correctly

---

## Next Steps

- [Example 05: BinaryConverter](example_05_binary_converter.md) - Conversion utilities
- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - Arithmetic operations
- [Back to Index](index.md)

