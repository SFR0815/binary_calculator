"""Unit tests for BinaryInstruction property getters and setters."""

import unittest as p_ut
from binary_calculator import BinaryInstruction, OperationEnum


class TestBinaryInstructionProperties(p_ut.TestCase):
    """Test suite for BinaryInstruction property encapsulation."""
    
    def test_01_operand_1_getter(self) -> None:
        """Test getting operand_1 property."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        self.assertEqual(instruction.operand_1, '1010')
    
    def test_02_operand_2_getter(self) -> None:
        """Test getting operand_2 property."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        self.assertEqual(instruction.operand_2, '0101')
    
    def test_03_operation_getter(self) -> None:
        """Test getting operation property."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        self.assertEqual(instruction.operation, OperationEnum.ADD)
        self.assertEqual(instruction.operation.symbol, '+')
    
    def test_04_operand_1_setter_valid(self) -> None:
        """Test setting operand_1 with valid binary string."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        instruction.operand_1 = '1111'
        self.assertEqual(instruction.operand_1, '1111')
    
    def test_05_operand_2_setter_valid(self) -> None:
        """Test setting operand_2 with valid binary string."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        instruction.operand_2 = '1111'
        self.assertEqual(instruction.operand_2, '1111')
    
    def test_06_operation_setter_valid(self) -> None:
        """Test setting operation with valid operator."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Test all valid calculation operations
        expected_enums = [
            ('-', OperationEnum.SUBTRACT),
            ('*', OperationEnum.MULTIPLY),
            ('/', OperationEnum.DIVIDE),
            ('+', OperationEnum.ADD)]
        
        for symbol, expected_enum in expected_enums:
            instruction.operation = symbol
            self.assertEqual(instruction.operation, expected_enum)
            self.assertEqual(instruction.operation.symbol, symbol)
    
    def test_07_operand_1_setter_invalid_characters(self) -> None:
        """Test setting operand_1 with invalid characters."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            instruction.operand_1 = '1012'
        
        self.assertIn("Invalid binary string", str(context.exception))
    
    def test_08_operand_2_setter_invalid_characters(self) -> None:
        """Test setting operand_2 with invalid characters."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            instruction.operand_2 = 'abc'
        
        self.assertIn("Invalid binary string", str(context.exception))
    
    def test_09_operand_1_setter_empty_string(self) -> None:
        """Test setting operand_1 with empty string."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            instruction.operand_1 = ''
        
        self.assertIn("cannot be empty", str(context.exception))
    
    def test_10_operand_2_setter_empty_string(self) -> None:
        """Test setting operand_2 with empty string."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            instruction.operand_2 = ''
        
        self.assertIn("cannot be empty", str(context.exception))
    
    def test_11_operation_setter_invalid(self) -> None:
        """Test setting operation with invalid operator."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            instruction.operation = '%'
        
        self.assertIn("Invalid operation", str(context.exception))
    
    def test_12_multiple_property_changes(self) -> None:
        """Test changing multiple properties sequentially."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Change operand_1
        instruction.operand_1 = '1111'
        self.assertEqual(instruction.operand_1, '1111')
        self.assertEqual(instruction.operand_2, '0101')
        self.assertEqual(instruction.operation, OperationEnum.ADD)
        
        # Change operand_2
        instruction.operand_2 = '1000'
        self.assertEqual(instruction.operand_1, '1111')
        self.assertEqual(instruction.operand_2, '1000')
        self.assertEqual(instruction.operation, OperationEnum.ADD)
        
        # Change operation
        instruction.operation = '*'
        self.assertEqual(instruction.operand_1, '1111')
        self.assertEqual(instruction.operand_2, '1000')
        self.assertEqual(instruction.operation, OperationEnum.MULTIPLY)
    
    def test_13_setter_with_leading_zeros(self) -> None:
        """Test setting operands with leading zeros."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Leading zeros should be accepted (valid binary)
        instruction.operand_1 = '0001'
        self.assertEqual(instruction.operand_1, '0001')
        
        instruction.operand_2 = '00000'
        self.assertEqual(instruction.operand_2, '00000')
    
    def test_14_setter_with_long_binary_strings(self) -> None:
        """Test setting operands with very long binary strings."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        long_binary = '1' * 100
        instruction.operand_1 = long_binary
        self.assertEqual(instruction.operand_1, long_binary)
        
        long_binary_2 = '0' * 100
        instruction.operand_2 = long_binary_2
        self.assertEqual(instruction.operand_2, long_binary_2)
    
    def test_15_setter_preserves_other_properties(self) -> None:
        """Test that setting one property doesn't affect others."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        original_operand_2 = instruction.operand_2
        original_operation = instruction.operation
        
        # Change operand_1
        instruction.operand_1 = '1111'
        
        # Others should remain unchanged
        self.assertEqual(instruction.operand_2, original_operand_2)
        self.assertEqual(instruction.operation, original_operation)
        self.assertEqual(instruction.operation, OperationEnum.ADD)
    
    def test_16_property_validation_on_init(self) -> None:
        """Test that property setters are used during initialization."""
        # Invalid operand_1 during init
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='invalid',
                operand_2='0101',
                operation='+')
        
        # Invalid operand_2 during init
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1010',
                operand_2='2',
                operation='+')
        
        # Invalid operation during init
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation='%')
    
    def test_17_all_valid_operations_via_setter(self) -> None:
        """Test all valid operations can be set."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        operation_pairs = [
            ('+', OperationEnum.ADD),
            ('-', OperationEnum.SUBTRACT),
            ('*', OperationEnum.MULTIPLY),
            ('/', OperationEnum.DIVIDE),
            ('<', OperationEnum.SMALLER),
            ('>', OperationEnum.LARGER),
            ('==', OperationEnum.EQUAL)]
        
        for symbol, expected_enum in operation_pairs:
            instruction.operation = symbol
            self.assertEqual(
                instruction.operation,
                expected_enum,
                msg=f"Failed to set operation '{symbol}'")
    
    def test_18_alternating_binary_patterns_via_setter(self) -> None:
        """Test setting various binary patterns."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        test_patterns = [
            '0',
            '1',
            '10',
            '01',
            '11',
            '00',
            '10101010',
            '01010101',
            '11111111',
            '00000000']
        
        for pattern in test_patterns:
            instruction.operand_1 = pattern
            self.assertEqual(
                instruction.operand_1,
                pattern,
                msg=f"Failed for pattern '{pattern}'")
            
            instruction.operand_2 = pattern
            self.assertEqual(
                instruction.operand_2,
                pattern,
                msg=f"Failed for pattern '{pattern}'")
    
    def test_19_repr_uses_property_getters(self) -> None:
        """Test that __repr__ works with property getters."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Change properties
        instruction.operand_1 = '1111'
        instruction.operand_2 = '1000'
        instruction.operation = '*'
        
        # __repr__ should reflect new values
        repr_str = repr(instruction)
        self.assertIn('1111', repr_str)
        self.assertIn('1000', repr_str)
        self.assertIn("operation='*'", repr_str)
    
    def test_20_property_access_via_executor(self) -> None:
        """Test that properties work correctly with InstructionExecutor."""
        from binary_calculator import InstructionExecutor
        
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Execute with original values
        result1 = executor.calculate(instruction=instruction)
        
        # Modify instruction
        instruction.operation = '*'
        
        # Execute with modified values
        result2 = executor.calculate(instruction=instruction)
        
        # Results should be different
        self.assertNotEqual(result1, result2)
        self.assertEqual(result1, '1111')  # 10 + 5 = 15
        self.assertEqual(result2, '110010')  # 10 * 5 = 50


if __name__ == '__main__':
    p_ut.main()

