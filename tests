"""Unit tests for binary calculator module."""

import unittest as p_ut
from binary_calculator import (
    InstructionExecutor,
    ArithmeticCalculator,
    BinaryInstruction,
    BinaryConverter)


class TestBinaryCalculator(p_ut.TestCase):
    """Test suite for arithmetic calculator and instruction execution."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.executor = InstructionExecutor()
        self.arithmetic = ArithmeticCalculator()
        self.converter = BinaryConverter()
    
    def test_01_binary_instruction_creation(self) -> None:
        """Test creating a valid BinaryInstruction."""
        from binary_calculator import OperationEnum, OperationType
        
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        self.assertEqual(instruction.operand_1, '1010')
        self.assertEqual(instruction.operand_2, '0101')
        self.assertEqual(instruction.operation, OperationEnum.ADD)
        self.assertEqual(instruction.operation.symbol, '+')
        self.assertEqual(instruction.state, OperationType.CALCULATE)
        self.assertTrue(instruction.is_calculation())
        self.assertFalse(instruction.is_comparison())
    
    def test_02_invalid_binary_string(self) -> None:
        """Test that invalid binary strings raise ValueError."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1012',
                operand_2='0101',
                operation='+')
        
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='abc',
                operand_2='0101',
                operation='+')
    
    def test_03_empty_binary_string(self) -> None:
        """Test that empty binary strings raise ValueError."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='',
                operand_2='0101',
                operation='+')
    
    def test_04_invalid_operation(self) -> None:
        """Test that invalid operations raise ValueError."""
        with self.assertRaises(ValueError):
            BinaryInstruction(
                operand_1='1010',
                operand_2='0101',
                operation='%')
    
    def test_05_binary_to_decimal_conversion(self) -> None:
        """Test converting binary strings to decimal integers."""
        test_cases = {
            '0': 0,
            '1': 1,
            '10': 2,
            '11': 3,
            '100': 4,
            '1010': 10,
            '1111': 15,
            '10000': 16,
            '11111111': 255}
        
        for binary_str, expected_decimal in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected_decimal,
                msg=f"Failed for {binary_str}")
    
    def test_06_decimal_to_binary_conversion(self) -> None:
        """Test converting decimal integers to binary strings."""
        test_cases = {
            0: '0',
            1: '1',
            2: '10',
            3: '11',
            4: '100',
            10: '1010',
            15: '1111',
            16: '10000',
            255: '11111111'}
        
        for decimal_num, expected_binary in test_cases.items():
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            self.assertEqual(
                result,
                expected_binary,
                msg=f"Failed for {decimal_num}")
    
    def test_07_addition_basic(self) -> None:
        """Test basic binary addition."""
        result = self.arithmetic.add(operand_1='1010', operand_2='0101')
        self.assertEqual(result, '1111')  # 10 + 5 = 15
    
    def test_08_addition_with_carry(self) -> None:
        """Test binary addition with carry."""
        result = self.arithmetic.add(operand_1='1111', operand_2='1')
        self.assertEqual(result, '10000')  # 15 + 1 = 16
    
    def test_09_addition_zero(self) -> None:
        """Test binary addition with zero."""
        result = self.arithmetic.add(operand_1='1010', operand_2='0')
        self.assertEqual(result, '1010')  # 10 + 0 = 10
    
    def test_10_subtraction_basic(self) -> None:
        """Test basic binary subtraction."""
        result = self.arithmetic.subtract(
            operand_1='1010',
            operand_2='0101')
        self.assertEqual(result, '101')  # 10 - 5 = 5
    
    def test_11_subtraction_to_zero(self) -> None:
        """Test binary subtraction resulting in zero."""
        result = self.arithmetic.subtract(
            operand_1='1111',
            operand_2='1111')
        self.assertEqual(result, '0')  # 15 - 15 = 0
    
    def test_12_subtraction_negative_result(self) -> None:
        """Test binary subtraction with negative result."""
        result = self.arithmetic.subtract(
            operand_1='0101',
            operand_2='1010')
        self.assertEqual(result, '-101')  # 5 - 10 = -5
    
    def test_13_multiplication_basic(self) -> None:
        """Test basic binary multiplication."""
        result = self.arithmetic.multiply(
            operand_1='101',
            operand_2='11')
        self.assertEqual(result, '1111')  # 5 * 3 = 15
    
    def test_14_multiplication_by_zero(self) -> None:
        """Test binary multiplication by zero."""
        result = self.arithmetic.multiply(operand_1='1111', operand_2='0')
        self.assertEqual(result, '0')  # 15 * 0 = 0
    
    def test_15_multiplication_by_one(self) -> None:
        """Test binary multiplication by one."""
        result = self.arithmetic.multiply(operand_1='1010', operand_2='1')
        self.assertEqual(result, '1010')  # 10 * 1 = 10
    
    def test_16_division_basic(self) -> None:
        """Test basic binary division."""
        result = self.arithmetic.divide(operand_1='1010', operand_2='10')
        self.assertEqual(result, '101')  # 10 / 2 = 5
    
    def test_17_division_exact(self) -> None:
        """Test exact binary division."""
        result = self.arithmetic.divide(operand_1='1111', operand_2='11')
        self.assertEqual(result, '101')  # 15 / 3 = 5
    
    def test_18_division_with_remainder(self) -> None:
        """Test binary division with remainder (integer division)."""
        result = self.arithmetic.divide(operand_1='1010', operand_2='11')
        self.assertEqual(result, '11')  # 10 / 3 = 3 (integer division)
    
    def test_19_division_by_zero(self) -> None:
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            self.arithmetic.divide(operand_1='1010', operand_2='0')
    
    def test_20_division_by_one(self) -> None:
        """Test binary division by one."""
        result = self.arithmetic.divide(operand_1='1111', operand_2='1')
        self.assertEqual(result, '1111')  # 15 / 1 = 15
    
    def test_21_execute_addition_instruction(self) -> None:
        """Test executing an addition instruction."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertEqual(result, '1111')  # 10 + 5 = 15
    
    def test_22_execute_subtraction_instruction(self) -> None:
        """Test executing a subtraction instruction."""
        instruction = BinaryInstruction(
            operand_1='1111',
            operand_2='0101',
            operation='-')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertEqual(result, '1010')  # 15 - 5 = 10
    
    def test_23_execute_multiplication_instruction(self) -> None:
        """Test executing a multiplication instruction."""
        instruction = BinaryInstruction(
            operand_1='101',
            operand_2='11',
            operation='*')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertEqual(result, '1111')  # 5 * 3 = 15
    
    def test_24_execute_division_instruction(self) -> None:
        """Test executing a division instruction."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='10',
            operation='/')
        
        result = self.executor.calculate(instruction=instruction)
        self.assertEqual(result, '101')  # 10 / 2 = 5
    
    def test_25_instruction_repr(self) -> None:
        """Test string representation of BinaryInstruction."""
        instruction = BinaryInstruction(
            operand_1='1010',
            operand_2='0101',
            operation='+')
        
        repr_str = repr(instruction)
        self.assertIn("operand_1='1010'", repr_str)
        self.assertIn("operand_2='0101'", repr_str)
        self.assertIn("operation='+'", repr_str)
        self.assertIn("state=calculate", repr_str)
    
    def test_26_large_numbers_addition(self) -> None:
        """Test addition with large binary numbers."""
        result = self.arithmetic.add(
            operand_1='11111111',
            operand_2='1')
        self.assertEqual(result, '100000000')  # 255 + 1 = 256
    
    def test_27_large_numbers_multiplication(self) -> None:
        """Test multiplication with large binary numbers."""
        result = self.arithmetic.multiply(
            operand_1='1111',
            operand_2='1111')
        self.assertEqual(result, '11100001')  # 15 * 15 = 225


if __name__ == '__main__':
    p_ut.main()

