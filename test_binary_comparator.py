"""Unit tests for BinaryComparator class."""

import unittest as p_ut
from binary_calculator import BinaryComparator


class TestBinaryComparator(p_ut.TestCase):
    """Test suite for BinaryComparator class."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.comparator = BinaryComparator()
    
    def test_01_compare_equal(self) -> None:
        """Test compare method with equal values."""
        result = self.comparator.compare(binary_1='101', binary_2='101')
        self.assertEqual(result, 0)
        
        # With leading zeros
        result = self.comparator.compare(binary_1='0101', binary_2='101')
        self.assertEqual(result, 0)
    
    def test_02_compare_smaller(self) -> None:
        """Test compare method when first is smaller."""
        result = self.comparator.compare(binary_1='10', binary_2='101')
        self.assertEqual(result, -1)
    
    def test_03_compare_larger(self) -> None:
        """Test compare method when first is larger."""
        result = self.comparator.compare(binary_1='101', binary_2='10')
        self.assertEqual(result, 1)
    
    def test_04_smaller_true(self) -> None:
        """Test smaller method returns True."""
        self.assertTrue(self.comparator.smaller(
            binary_1='10',
            binary_2='101'))
        self.assertTrue(self.comparator.smaller(
            binary_1='1',
            binary_2='10'))
    
    def test_05_smaller_false(self) -> None:
        """Test smaller method returns False."""
        self.assertFalse(self.comparator.smaller(
            binary_1='101',
            binary_2='10'))
        self.assertFalse(self.comparator.smaller(
            binary_1='101',
            binary_2='101'))
    
    def test_06_smaller_equal_true(self) -> None:
        """Test smaller_equal method returns True."""
        self.assertTrue(self.comparator.smaller_equal(
            binary_1='10',
            binary_2='101'))
        self.assertTrue(self.comparator.smaller_equal(
            binary_1='101',
            binary_2='101'))
    
    def test_07_smaller_equal_false(self) -> None:
        """Test smaller_equal method returns False."""
        self.assertFalse(self.comparator.smaller_equal(
            binary_1='101',
            binary_2='10'))
    
    def test_08_larger_true(self) -> None:
        """Test larger method returns True."""
        self.assertTrue(self.comparator.larger(
            binary_1='101',
            binary_2='10'))
        self.assertTrue(self.comparator.larger(
            binary_1='1000',
            binary_2='111'))
    
    def test_09_larger_false(self) -> None:
        """Test larger method returns False."""
        self.assertFalse(self.comparator.larger(
            binary_1='10',
            binary_2='101'))
        self.assertFalse(self.comparator.larger(
            binary_1='101',
            binary_2='101'))
    
    def test_10_larger_equal_true(self) -> None:
        """Test larger_equal method returns True."""
        self.assertTrue(self.comparator.larger_equal(
            binary_1='101',
            binary_2='10'))
        self.assertTrue(self.comparator.larger_equal(
            binary_1='101',
            binary_2='101'))
    
    def test_11_larger_equal_false(self) -> None:
        """Test larger_equal method returns False."""
        self.assertFalse(self.comparator.larger_equal(
            binary_1='10',
            binary_2='101'))
    
    def test_12_equal_true(self) -> None:
        """Test equal method returns True."""
        self.assertTrue(self.comparator.equal(
            binary_1='101',
            binary_2='101'))
        self.assertTrue(self.comparator.equal(
            binary_1='0101',
            binary_2='101'))
        self.assertTrue(self.comparator.equal(
            binary_1='00000',
            binary_2='0'))
    
    def test_13_equal_false(self) -> None:
        """Test equal method returns False."""
        self.assertFalse(self.comparator.equal(
            binary_1='101',
            binary_2='110'))
        self.assertFalse(self.comparator.equal(
            binary_1='10',
            binary_2='101'))
    
    def test_14_not_equal_true(self) -> None:
        """Test not_equal method returns True."""
        self.assertTrue(self.comparator.not_equal(
            binary_1='101',
            binary_2='110'))
        self.assertTrue(self.comparator.not_equal(
            binary_1='10',
            binary_2='101'))
    
    def test_15_not_equal_false(self) -> None:
        """Test not_equal method returns False."""
        self.assertFalse(self.comparator.not_equal(
            binary_1='101',
            binary_2='101'))
        self.assertFalse(self.comparator.not_equal(
            binary_1='0101',
            binary_2='101'))
    
    def test_16_compare_with_leading_zeros(self) -> None:
        """Test all comparisons handle leading zeros correctly."""
        # Equal with different leading zeros
        self.assertTrue(self.comparator.equal(
            binary_1='00101',
            binary_2='000101'))
        
        # Smaller with leading zeros
        self.assertTrue(self.comparator.smaller(
            binary_1='0010',
            binary_2='101'))
        
        # Larger with leading zeros
        self.assertTrue(self.comparator.larger(
            binary_1='00101',
            binary_2='010'))
    
    def test_17_compare_zero_values(self) -> None:
        """Test comparisons with zero values."""
        self.assertTrue(self.comparator.equal(
            binary_1='0',
            binary_2='00'))
        self.assertTrue(self.comparator.larger(
            binary_1='1',
            binary_2='0'))
        self.assertTrue(self.comparator.smaller(
            binary_1='0',
            binary_2='1'))
    
    def test_18_compare_same_length_different_values(self) -> None:
        """Test comparison of same length but different values."""
        self.assertTrue(self.comparator.smaller(
            binary_1='100',
            binary_2='101'))
        self.assertTrue(self.comparator.larger(
            binary_1='111',
            binary_2='110'))
        self.assertFalse(self.comparator.equal(
            binary_1='100',
            binary_2='101'))
    
    def test_19_comprehensive_comparison_set(self) -> None:
        """Test comprehensive set of comparisons."""
        test_cases = [
            ('10', '101', -1),  # 2 < 5
            ('101', '10', 1),   # 5 > 2
            ('11', '11', 0),    # 3 == 3
            ('1010', '1010', 0),  # 10 == 10
            ('1', '1111', -1),  # 1 < 15
            ('1111', '1', 1),   # 15 > 1
        ]
        
        for binary_1, binary_2, expected in test_cases:
            result = self.comparator.compare(
                binary_1=binary_1,
                binary_2=binary_2)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_1} vs {binary_2}")
    
    def test_20_all_comparison_methods_consistent(self) -> None:
        """Test that all comparison methods are consistent."""
        pairs = [
            ('101', '10'),   # 5 > 2
            ('10', '101'),   # 2 < 5
            ('11', '11'),    # 3 == 3
        ]
        
        for binary_1, binary_2 in pairs:
            cmp_result = self.comparator.compare(
                binary_1=binary_1,
                binary_2=binary_2)
            
            # Check consistency
            if cmp_result < 0:
                self.assertTrue(self.comparator.smaller(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.smaller_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.larger(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.larger_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.not_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
            elif cmp_result > 0:
                self.assertFalse(self.comparator.smaller(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.smaller_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.larger(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.larger_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.not_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
            else:  # equal
                self.assertFalse(self.comparator.smaller(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.smaller_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.larger(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.larger_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertTrue(self.comparator.equal(
                    binary_1=binary_1,
                    binary_2=binary_2))
                self.assertFalse(self.comparator.not_equal(
                    binary_1=binary_1,
                    binary_2=binary_2))


if __name__ == '__main__':
    p_ut.main()

