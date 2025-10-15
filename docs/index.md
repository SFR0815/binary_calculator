# Binary Calculator Examples

Welcome to the comprehensive examples documentation for the Binary Calculator system.

## Overview

This documentation provides detailed walkthroughs of realistic scenarios using the binary calculator. Each example demonstrates:

- Clean, executable Python code
- Real-world applications
- Bit-by-bit processing explanations
- Expected console outputs
- Verification against decimal arithmetic

## Example Categories

### Basic Examples

Component-by-component demonstrations, each with simple operations, error handling, and larger number scenarios:

- [01 - BinaryNumber](basic/example_01_binary_number.md) - Core data structure
- [02 - BinaryInstruction](basic/example_02_binary_instruction.md) - Instruction validation
- [03 - ArithmeticCalculator](basic/example_03_arithmetic_calculator.md) - Pure binary arithmetic
- [04 - BinaryComparator](basic/example_04_binary_comparator.md) - Comparison logic
- [05 - BinaryConverter](basic/example_05_binary_converter.md) - Conversion utilities
- [06 - BinaryNormalizer](basic/example_06_binary_normalizer.md) - String normalization
- [07 - InstructionExecutor](basic/example_07_instruction_executor.md) - Execution engine

[**Browse all basic examples →**](basic/index.md)

### Realistic Scenarios

Complete end-to-end examples with large numbers (1,000 - 1,000,000 range) demonstrating practical computing use cases:

- [01 - Memory Address Calculation](realistic_scenarios/scenario_01_memory_address.md) - OS memory management
- [02 - File Storage Calculation](realistic_scenarios/scenario_02_file_storage.md) - Disk space planning
- [03 - Network Bandwidth Calculation](realistic_scenarios/scenario_03_network_bandwidth.md) - Throughput analysis

[**Browse all realistic scenarios →**](realistic_scenarios/index.md)

## Quick Start

### Running Examples

```bash
# Install dependencies
pip install -r requirements.txt

# Run individual example
python examples/realistic_scenarios/scenario_01_memory_address.py

# View documentation locally
pip install -r requirements-docs.txt
mkdocs serve
```

### Documentation Features

!!! info "Live Code References"
    All code shown in this documentation is **automatically imported** from the actual Python files. 
    When code changes, documentation updates automatically - no duplication!

## Key Concepts

### BinaryNumber
Encapsulates binary string values with methods for conversion and manipulation.

### BinaryInstruction
Validates and stores operation details (operands + operation).

### InstructionExecutor
Routes instructions to appropriate calculators and optionally displays formatted results.

## Navigation

Use the navigation menu to explore specific scenarios. Each page includes:

- ✅ Context and real-world application
- ✅ Executable code (imported from source)
- ✅ Character-by-character processing explanation  
- ✅ Expected console output
- ✅ Verification calculations

