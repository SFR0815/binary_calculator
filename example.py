"""Binary Calculator Examples - CLI Runner Shortcut

This is a convenience shortcut to the main example runner.
For the comprehensive demonstration, see example_comprehensive_demo.py

Usage:
    python example.py numb01       # Run specific example
    python example.py --all-calc   # Run all calculator examples
    python example.py --all        # Run all examples
    python example.py --list       # List available examples

For more information, see: examples/example.py
"""

import sys
import pathlib as p_pthl

# Add examples directory to path
examples_dir = p_pthl.Path(__file__).parent / 'examples'
sys.path.insert(0, str(p_pthl.Path(__file__).parent))

# Import and run the main example runner
from examples.example import main

if __name__ == '__main__':
    main()
