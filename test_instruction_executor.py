"""Unit tests for InstructionExecutor class."""

import unittest as p_ut
from binary_calculator import BinaryInstruction, InstructionExecutor


class TestInstructionExecutor(p_ut.TestCase):
    """Test suite for InstructionExecutor class."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.executor = InstructionExecutor()
    
    def test_01_calculate_with_calculation_instruction(self) -> None:
        """Test calculate method with valid calculation instruction."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertIsInstance(result, str)
        self.assertEqual(result, '1111')
    
    def test_02_compare_with_comparison_instruction(self) -> None:
        """Test compare method with valid comparison instruction."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='<')
        
        result = self.executor.compare(instruction=instruction)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)
    
    def test_03_calculate_with_comparison_instruction_errors(self) -> None:
        """Test that calculate() errors with comparison instruction."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='<')
        
        with self.assertRaises(ValueError) as context:
            self.executor.calculate(instruction=instruction)
        
        error_msg = str(context.exception)
        self.assertIn("Cannot calculate comparison instruction", error_msg)
        self.assertIn("<", error_msg)
        self.assertIn("Use compare() instead", error_msg)
    
    def test_04_compare_with_calculation_instruction_errors(self) -> None:
        """Test that compare() errors with calculation instruction."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        with self.assertRaises(ValueError) as context:
            self.executor.compare(instruction=instruction)
        
        error_msg = str(context.exception)
        self.assertIn("Cannot compare calculation instruction", error_msg)
        self.assertIn("+", error_msg)
        self.assertIn("Use calculate() instead", error_msg)
    
    def test_05_all_calculation_operations_via_calculate(self) -> None:
        """Test all calculation operations through calculate method."""
        calc_operations = ['+', '-', '*', '/']
        
        for op in calc_operations:
            instruction = BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation=op)
            
            result = self.executor.calculate(instruction=instruction)
            self.assertIsInstance(result, str)
    
    def test_06_all_comparison_operations_via_compare(self) -> None:
        """Test all comparison operations through compare method."""
        comp_operations = ['<', '<=', '>', '>=', '==', '!=']
        
        for op in comp_operations:
            instruction = BinaryInstruction(
                operand_1='10',
                operand_2='101',
                operation=op)
            
            result = self.executor.compare(instruction=instruction)
            self.assertIsInstance(result, bool)
    
    def test_07_calculate_all_operation_types_error(self) -> None:
        """Test calculate errors for all comparison operations."""
        comp_operations = ['<', '<=', '>', '>=', '==', '!=']
        
        for op in comp_operations:
            instruction = BinaryInstruction(
                operand_1='10',
                operand_2='101',
                operation=op)
            
            with self.assertRaises(ValueError):
                self.executor.calculate(instruction=instruction)
    
    def test_08_compare_all_operation_types_error(self) -> None:
        """Test compare errors for all calculation operations."""
        calc_operations = ['+', '-', '*', '/']
        
        for op in calc_operations:
            instruction = BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation=op)
            
            with self.assertRaises(ValueError):
                self.executor.compare(instruction=instruction)
    
    def test_09_calculate_returns_string_type(self) -> None:
        """Test that calculate always returns string type."""
        instructions = [
            BinaryInstruction(operand_1='10', operand_2='1', operation='+'),
            BinaryInstruction(operand_1='10', operand_2='1', operation='-'),
            BinaryInstruction(operand_1='10', operand_2='1', operation='*'),
            BinaryInstruction(operand_1='10', operand_2='1', operation='/')]
        
        for inst in instructions:
            result = self.executor.calculate(instruction=inst)
            self.assertIsInstance(result, str)
            self.assertNotIsInstance(result, bool)
    
    def test_10_compare_returns_bool_type(self) -> None:
        """Test that compare always returns bool type."""
        instructions = [
            BinaryInstruction(operand_1='10', operand_2='101', operation='<'),
            BinaryInstruction(operand_1='10', operand_2='101', operation='<='),
            BinaryInstruction(operand_1='10', operand_2='101', operation='>'),
            BinaryInstruction(operand_1='10', operand_2='101', operation='>='),
            BinaryInstruction(operand_1='10', operand_2='101', operation='=='),
            BinaryInstruction(operand_1='10', operand_2='101', operation='!=')]
        
        for inst in instructions:
            result = self.executor.compare(instruction=inst)
            self.assertIsInstance(result, bool)
    
    def test_11_error_message_quality_calculate_wrong_type(self) -> None:
        """Test that error message is clear when using calculate wrong."""
        instruction = BinaryInstruction(
            operand_1='10',
            operand_2='101',
            operation='>')
        
        try:
            self.executor.calculate(instruction=instruction)
            self.fail("Should have raised ValueError")
        except ValueError as e:
            msg = str(e)
            # Should mention what went wrong
            self.assertIn("Cannot calculate", msg)
            # Should mention the operation
            self.assertIn(">", msg)
            # Should mention what to use instead
            self.assertIn("compare()", msg)
    
    def test_12_error_message_quality_compare_wrong_type(self) -> None:
        """Test that error message is clear when using compare wrong."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='-')
        
        try:
            self.executor.compare(instruction=instruction)
            self.fail("Should have raised ValueError")
        except ValueError as e:
            msg = str(e)
            # Should mention what went wrong
            self.assertIn("Cannot compare", msg)
            # Should mention the operation
            self.assertIn("-", msg)
            # Should mention what to use instead
            self.assertIn("calculate()", msg)


if __name__ == '__main__':
    p_ut.main()

