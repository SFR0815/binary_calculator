# Technical Context: Binary Calculator

## Technology Stack

### Core Language
- **Python 3.x** (tested with 3.13)
- No external dependencies for core library
- Pure Python implementation

### Development Tools
- **unittest**: Testing framework (built-in)
- **MkDocs**: Documentation generation
- **mkdocs-material**: Documentation theme
- **pymdown-extensions**: Enhanced markdown features

### Documentation Stack
- **MkDocs** version: Latest
- **Theme**: Material for MkDocs
- **Extensions**:
  - `pymdownx.highlight`: Syntax highlighting
  - `pymdownx.snippets`: Code snippet inclusion
  - `pymdownx.superfences`: Enhanced code blocks
  - `pymdownx.inlinehilite`: Inline code highlighting
  - `pymdownx.tabbed`: Tabbed content
  - `admonition`: Call-out boxes
  - `pymdownx.details`: Collapsible sections

### Syntax Highlighting
- **Pygments**: Code highlighter
- **Style**: Monokai
- **Custom CSS**: Enhanced colors for Python
  - Comments: #80D8FF (bright blue)
  - Keywords: #FFD700 (yellow/gold)
  - Functions: #FDD835 (bright yellow)
  - Variables/Attributes: #E040FB (bright purple)
  - Strings: #A5D6A7 (green)
  - Numbers: #FFAB40 (orange)
  - self/cls: #00E5FF (bright cyan)

## Development Setup

### Required Files
```
requirements-docs.txt  # Documentation dependencies
mkdocs.yml            # Documentation configuration
docs/stylesheets/extra.css  # Custom syntax highlighting
```

### Development Commands
```bash
# Install documentation dependencies
pip install -r requirements-docs.txt

# Serve documentation locally
python -m mkdocs serve

# Build static documentation
python -m mkdocs build

# Run all tests
python -m unittest discover

# Run specific test
python -m unittest test_binary_calculator.TestArithmeticCalculator

# Run examples
python example.py --list          # List all
python example.py numb01          # Run specific
python example.py --all-calc      # Run group
python example.py --all           # Run all
```

## Project Structure

### Package Structure
```
binary_calculator/
├── __init__.py                    # Package exports
├── calculator/
│   ├── __init__.py
│   └── arithmetic_calculator.py  # Pure binary arithmetic
├── comparator/
│   ├── __init__.py
│   └── binary_comparator.py     # Binary comparisons
├── converter/
│   ├── __init__.py
│   └── binary_converter.py      # Binary ↔ Decimal
├── executor/
│   ├── __init__.py
│   └── instruction_executor.py  # Instruction execution
├── instruction/
│   ├── __init__.py
│   ├── binary_instruction.py    # Instruction class
│   ├── binary_number.py         # Number encapsulation
│   └── operation_enum.py        # Operation definitions
└── normalizer/
    ├── __init__.py
    └── binary_normalizer.py     # Binary normalization
```

### Example Structure
```
examples/
├── example.py                    # Central CLI runner
└── basic/
    ├── example_01_binary_number.py         # 9 functions
    ├── example_02_binary_instruction.py    # 6 functions
    ├── example_03_arithmetic_calculator.py # 7 functions
    ├── example_04_binary_comparator.py     # 9 functions
    ├── example_05_binary_converter.py      # 7 functions
    ├── example_06_binary_normalizer.py     # 6 functions
    └── example_07_instruction_executor.py  # 9 functions
```

### Documentation Structure
```
docs/
├── index.md                      # Home page
├── stylesheets/
│   └── extra.css                 # Custom CSS
├── basic/
│   ├── index.md                  # Basic examples overview
│   ├── example_01_binary_number.md
│   ├── example_02_binary_instruction.md
│   ├── example_03_arithmetic_calculator.md
│   ├── example_04_binary_comparator.md
│   ├── example_05_binary_converter.md
│   ├── example_06_binary_normalizer.md
│   └── example_07_instruction_executor.md
└── realistic_scenarios/
    ├── index.md
    ├── scenario_01_memory_address.md
    ├── scenario_02_file_storage.md
    └── scenario_03_network_bandwidth.md
```

## Technical Constraints

### No External Dependencies (Core)
The binary_calculator package itself has ZERO external dependencies. It uses only Python standard library.

### Python Version
Minimum Python 3.7+ (for type hints and dataclass support if added)
Tested with Python 3.13

### Performance Considerations
- String-based binary operations are NOT optimized for speed
- Intended for educational purposes, not production arithmetic
- Large numbers (>1000 bits) may be slow for multiplication/division

## Configuration Files

### mkdocs.yml
```yaml
site_name: Binary Calculator Examples
theme:
  name: material
  palette:
    primary: indigo
    accent: indigo
markdown_extensions:
  - pymdownx.highlight:
      pygments_style: monokai
  - pymdownx.snippets:
      base_path: ['.']
extra_css:
  - stylesheets/extra.css
```

### Import Conventions
```python
# Standard library
import datetime as p_dtt
import pathlib as p_pthl
import typing as p_typ
import uuid as p_uuid
import unittest as p_ut

# Third-party (none for core package)

# Local (relative imports within package)
from ..normalizer import BinaryNormalizer
from ..comparator import BinaryComparator
```

## Deployment

### Documentation Hosting
- MkDocs generates static HTML in `site/` directory
- Can be hosted on GitHub Pages, Netlify, or any static host
- Local serving via `mkdocs serve` on port 8000

### Package Distribution (Planned)
- PyPI package distribution
- setup.py and pyproject.toml
- Wheel and sdist formats

