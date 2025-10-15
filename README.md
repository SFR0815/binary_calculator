# Binary Calculator

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: Type Hints](https://img.shields.io/badge/code%20style-type%20hints-brightgreen.svg)](https://docs.python.org/3/library/typing.html)

A comprehensive Python library for **pure binary arithmetic operations** without decimal conversion. Perfect for learning how computers perform calculations at the bit level!

## 🌟 Features

- **Pure Binary Arithmetic**: All operations work directly on binary strings
- **7 Core Components**: Number, Instruction, Calculator, Comparator, Converter, Normalizer, Executor
- **53 Runnable Examples**: Extensive example library with CLI runner
- **Zero Dependencies**: Core library uses only Python standard library
- **Type-Safe**: Complete type hints throughout
- **Well-Documented**: Comprehensive MkDocs documentation with colorful syntax highlighting
- **Educational**: Detailed comments explaining every algorithm step

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/SFR0815/binary_calculator.git
cd binary_calculator

# Install (optional, for documentation)
pip install -e ".[docs]"
```

### Basic Usage

```python
from binary_calculator import BinaryNumber, ArithmeticCalculator

# Create binary numbers
num1 = BinaryNumber(binary_str='1010')  # 10 in decimal
num2 = BinaryNumber(binary_str='101')   # 5 in decimal

# Perform pure binary addition
calculator = ArithmeticCalculator()
result = calculator.add(operand_1=num1, operand_2=num2)

print(result.value)    # Output: '1111'
print(result.to_int()) # Output: 15
```

### Run Examples

```bash
# List all 53 examples
python example.py --list

# Run specific example
python example.py numb01      # BinaryNumber basics
python example.py calc03      # Multiplication
python example.py exec09      # Executor with large numbers

# Run all examples from a component
python example.py --all-calc  # All calculator examples

# Run everything
python example.py --all
```

## 📚 Documentation

Build and serve the documentation locally:

```bash
pip install -r requirements-docs.txt
python -m mkdocs serve
```

Then open http://127.0.0.1:8000

## 🎯 Core Components

### BinaryNumber
Encapsulates binary string values with validation, conversion, and arithmetic operations.

```python
num = BinaryNumber(binary_str='1010')
num.incr()  # In-place increment
print(num.value)  # '1011'
```

### ArithmeticCalculator
Pure binary arithmetic without decimal conversion.

```python
calc = ArithmeticCalculator()
result = calc.multiply(
    operand_1=BinaryNumber(binary_str='101'),
    operand_2=BinaryNumber(binary_str='11'))
# Uses shift-and-add algorithm: '101' * '11' = '1111'
```

### BinaryInstruction
Encapsulates operations with formatted output.

```python
from binary_calculator import BinaryInstruction, InstructionExecutor

instruction = BinaryInstruction(
    operand_1=BinaryNumber(binary_str='1010'),
    operand_2=BinaryNumber(binary_str='101'),
    operation='+')

executor = InstructionExecutor()
result = executor.calculate(instruction=instruction, print_result=True)
# Output:
#   1010
# +  101
# ------
#   1111
# ======
```

## 📖 Example Categories

- **BinaryNumber** (9 examples): numb01-numb09
- **BinaryInstruction** (6 examples): inst01-inst06
- **ArithmeticCalculator** (7 examples): calc01-calc07
- **BinaryComparator** (9 examples): comp01-comp09
- **BinaryConverter** (7 examples): conv01-conv07
- **BinaryNormalizer** (6 examples): norm01-norm06
- **InstructionExecutor** (9 examples): exec01-exec09

## 🧮 Algorithms Implemented

- **Addition**: Bit-by-bit with carry propagation
- **Subtraction**: Bit-by-bit with borrow handling
- **Multiplication**: Shift-and-add algorithm
- **Division**: Binary long division
- **Comparison**: Length-based with lexicographic fallback
- **Normalization**: Leading zero removal and length equalization

## 🧪 Testing

```bash
# Run all tests
python -m unittest discover

# Run specific test module
python -m unittest test_binary_calculator

# Run specific test
python -m unittest test_binary_calculator.TestArithmeticCalculator.test_01_addition
```

## 📦 Package Structure

```
binary_calculator/
├── binary_calculator/          # Main package
│   ├── calculator/            # Arithmetic operations
│   ├── comparator/            # Binary comparisons
│   ├── converter/             # Binary ↔ Decimal
│   ├── executor/              # Instruction execution
│   ├── instruction/           # Instructions & operations
│   └── normalizer/            # Binary normalization
├── examples/                  # 53 runnable examples
│   ├── example.py            # CLI runner
│   ├── basic/                # 7 example modules
│   └── realistic_scenarios/  # 3 real-world scenarios
├── docs/                     # MkDocs documentation
├── tests/                    # Unit tests
└── memory-bank/              # Project documentation
```

## 🎓 Educational Value

This project demonstrates:
- How binary arithmetic actually works
- Classic computer science algorithms
- Clean Python code organization
- Type-safe programming with type hints
- Comprehensive documentation practices
- Test-driven development

## 🤝 Contributing

This is an educational project. Feel free to:
- Report bugs or suggest improvements
- Add more examples
- Improve documentation
- Optimize algorithms (while maintaining educational clarity)

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [GitHub Pages](https://SFR0815.github.io/binary_calculator) (after deployment)
- **Examples**: See `examples/` directory or run `python example.py --list`
- **Tests**: See `test_*.py` files

## ⭐ Project Statistics

- **Lines of Code**: 13,000+
- **Functions**: 53 examples + 50+ class methods
- **Test Cases**: 7 test files with 20+ test methods
- **Documentation Pages**: 11 pages
- **Examples**: 53 individual runnable examples

## 🚀 Next Steps

1. Explore the examples: `python example.py --list`
2. Read the documentation: `python -m mkdocs serve`
3. Run the tests: `python -m unittest discover`
4. Study the algorithms in `binary_calculator/calculator/`

---

**Built with ❤️ for learning binary arithmetic**
