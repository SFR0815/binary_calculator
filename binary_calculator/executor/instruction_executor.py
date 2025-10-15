"""Instruction executor class for executing binary instructions."""

import typing as p_typ
from ..calculator.arithmetic_calculator import ArithmeticCalculator
from ..comparator import BinaryComparator
from ..instruction.binary_number import BinaryNumber
from ..instruction.operation_enum import OperationEnum, OperationType

if p_typ.TYPE_CHECKING:
    from ..instruction.binary_instruction import BinaryInstruction


class InstructionExecutor:
    """Executor for binary instructions (calculations and comparisons).
    
    This class executes BinaryInstruction objects by delegating to the
    appropriate handler based on the instruction's state.
    
    Methods:
        calculate(): Execute calculation instructions (returns binary string)
        compare(): Execute comparison instructions (returns boolean)
    """
    
    def __init__(self) -> None:
        """Initialize the instruction executor with dependencies."""
        self._arithmetic_calculator = ArithmeticCalculator()
        self._comparator = BinaryComparator()
    
    def calculate(
            self,
            *,
            instruction: 'BinaryInstruction',
            print_result: bool = False) -> BinaryNumber:
        """Execute a calculation instruction.
        
        This method executes arithmetic operations (+, -, *, /) and returns
        the result as a BinaryNumber object.
        
        Args:
            instruction: BinaryInstruction with CALCULATE state
            print_result: If True, print formatted calculation with result
            
        Returns:
            Result as BinaryNumber object
            
        Raises:
            ValueError: If instruction is not a calculation (is comparison)
            ZeroDivisionError: If dividing by zero
            
        Example:
            >>> executor = InstructionExecutor()
            >>> instruction = BinaryInstruction(
            ...     operand_1=BinaryNumber(binary_str='1010'),
            ...     operand_2=BinaryNumber(binary_str='0101'),
            ...     operation='+')
            >>> result = executor.calculate(instruction=instruction)
            >>> print(result.value)
            '1111'
        """
        if not instruction.is_calculation():
            raise ValueError(
                f"Cannot calculate comparison instruction. "
                f"Operation '{instruction.operation.symbol}' is a "
                f"comparison, not a calculation. Use compare() instead.")
        
        operation_map = {
            OperationEnum.ADD: self._arithmetic_calculator.add,
            OperationEnum.SUBTRACT: self._arithmetic_calculator.subtract,
            OperationEnum.MULTIPLY: self._arithmetic_calculator.multiply,
            OperationEnum.DIVIDE: self._arithmetic_calculator.divide}
        
        if instruction.operation not in operation_map:
            raise ValueError(
                f"Unsupported calculation operation: "
                f"'{instruction.operation.symbol}'")
        
        operation_func = operation_map[instruction.operation]
        result = operation_func(
            operand_1=instruction.operand_1,
            operand_2=instruction.operand_2)
        
        if print_result:
            self._print_calculation(instruction=instruction, result=result)
        
        return result
    
    def compare(
            self,
            *,
            instruction: 'BinaryInstruction',
            print_result: bool = False) -> bool:
        """Execute a comparison instruction.
        
        This method executes comparison operations (<, <=, >, >=, ==, !=)
        and returns the result as a boolean.
        
        Args:
            instruction: BinaryInstruction with COMPARE state
            print_result: If True, print formatted comparison with result
            
        Returns:
            Result as boolean
            
        Raises:
            ValueError: If instruction is not a comparison (is calculation)
            
        Example:
            >>> executor = InstructionExecutor()
            >>> instruction = BinaryInstruction(
            ...     operand_1=BinaryNumber(binary_str='10'),
            ...     operand_2=BinaryNumber(binary_str='101'),
            ...     operation='<')
            >>> result = executor.compare(instruction=instruction)
            >>> print(result)
            True
        """
        if not instruction.is_comparison():
            raise ValueError(
                f"Cannot compare calculation instruction. "
                f"Operation '{instruction.operation.symbol}' is a "
                f"calculation, not a comparison. Use calculate() instead.")
        
        operation_map = {
            OperationEnum.SMALLER: self._comparator.smaller,
            OperationEnum.SMALLER_EQUAL: self._comparator.smaller_equal,
            OperationEnum.LARGER: self._comparator.larger,
            OperationEnum.LARGER_EQUAL: self._comparator.larger_equal,
            OperationEnum.EQUAL: self._comparator.equal,
            OperationEnum.NOT_EQUAL: self._comparator.not_equal}
        
        if instruction.operation not in operation_map:
            raise ValueError(
                f"Unsupported comparison operation: "
                f"'{instruction.operation.symbol}'")
        
        operation_func = operation_map[instruction.operation]
        result = operation_func(
            binary_1=instruction.operand_1.value,
            binary_2=instruction.operand_2.value)
        
        if print_result:
            self._print_comparison(instruction=instruction, result=result)
        
        return result
    
    def _print_calculation(
            self,
            *,
            instruction: 'BinaryInstruction',
            result: BinaryNumber) -> None:
        """Print formatted calculation with result.
        
        Format:
            <indent>operand_1
          <op> operand_2
          -----------
          <indent>result
          ===========
        
        Args:
            instruction: The instruction being executed
            result: The calculated result
        """
        # Print instruction
        print(instruction)
        
        # Calculate width for separator lines
        max_operand_width = max(
            len(instruction.operand_1.value),
            len(instruction.operand_2.value))
        result_width = len(result.value)
        total_width = max(
            instruction.__repr_indent__() + max_operand_width,
            instruction.__repr_indent__() + result_width)
        
        # Print separator line
        print('-' * total_width)
        
        # Print result (right-aligned with indent)
        indent = ' ' * instruction.__repr_indent__()
        max_width = max(max_operand_width, result_width)
        print(f"{indent}{result.value.rjust(max_width)}")
        
        # Print final separator line
        print('=' * total_width)
    
    def _print_comparison(
            self,
            *,
            instruction: 'BinaryInstruction',
            result: bool) -> None:
        """Print formatted comparison with result.
        
        Format:
            <indent>operand_1
          <op> operand_2
          -----------
          <indent>result
          ===========
        
        Args:
            instruction: The instruction being executed
            result: The comparison result (boolean)
        """
        # Print instruction
        print(instruction)
        
        # Calculate width for separator lines
        max_operand_width = max(
            len(instruction.operand_1.value),
            len(instruction.operand_2.value))
        result_str = str(result)
        result_width = len(result_str)
        total_width = max(
            instruction.__repr_indent__() + max_operand_width,
            instruction.__repr_indent__() + result_width)
        
        # Print separator line
        print('-' * total_width)
        
        # Print result (right-aligned with indent)
        indent = ' ' * instruction.__repr_indent__()
        max_width = max(max_operand_width, result_width)
        print(f"{indent}{result_str.rjust(max_width)}")
        
        # Print final separator line
        print('=' * total_width)

