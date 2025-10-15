"""Unit tests for comparison instructions."""

import unittest as p_ut
from binary_calculator import (
    BinaryInstruction,
    InstructionExecutor,
    OperationEnum,
    OperationType)


class TestComparisonInstructions(p_ut.TestCase):
    """Test suite for comparison instructions."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.executor = InstructionExecutor()
    
    def test_01_create_smaller_instruction(self) -> None:
        """Test creating a smaller comparison instruction."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='<')
        
        self.assertEqual(instruction.operation, OperationEnum.SMALLER)
        self.assertEqual(instruction.state, OperationType.COMPARE)
        self.assertTrue(instruction.is_comparison())
        self.assertFalse(instruction.is_calculation())
    
    def test_02_create_larger_instruction(self) -> None:
        """Test creating a larger comparison instruction."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='10',
            operation='>')
        
        self.assertEqual(instruction.operation, OperationEnum.LARGER)
        self.assertEqual(instruction.state, OperationType.COMPARE)
    
    def test_03_create_equal_instruction(self) -> None:
        """Test creating an equal comparison instruction."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='101',
            operation='==')
        
        self.assertEqual(instruction.operation, OperationEnum.EQUAL)
        self.assertEqual(instruction.state, OperationType.COMPARE)
    
    def test_04_execute_smaller_true(self) -> None:
        """Test executing smaller comparison that returns True."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='<')
        
        result = self.executor.compare(instruction=instruction)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)
    
    def test_05_execute_smaller_false(self) -> None:
        """Test executing smaller comparison that returns False."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='10',
            operation='<')
        
        result = self.executor.compare(instruction=instruction)
        self.assertIsInstance(result, bool)
        self.assertFalse(result)
    
    def test_06_execute_larger_true(self) -> None:
        """Test executing larger comparison that returns True."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='10',
            operation='>')
        
        result = self.executor.compare(instruction=instruction)
        self.assertTrue(result)
    
    def test_07_execute_equal_true(self) -> None:
        """Test executing equal comparison that returns True."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='0101',
            operation='==')
        
        result = self.executor.compare(instruction=instruction)
        self.assertTrue(result)
    
    def test_08_execute_equal_false(self) -> None:
        """Test executing equal comparison that returns False."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='110',
            operation='==')
        
        result = self.executor.compare(instruction=instruction)
        self.assertFalse(result)
    
    def test_09_execute_not_equal_true(self) -> None:
        """Test executing not equal comparison that returns True."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='110',
            operation='!=')
        
        result = self.executor.compare(instruction=instruction)
        self.assertTrue(result)
    
    def test_10_execute_smaller_equal_true(self) -> None:
        """Test executing smaller_equal comparison."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='101',
            operation='<=')
        
        result = self.executor.compare(instruction=instruction)
        self.assertTrue(result)
    
    def test_11_execute_larger_equal_true(self) -> None:
        """Test executing larger_equal comparison."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='101',
            operation='>=')
        
        result = self.executor.compare(instruction=instruction)
        self.assertTrue(result)
    
    def test_12_calculate_vs_compare_state(self) -> None:
        """Test that state correctly identifies instruction type."""
        calc_inst = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        comp_inst = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='<')
        
        self.assertEqual(calc_inst.state, OperationType.CALCULATE)
        self.assertEqual(comp_inst.state, OperationType.COMPARE)
    
    def test_13_all_comparison_operations(self) -> None:
        """Test all comparison operations."""
        comparisons = ['<', '<=', '>', '>=', '==', '!=']
        
        for op in comparisons:
            instruction = BinaryInstruction(
                operand_1='101',
                operand_2='110',
                operation=op)
            
            self.assertEqual(instruction.state, OperationType.COMPARE)
            result = self.executor.compare(instruction=instruction)
            self.assertIsInstance(result, bool)
    
    def test_14_all_calculation_operations(self) -> None:
        """Test all calculation operations."""
        calculations = ['+', '-', '*', '/']
        
        for op in calculations:
            instruction = BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation=op)
            
            self.assertEqual(instruction.state, OperationType.CALCULATE)
            result = self.executor.calculate(instruction=instruction)
            self.assertIsInstance(result, str)
    
    def test_15_comparison_result_type(self) -> None:
        """Test that comparison results are boolean."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='<')
        
        result = self.executor.compare(instruction=instruction)
        self.assertIsInstance(result, bool)
        self.assertNotIsInstance(result, str)
    
    def test_16_calculation_result_type(self) -> None:
        """Test that calculation results are strings."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, bool)
    
    def test_17_modify_operation_changes_state(self) -> None:
        """Test that modifying operation changes state."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        self.assertEqual(instruction.state, OperationType.CALCULATE)
        
        # Change to comparison
        instruction.operation = '<'
        self.assertEqual(instruction.state, OperationType.COMPARE)
        
        # Change back to calculation
        instruction.operation = '*'
        self.assertEqual(instruction.state, OperationType.CALCULATE)
    
    def test_18_comprehensive_comparison_execution(self) -> None:
        """Test comprehensive comparison execution."""
        test_cases = [
            ('10', '101', '<', True),
            ('101', '10', '<', False),
            ('10', '101', '>', False),
            ('101', '10', '>', True),
            ('101', '101', '==', True),
            ('101', '110', '==', False),
            ('101', '110', '!=', True),
            ('101', '101', '!=', False),
            ('10', '101', '<=', True),
            ('101', '101', '<=', True),
            ('101', '10', '<=', False),
            ('101', '10', '>=', True),
            ('101', '101', '>=', True),
            ('10', '101', '>=', False)]
        
        for op1, op2, operation, expected in test_cases:
            instruction = BinaryInstruction(
                operand_1=op1,
                operand_2=op2,
                operation=operation)
            
            result = self.executor.compare(instruction=instruction)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {op1} {operation} {op2}")
    
    def test_19_operation_enum_properties(self) -> None:
        """Test operation enum properties."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Operation should be an enum
        self.assertIsInstance(instruction.operation, OperationEnum)
        self.assertEqual(instruction.operation.symbol, '+')
        self.assertTrue(instruction.operation.is_calculation())
        self.assertFalse(instruction.operation.is_comparison())
    
    def test_20_invalid_operation_symbol(self) -> None:
        """Test that invalid operation symbols are rejected."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation='%')


if __name__ == '__main__':
    p_ut.main()

