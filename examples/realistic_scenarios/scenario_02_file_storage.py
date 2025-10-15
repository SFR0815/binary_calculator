"""Scenario 02: File Storage Calculation

Real-world context: Disk space management and capacity planning
Operation: File size 1 + File size 2
Numbers: 524,288 + 786,432 = 1,310,720 bytes (1.25 MB)
"""

import sys
import pathlib as p_pthl

# Add parent directory to path for imports
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, BinaryInstruction, InstructionExecutor


def main() -> None:
    """Calculate total storage for multiple files."""
    # --8<-- [start:setup]
    executor = InstructionExecutor()
    # --8<-- [end:setup]
    
    # --8<-- [start:create_operands]
    # File 1: 524288 bytes (512 KB, exactly 2^19)
    # Binary: 10000000000000000000 (20 bits)
    file1_size = BinaryNumber.from_int(decimal_num=524288)
    
    # File 2: 786432 bytes (768 KB, 3 × 2^18)
    # Binary: 11000000000000000000 (20 bits)
    file2_size = BinaryNumber.from_int(decimal_num=786432)
    # --8<-- [end:create_operands]
    
    # --8<-- [start:display_input]
    print("File Storage Calculation")
    print("=" * 60)
    print(f"File 1 size:  {file1_size.value}")
    print(f"              ({file1_size.to_int()} bytes = "
          f"{file1_size.to_int() // 1024} KB)")
    print(f"              Bit length: {len(file1_size.value)} bits")
    print()
    print(f"File 2 size:  {file2_size.value}")
    print(f"              ({file2_size.to_int()} bytes = "
          f"{file2_size.to_int() // 1024} KB)")
    print(f"              Bit length: {len(file2_size.value)} bits")
    print()
    # --8<-- [end:display_input]
    
    # --8<-- [start:create_instruction]
    instruction = BinaryInstruction(
        operand_1=file1_size,
        operand_2=file2_size,
        operation='+')
    # --8<-- [end:create_instruction]
    
    # --8<-- [start:execute]
    print("Calculation:")
    result = executor.calculate(instruction=instruction, print_result=True)
    # --8<-- [end:execute]
    
    # --8<-- [start:display_result]
    print()
    total_kb = result.to_int() // 1024
    total_mb = result.to_int() / (1024 * 1024)
    print(f"Total storage: {result.to_int()} bytes")
    print(f"               {total_kb} KB")
    print(f"               {total_mb:.2f} MB")
    print(f"Verification:  512 KB + 768 KB = {total_kb} KB")
    print("=" * 60)
    # --8<-- [end:display_result]


if __name__ == '__main__':
    main()

