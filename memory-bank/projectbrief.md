# Project Brief: Binary Calculator

## Project Overview
A comprehensive Python library for pure binary arithmetic operations without decimal conversion. Demonstrates binary algorithms through clean, well-documented code with extensive examples and documentation.

## Core Objectives
1. Implement pure binary arithmetic (addition, subtraction, multiplication, division)
2. Provide binary comparison operations
3. Offer binary-decimal conversion utilities
4. Create a comprehensive example system with CLI runner
5. Generate professional documentation with MkDocs

## Key Components
- **BinaryNumber**: Encapsulates binary values with validation
- **BinaryInstruction**: Represents operations with operands
- **ArithmeticCalculator**: Pure binary arithmetic algorithms
- **BinaryComparator**: Binary comparison operations
- **BinaryConverter**: Binary ↔ Decimal conversions
- **BinaryNormalizer**: Binary string normalization
- **InstructionExecutor**: Executes instructions with formatted output

## Project Structure
```
binary_calculator/
├── binary_calculator/          # Main package
│   ├── calculator/            # Arithmetic operations
│   ├── comparator/            # Comparison operations
│   ├── converter/             # Conversion utilities
│   ├── executor/              # Instruction execution
│   ├── instruction/           # Instruction & operation definitions
│   └── normalizer/            # Binary normalization
├── examples/                  # Executable examples
│   ├── example.py            # CLI runner (53 examples)
│   └── basic/                # 7 example modules
├── docs/                     # MkDocs documentation
│   ├── basic/                # Example documentation (7 files)
│   └── stylesheets/          # Custom CSS for syntax highlighting
└── tests/                    # Unit tests
```

## Technical Stack
- **Language**: Python 3.x
- **Documentation**: MkDocs with Material theme
- **Testing**: unittest framework
- **Package Management**: setuptools

## Success Criteria
✅ All binary operations work without decimal conversion
✅ 53 individual examples accessible via CLI
✅ Complete documentation with colorful syntax highlighting
✅ All examples run independently or in groups
✅ Professional package structure ready for distribution

