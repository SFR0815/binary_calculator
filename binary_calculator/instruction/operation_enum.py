"""Operation type enumeration for binary instructions."""

import enum as p_enum


class OperationType(p_enum.Enum):
    """Enumeration of operation types (calculation vs comparison)."""
    
    CALCULATE = 'calculate'
    COMPARE = 'compare'


class OperationEnum(p_enum.Enum):
    """Enumeration of all supported operations.
    
    Each operation has a symbol and a type (CALCULATE or COMPARE).
    """
    
    # Calculation operations
    ADD = ('+', OperationType.CALCULATE)
    SUBTRACT = ('-', OperationType.CALCULATE)
    MULTIPLY = ('*', OperationType.CALCULATE)
    DIVIDE = ('/', OperationType.CALCULATE)
    
    # Comparison operations
    SMALLER = ('<', OperationType.COMPARE)
    SMALLER_EQUAL = ('<=', OperationType.COMPARE)
    LARGER = ('>', OperationType.COMPARE)
    LARGER_EQUAL = ('>=', OperationType.COMPARE)
    EQUAL = ('==', OperationType.COMPARE)
    NOT_EQUAL = ('!=', OperationType.COMPARE)
    
    def __init__(self, symbol: str, op_type: OperationType) -> None:
        """Initialize operation enum member.
        
        Args:
            symbol: Operation symbol (e.g., '+', '<', '==')
            op_type: Type of operation (CALCULATE or COMPARE)
        """
        self.symbol = symbol
        self.op_type = op_type
    
    @classmethod
    def from_symbol(cls, symbol: str) -> 'OperationEnum':
        """Get operation enum from symbol.
        
        Args:
            symbol: Operation symbol to look up
            
        Returns:
            Corresponding OperationEnum member
            
        Raises:
            ValueError: If symbol is not recognized
        """
        for op in cls:
            if op.symbol == symbol:
                return op
        
        raise ValueError(
            f"Invalid operation: '{symbol}'. "
            f"Must be one of {[op.symbol for op in cls]}")
    
    @classmethod
    def get_calculation_operations(cls) -> list:
        """Get all calculation operations.
        
        Returns:
            List of OperationEnum members that are calculations
        """
        return [op for op in cls if op.op_type == OperationType.CALCULATE]
    
    @classmethod
    def get_comparison_operations(cls) -> list:
        """Get all comparison operations.
        
        Returns:
            List of OperationEnum members that are comparisons
        """
        return [op for op in cls if op.op_type == OperationType.COMPARE]
    
    def is_calculation(self) -> bool:
        """Check if this operation is a calculation.
        
        Returns:
            True if operation type is CALCULATE
        """
        return self.op_type == OperationType.CALCULATE
    
    def is_comparison(self) -> bool:
        """Check if this operation is a comparison.
        
        Returns:
            True if operation type is COMPARE
        """
        return self.op_type == OperationType.COMPARE

