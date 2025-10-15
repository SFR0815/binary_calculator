# Scenario 03: Network Bandwidth Calculation

## Context

Network capacity planning requires calculating how many packets can be transmitted per second given a specific throughput and packet size. This scenario demonstrates division of large numbers.

## Real-World Application

**Situation:** A network engineer needs to determine packet throughput capacity.

- **Throughput:** 1,048,576 bits/second (1 Mbps, exactly 2^20)
- **Packet Size:** 8,192 bits (1024 bytes, 2^13)
- **Goal:** Calculate packets per second

## Executable Code

**File:** `examples/realistic_scenarios/scenario_03_network_bandwidth.py`

**Run it:**
```bash
python examples/realistic_scenarios/scenario_03_network_bandwidth.py
```

---

## Setup

### Code

```python title="Initialize executor"
--8<-- "examples/realistic_scenarios/scenario_03_network_bandwidth.py:setup"
```

---

## Creating Operands

### Code

```python title="Create throughput and packet size"
--8<-- "examples/realistic_scenarios/scenario_03_network_bandwidth.py:create_operands"
```

### Binary Representation Analysis

#### Throughput: 1,048,576 bits/sec

```
Decimal: 1,048,576
Factorization: 2^20 (1 megabit exactly)

Binary conversion:
  1,048,576 = 1 × 2^20 + 0 × 2^19 + ... + 0 × 2^0

Result: 100000000000000000000 (21 bits)

Pattern: ONE bit set at position 20
```

#### Packet Size: 8,192 bits

```
Decimal: 8,192
Factorization: 2^13 (8 kilobits)

Binary conversion:
  8,192 = 1 × 2^13 + 0 × 2^12 + ... + 0 × 2^0

Result: 10000000000000 (14 bits)

Pattern: ONE bit set at position 13
```

---

## Display Input

### Code

```python title="Display network parameters"
--8<-- "examples/realistic_scenarios/scenario_03_network_bandwidth.py:display_input"
```

### Expected Console Output

```
Network Bandwidth Calculation
============================================================
Throughput:   100000000000000000000
              (1048576 bits/sec)
              (1024 Kbps)
              (1 Mbps)
              Bit length: 21 bits

Packet size:  10000000000000
              (8192 bits)
              (1024 bytes)
              Bit length: 14 bits

```

---

## Execute Calculation

### Code

```python title="Execute division"
--8<-- "examples/realistic_scenarios/scenario_03_network_bandwidth.py:execute"
```

### Binary Long Division Processing

#### Overview

Dividing 21-bit number by 14-bit number using binary long division algorithm.

```
Dividend: 100000000000000000000 (21 bits)
Divisor:  10000000000000       (14 bits)
```

#### Step-by-Step Division

The algorithm processes the dividend left to right, bringing down one bit at a time:

```
Bits 0-12: Building remainder
  Remainder grows: 1, 10, 100, ..., 1000000000000
  All < 10000000000000 (divisor)
  Quotient so far: 0000000000000 (13 zeros)

Bit 13: Remainder = 10000000000000
  Compare: 10000000000000 >= 10000000000000 ✓ (equal!)
  Subtract: 10000000000000 - 10000000000000 = 0
  Quotient += '1'
  
Bits 14-20: All zeros
  Remainder stays 0
  All comparisons: 0 < divisor
  Quotient += '0000000' (7 zeros)

Final quotient: 00000000000000010000000
Remove leading zeros: 10000000 (8 bits)
```

#### Why It's Exactly 128

```
2^20 ÷ 2^13 = 2^(20-13) = 2^7 = 128

Binary: 10000000 (8 bits, bit 7 set)
```

**Division of powers of 2:** Subtract exponents!

### Expected Console Output

```
Calculation:
  100000000000000000000
/   10000000000000
---------------------
            10000000
=====================
```

---

## Display Result

### Code

```python title="Show packets per second"
--8<-- "examples/realistic_scenarios/scenario_03_network_bandwidth.py:display_result"
```

### Expected Console Output

```
Packets per second: 128
Verification:       128 packets/sec
============================================================
```

---

## Complete Example Output

```
Network Bandwidth Calculation
============================================================
Throughput:   100000000000000000000
              (1048576 bits/sec)
              (1024 Kbps)
              (1 Mbps)
              Bit length: 21 bits

Packet size:  10000000000000
              (8192 bits)
              (1024 bytes)
              Bit length: 14 bits

Calculation:
  100000000000000000000
/   10000000000000
---------------------
            10000000
=====================

Packets per second: 128
Verification:       128 packets/sec
============================================================
```

---

## Mathematical Analysis

### Powers of 2 Division

When dividing powers of 2:
```
2^a ÷ 2^b = 2^(a-b)

In this case:
  2^20 ÷ 2^13 = 2^7 = 128
```

**Binary pattern:**
```
Result: 2^7 = 10000000 (8 bits)
```

### Bit Length Relationship

```
Dividend bits:  21
Divisor bits:   14
Result bits:    21 - 14 + 1 = 8

General rule for powers of 2:
  (a+1) - (b+1) + 1 = a - b + 1
```

---

## Algorithm Complexity

- **Time:** O(n × m) where n=21 (dividend bits), m=14 (divisor bits)
- **Space:** O(max(n, m))
- **Operations:** 21 iterations × comparison + subtraction

For this specific case:
- **Iterations:** 21
- **Comparisons:** 21
- **Subtractions:** 1 (only at bit 13 where remainder == divisor)

---

## Real-World Implications

### Network Planning

**Given:**
- Link capacity: 1 Mbps
- Packet overhead: 1024 bytes per packet

**Calculate:**
- Maximum packets/sec: 128
- Per-packet transmission time: 1/128 sec ≈ 7.8 ms
- Useful for QoS planning and buffer sizing

### Why Binary Division is Efficient

For powers of 2:
- Most comparisons are trivial (0 < divisor)
- Only ONE subtraction needed
- Result is immediate from exponent difference

---

## Key Learning Points

1. **Division Scales:** Handles 21-bit by 14-bit efficiently
2. **Powers of 2:** Extremely efficient division
3. **Sparse Operations:** Most comparisons resolve quickly
4. **Real Throughput:** Common network calculation
5. **Bit Length Math:** Quotient bits ≈ dividend bits - divisor bits

---

## Next Steps

- [Scenario 01: Memory Address](scenario_01_memory_address.md) - Addition example
- [Scenario 02: File Storage](scenario_02_file_storage.md) - Another addition
- [Back to Overview](index.md)

