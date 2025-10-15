# Binary Calculator Examples

This directory contains comprehensive examples demonstrating the binary calculator system with realistic scenarios.

## Documentation System

This project uses **MkDocs with PyMdown Extensions** to create documentation that **automatically imports code from the executable Python files**. This means:

- ✅ **No code duplication** - Code shown in docs comes directly from working examples
- ✅ **Always in sync** - When code changes, docs update automatically
- ✅ **Single source of truth** - Python files are the only place code exists

## Structure

```
examples/
├── realistic_scenarios/
│   ├── scenario_01_memory_address.py      # Executable example
│   ├── scenario_02_file_storage.py        # Executable example
│   └── scenario_03_network_bandwidth.py   # Executable example
├── README.md                               # This file
│
docs/                                       # Documentation source
├── index.md                                # Home page
└── realistic_scenarios/
    ├── index.md                            # Scenarios overview
    ├── scenario_01_memory_address.md       # Full documentation with imported code
    ├── scenario_02_file_storage.md         # (references scenario_02_*.py)
    └── scenario_03_network_bandwidth.md    # (references scenario_03_*.py)
```

## How It Works

### 1. Mark Code Sections in Python

Use special snippet markers in your Python code:

```python
# --8<-- [start:section_name]
# Your code here
executor = InstructionExecutor()
# --8<-- [end:section_name]
```

### 2. Reference Sections in Markdown

In your `.md` files, import the marked sections:

````markdown
```python title="Setup executor"
--8<-- "examples/realistic_scenarios/scenario_01_memory_address.py:setup"
```
````

The code will be automatically imported from the Python file!

## Running Examples

### Individual Examples

```bash
python examples/realistic_scenarios/scenario_01_memory_address.py
python examples/realistic_scenarios/scenario_02_file_storage.py
python examples/realistic_scenarios/scenario_03_network_bandwidth.py
```

### All Examples

**Windows:**
```cmd
for %f in (examples\realistic_scenarios\scenario_*.py) do python "%f"
```

**Linux/Mac:**
```bash
for file in examples/realistic_scenarios/scenario_*.py; do
    python "$file"
done
```

## Viewing Documentation

### Install Dependencies

```bash
pip install -r requirements-docs.txt
```

### Build Documentation

```bash
mkdocs build
```

This generates static HTML in the `site/` directory.

### Serve Documentation Locally

```bash
mkdocs serve
```

Then open http://127.0.0.1:8000 in your browser.

The server watches for changes and auto-reloads!

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## Creating New Examples

### 1. Create Python File

```python
"""Scenario XX: Description

Real-world context: ...
Operation: ...
Numbers: ...
"""

import sys
import pathlib as p_pthl

# Add parent directory to path
sys.path.insert(0, str(p_pthl.Path(__file__).parent.parent.parent))

from binary_calculator import BinaryNumber, BinaryInstruction, InstructionExecutor


def main() -> None:
    """Description of what this example does."""
    # --8<-- [start:setup]
    executor = InstructionExecutor()
    # --8<-- [end:setup]
    
    # --8<-- [start:operands]
    num1 = BinaryNumber.from_int(decimal_num=1000)
    num2 = BinaryNumber.from_int(decimal_num=500)
    # --8<-- [end:operands]
    
    # --8<-- [start:execute]
    instruction = BinaryInstruction(
        operand_1=num1,
        operand_2=num2,
        operation='+')
    result = executor.calculate(instruction=instruction, print_result=True)
    # --8<-- [end:execute]
    
    print(f"Result: {result.to_int()}")


if __name__ == '__main__':
    main()
```

### 2. Create Documentation File

Create `docs/realistic_scenarios/scenario_XX_name.md`:

````markdown
# Scenario XX: Title

## Context

Explain the real-world scenario...

## Executable Code

```python title="Setup"
--8<-- "examples/realistic_scenarios/scenario_XX_name.py:setup"
```

Explain what this code does...

```python title="Create operands"
--8<-- "examples/realistic_scenarios/scenario_XX_name.py:operands"
```

More explanation...

## Expected Output

```
Show the console output here...
```

## Character-by-Character Processing

Explain the algorithm step-by-step...
````

### 3. Update Navigation

Add your new scenario to `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Realistic Scenarios:
      - Overview: realistic_scenarios/index.md
      - XX - Your Title: realistic_scenarios/scenario_XX_name.md
```

## Benefits of This Approach

1. **Maintainability** - Change code once, docs update everywhere
2. **Accuracy** - Docs always match working code
3. **Testing** - Examples are runnable and can be tested
4. **Readability** - Clean Python code without excessive comments
5. **Documentation** - Comprehensive explanations in Markdown
6. **Version Control** - Easy to see code and doc changes together

## Snippet Marker Syntax

PyMdown Extensions uses special markers:

```python
# --8<-- [start:name]    # Start of snippet
# Code here
# --8<-- [end:name]      # End of snippet
```

**Rules:**
- Marker comments are invisible to Python (just comments)
- Section names must be unique within a file
- Markers can be on same line as code or separate lines
- Nested sections are supported

## Tips

### For Clean Code

- Mark only essential sections
- Use descriptive section names
- Keep print statements separate from logic
- Group related operations

### For Good Documentation

- Show code in logical chunks
- Explain WHY, not just WHAT
- Include expected outputs
- Add complexity analysis
- Provide verification steps

### For Maintainability

- Test examples regularly
- Update docs when code changes
- Use consistent naming
- Document assumptions

## MkDocs Features

### Code Highlighting

```python title="Filename.py" linenums="1"
# Code with syntax highlighting, title, and line numbers
```

### Admonitions

```markdown
!!! info "Information"
    Important information here

!!! tip "Pro Tip"
    Helpful tip here

!!! warning "Warning"
    Warning message here
```

### Tabs

```markdown
=== "Python"
    Python code here

=== "Output"
    Expected output here
```

## Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [Snippets Extension](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)

