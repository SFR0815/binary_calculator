# Basic Examples - Component-by-Component Guide

This directory contains focused examples demonstrating each component of the binary calculator system, from simple operations to realistic scenarios with larger numbers.

## 📚 Example Structure

Each example follows a consistent pattern:

1. **Simple demonstrations** - Basic usage with small numbers (under 100)
2. **Error handling** - Common edge cases and validation
3. **Larger numbers** - Realistic scenarios (thousands to millions)

## 📁 Available Examples

### Example 01: BinaryNumber
**File:** `example_01_binary_number.py`

**Demonstrates:**
- Creating from binary string and integers
- Converting to/from integers
- Increment and decrement operations
- Copy operation
- Comparison operators
- Working with large numbers (65K, 1MB)

**Key Concepts:**
- Encapsulation of binary values
- In-place modifications
- Comparison using BinaryComparator internally

**Run:**
```bash
python examples/basic/example_01_binary_number.py
```

---

### Example 02: BinaryInstruction
**File:** `example_02_binary_instruction.py`

**Demonstrates:**
- Creating arithmetic instructions (+, -, *, /)
- Creating comparison instructions (<, <=, >, >=, ==, !=)
- Instruction state management
- Representation with proper indentation
- Instructions with large numbers (512KB, 768KB)

**Key Concepts:**
- Validation of operands and operations
- Automatic state detection
- Two-line repr format with right-alignment

**Run:**
```bash
python examples/basic/example_02_binary_instruction.py
```

---

### Example 03: ArithmeticCalculator
**File:** `example_03_arithmetic_calculator.py`

**Demonstrates:**
- Addition, subtraction, multiplication, division
- Chained operations
- Error handling (division by zero, negative results)
- Real-world calculations (memory addresses, file sizes, network throughput, image dimensions)

**Key Concepts:**
- Pure binary arithmetic algorithms
- Character-by-character processing
- No decimal conversion during calculation

**Run:**
```bash
python examples/basic/example_03_arithmetic_calculator.py
```

**Realistic Scenarios Included:**
- Memory address: 65,536 + 4,096
- File storage: 512 KB + 768 KB
- Network: 1 Mbps / 8192 bits
- Images: 1920 × 1080 pixels

---

### Example 04: BinaryComparator
**File:** `example_04_binary_comparator.py`

**Demonstrates:**
- Basic compare() method (-1, 0, 1)
- All comparison operations (6 types)
- Leading zero handling
- Large number comparisons (performance checks, memory capacity, time limits)

**Key Concepts:**
- Length-based comparison
- Lexicographic comparison for same length
- No decimal conversion

**Run:**
```bash
python examples/basic/example_04_binary_comparator.py
```

**Realistic Scenarios Included:**
- Performance: 750,000 ops/sec vs 500,000 threshold
- Memory: 8 MB available vs 512 KB required
- Time: 300,000 ms vs 60,000 ms limit

---

### Example 05: BinaryConverter
**File:** `example_05_binary_converter.py`

**Demonstrates:**
- Binary to decimal conversion
- Decimal to binary conversion
- Round-trip verification
- Powers of 2 analysis
- Large number representations
- Realistic conversions (memory sizes, network speeds, time durations, image dimensions)

**Key Concepts:**
- Utility conversions (not used internally)
- Binary representation efficiency
- Bit length analysis

**Run:**
```bash
python examples/basic/example_05_binary_converter.py
```

**Realistic Scenarios Included:**
- Memory: 1 KB to 8 MB
- Network: 128 Kbps to 10 Mbps
- Time: 1 second to 1 hour
- Images: Full HD to 4K resolutions

---

### Example 06: BinaryNormalizer
**File:** `example_06_binary_normalizer.py`

**Demonstrates:**
- Removing leading zeros
- Normalizing lengths for bit-wise operations
- Practical use cases
- Edge cases
- Large number normalization (memory addresses, file sizes, network calculations)

**Key Concepts:**
- Preparation for binary operations
- Length matching with zero-padding
- Leading zero removal for comparisons

**Run:**
```bash
python examples/basic/example_06_binary_normalizer.py
```

**Realistic Scenarios Included:**
- Memory addresses: 65,536 and 4,096
- File sizes: 512 KB and 768 KB
- Network: 1 Mbps bandwidth vs 8192-bit packets

---

### Example 07: InstructionExecutor
**File:** `example_07_instruction_executor.py`

**Demonstrates:**
- Executing calculations (with/without formatted output)
- Executing comparisons
- All arithmetic operations
- All comparison operations
- Error handling
- Real-world scenarios (memory, storage, network, performance)

**Key Concepts:**
- Routing to appropriate calculator
- Formatted output with `print_result=True`
- Type validation (CALCULATE vs COMPARE)

**Run:**
```bash
python examples/basic/example_07_instruction_executor.py
```

**Realistic Scenarios Included:**
- Memory: 65,536 + 4,096
- Storage: 512 KB + 768 KB
- Network: 1 Mbps / 8192 bits
- Performance: 750,000 >= 500,000

---

## 🎯 Quick Reference

| Component | Primary Function | Example File |
|-----------|-----------------|--------------|
| BinaryNumber | Encapsulate binary values | `example_01_*.py` |
| BinaryInstruction | Validate & store operations | `example_02_*.py` |
| ArithmeticCalculator | Perform arithmetic | `example_03_*.py` |
| BinaryComparator | Compare binary values | `example_04_*.py` |
| BinaryConverter | Convert binary ↔ decimal | `example_05_*.py` |
| BinaryNormalizer | Normalize representations | `example_06_*.py` |
| InstructionExecutor | Execute instructions | `example_07_*.py` |

## 🚀 Running All Examples

**Run all basic examples:**

### Windows
```cmd
for %f in (examples\basic\example_*.py) do python "%f"
```

### Linux/Mac
```bash
for file in examples/basic/example_*.py; do
    python "$file"
done
```

## 📊 Example Progression

### Level 1: Fundamentals (Small Numbers)
Each example starts with simple operations using small numbers (< 100) to demonstrate core concepts clearly.

**Example output:**
```
1010 + 101 = 1111
(10 + 5 = 15 in decimal)
```

### Level 2: Error Handling
Each example includes error scenarios to show proper validation and exception handling.

**Example output:**
```
[OK] Caught ValueError: Cannot divide by zero
```

### Level 3: Realistic Scenarios (Large Numbers)
Each example concludes with practical use cases using realistic numbers (1,000 - 1,000,000).

**Example output:**
```
Memory address: 65,536 + 4,096 = 69,632 bytes (0x11000)
File storage: 512 KB + 768 KB = 1,280 KB (1.25 MB)
```

## 🔍 Learning Path

**Recommended order for beginners:**

1. **Start here:** `example_01_binary_number.py` - Core data structure
2. **Then:** `example_02_binary_instruction.py` - How operations are defined
3. **Next:** `example_07_instruction_executor.py` - How instructions are executed
4. **Deep dive:** `example_03_arithmetic_calculator.py` - Arithmetic algorithms
5. **Understand:** `example_04_binary_comparator.py` - Comparison logic
6. **Optional:** `example_05_binary_converter.py` - Utility conversions
7. **Advanced:** `example_06_binary_normalizer.py` - Internal normalization

## 💡 Key Takeaways

### Design Patterns
- **Encapsulation:** BinaryNumber wraps binary strings
- **Validation:** BinaryInstruction validates on creation
- **Delegation:** InstructionExecutor routes to appropriate calculators
- **Pure Functions:** Calculators work directly on binary

### Performance Characteristics
- **Linear operations:** Addition, subtraction, comparison = O(n) where n = bit length
- **Quadratic operations:** Multiplication, division = O(n²)
- **Efficient for powers of 2:** Sparse binary representations

### Real-World Applications
- Memory management (addresses, allocation)
- File system operations (sizes, capacities)
- Network calculations (throughput, packets)
- Image processing (dimensions, memory requirements)
- Performance monitoring (thresholds, checks)

## 📚 Related Documentation

- **Realistic Scenarios:** `../realistic_scenarios/` - Complete end-to-end examples
- **Full Documentation:** `../../docs/` - MkDocs documentation with code imports
- **Architecture:** `../../ARCHITECTURE.md` - System design overview
- **Main Example:** `../../example.py` - Comprehensive demonstration

## 🎓 Next Steps

After mastering these basic examples:

1. Explore `../realistic_scenarios/` for complete use cases
2. Read the MkDocs documentation at `../../docs/`
3. Try modifying examples to experiment
4. Create your own scenarios
5. Contribute new examples!

---

**All examples are fully executable and include detailed comments!**

