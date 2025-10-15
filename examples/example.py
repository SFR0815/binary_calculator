"""Central Example Runner - CLI Interface for Binary Calculator Examples

This script provides a command-line interface to run individual examples or
groups of examples from the binary calculator documentation.

Usage:
    python examples/example.py numb01              # Run specific example
    python examples/example.py --all-numb          # Run all BinaryNumber examples
    python examples/example.py --all               # Run all examples
    python examples/example.py --list              # List all available examples

Example Keys:
    numb01-numb09: BinaryNumber examples
    inst01-inst06: BinaryInstruction examples
    calc01-calc07: ArithmeticCalculator examples
    comp01-comp09: BinaryComparator examples
    conv01-conv07: BinaryConverter examples
    norm01-norm06: BinaryNormalizer examples
    exec01-exec09: InstructionExecutor examples
"""

import sys
import pathlib as p_pthl
import argparse as p_argp
import typing as p_typ

# Add parent directory to path
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent))

# Import all example modules
from examples.basic import example_01_binary_number as numb
from examples.basic import example_02_binary_instruction as inst
from examples.basic import example_03_arithmetic_calculator as calc
from examples.basic import example_04_binary_comparator as comp
from examples.basic import example_05_binary_converter as conv
from examples.basic import example_06_binary_normalizer as norm
from examples.basic import example_07_instruction_executor as exec_mod


# Example registry mapping keys to (function, description)
EXAMPLES: p_typ.Dict[str, p_typ.Tuple[p_typ.Callable, str]] = {
    # BinaryNumber examples
    'numb01': (numb.numb01_create_from_string, 'Create from string'),
    'numb02': (numb.numb02_create_from_int, 'Create from integer'),
    'numb03': (numb.numb03_convert_to_int, 'Convert to integer'),
    'numb04': (numb.numb04_increment, 'Increment operations'),
    'numb05': (numb.numb05_decrement, 'Decrement operations'),
    'numb06': (numb.numb06_copy, 'Copy operation'),
    'numb07': (numb.numb07_comparisons, 'Comparison operators'),
    'numb08': (numb.numb08_error_handling, 'Error handling'),
    'numb09': (numb.numb09_larger_numbers, 'Larger numbers'),
    
    # BinaryInstruction examples
    'inst01': (inst.inst01_create_arithmetic_instruction, 'Create arithmetic instruction'),
    'inst02': (inst.inst02_create_comparison_instruction, 'Create comparison instruction'),
    'inst03': (inst.inst03_all_operations, 'All operations'),
    'inst04': (inst.inst04_repr_indent, 'Representation indentation'),
    'inst05': (inst.inst05_error_handling, 'Error handling'),
    'inst06': (inst.inst06_larger_numbers, 'Larger numbers'),
    
    # ArithmeticCalculator examples
    'calc01': (calc.calc01_addition, 'Addition'),
    'calc02': (calc.calc02_subtraction, 'Subtraction'),
    'calc03': (calc.calc03_multiplication, 'Multiplication'),
    'calc04': (calc.calc04_division, 'Division'),
    'calc05': (calc.calc05_chained_operations, 'Chained operations'),
    'calc06': (calc.calc06_error_handling, 'Error handling'),
    'calc07': (calc.calc07_larger_numbers, 'Larger numbers'),
    
    # BinaryComparator examples
    'comp01': (comp.comp01_basic_compare, 'Basic compare'),
    'comp02': (comp.comp02_smaller, 'Less than'),
    'comp03': (comp.comp03_smaller_equal, 'Less than or equal'),
    'comp04': (comp.comp04_larger, 'Greater than'),
    'comp05': (comp.comp05_larger_equal, 'Greater than or equal'),
    'comp06': (comp.comp06_equal, 'Equality'),
    'comp07': (comp.comp07_not_equal, 'Inequality'),
    'comp08': (comp.comp08_all_comparisons, 'All comparisons'),
    'comp09': (comp.comp09_larger_numbers, 'Larger numbers'),
    
    # BinaryConverter examples
    'conv01': (conv.conv01_binary_to_decimal, 'Binary to decimal'),
    'conv02': (conv.conv02_decimal_to_binary, 'Decimal to binary'),
    'conv03': (conv.conv03_round_trip, 'Round-trip conversion'),
    'conv04': (conv.conv04_powers_of_two, 'Powers of 2'),
    'conv05': (conv.conv05_large_numbers, 'Larger numbers'),
    'conv06': (conv.conv06_comparison, 'Representation comparison'),
    'conv07': (conv.conv07_realistic_conversions, 'Realistic conversions'),
    
    # BinaryNormalizer examples
    'norm01': (norm.norm01_remove_leading_zeros, 'Remove leading zeros'),
    'norm02': (norm.norm02_normalize_length, 'Normalize length'),
    'norm03': (norm.norm03_practical_use, 'Practical use case'),
    'norm04': (norm.norm04_edge_cases, 'Edge cases'),
    'norm05': (norm.norm05_comparison_demo, 'Why normalization matters'),
    'norm06': (norm.norm06_larger_numbers, 'Larger numbers'),
    
    # InstructionExecutor examples
    'exec01': (exec_mod.exec01_simple_addition, 'Simple addition'),
    'exec02': (exec_mod.exec02_formatted_addition, 'Formatted addition'),
    'exec03': (exec_mod.exec03_subtraction, 'Subtraction'),
    'exec04': (exec_mod.exec04_multiplication, 'Multiplication'),
    'exec05': (exec_mod.exec05_division, 'Division'),
    'exec06': (exec_mod.exec06_comparison, 'Comparison'),
    'exec07': (exec_mod.exec07_all_comparisons, 'All comparisons'),
    'exec08': (exec_mod.exec08_error_handling, 'Error handling'),
    'exec09': (exec_mod.exec09_larger_numbers, 'Larger numbers'),
}


# Group definitions
GROUPS: p_typ.Dict[str, p_typ.List[str]] = {
    'numb': [k for k in EXAMPLES if k.startswith('numb')],
    'inst': [k for k in EXAMPLES if k.startswith('inst')],
    'calc': [k for k in EXAMPLES if k.startswith('calc')],
    'comp': [k for k in EXAMPLES if k.startswith('comp')],
    'conv': [k for k in EXAMPLES if k.startswith('conv')],
    'norm': [k for k in EXAMPLES if k.startswith('norm')],
    'exec': [k for k in EXAMPLES if k.startswith('exec')],
}


def list_examples() -> None:
    """List all available examples organized by component."""
    print("=" * 70)
    print("Available Examples")
    print("=" * 70)
    print()
    
    for group_name, keys in GROUPS.items():
        component_names = {
            'numb': 'BinaryNumber',
            'inst': 'BinaryInstruction',
            'calc': 'ArithmeticCalculator',
            'comp': 'BinaryComparator',
            'conv': 'BinaryConverter',
            'norm': 'BinaryNormalizer',
            'exec': 'InstructionExecutor'}
        
        print(f"{component_names[group_name]} Examples:")
        for key in keys:
            func, desc = EXAMPLES[key]
            print(f"  {key:8} - {desc}")
        print()
    
    print("Group Commands:")
    for group_name in GROUPS:
        print(f"  --all-{group_name:4} - Run all {group_name} examples")
    print(f"  --all        - Run ALL examples")
    print()
    print("=" * 70)


def run_example(key: str) -> None:
    """Run a single example by key."""
    if key in EXAMPLES:
        func, desc = EXAMPLES[key]
        func()
    else:
        print(f"Unknown example key: {key}")
        print(f"Use '--list' to see all available examples")
        sys.exit(1)


def run_group(group_name: str) -> None:
    """Run all examples in a group."""
    if group_name in GROUPS:
        print(f"Running all {group_name} examples...")
        print()
        for key in GROUPS[group_name]:
            func, desc = EXAMPLES[key]
            func()
    else:
        print(f"Unknown group: {group_name}")
        print(f"Available groups: {', '.join(GROUPS.keys())}")
        sys.exit(1)


def run_all() -> None:
    """Run all examples in order."""
    print("Running ALL examples...")
    print()
    
    for group_name in ['numb', 'inst', 'calc', 'comp', 'conv', 'norm', 'exec']:
        for key in GROUPS[group_name]:
            func, desc = EXAMPLES[key]
            func()


def main() -> None:
    """Main entry point for CLI."""
    parser = p_argp.ArgumentParser(
        description='Binary Calculator Examples Runner',
        epilog='Use --list to see all available examples')
    
    parser.add_argument(
        'example',
        nargs='?',
        help='Example key (e.g., numb01, calc03, exec09)')
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all available examples')
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all examples')
    
    parser.add_argument(
        '--all-numb',
        action='store_true',
        help='Run all BinaryNumber examples')
    
    parser.add_argument(
        '--all-inst',
        action='store_true',
        help='Run all BinaryInstruction examples')
    
    parser.add_argument(
        '--all-calc',
        action='store_true',
        help='Run all ArithmeticCalculator examples')
    
    parser.add_argument(
        '--all-comp',
        action='store_true',
        help='Run all BinaryComparator examples')
    
    parser.add_argument(
        '--all-conv',
        action='store_true',
        help='Run all BinaryConverter examples')
    
    parser.add_argument(
        '--all-norm',
        action='store_true',
        help='Run all BinaryNormalizer examples')
    
    parser.add_argument(
        '--all-exec',
        action='store_true',
        help='Run all InstructionExecutor examples')
    
    args = parser.parse_args()
    
    # Handle --list
    if args.list:
        list_examples()
        return
    
    # Handle --all
    if args.all:
        run_all()
        return
    
    # Handle group flags
    if args.all_numb:
        run_group(group_name='numb')
        return
    if args.all_inst:
        run_group(group_name='inst')
        return
    if args.all_calc:
        run_group(group_name='calc')
        return
    if args.all_comp:
        run_group(group_name='comp')
        return
    if args.all_conv:
        run_group(group_name='conv')
        return
    if args.all_norm:
        run_group(group_name='norm')
        return
    if args.all_exec:
        run_group(group_name='exec')
        return
    
    # Handle individual example
    if args.example:
        run_example(key=args.example)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

