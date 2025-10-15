"""Binary normalizer class for binary string utility operations."""

import typing as p_typ


class BinaryNormalizer:
    """Normalizer for binary string utility operations.
    
    This class provides utility methods for normalizing binary strings,
    such as padding to equal length and removing leading zeros.
    """
    
    @staticmethod
    def normalize_length(
            *,
            binary_1: str,
            binary_2: str) -> p_typ.Tuple[str, str]:
        """Normalize two binary strings to same length by padding with zeros.
        
        Pads the shorter binary string with leading zeros so both strings
        have the same length. This is useful for bit-by-bit operations.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            Tuple of normalized binary strings with equal length
            
        Example:
            >>> normalizer = BinaryNormalizer()
            >>> normalizer.normalize_length(binary_1='101', binary_2='11')
            ('101', '011')
        """
        max_len = max(len(binary_1), len(binary_2))
        return binary_1.zfill(max_len), binary_2.zfill(max_len)
    
    @staticmethod
    def remove_leading_zeros(*, binary_str: str) -> str:
        """Remove leading zeros from binary string.
        
        Strips all leading zeros from a binary string, except when the
        entire string is zeros (returns '0').
        
        Args:
            binary_str: Binary string potentially with leading zeros
            
        Returns:
            Binary string without leading zeros (except for '0' itself)
            
        Example:
            >>> normalizer = BinaryNormalizer()
            >>> normalizer.remove_leading_zeros(binary_str='00101')
            '101'
            >>> normalizer.remove_leading_zeros(binary_str='000')
            '0'
        """
        result = binary_str.lstrip('0')
        return result if result else '0'

