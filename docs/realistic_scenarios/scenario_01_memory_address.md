# Scenario 01: Memory Address Calculation

## Context

Operating systems frequently need to calculate memory addresses by adding a base address to an offset. This is fundamental for:

- Memory allocation
- Pointer arithmetic
- Address space layout
- Page table management

## Real-World Application

**Situation:** You're implementing a memory allocator that needs to calculate the final address for a data structure.

- **Base Address:** 65,536 bytes (0x10000) - typical 16-bit boundary
- **Offset:** 4,096 bytes - size of one memory page
- **Goal:** Calculate the final memory address

## Executable Code

**File:** `examples/realistic_scenarios/scenario_01_memory_address.py`

### Imports and Setup

```python title="Setup executor" linenums="1"
--8<-- "examples/realistic_scenarios/scenario_01_memory_address.py:setup"
```

!!! info "InstructionExecutor"
    The executor routes instructions to the appropriate calculator (arithmetic or comparison) based on the operation type.

### Creating Operands

```python title="Create BinaryNumber objects" linenums="1"
--8<-- "examples/realistic_scenarios/scenario_01_memory_address.py:create_operands"
```

!!! tip "from_int() Method"
    The `from_int()` class method converts decimal integers to binary using Python's `bin()` function, then strips the '0b' prefix.
    
    **Processing:**
    
    1. `65536` → `bin(65536)` → `'0b10000000000000000'`
    2. Strip prefix → `'10000000000000000'`
    3. Create BinaryNumber with validated string

### Creating the Instruction

```python title="Build instruction" linenums="1"
--8<-- "examples/realistic_scenarios/scenario_01_memory_address.py:create_instruction"
```

!!! info "BinaryInstruction"
    Validates operands are BinaryNumber instances and operation is supported. Automatically determines instruction state (CALCULATE vs COMPARE).

### Executing the Calculation

```python title="Execute and display" linenums="1"
--8<-- "examples/realistic_scenarios/scenario_01_memory_address.py:execute"
```

## Character-by-Character Processing

When `executor.calculate()` is called with `print_result=True`, it performs these steps:

### Step 1: Validation
- Checks instruction is CALCULATE type (not COMPARE)
- Maps '+' operation to `ArithmeticCalculator.add()` method

### Step 2: Normalization

The `add()` method normalizes operand lengths:

```
Input lengths:
  base:   10000000000000000  (17 bits)
  offset: 1000000000000      (13 bits)

After normalization (pad offset with leading zeros):
  base:   10000000000000000  (17 bits)
  offset: 00001000000000000  (17 bits, prepended 4 zeros)
```

### Step 3: Bit-by-Bit Addition (Right to Left)

Addition processes from **rightmost bit (position 16)** to **leftmost (position 0)**:

| Position | Base | Offset | Carry In | Sum | Result Bit | Carry Out |
|----------|------|--------|----------|-----|------------|-----------|
| 16       | 0    | 0      | 0        | 0   | 0          | 0         |
| 15       | 0    | 0      | 0        | 0   | 0          | 0         |
| 14       | 0    | 0      | 0        | 0   | 0          | 0         |
| 13       | 0    | 0      | 0        | 0   | 0          | 0         |
| 12       | 0    | 1      | 0        | 1   | 1          | 0         |
| 11-1     | 0    | 0      | 0        | 0   | 0          | 0         |
| 0        | 1    | 0      | 0        | 1   | 1          | 0         |

!!! note "Sparse Calculations"
    Most bits are 0+0=0! Only positions 0 and 12 have actual work. This is common when adding powers of 2.

### Step 4: Result Array Construction

The algorithm builds the result backwards (right to left), then reverses:

```
Built array: [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
Reversed:    10001000000000000
```

### Step 5: Create BinaryNumber

```python
result_binary = '10001000000000000'
return BinaryNumber(binary_str=result_binary)
```

## Expected Console Output

```
Memory Address Calculation
============================================================
Base address: 10000000000000000
              (65536 bytes, 0x10000)
              Bit length: 17 bits

Offset:       1000000000000
              (4096 bytes, 0x1000)
              Bit length: 13 bits

Calculation:
  10000000000000000
+  1000000000000
-----------------
  10001000000000000
=================

Final address: 69632 bytes
               (0x11000)
Verification:  69632 = 69632
============================================================
```

!!! success "Formatted Output Explanation"
    The formatted output shows:
    
    - **Line 1:** First operand (right-aligned)
    - **Line 2:** Operation symbol + second operand (right-aligned)
    - **Separator:** Dashes matching total width
    - **Line 3:** Result (right-aligned with proper indentation)
    - **Final separator:** Equals signs

## Verification

### Decimal Check
```python
65536 + 4096 = 69632  ✓
```

### Hexadecimal Check
```python
0x10000 + 0x1000 = 0x11000  ✓
```

### Binary Check
```
10000000000000000₂ + 1000000000000₂ = 10001000000000000₂  ✓
```

## Algorithm Complexity

- **Time:** O(17) - linear in max bit length
- **Space:** O(17) - for normalized operands and result
- **Bit Operations:** 17 additions + normalization

## Key Learning Points

1. **Binary Efficiency:** 65,536 only needs 17 bits (vs 6 decimal digits)
2. **Normalization:** Critical for bit-wise operations
3. **Carry Propagation:** Most carries are 0 with sparse binaries
4. **Powers of 2:** Have very clean binary representations
5. **Memory Alignment:** Common in systems programming

## Running This Example

```bash
python examples/realistic_scenarios/scenario_01_memory_address.py
```

