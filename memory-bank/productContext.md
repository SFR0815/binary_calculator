# Product Context: Binary Calculator

## Why This Project Exists
Educational demonstration of pure binary arithmetic algorithms, showing how computers perform calculations at the bit level without relying on built-in decimal conversion.

## Problems It Solves
1. **Understanding Binary Arithmetic**: Shows step-by-step how binary addition, subtraction, multiplication, and division work
2. **Algorithm Demonstration**: Provides clear implementations of classic algorithms (carry propagation, borrow handling, shift-and-add, long division)
3. **Learning Tool**: Extensive examples with detailed comments explain every operation
4. **Reference Implementation**: Clean, well-structured code following Python best practices

## How It Works

### Core Concept
All operations work directly on binary strings (sequences of '0' and '1' characters) without converting to decimal integers internally.

### Example Flow
```python
# User creates binary numbers
num1 = BinaryNumber(binary_str='1010')  # 10 in decimal
num2 = BinaryNumber(binary_str='101')   # 5 in decimal

# Calculator performs pure binary addition
calculator = ArithmeticCalculator()
result = calculator.add(operand_1=num1, operand_2=num2)
# Result: '1111' (15 in decimal)

# Or use instruction-based approach
instruction = BinaryInstruction(
    operand_1=num1,
    operand_2=num2,
    operation='+')

executor = InstructionExecutor()
result = executor.calculate(instruction=instruction, print_result=True)
# Prints formatted output:
#   1010
# +  101
# ------
#   1111
# ======
```

### User Experience Goals
1. **Easy Discovery**: CLI with `--list` shows all 53 examples
2. **Quick Access**: Run any example with simple command (`python example.py calc03`)
3. **Clear Documentation**: Every example shows exactly how to run it
4. **Visual Learning**: Formatted output shows operations step-by-step
5. **Colorful Code**: Syntax-highlighted documentation makes code easy to read

## Target Audience
- Computer Science students learning binary arithmetic
- Developers wanting to understand low-level operations
- Educators teaching binary number systems
- Anyone curious about how computers do math

