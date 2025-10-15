"""Scenario 03: Network Bandwidth Calculation

Real-world context: Network capacity planning and throughput analysis
Operation: Total bits per second / Packet size in bits
Numbers: 1,048,576 / 8,192 = 128 packets per second
"""

import sys
import pathlib as p_pthl

# Add parent directory to path for imports
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, BinaryInstruction, InstructionExecutor


def main() -> None:
    """Calculate packets per second given throughput and packet size."""
    # --8<-- [start:setup]
    executor = InstructionExecutor()
    # --8<-- [end:setup]
    
    # --8<-- [start:create_operands]
    # Throughput: 1048576 bits/second (1 Mbps, exactly 2^20)
    # Binary: 100000000000000000000 (21 bits)
    throughput = BinaryNumber.from_int(decimal_num=1048576)
    
    # Packet size: 8192 bits (1024 bytes, 2^13)
    # Binary: 10000000000000 (14 bits)
    packet_size = BinaryNumber.from_int(decimal_num=8192)
    # --8<-- [end:create_operands]
    
    # --8<-- [start:display_input]
    print("Network Bandwidth Calculation")
    print("=" * 60)
    print(f"Throughput:   {throughput.value}")
    print(f"              ({throughput.to_int()} bits/sec)")
    print(f"              ({throughput.to_int() // 1024} Kbps)")
    print(f"              ({throughput.to_int() // (1024*1024)} Mbps)")
    print(f"              Bit length: {len(throughput.value)} bits")
    print()
    print(f"Packet size:  {packet_size.value}")
    print(f"              ({packet_size.to_int()} bits)")
    print(f"              ({packet_size.to_int() // 8} bytes)")
    print(f"              Bit length: {len(packet_size.value)} bits")
    print()
    # --8<-- [end:display_input]
    
    # --8<-- [start:create_instruction]
    instruction = BinaryInstruction(
        operand_1=throughput,
        operand_2=packet_size,
        operation='/')
    # --8<-- [end:create_instruction]
    
    # --8<-- [start:execute]
    print("Calculation:")
    result = executor.calculate(instruction=instruction, print_result=True)
    # --8<-- [end:execute]
    
    # --8<-- [start:display_result]
    print()
    print(f"Packets per second: {result.to_int()}")
    print(f"Verification:       {1048576 // 8192} packets/sec")
    print("=" * 60)
    # --8<-- [end:display_result]


if __name__ == '__main__':
    main()

