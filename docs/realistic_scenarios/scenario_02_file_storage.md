# Scenario 02: File Storage Calculation

## Context

Disk space management and capacity planning require calculating total storage across multiple files. This scenario demonstrates adding two file sizes to determine total storage requirements.

## Real-World Application

**Situation:** A file system needs to allocate space for two large files.

- **File 1:** 524,288 bytes (512 KB, exactly 2^19)
- **File 2:** 786,432 bytes (768 KB, 3 × 2^18)
- **Goal:** Calculate total storage needed

## Executable Code

**File:** `examples/realistic_scenarios/scenario_02_file_storage.py`

**Run it:**
```bash
python examples/realistic_scenarios/scenario_02_file_storage.py
```

---

## Setup

### Code

```python title="Initialize executor"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:setup"
```

---

## Creating Operands

### Code

```python title="Create file size BinaryNumbers"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:create_operands"
```

### Binary Representation Analysis

#### File 1: 524,288 bytes (512 KB)

```
Decimal: 524,288
Factorization: 512 × 1,024 = 2^9 × 2^10 = 2^19

Binary conversion:
  524,288 = 1 × 2^19 + 0 × 2^18 + ... + 0 × 2^0

Result: 10000000000000000000 (20 bits)

Pattern: Exactly ONE bit set at position 19
```

#### File 2: 786,432 bytes (768 KB)

```
Decimal: 786,432
Factorization: 768 × 1,024 = (512+256) × 1,024 = 3 × 2^18

Binary conversion:
  786,432 = 1 × 2^19 + 1 × 2^18 + 0 × 2^17 + ...

Result: 11000000000000000000 (20 bits)

Pattern: TWO bits set (positions 19 and 18)
```

---

## Display Input

### Code

```python title="Display file information"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:display_input"
```

### Expected Console Output

```
File Storage Calculation
============================================================
File 1 size:  10000000000000000000
              (524288 bytes = 512 KB)
              Bit length: 20 bits

File 2 size:  11000000000000000000
              (786432 bytes = 768 KB)
              Bit length: 20 bits

```

---

## Create Instruction

### Code

```python title="Create addition instruction"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:create_instruction"
```

---

## Execute Calculation

### Code

```python title="Execute with formatted output"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:execute"
```

### Character-by-Character Processing

#### Step 1: Normalization

Both operands already have 20 bits - no padding needed!

```
File 1: 10000000000000000000
File 2: 11000000000000000000
```

#### Step 2: Bit-by-Bit Addition (Right to Left)

| Position | File 1 | File 2 | Carry In | Sum | Result | Carry Out |
|----------|--------|--------|----------|-----|--------|-----------|
| 19 (LSB) | 0 | 0 | 0 | 0 | 0 | 0 |
| 18 | 0 | 0 | 0 | 0 | 0 | 0 |
| ... | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 (MSB) | 1 | 1 | 0 | 2 | 0 | 1 |

**Most positions:** 0 + 0 = 0 (all trailing zeros)

**Position 1 (2^18):** 0 + 1 = 1

**Position 0 (2^19):** 1 + 1 = 2 → result bit = 0, carry = 1

**Final carry:** Prepends '1' to result

#### Step 3: Build Result

```
Built array: [0,0,0,...,0,1,0,0] with final carry '1'
Reversed with carry: '101000000000000000000'
```

**Result:** 21 bits (grows by one bit due to carry)

#### Decimal Verification

```
2^20 + 2^19 + 2^18 = 1,048,576 + 524,288 + 0 = ...

Wait, let me recalculate:
  File 1: 524,288 = 2^19
  File 2: 786,432 = 3 × 2^18 = 2^19 + 2^18

  Total: 2^19 + (2^19 + 2^18)
       = 2 × 2^19 + 2^18
       = 2^20 + 2^18
       = 1,048,576 + 262,144
       = 1,310,720
```

### Expected Console Output

```
Calculation:
   10000000000000000000
+  11000000000000000000
----------------------
  101000000000000000000
======================
```

---

## Display Result

### Code

```python title="Show totals"
--8<-- "examples/realistic_scenarios/scenario_02_file_storage.py:display_result"
```

### Expected Console Output

```
Total storage: 1310720 bytes
               1280 KB
               1.25 MB
Verification:  512 KB + 768 KB = 1280 KB
============================================================
```

---

## Complete Example Output

```
File Storage Calculation
============================================================
File 1 size:  10000000000000000000
              (524288 bytes = 512 KB)
              Bit length: 20 bits

File 2 size:  11000000000000000000
              (786432 bytes = 768 KB)
              Bit length: 20 bits

Calculation:
   10000000000000000000
+  11000000000000000000
----------------------
  101000000000000000000
======================

Total storage: 1310720 bytes
               1280 KB
               1.25 MB
Verification:  512 KB + 768 KB = 1280 KB
============================================================
```

---

## Binary Analysis

### Bit Pattern Observation

```
File 1: 10000000000000000000  (only bit 19 set)
File 2: 11000000000000000000  (bits 19 and 18 set)
Result: 101000000000000000000 (bits 20 and 18 set)
```

**Why bit 20?**
```
Position 19: 1 + 1 = 2 (binary 10)
  → result bit = 0, carry = 1
Carry goes to position 20
```

---

## Algorithm Complexity

- **Time:** O(20) - constant for these specific values
- **Space:** O(21) - result has 21 bits
- **Operations:** 20 bit additions + 1 carry

---

## Key Learning Points

1. **Bit Growth:** Result can be one bit longer than operands
2. **Powers of 2:** Clean binary patterns
3. **Multiples:** 768 = 3 × 256 shows multiple bits set
4. **Carry Propagation:** Creates new bit position
5. **Real Storage:** Common file system calculations

---

## Next Steps

- [Scenario 01: Memory Address](scenario_01_memory_address.md) - Memory calculation
- [Scenario 03: Network Bandwidth](scenario_03_network_bandwidth.md) - Division example
- [Back to Overview](index.md)

