"""Comprehensive and in-depth tests for binary-decimal conversions."""

import unittest as p_ut
import random as p_rnd
from binary_calculator import BinaryConverter


class TestBinaryToDecimalConversion(p_ut.TestCase):
    """Extensive tests for binary to decimal conversion."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.converter = BinaryConverter()
    
    def test_01_zero_conversion(self) -> None:
        """Test conversion of zero in various representations."""
        test_cases = ['0', '00', '000', '0000', '00000000']
        for binary_str in test_cases:
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                0,
                msg=f"Failed for {binary_str}")
    
    def test_02_single_bit_values(self) -> None:
        """Test all single bit positions."""
        for bit_position in range(32):
            binary_str = '1' + ('0' * bit_position)
            expected = 2 ** bit_position
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for bit position {bit_position}")
    
    def test_03_all_bits_set(self) -> None:
        """Test numbers with all bits set for various widths."""
        for num_bits in [1, 2, 4, 8, 16, 32, 64, 128]:
            binary_str = '1' * num_bits
            expected = (2 ** num_bits) - 1
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {num_bits} bits")
    
    def test_04_powers_of_two(self) -> None:
        """Test all powers of two up to 2^100."""
        for power in range(101):
            expected = 2 ** power
            binary_str = bin(expected)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for 2^{power}")
    
    def test_05_powers_of_two_minus_one(self) -> None:
        """Test (2^n - 1) for various n."""
        for power in range(1, 65):
            expected = (2 ** power) - 1
            binary_str = bin(expected)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for 2^{power} - 1")
    
    def test_06_eight_bit_boundaries(self) -> None:
        """Test 8-bit boundary values."""
        test_cases = {
            '00000000': 0,
            '00000001': 1,
            '01111111': 127,
            '10000000': 128,
            '11111110': 254,
            '11111111': 255}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_07_sixteen_bit_boundaries(self) -> None:
        """Test 16-bit boundary values."""
        test_cases = {
            '0000000000000000': 0,
            '0000000000000001': 1,
            '0111111111111111': 32767,
            '1000000000000000': 32768,
            '1111111111111110': 65534,
            '1111111111111111': 65535}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_08_thirtytwo_bit_boundaries(self) -> None:
        """Test 32-bit boundary values."""
        test_cases = {
            '0' * 32: 0,
            '0' * 31 + '1': 1,
            '0' + '1' * 31: 2147483647,
            '1' + '0' * 31: 2147483648,
            '1' * 31 + '0': 4294967294,
            '1' * 32: 4294967295}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_09_sixtyfour_bit_boundaries(self) -> None:
        """Test 64-bit boundary values."""
        test_cases = {
            '0' * 64: 0,
            '0' * 63 + '1': 1,
            '0' + '1' * 63: 9223372036854775807,
            '1' + '0' * 63: 9223372036854775808,
            '1' * 64: 18446744073709551615}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_10_sequential_numbers_small(self) -> None:
        """Test sequential numbers from 0 to 1000."""
        for decimal in range(1001):
            binary_str = bin(decimal)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                decimal,
                msg=f"Failed for {decimal}")
    
    def test_11_sequential_numbers_around_boundaries(self) -> None:
        """Test sequential numbers around important boundaries."""
        boundaries = [127, 128, 255, 256, 1023, 1024, 32767, 32768,
                      65535, 65536]
        
        for boundary in boundaries:
            for offset in range(-10, 11):
                decimal = boundary + offset
                if decimal >= 0:
                    binary_str = bin(decimal)[2:]
                    result = self.converter.binary_to_decimal(
                        binary_str=binary_str)
                    self.assertEqual(
                        result,
                        decimal,
                        msg=f"Failed for {decimal}")
    
    def test_12_alternating_bit_patterns(self) -> None:
        """Test alternating bit patterns."""
        test_cases = {
            '10101010': 170,
            '01010101': 85,
            '1010101010101010': 43690,
            '0101010101010101': 21845,
            '10': 2,
            '101': 5,
            '1010': 10,
            '10101': 21}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_13_walking_ones_pattern(self) -> None:
        """Test walking ones pattern (single 1 walking through positions)."""
        for length in [8, 16, 32]:
            for position in range(length):
                binary_str = '0' * position + '1' + '0' * (length - position - 1)
                expected = 2 ** (length - position - 1)
                result = self.converter.binary_to_decimal(
                    binary_str=binary_str)
                self.assertEqual(
                    result,
                    expected,
                    msg=f"Failed for position {position} in {length} bits")
    
    def test_14_walking_zeros_pattern(self) -> None:
        """Test walking zeros pattern (single 0 in field of 1s)."""
        for length in [8, 16, 32]:
            for position in range(length):
                binary_str = '1' * position + '0' + '1' * (length - position - 1)
                expected = (2 ** length) - 1 - (2 ** (length - position - 1))
                result = self.converter.binary_to_decimal(
                    binary_str=binary_str)
                self.assertEqual(
                    result,
                    expected,
                    msg=f"Failed for position {position} in {length} bits")
    
    def test_15_fibonacci_numbers(self) -> None:
        """Test Fibonacci sequence numbers up to large values."""
        fib_prev, fib_curr = 0, 1
        for _ in range(100):
            if fib_curr > 0:
                binary_str = bin(fib_curr)[2:]
                result = self.converter.binary_to_decimal(
                    binary_str=binary_str)
                self.assertEqual(
                    result,
                    fib_curr,
                    msg=f"Failed for Fibonacci number {fib_curr}")
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    
    def test_16_mersenne_numbers(self) -> None:
        """Test Mersenne numbers (2^p - 1)."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71]
        
        for prime in primes:
            mersenne = (2 ** prime) - 1
            binary_str = bin(mersenne)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                mersenne,
                msg=f"Failed for Mersenne number 2^{prime} - 1")
    
    def test_17_random_large_numbers(self) -> None:
        """Test random large numbers."""
        p_rnd.seed(42)
        
        for _ in range(100):
            # Generate random numbers with varying bit lengths
            bit_length = p_rnd.randint(1, 256)
            decimal = p_rnd.randint(0, 2 ** bit_length - 1)
            binary_str = bin(decimal)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                decimal,
                msg=f"Failed for random number {decimal}")
    
    def test_18_very_large_numbers(self) -> None:
        """Test very large numbers (hundreds of bits)."""
        test_cases = [
            2 ** 100,
            2 ** 200,
            2 ** 500,
            2 ** 1000,
            (2 ** 100) - 1,
            (2 ** 256) - 1,
            (2 ** 512) + 12345]
        
        for decimal in test_cases:
            binary_str = bin(decimal)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                decimal,
                msg=f"Failed for {decimal}")
    
    def test_19_prime_numbers(self) -> None:
        """Test prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                  107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                  167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                  229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281]
        
        for prime in primes:
            binary_str = bin(prime)[2:]
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                prime,
                msg=f"Failed for prime {prime}")
    
    def test_20_specific_patterns(self) -> None:
        """Test specific bit patterns."""
        test_cases = {
            '11001100': 204,
            '11110000': 240,
            '00001111': 15,
            '11111110': 254,
            '01111111': 127,
            '10000001': 129,
            '11000011': 195,
            '00111100': 60}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")


class TestDecimalToBinaryConversion(p_ut.TestCase):
    """Extensive tests for decimal to binary conversion."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.converter = BinaryConverter()
    
    def test_01_zero_conversion(self) -> None:
        """Test conversion of zero."""
        result = self.converter.decimal_to_binary(decimal_num=0)
        self.assertEqual(result, '0')
    
    def test_02_single_bit_values(self) -> None:
        """Test all single bit positions."""
        for bit_position in range(32):
            decimal_num = 2 ** bit_position
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = '1' + ('0' * bit_position)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for 2^{bit_position}")
    
    def test_03_powers_of_two(self) -> None:
        """Test all powers of two up to 2^100."""
        for power in range(101):
            decimal_num = 2 ** power
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for 2^{power}")
    
    def test_04_powers_of_two_minus_one(self) -> None:
        """Test (2^n - 1) for various n."""
        for power in range(1, 65):
            decimal_num = (2 ** power) - 1
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = '1' * power
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for 2^{power} - 1")
    
    def test_05_eight_bit_range(self) -> None:
        """Test all 8-bit values (0-255)."""
        for decimal_num in range(256):
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_06_sixteen_bit_boundaries(self) -> None:
        """Test 16-bit boundary values."""
        test_cases = [0, 1, 127, 128, 255, 256, 32767, 32768, 65535]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_07_thirtytwo_bit_boundaries(self) -> None:
        """Test 32-bit boundary values."""
        test_cases = [
            0,
            1,
            2147483647,
            2147483648,
            4294967295]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_08_sixtyfour_bit_boundaries(self) -> None:
        """Test 64-bit boundary values."""
        test_cases = [
            0,
            1,
            9223372036854775807,
            9223372036854775808,
            18446744073709551615]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_09_sequential_numbers_small(self) -> None:
        """Test sequential numbers from 0 to 1000."""
        for decimal_num in range(1001):
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_10_sequential_numbers_around_boundaries(self) -> None:
        """Test sequential numbers around important boundaries."""
        boundaries = [127, 128, 255, 256, 1023, 1024, 32767, 32768,
                      65535, 65536]
        
        for boundary in boundaries:
            for offset in range(-10, 11):
                decimal_num = boundary + offset
                if decimal_num >= 0:
                    result = self.converter.decimal_to_binary(
                        decimal_num=decimal_num)
                    expected = bin(decimal_num)[2:]
                    self.assertEqual(
                        result,
                        expected,
                        msg=f"Failed for {decimal_num}")
    
    def test_11_negative_numbers(self) -> None:
        """Test negative number conversions."""
        test_cases = [-1, -5, -10, -100, -255, -1000, -32768, -65536]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            # Should have '-' prefix
            self.assertTrue(
                result.startswith('-'),
                msg=f"Negative result should start with '-' for {decimal_num}")
            # Rest should be valid binary
            binary_part = result[1:]
            self.assertTrue(
                all(c in '01' for c in binary_part),
                msg=f"Invalid binary part for {decimal_num}")
    
    def test_12_fibonacci_numbers(self) -> None:
        """Test Fibonacci sequence numbers."""
        fib_prev, fib_curr = 0, 1
        for _ in range(100):
            result = self.converter.decimal_to_binary(
                decimal_num=fib_curr)
            expected = bin(fib_curr)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for Fibonacci number {fib_curr}")
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    
    def test_13_mersenne_numbers(self) -> None:
        """Test Mersenne numbers (2^p - 1)."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71]
        
        for prime in primes:
            mersenne = (2 ** prime) - 1
            result = self.converter.decimal_to_binary(
                decimal_num=mersenne)
            expected = '1' * prime
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for Mersenne number 2^{prime} - 1")
    
    def test_14_random_large_numbers(self) -> None:
        """Test random large numbers."""
        p_rnd.seed(42)
        
        for _ in range(100):
            bit_length = p_rnd.randint(1, 256)
            decimal_num = p_rnd.randint(0, 2 ** bit_length - 1)
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for random number {decimal_num}")
    
    def test_15_very_large_numbers(self) -> None:
        """Test very large numbers (hundreds of bits)."""
        test_cases = [
            2 ** 100,
            2 ** 200,
            2 ** 500,
            2 ** 1000,
            (2 ** 100) - 1,
            (2 ** 256) - 1,
            (2 ** 512) + 12345]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            expected = bin(decimal_num)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {decimal_num}")
    
    def test_16_prime_numbers(self) -> None:
        """Test prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                  107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                  167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                  229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281]
        
        for prime in primes:
            result = self.converter.decimal_to_binary(
                decimal_num=prime)
            expected = bin(prime)[2:]
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for prime {prime}")
    
    def test_17_no_leading_zeros(self) -> None:
        """Test that results have no unnecessary leading zeros."""
        test_cases = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        
        for decimal_num in test_cases:
            result = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            self.assertTrue(
                result[0] == '1' or result == '0',
                msg=f"Leading zeros found in {result} for {decimal_num}")
    
    def test_18_consistency_check(self) -> None:
        """Test that repeated conversions are consistent."""
        test_values = [0, 1, 42, 255, 1024, 65535]
        
        for decimal_num in test_values:
            result_1 = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            result_2 = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            self.assertEqual(
                result_1,
                result_2,
                msg=f"Inconsistent results for {decimal_num}")


class TestRoundTripConversion(p_ut.TestCase):
    """Test round-trip conversions (binary -> decimal -> binary)."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.converter = BinaryConverter()
    
    def test_01_round_trip_binary_to_decimal_to_binary(self) -> None:
        """Test binary -> decimal -> binary preserves value."""
        test_cases = [
            '0', '1', '10', '11', '100', '1010', '1111',
            '10000000', '11111111', '10101010', '01010101']
        
        for original_binary in test_cases:
            decimal = self.converter.binary_to_decimal(
                binary_str=original_binary)
            result_binary = self.converter.decimal_to_binary(
                decimal_num=decimal)
            
            # Remove leading zeros for comparison
            normalized_original = original_binary.lstrip('0') or '0'
            self.assertEqual(
                result_binary,
                normalized_original,
                msg=f"Round trip failed for {original_binary}")
    
    def test_02_round_trip_decimal_to_binary_to_decimal(self) -> None:
        """Test decimal -> binary -> decimal preserves value."""
        test_cases = [0, 1, 2, 3, 10, 15, 100, 255, 1000, 65535]
        
        for original_decimal in test_cases:
            binary = self.converter.decimal_to_binary(
                decimal_num=original_decimal)
            result_decimal = self.converter.binary_to_decimal(
                binary_str=binary)
            self.assertEqual(
                result_decimal,
                original_decimal,
                msg=f"Round trip failed for {original_decimal}")
    
    def test_03_round_trip_large_numbers(self) -> None:
        """Test round-trip with large numbers."""
        test_cases = [
            2 ** 50,
            2 ** 100,
            2 ** 200,
            (2 ** 64) - 1,
            (2 ** 128) - 1]
        
        for original_decimal in test_cases:
            binary = self.converter.decimal_to_binary(
                decimal_num=original_decimal)
            result_decimal = self.converter.binary_to_decimal(
                binary_str=binary)
            self.assertEqual(
                result_decimal,
                original_decimal,
                msg=f"Round trip failed for {original_decimal}")
    
    def test_04_round_trip_random_numbers(self) -> None:
        """Test round-trip with random numbers."""
        p_rnd.seed(42)
        
        for _ in range(200):
            bit_length = p_rnd.randint(1, 128)
            original_decimal = p_rnd.randint(0, 2 ** bit_length - 1)
            
            binary = self.converter.decimal_to_binary(
                decimal_num=original_decimal)
            result_decimal = self.converter.binary_to_decimal(
                binary_str=binary)
            
            self.assertEqual(
                result_decimal,
                original_decimal,
                msg=f"Round trip failed for {original_decimal}")
    
    def test_05_round_trip_sequential_range(self) -> None:
        """Test round-trip for sequential numbers."""
        for original_decimal in range(2000):
            binary = self.converter.decimal_to_binary(
                decimal_num=original_decimal)
            result_decimal = self.converter.binary_to_decimal(
                binary_str=binary)
            self.assertEqual(
                result_decimal,
                original_decimal,
                msg=f"Round trip failed for {original_decimal}")


class TestConversionEdgeCases(p_ut.TestCase):
    """Test edge cases and special scenarios."""
    
    def setUp(self) -> None:
        """Set up test fixtures."""
        self.converter = BinaryConverter()
    
    def test_01_leading_zeros_in_binary(self) -> None:
        """Test that leading zeros don't affect conversion."""
        test_cases = [
            ('1', '01', '001', '0001'),
            ('10', '010', '0010', '00010'),
            ('101', '0101', '00101', '000101')]
        
        for group in test_cases:
            results = [
                self.converter.binary_to_decimal(binary_str=b)
                for b in group]
            
            # All should be equal
            self.assertTrue(
                all(r == results[0] for r in results),
                msg=f"Leading zeros affected conversion for {group}")
    
    def test_02_maximum_python_int_support(self) -> None:
        """Test support for very large Python integers."""
        # Python supports arbitrary precision integers
        huge_number = 10 ** 100
        binary = self.converter.decimal_to_binary(
            decimal_num=huge_number)
        result = self.converter.binary_to_decimal(binary_str=binary)
        self.assertEqual(result, huge_number)
    
    def test_03_specific_problematic_values(self) -> None:
        """Test values that might cause issues."""
        test_cases = {
            '1000000000000000': 32768,
            '111111111111111': 32767,
            '10000000': 128,
            '1111111': 127}
        
        for binary_str, expected in test_cases.items():
            result = self.converter.binary_to_decimal(
                binary_str=binary_str)
            self.assertEqual(
                result,
                expected,
                msg=f"Failed for {binary_str}")
    
    def test_04_bit_length_verification(self) -> None:
        """Verify bit lengths are correct."""
        for power in range(1, 20):
            decimal_num = 2 ** power
            binary = self.converter.decimal_to_binary(
                decimal_num=decimal_num)
            # 2^n should have (n+1) bits
            self.assertEqual(
                len(binary),
                power + 1,
                msg=f"Wrong bit length for 2^{power}")
    
    def test_05_alternating_patterns_consistency(self) -> None:
        """Test alternating bit patterns convert correctly."""
        patterns = [
            '10' * 10,
            '01' * 10,
            '10' * 20,
            '01' * 20,
            '110' * 10,
            '101' * 10]
        
        for pattern in patterns:
            decimal = self.converter.binary_to_decimal(
                binary_str=pattern)
            binary = self.converter.decimal_to_binary(
                decimal_num=decimal)
            # Remove leading zeros
            normalized = pattern.lstrip('0') or '0'
            self.assertEqual(
                binary,
                normalized,
                msg=f"Pattern conversion failed for {pattern}")


if __name__ == '__main__':
    p_ut.main()

