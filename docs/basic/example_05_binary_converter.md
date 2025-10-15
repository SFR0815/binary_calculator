# Example 05: BinaryConverter - Binary ↔ Decimal Conversion

## Overview

This example demonstrates the `BinaryConverter` class, which provides utility methods for converting between binary string representations and decimal integer values.

**Important:** These conversions are **convenience methods**. The binary calculator performs arithmetic directly on binary strings without using these converters internally.

## Executable Code

**File:** `examples/basic/example_05_binary_converter.py`

**Run it:**
```bash
python examples/basic/example_05_binary_converter.py
```

---

## Example 1: Binary to Decimal

**Run this example:**

```bash
python example.py conv01
```

### Code

```python title="Binary to decimal conversion"
--8<-- "examples/basic/example_05_binary_converter.py:binary_to_decimal"
```

### What This Does

Converts binary strings to decimal integers using Python's `int(str, base)`.

### Input

Binary strings: `['1010', '1111', '10000', '11111111']`

### Processing for Each

**Example: `'1010'` → 10**

```
Method: int('1010', 2)

Bit-by-bit calculation:
  Position 3: 1 × 2³ = 1 × 8 = 8
  Position 2: 0 × 2² = 0 × 4 = 0
  Position 1: 1 × 2¹ = 1 × 2 = 2
  Position 0: 0 × 2⁰ = 0 × 1 = 0
  
  Total: 8 + 0 + 2 + 0 = 10
```

### Expected Console Output

```
       1010 (binary) =    10 (decimal)
       1111 (binary) =    15 (decimal)
      10000 (binary) =    16 (decimal)
   11111111 (binary) =   255 (decimal)
```

---

## Example 2: Decimal to Binary

**Run this example:**

```bash
python example.py conv02
```

### Code

```python title="Decimal to binary conversion"
--8<-- "examples/basic/example_05_binary_converter.py:decimal_to_binary"
```

### What This Does

Converts decimal integers to binary strings using Python's `bin()`.

### Processing

**Example: 10 → `'1010'`**

```
Method: bin(10)[2:]  # [2:] strips '0b' prefix

Division method (what bin() does internally):
  10 ÷ 2 = 5 remainder 0  → bit 0 = 0
   5 ÷ 2 = 2 remainder 1  → bit 1 = 1
   2 ÷ 2 = 1 remainder 0  → bit 2 = 0
   1 ÷ 2 = 0 remainder 1  → bit 3 = 1

Reading bottom to top: 1010
```

### Expected Console Output

```
   10 (decimal) =       1010 (binary)
   15 (decimal) =       1111 (binary)
   16 (decimal) =      10000 (binary)
  255 (decimal) =   11111111 (binary)
```

---

## Example 3: Round-Trip Conversion

**Run this example:**

```bash
python example.py conv03
```

### Code

```python title="Round-trip verification"
--8<-- "examples/basic/example_05_binary_converter.py:round_trip"
```

### What This Does

Verifies no data loss in conversion cycle: Decimal → Binary → Decimal

### Processing

```
Original: 42

Step 1: decimal_to_binary(42)
  bin(42) = '0b101010'
  Strip '0b': '101010'

Step 2: binary_to_decimal('101010')
  int('101010', 2) = 42

Step 3: Verify
  42 == 42 ✓
```

### Expected Console Output

```
Original decimal:   42
Converted to binary: 101010
Back to decimal:    42
Match: True
```

---

## Example 4: Powers of 2

**Run this example:**

```bash
python example.py conv04
```

### Code

```python title="Powers of 2"
--8<-- "examples/basic/example_05_binary_converter.py:powers_of_two"
```

### What This Does

Demonstrates the sparse binary representation of powers of 2.

### Key Insight

**Every power of 2 has exactly ONE bit set!**

```
2⁰ =    1 = 1           (1 bit set at position 0)
2¹ =    2 = 10          (1 bit set at position 1)
2² =    4 = 100         (1 bit set at position 2)
2³ =    8 = 1000        (1 bit set at position 3)
...
2¹⁰ = 1024 = 10000000000  (1 bit set at position 10)
```

### Expected Console Output

```
2^ 0 =     1 =            1 (1 bit set)
2^ 1 =     2 =           10 (1 bit set)
2^ 2 =     4 =          100 (1 bit set)
2^ 3 =     8 =         1000 (1 bit set)
2^ 4 =    16 =        10000 (1 bit set)
2^ 5 =    32 =       100000 (1 bit set)
2^ 6 =    64 =      1000000 (1 bit set)
2^ 7 =   128 =     10000000 (1 bit set)
2^ 8 =   256 =    100000000 (1 bit set)
2^ 9 =   512 =   1000000000 (1 bit set)
2^10 =  1024 =  10000000000 (1 bit set)
```

---

## Example 5: Large Numbers

**Run this example:**

```bash
python example.py conv05
```

### Code

```python title="Large number conversions"
--8<-- "examples/basic/example_05_binary_converter.py:large_numbers"
```

### What This Does

Shows binary representations of common large values and bit length growth.

### Bit Length Pattern

| Decimal | Binary Bits | Pattern |
|---------|-------------|---------|
| 1,024 | 11 | 2^10 + 1 bit |
| 4,096 | 13 | 2^12 + 1 bit |
| 65,536 | 17 | 2^16 + 1 bit |
| 1,048,576 | 21 | 2^20 + 1 bit |

**Rule:** For 2^n, bit length = n + 1

### Expected Console Output

```
      1024 = 10000000000
               (11 bits)
      4096 = 1000000000000
               (13 bits)
     65536 = 10000000000000000
               (17 bits)
   1048576 = 100000000000000000000
               (21 bits)
```

---

## Example 6: Representation Comparison

**Run this example:**

```bash
python example.py conv06
```

### Code

```python title="Decimal vs binary efficiency"
--8<-- "examples/basic/example_05_binary_converter.py:comparison"
```

### What This Does

Compares the efficiency of decimal vs binary representations.

### Analysis

| Value | Decimal Digits | Binary Bits | Ratio |
|-------|----------------|-------------|-------|
| 1 | 1 | 1 | 1.00 |
| 10 | 2 | 4 | 2.00 |
| 100 | 3 | 7 | 2.33 |
| 1000 | 4 | 10 | 2.50 |

**Observation:** Binary requires ~log₂(n) bits, decimal requires ~log₁₀(n) digits.

**Efficiency factor:** log₂/log₁₀ ≈ 3.32, so binary uses ~3.3× more "digits"

### Expected Console Output

```
     1: 1 decimal digits vs 1 binary bits (ratio: 1.00)
    10: 2 decimal digits vs 4 binary bits (ratio: 2.00)
   100: 3 decimal digits vs 7 binary bits (ratio: 2.33)
  1000: 4 decimal digits vs 10 binary bits (ratio: 2.50)
```

---

## Example 7: Realistic Use Cases

**Run this example:**

```bash
python example.py conv07
```

### Code

```python title="Realistic conversions"
--8<-- "examples/basic/example_05_binary_converter.py:realistic_conversions"
```

### Scenarios

#### a) Memory Sizes

Common memory values from 1 KB to 8 MB:

```
    1 KB =      1,024 = 10000000000 (11 bits)
   64 KB =     65,536 = 10000000000000000 (17 bits)
  512 KB =    524,288 = 10000000000000000000 (20 bits)
    1 MB =  1,048,576 = 100000000000000000000 (21 bits)
    8 MB =  8,388,608 = 100000000000000000000000 (24 bits)
```

#### b) Network Throughput

```
 128 Kbps =    128,000 bits/sec (17 bits)
   1 Mbps =  1,048,576 bits/sec (21 bits)
  10 Mbps = 10,485,760 bits/sec (24 bits)
```

#### c) Time Durations

```
1 second  =     1,000 ms (10 bits)
1 minute  =    60,000 ms (16 bits)
5 minutes =   300,000 ms (19 bits)
1 hour    = 3,600,000 ms (22 bits)
```

#### d) Image Dimensions

```
Full HD:  2,073,600 pixels (1920×1080) - 21 bits
2K:       3,686,400 pixels (2560×1440) - 22 bits
4K:       8,294,400 pixels (3840×2160) - 23 bits
```

---

## Algorithm Complexity

| Operation | Time | Space |
|-----------|------|-------|
| `binary_to_decimal()` | O(n) | O(1) |
| `decimal_to_binary()` | O(log m) | O(log m) |

Where:
- n = length of binary string
- m = decimal value

---

## Key Takeaways

1. **Utility Only:** Not used internally by calculator
2. **Convenient:** Easy conversion for display/verification
3. **Powers of 2:** Have very sparse representations
4. **Bit Growth:** Logarithmic with value
5. **Round-Trip Safe:** No data loss in conversions

---

## Next Steps

- [Example 06: BinaryNormalizer](example_06_binary_normalizer.md) - Normalization
- [Example 03: ArithmeticCalculator](example_03_arithmetic_calculator.md) - Pure binary arithmetic
- [Back to Index](index.md)

