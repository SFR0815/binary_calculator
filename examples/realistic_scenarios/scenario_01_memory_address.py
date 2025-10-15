"""Scenario 01: Memory Address Calculation

Real-world context: Operating system memory management
Operation: Base address + offset
Numbers: 65,536 + 4,096 = 69,632 bytes
"""

import sys
import pathlib as p_pthl

# Add parent directory to path for imports
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, BinaryInstruction, InstructionExecutor


def main() -> None:
    """Calculate memory address by adding base address and offset."""
    # --8<-- [start:setup]
    executor = InstructionExecutor()
    # --8<-- [end:setup]
    
    # --8<-- [start:create_operands]
    # Create base address: 65536 bytes (0x10000, 16-bit boundary)
    base_address = BinaryNumber.from_int(decimal_num=65536)
    
    # Create offset: 4096 bytes (one memory page)
    offset = BinaryNumber.from_int(decimal_num=4096)
    # --8<-- [end:create_operands]
    
    # --8<-- [start:display_input]
    print("Memory Address Calculation")
    print("=" * 60)
    print(f"Base address: {base_address.value}")
    print(f"              ({base_address.to_int()} bytes, "
          f"0x{base_address.to_int():X})")
    print(f"              Bit length: {len(base_address.value)} bits")
    print()
    print(f"Offset:       {offset.value}")
    print(f"              ({offset.to_int()} bytes, "
          f"0x{offset.to_int():X})")
    print(f"              Bit length: {len(offset.value)} bits")
    print()
    # --8<-- [end:display_input]
    
    # --8<-- [start:create_instruction]
    # Create instruction for addition operation
    instruction = BinaryInstruction(
        operand_1=base_address,
        operand_2=offset,
        operation='+')
    # --8<-- [end:create_instruction]
    
    # --8<-- [start:execute]
    # Execute with formatted output display
    print("Calculation:")
    result = executor.calculate(instruction=instruction, print_result=True)
    # --8<-- [end:execute]
    
    # --8<-- [start:display_result]
    print()
    print(f"Final address: {result.to_int()} bytes")
    print(f"               (0x{result.to_int():X})")
    print(f"Verification:  {65536 + 4096} = {result.to_int()}")
    print("=" * 60)
    # --8<-- [end:display_result]


if __name__ == '__main__':
    main()

