"""Binary instruction class for encapsulating binary operations."""

import typing as p_typ
from .binary_number import BinaryNumber
from .operation_enum import OperationEnum, OperationType


class BinaryInstruction:
    """Represents an instruction with two binary operands and an operation.
    
    This class encapsulates binary operands and operations with validation.
    All attributes are accessed through properties with validated setters.
    
    Instructions have two states:
    - CALCULATE: Arithmetic operations (+, -, *, /)
    - COMPARE: Comparison operations (<, <=, >, >=, ==, !=)
    
    Attributes:
        operand_1: First binary number as BinaryNumber object
        operand_2: Second binary number as BinaryNumber object
        operation: Operation enum member (e.g., OperationEnum.ADD)
        state: Instruction state (OperationType.CALCULATE or OperationType.COMPARE)
    """
    
    def __init__(
            self,
            *,
            operand_1: BinaryNumber,
            operand_2: BinaryNumber,
            operation: str) -> None:
        """Initialize a binary instruction.
        
        Args:
            operand_1: First binary number as BinaryNumber object
            operand_2: Second binary number as BinaryNumber object
            operation: Operation symbol (+, -, *, /, <, <=, >, >=, ==, !=)
            
        Raises:
            ValueError: If operation is not supported
            TypeError: If operands are not BinaryNumber instances
        """
        # Use property setters for validation
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operation = operation
        # State is automatically set based on operation type
    
    @property
    def operand_1(self) -> BinaryNumber:
        """Get the first binary operand.
        
        Returns:
            First binary operand as BinaryNumber object
        """
        return self._operand_1
    
    @operand_1.setter
    def operand_1(self, value: BinaryNumber) -> None:
        """Set the first binary operand with validation.
        
        Args:
            value: BinaryNumber object to set
            
        Raises:
            TypeError: If value is not a BinaryNumber instance
        """
        if not isinstance(value, BinaryNumber):
            raise TypeError(
                f"operand_1 must be a BinaryNumber instance, "
                f"got {type(value).__name__}")
        self._operand_1 = value
    
    @property
    def operand_2(self) -> BinaryNumber:
        """Get the second binary operand.
        
        Returns:
            Second binary operand as BinaryNumber object
        """
        return self._operand_2
    
    @operand_2.setter
    def operand_2(self, value: BinaryNumber) -> None:
        """Set the second binary operand with validation.
        
        Args:
            value: BinaryNumber object to set
            
        Raises:
            TypeError: If value is not a BinaryNumber instance
        """
        if not isinstance(value, BinaryNumber):
            raise TypeError(
                f"operand_2 must be a BinaryNumber instance, "
                f"got {type(value).__name__}")
        self._operand_2 = value
    
    @property
    def operation(self) -> OperationEnum:
        """Get the operation enum.
        
        Returns:
            Operation enum member
        """
        return self._operation
    
    @operation.setter
    def operation(self, value: str) -> None:
        """Set the operation with validation.
        
        Args:
            value: Operation symbol to set (+, -, *, /, <, <=, >, >=, ==, !=)
            
        Raises:
            ValueError: If value is not a supported operation
        """
        # Convert symbol to enum and validate
        operation_enum = OperationEnum.from_symbol(symbol=value)
        self._operation = operation_enum
    
    @property
    def state(self) -> OperationType:
        """Get the instruction state based on operation type.
        
        Returns:
            OperationType.CALCULATE for arithmetic operations
            OperationType.COMPARE for comparison operations
        """
        return self._operation.op_type
    
    def is_calculation(self) -> bool:
        """Check if this instruction is a calculation.
        
        Returns:
            True if instruction state is CALCULATE
        """
        return self.state == OperationType.CALCULATE
    
    def is_comparison(self) -> bool:
        """Check if this instruction is a comparison.
        
        Returns:
            True if instruction state is COMPARE
        """
        return self.state == OperationType.COMPARE
    
    def __repr_indent__(self) -> int:
        """Get the indent length for the repr format.
        
        Returns:
            Length of indent (operation symbol length + 1 space)
        """
        return len(self.operation.symbol) + 1
    
    def __repr__(self) -> str:
        """Return two-line string representation of the instruction.
        
        Format (right-aligned binary numbers):
            <indent>operand_1
          <op> operand_2
        
        Returns:
            Two-line formatted string showing the binary operation
        """
        indent = ' ' * self.__repr_indent__()
        
        # Calculate maximum width for right alignment
        max_width = max(len(self.operand_1.value), len(self.operand_2.value))
        
        # Right-align both operands
        line_1 = f"{indent}{self.operand_1.value.rjust(max_width)}"
        line_2 = (f"{self.operation.symbol} "
                  f"{self.operand_2.value.rjust(max_width)}")
        
        return f"{line_1}\n{line_2}"

