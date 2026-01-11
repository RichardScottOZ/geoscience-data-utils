# Documentation Quick Start Guide

This is a quick reference for common documentation tasks. For detailed instructions, see [updating_documentation.md](updating_documentation.md).

## Prerequisites

Install development dependencies:
```bash
pip install -e .[dev]
```

## Common Tasks

### Build Documentation Locally

```bash
cd docs
make html
```

Or use the helper script:
```bash
./scripts/build_docs.sh build
```

### View Documentation

After building, open in browser:
```bash
./scripts/build_docs.sh open
```

Or serve locally:
```bash
./scripts/build_docs.sh serve
# Visit http://localhost:8000
```

### Add a New Function

1. Write the function with docstring:
```python
def my_new_function(param1: str, param2: int = 0) -> bool:
    """
    Brief description of what the function does.
    
    More detailed description if needed.
    
    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 0.
    
    Returns:
        Description of return value.
    
    Examples:
        >>> my_new_function("test", 5)
        True
    """
    # Implementation
    pass
```

2. Rebuild docs to see it in API reference:
```bash
cd docs
make html
```

### Add a New Documentation Page

1. Create new markdown file:
```bash
touch docs/my_new_page.md
```

2. Add content:
```markdown
# My New Page

Content here...
```

3. Add to `docs/index.rst`:
```rst
.. toctree::
    :maxdepth: 2
    :caption: User guide
    
    existing_page
    my_new_page
```

4. Rebuild:
```bash
cd docs
make html
```

### Check Docstring Coverage

```bash
python scripts/check_docstrings.py
```

### Validate Links

```bash
python scripts/validate_links.py
```

### Clean Rebuild

If things aren't working, try a clean rebuild:
```bash
./scripts/build_docs.sh rebuild
```

## Docstring Format Quick Reference

### Function Docstring Template

```python
def function_name(arg1, arg2=default):
    """
    One-line summary.
    
    Longer description.
    
    Args:
        arg1: Description.
        arg2: Description. Defaults to default.
    
    Returns:
        Description of return value.
    
    Raises:
        ErrorType: When this happens.
    
    Examples:
        >>> function_name(1, 2)
        expected_output
    """
```

### Class Docstring Template

```python
class MyClass:
    """
    One-line summary.
    
    Longer description.
    
    Args:
        param1: Description.
        param2: Description.
    
    Attributes:
        attr1: Description.
        attr2: Description.
    
    Examples:
        >>> obj = MyClass(1, 2)
        >>> obj.attr1
        1
    """
```

## Helper Scripts Quick Reference

| Script | Purpose | Example |
|--------|---------|---------|
| `build_docs.sh` | Build and serve docs | `./scripts/build_docs.sh serve` |
| `check_docstrings.py` | Check coverage | `python scripts/check_docstrings.py` |
| `validate_links.py` | Check links | `python scripts/validate_links.py` |

## Troubleshooting

### Build fails
```bash
./scripts/build_docs.sh rebuild
```

### Changes not showing
```bash
cd docs
rm -rf _build
make html
```

### Import errors
```bash
pip install -e .[dev]
```

## More Information

- Full guide: [updating_documentation.md](updating_documentation.md)
- Scripts documentation: [scripts/README.md on GitHub](https://github.com/RichardScottOZ/geoscience-data-utils/blob/main/scripts/README.md)
- Development guide: [development.md](development.md)
