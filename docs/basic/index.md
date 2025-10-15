# Basic Examples - Component Guide

Welcome to the basic examples section! These examples demonstrate each component of the binary calculator system, progressing from simple operations to realistic scenarios with larger numbers.

## Overview

Each example follows a consistent pattern:

1. **Simple demonstrations** - Basic usage with small numbers (< 100)
2. **Error handling** - Common edge cases and validation
3. **Larger numbers** - Realistic scenarios (1,000 - 1,000,000)

All code is **executable and fully tested**. The documentation imports code directly from the Python files - **no duplication!**

## Available Examples

### [01 - BinaryNumber](example_01_binary_number.md)
**Component:** Core data structure  
**Demonstrates:** Creating, converting, incrementing, comparing  
**File:** `examples/basic/example_01_binary_number.py`

### [02 - BinaryInstruction](example_02_binary_instruction.md)
**Component:** Instruction validation and formatting  
**Demonstrates:** Creating instructions, state management, representation  
**File:** `examples/basic/example_02_binary_instruction.py`

### [03 - ArithmeticCalculator](example_03_arithmetic_calculator.md)
**Component:** Pure binary arithmetic  
**Demonstrates:** Add, subtract, multiply, divide operations  
**File:** `examples/basic/example_03_arithmetic_calculator.py`

### [04 - BinaryComparator](example_04_binary_comparator.md)
**Component:** Binary comparison logic  
**Demonstrates:** All 6 comparison operations  
**File:** `examples/basic/example_04_binary_comparator.py`

### [05 - BinaryConverter](example_05_binary_converter.md)
**Component:** Binary ↔ Decimal conversion  
**Demonstrates:** Utility conversions, round-trip verification  
**File:** `examples/basic/example_05_binary_converter.py`

### [06 - BinaryNormalizer](example_06_binary_normalizer.md)
**Component:** Binary string normalization  
**Demonstrates:** Leading zero removal, length matching  
**File:** `examples/basic/example_06_binary_normalizer.py`

### [07 - InstructionExecutor](example_07_instruction_executor.md)
**Component:** Instruction execution engine  
**Demonstrates:** Executing instructions with formatted output  
**File:** `examples/basic/example_07_instruction_executor.py`

## Quick Start

### Run All Examples

```bash
# Windows
for %f in (examples\basic\example_*.py) do python "%f"

# Linux/Mac
for file in examples/basic/example_*.py; do python "$file"; done
```

### Run Individual Example

```bash
python examples/basic/example_01_binary_number.py
```

## Documentation Features

!!! info "Live Code Imports"
    All code shown in this documentation is **automatically imported** from the actual Python files using MkDocs snippets.
    
    When the Python code changes, the documentation updates automatically!

Each documentation page includes:

- ✅ **What This Does** - Clear operation explanation
- ✅ **Input** - Data that goes into the operation
- ✅ **Processing Steps** - Detailed step-by-step walkthrough
- ✅ **Character-by-Character** - Bit-level processing details
- ✅ **Expected Output** - Exact console output
- ✅ **Return Values** - Type and structure information
- ✅ **Algorithm Complexity** - Time and space analysis

## Learning Path

**Recommended order:**

1. **[BinaryNumber](example_01_binary_number.md)** - Start here, learn the core data structure
2. **[BinaryInstruction](example_02_binary_instruction.md)** - Understand how operations are defined
3. **[InstructionExecutor](example_07_instruction_executor.md)** - See how instructions are executed
4. **[ArithmeticCalculator](example_03_arithmetic_calculator.md)** - Deep dive into arithmetic algorithms
5. **[BinaryComparator](example_04_binary_comparator.md)** - Understand comparison logic
6. **[BinaryConverter](example_05_binary_converter.md)** - Learn utility conversions
7. **[BinaryNormalizer](example_06_binary_normalizer.md)** - See internal normalization

## Key Concepts

### Encapsulation
`BinaryNumber` wraps binary strings with validation and methods.

### Validation
`BinaryInstruction` validates operands and operations on creation.

### Delegation  
`InstructionExecutor` routes to appropriate calculators.

### Pure Binary
Calculations work directly on binary strings, no decimal conversion.

## Next Steps

After mastering these basics:

- Explore [Realistic Scenarios](../realistic_scenarios/index.md) for complete use cases
- View the full documentation at the [Home Page](../index.md)
- Try modifying examples to experiment
- Create your own scenarios!

