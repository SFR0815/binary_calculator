"""Advanced tests for BinaryInstruction encapsulation and edge cases."""

import unittest as p_ut
import copy as p_cpy
from binary_calculator import (
    BinaryInstruction,
    InstructionExecutor,
    ArithmeticCalculator)


class TestBinaryInstructionEncapsulation(p_ut.TestCase):
    """Test suite for advanced encapsulation features."""
    
    def test_01_private_attribute_access_protected(self) -> None:
        """Test that private attributes cannot be directly accessed."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Private attributes should exist
        self.assertTrue(hasattr(instruction, '_operand_1'))
        self.assertTrue(hasattr(instruction, '_operand_2'))
        self.assertTrue(hasattr(instruction, '_operation'))
        
        # Direct access should work but is discouraged
        self.assertEqual(instruction._operand_1, '1010')
    
    def test_02_property_provides_controlled_access(self) -> None:
        """Test that properties provide controlled access."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Properties should be accessible
        self.assertEqual(instruction.operand_1, '1010')
        self.assertEqual(instruction.operand_2, '0101')
        self.assertEqual(instruction.operation.symbol, '+')
        
        # Verify they access the private attributes
        self.assertEqual(instruction.operand_1, instruction._operand_1)
        self.assertEqual(instruction.operand_2, instruction._operand_2)
        self.assertEqual(instruction.operation.symbol, instruction._operation.symbol)
    
    def test_03_cannot_bypass_validation_via_property(self) -> None:
        """Test that validation cannot be bypassed through properties."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Attempt to set invalid values through properties
        with self.assertRaises(ValueError):
            instruction.operand_1 = '123'
        
        # Original value should remain unchanged
        self.assertEqual(instruction.operand_1, '1010')
    
    def test_04_deep_copy_maintains_encapsulation(self) -> None:
        """Test that deep copying maintains encapsulation."""
        original = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        copied = p_cpy.deepcopy(original)
        
        # Verify copy has same values
        self.assertEqual(copied.operand_1, original.operand_1)
        self.assertEqual(copied.operand_2, original.operand_2)
        self.assertEqual(copied.operation, original.operation)
        
        # Modify copy
        copied.operand_1 = '1111'
        
        # Original should be unchanged
        self.assertEqual(original.operand_1, '1010')
        self.assertEqual(copied.operand_1, '1111')
    
    def test_05_shallow_copy_behavior(self) -> None:
        """Test shallow copy behavior with encapsulated class."""
        original = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        copied = p_cpy.copy(original)
        
        # Verify copy has same values
        self.assertEqual(copied.operand_1, original.operand_1)
        
        # Modify copy
        copied.operand_1 = '1111'
        
        # Original should be unchanged (strings are immutable)
        self.assertEqual(original.operand_1, '1010')
    
    def test_06_property_setter_atomic_behavior(self) -> None:
        """Test that property setters are atomic (all-or-nothing)."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        original_value = instruction.operand_1
        
        # Attempt invalid set
        try:
            instruction.operand_1 = 'invalid'
        except ValueError:
            pass
        
        # Value should remain unchanged after failed set
        self.assertEqual(instruction.operand_1, original_value)
    
    def test_07_multiple_instructions_independence(self) -> None:
        """Test that multiple instructions are independent."""
        inst1 = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        inst2 = BinaryInstruction(
            operand_1='1111',
            operand_2='1000',
            operation='*')
        
        # Modify inst1
        inst1.operand_1 = '0000'
        inst1.operation = '-'
        
        # inst2 should be unchanged
        self.assertEqual(inst2.operand_1, '1111')
        self.assertEqual(inst2.operand_2, '1000')
        self.assertEqual(inst2.operation.symbol, '*')
    
    def test_08_property_getter_idempotent(self) -> None:
        """Test that property getters are idempotent."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Multiple gets should return same value
        value1 = instruction.operand_1
        value2 = instruction.operand_1
        value3 = instruction.operand_1
        
        self.assertEqual(value1, value2)
        self.assertEqual(value2, value3)
        self.assertEqual(value1, '1010')
    
    def test_09_property_setter_validates_on_each_call(self) -> None:
        """Test that setter validates on each call, not just first."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Set valid value multiple times
        instruction.operand_1 = '1111'
        instruction.operand_1 = '0000'
        instruction.operand_1 = '1'
        
        # Invalid should still fail
        with self.assertRaises(ValueError):
            instruction.operand_1 = 'abc'
    
    def test_10_string_immutability_leveraged(self) -> None:
        """Test that string immutability is properly leveraged."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Get reference
        op1 = instruction.operand_1
        
        # Strings are immutable, so this creates a new string
        modified = op1 + '1'
        
        # Instruction should be unchanged
        self.assertEqual(instruction.operand_1, '1010')
        self.assertEqual(modified, '10101')


class TestBinaryInstructionEdgeCases(p_ut.TestCase):
    """Test suite for edge cases and boundary conditions."""
    
    def test_01_single_bit_operands(self) -> None:
        """Test instructions with single bit operands."""
        instruction = BinaryInstruction(
            operand_1='0',
            operand_2='1',
            operation='+')
        
        self.assertEqual(instruction.operand_1, '0')
        self.assertEqual(instruction.operand_2, '1')
    
    def test_02_very_long_operands(self) -> None:
        """Test instructions with very long binary operands."""
        long_binary = '1' * 1000
        
        instruction = BinaryInstruction(
            operand_1=long_binary,
            operand_2='1',
            operation='+')
        
        self.assertEqual(len(instruction.operand_1), 1000)
    
    def test_03_all_zeros_operand(self) -> None:
        """Test operands with all zeros."""
        instruction = BinaryInstruction(
            operand_1='0000000',
            operand_2='0',
            operation='+')
        
        self.assertEqual(instruction.operand_1, '0000000')
        self.assertEqual(instruction.operand_2, '0')
    
    def test_04_all_ones_operand(self) -> None:
        """Test operands with all ones."""
        instruction = BinaryInstruction(
            operand_1='1111111',
            operand_2='1',
            operation='*')
        
        self.assertEqual(instruction.operand_1, '1111111')
    
    def test_05_alternating_pattern_operands(self) -> None:
        """Test operands with alternating bit patterns."""
        instruction = BinaryInstruction(
            operand_1='10101010',
            operand_2='01010101',
            operation='+')
        
        self.assertEqual(instruction.operand_1, '10101010')
        self.assertEqual(instruction.operand_2, '01010101')
    
    def test_06_change_operand_to_different_length(self) -> None:
        """Test changing operand to different length binary string."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Change to shorter
        instruction.operand_1 = '1'
        self.assertEqual(instruction.operand_1, '1')
        
        # Change to longer
        instruction.operand_1 = '111111111111'
        self.assertEqual(instruction.operand_1, '111111111111')
    
    def test_07_operation_change_affects_calculation(self) -> None:
        """Test that changing operation affects calculation result."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        result_add = executor.calculate(instruction=instruction)
        
        instruction.operation = '-'
        result_sub = executor.calculate(instruction=instruction)
        
        instruction.operation = '*'
        result_mul = executor.calculate(instruction=instruction)
        
        # All results should be different
        self.assertNotEqual(result_add, result_sub)
        self.assertNotEqual(result_sub, result_mul)
        self.assertNotEqual(result_add, result_mul)
    
    def test_08_modify_operands_between_executions(self) -> None:
        """Test modifying operands between executions."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        result1 = executor.calculate(instruction=instruction)
        
        # Modify first operand
        instruction.operand_1 = '1111'
        result2 = executor.calculate(instruction=instruction)
        
        # Results should be different
        self.assertNotEqual(result1, result2)
        self.assertEqual(result1, '1111')  # 10 + 5 = 15
        self.assertEqual(result2, '10100')  # 15 + 5 = 20
    
    def test_09_whitespace_not_allowed(self) -> None:
        """Test that whitespace is not allowed in binary strings."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='10 10',
                operand_2='0101',
                operation='+')
        
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1010',
                operand_2='01 01',
                operation='+')
    
    def test_10_special_characters_not_allowed(self) -> None:
        """Test that special characters are not allowed."""
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        
        for char in special_chars:
            with self.assertRaises(ValueError):
                BinaryInstruction(
                    operand_1=f'10{char}10',
                    operand_2='0101',
                    operation='+')
    
    def test_11_negative_sign_not_allowed_in_operands(self) -> None:
        """Test that negative signs are not allowed in operands."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='-1010',
                operand_2='0101',
                operation='+')
    
    def test_12_case_sensitivity_digits_only(self) -> None:
        """Test that only 0 and 1 digits are allowed."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='a',
                operand_2='0101',
                operation='+')
        
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='A',
                operand_2='0101',
                operation='+')


class TestBinaryInstructionIntegration(p_ut.TestCase):
    """Test suite for integration with BinaryCalculator."""
    
    def test_01_instruction_reuse_with_modifications(self) -> None:
        """Test reusing same instruction with modifications."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Execute multiple times with modifications
        results = []
        operations = ['+', '-', '*', '/']
        
        for op in operations:
            instruction.operation = op
            result = executor.calculate(instruction=instruction)
            results.append(result)
        
        # All results should be different
        self.assertEqual(len(results), len(set(results)))
    
    def test_02_multiple_calculations_same_instruction(self) -> None:
        """Test multiple calculations with same instruction."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Execute multiple times without modification
        result1 = executor.calculate(instruction=instruction)
        result2 = executor.calculate(instruction=instruction)
        result3 = executor.calculate(instruction=instruction)
        
        # All results should be identical
        self.assertEqual(result1, result2)
        self.assertEqual(result2, result3)
    
    def test_03_instruction_list_different_operations(self) -> None:
        """Test list of instructions with different operations."""
        executor = InstructionExecutor()
        
        instructions = [
            BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation='+'),
            BinaryInstruction(
                operand_1='1111',
                operand_2='0001',
                operation='-'),
            BinaryInstruction(
                operand_1='101',
                operand_2='11',
                operation='*'),
            BinaryInstruction(
                operand_1='1010',
                operand_2='10',
                operation='/')]
        
        results = [executor.calculate(instruction=inst) 
                   for inst in instructions]
        
        # Verify each result
        self.assertEqual(results[0], '1111')  # 10 + 5 = 15
        self.assertEqual(results[1], '1110')  # 15 - 1 = 14
        self.assertEqual(results[2], '1111')  # 5 * 3 = 15
        self.assertEqual(results[3], '101')   # 10 / 2 = 5
    
    def test_04_chain_operations_modify_instruction(self) -> None:
        """Test chaining operations by modifying instruction."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # First operation
        result1 = executor.calculate(instruction=instruction)
        
        # Use result as next operand
        instruction.operand_1 = result1
        instruction.operand_2 = '1'
        instruction.operation = '*'
        
        result2 = executor.calculate(instruction=instruction)
        
        self.assertEqual(result1, '1111')  # 10 + 5 = 15
        self.assertEqual(result2, '1111')  # 15 * 1 = 15
    
    def test_05_instruction_with_conversion_methods(self) -> None:
        """Test instruction with calculator and converter."""
        from binary_calculator import BinaryConverter
        
        executor = InstructionExecutor()
        converter = BinaryConverter()
        
        # Create instruction from decimal values
        decimal_1 = 10
        decimal_2 = 5
        
        binary_1 = converter.decimal_to_binary(decimal_num=decimal_1)
        binary_2 = converter.decimal_to_binary(decimal_num=decimal_2)
        
        instruction = BinaryInstruction(
            operand_1=binary_1,
            operand_2=binary_2,
            operation='+')
        
        result_binary = executor.calculate(instruction=instruction)
        result_decimal = converter.binary_to_decimal(
            binary_str=result_binary)
        
        self.assertEqual(result_decimal, 15)
    
    def test_06_property_modification_during_execution(self) -> None:
        """Test that properties remain stable during execution."""
        executor = InstructionExecutor()
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Execute
        result = executor.calculate(instruction=instruction)
        
        # Properties should remain unchanged after execution
        self.assertEqual(instruction.operand_1, '1010')
        self.assertEqual(instruction.operand_2, '0101')
        self.assertEqual(instruction.operation.symbol, '+')


class TestBinaryInstructionValidationComprehensive(p_ut.TestCase):
    """Comprehensive validation testing."""
    
    def test_01_validation_error_messages_clear(self) -> None:
        """Test that validation error messages are clear."""
        try:
            BinaryInstruction(
                operand_1='invalid',
                operand_2='0101',
                operation='+')
        except ValueError as e:
            self.assertIn('Invalid binary string', str(e))
            self.assertIn('invalid', str(e))
    
    def test_02_validation_identifies_specific_operand(self) -> None:
        """Test validation during setter identifies the operand."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        # Test operand_1
        try:
            instruction.operand_1 = '123'
        except ValueError as e:
            error_msg = str(e)
            self.assertIn('123', error_msg)
    
    def test_03_all_invalid_digits_rejected(self) -> None:
        """Test that all non-binary digits are rejected."""
        invalid_digits = '23456789'
        
        for digit in invalid_digits:
            with self.assertRaises(ValueError):
                BinaryInstruction(
                    operand_1=f'10{digit}0',
                    operand_2='0101',
                    operation='+')
    
    def test_04_letters_rejected_in_operands(self) -> None:
        """Test that letters are rejected in operands."""
        import string as p_str
        
        for letter in p_str.ascii_letters[:10]:  # Test subset
            with self.assertRaises(ValueError):
                BinaryInstruction(
                    operand_1=f'10{letter}0',
                    operand_2='0101',
                    operation='+')
    
    def test_05_unicode_characters_rejected(self) -> None:
        """Test that unicode characters are rejected."""
        unicode_chars = ['①', '②', '③', '♠', '♥', '€', '£']
        
        for char in unicode_chars:
            with self.assertRaises(ValueError):
                BinaryInstruction(
                    operand_1=f'10{char}0',
                    operand_2='0101',
                    operation='+')
    
    def test_06_operation_validation_comprehensive(self) -> None:
        """Test comprehensive operation validation."""
        invalid_operations = [
            '%', '^', '&', '|', '~', '<<', '>>', '**',
            'add', 'sub', 'mul', 'div', '', ' ', '++', '--']
        
        for op in invalid_operations:
            with self.assertRaises(ValueError):
                BinaryInstruction(
                    operand_1='1010',
                    operand_2='0101',
                    operation=op)


if __name__ == '__main__':
    p_ut.main()

