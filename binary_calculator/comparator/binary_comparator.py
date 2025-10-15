"""Binary comparator class for comparing binary strings."""


class BinaryComparator:
    """Comparator for binary string comparison operations.
    
    This class provides methods for comparing binary strings without
    converting to decimal, working directly on the string representations.
    """
    
    @staticmethod
    def compare(*, binary_1: str, binary_2: str) -> int:
        """Compare two binary strings.
        
        Compares binary strings by first removing leading zeros, then
        comparing lengths, and finally comparing lexicographically if
        lengths are equal.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            -1 if binary_1 < binary_2
             0 if binary_1 == binary_2
             1 if binary_1 > binary_2
             
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.compare(binary_1='101', binary_2='11')
            1
            >>> comparator.compare(binary_1='10', binary_2='10')
            0
        """
        # Remove leading zeros for comparison
        b1 = binary_1.lstrip('0') or '0'
        b2 = binary_2.lstrip('0') or '0'
        
        # Compare lengths first
        if len(b1) < len(b2):
            return -1
        elif len(b1) > len(b2):
            return 1
        
        # Same length, compare lexicographically
        if b1 < b2:
            return -1
        elif b1 > b2:
            return 1
        else:
            return 0
    
    def smaller(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if first binary string is smaller than second.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 < binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.smaller(binary_1='10', binary_2='101')
            True
            >>> comparator.smaller(binary_1='101', binary_2='10')
            False
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) < 0
    
    def smaller_equal(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if first binary string is smaller than or equal to second.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 <= binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.smaller_equal(binary_1='10', binary_2='10')
            True
            >>> comparator.smaller_equal(binary_1='10', binary_2='101')
            True
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) <= 0
    
    def larger(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if first binary string is larger than second.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 > binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.larger(binary_1='101', binary_2='10')
            True
            >>> comparator.larger(binary_1='10', binary_2='101')
            False
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) > 0
    
    def larger_equal(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if first binary string is larger than or equal to second.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 >= binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.larger_equal(binary_1='101', binary_2='101')
            True
            >>> comparator.larger_equal(binary_1='101', binary_2='10')
            True
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) >= 0
    
    def equal(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if two binary strings are equal.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 == binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.equal(binary_1='101', binary_2='0101')
            True
            >>> comparator.equal(binary_1='101', binary_2='110')
            False
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) == 0
    
    def not_equal(self, *, binary_1: str, binary_2: str) -> bool:
        """Check if two binary strings are not equal.
        
        Args:
            binary_1: First binary string
            binary_2: Second binary string
            
        Returns:
            True if binary_1 != binary_2, False otherwise
            
        Example:
            >>> comparator = BinaryComparator()
            >>> comparator.not_equal(binary_1='101', binary_2='110')
            True
            >>> comparator.not_equal(binary_1='101', binary_2='0101')
            False
        """
        return self.compare(binary_1=binary_1, binary_2=binary_2) != 0

