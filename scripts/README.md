# Documentation Helper Scripts

This directory contains helper scripts for maintaining and updating documentation in the richardutils repository.

## Available Scripts

### 1. build_docs.sh

A comprehensive bash script for building and serving documentation.

**Usage:**
```bash
./scripts/build_docs.sh [COMMAND] [OPTIONS]
```

**Commands:**
- `build` - Build the documentation (default)
- `clean` - Clean the build directory
- `rebuild` - Clean and rebuild from scratch
- `serve [PORT]` - Serve documentation locally (default port: 8000)
- `open` - Open documentation in default browser
- `check` - Build and check for warnings/errors
- `help` - Show help message

**Examples:**
```bash
# Build documentation
./scripts/build_docs.sh build

# Clean build from scratch
./scripts/build_docs.sh rebuild

# Serve on localhost:8000
./scripts/build_docs.sh serve

# Serve on custom port
./scripts/build_docs.sh serve 9000

# Build and check for issues
./scripts/build_docs.sh check

# Open docs in browser
./scripts/build_docs.sh open
```

### 2. check_docstrings.py

A Python script to check docstring coverage and validate format.

**Usage:**
```bash
python scripts/check_docstrings.py [SOURCE_DIR] [OPTIONS]
```

**Options:**
- `-q, --quiet` - Only show summary
- `--min-coverage PERCENT` - Require minimum coverage percentage

**Examples:**
```bash
# Check default source directory
python scripts/check_docstrings.py

# Check specific directory
python scripts/check_docstrings.py src/richardutils

# Require 80% coverage
python scripts/check_docstrings.py --min-coverage 80

# Quiet mode (summary only)
python scripts/check_docstrings.py --quiet
```

**Output:**
- Shows module, class, and function docstring coverage
- Lists all missing docstrings with file and line numbers
- Checks for basic docstring format issues

### 3. validate_links.py

A Python script to check for broken links in documentation files.

**Usage:**
```bash
python scripts/validate_links.py [DOCS_DIR] [OPTIONS]
```

**Options:**
- `-e, --external` - Check external URLs (requires network, slower)
- `-q, --quiet` - Only show summary

**Examples:**
```bash
# Check all documentation links
python scripts/validate_links.py

# Check specific docs directory
python scripts/validate_links.py docs

# Check including external URLs
python scripts/validate_links.py --external

# Quiet mode
python scripts/validate_links.py --quiet
```

**Features:**
- Validates links in Markdown (.md) files
- Validates links in reStructuredText (.rst) files
- Checks links in Jupyter notebooks (.ipynb)
- Detects broken internal file links
- Optionally checks external URLs

## Quick Start

To use these scripts:

1. **Install dependencies:**
   ```bash
   pip install -e .[dev]
   ```

2. **Build documentation:**
   ```bash
   ./scripts/build_docs.sh build
   ```

3. **Check docstring coverage:**
   ```bash
   python scripts/check_docstrings.py
   ```

4. **Validate documentation links:**
   ```bash
   python scripts/validate_links.py
   ```

5. **Serve documentation locally:**
   ```bash
   ./scripts/build_docs.sh serve
   ```

## Integration with Workflow

These scripts can be integrated into your development workflow:

### Pre-commit Checks

Before committing documentation changes:
```bash
# Check docstrings
python scripts/check_docstrings.py

# Validate links
python scripts/validate_links.py

# Build and check for warnings
./scripts/build_docs.sh check
```

### CI/CD Integration

Add to your CI pipeline:
```yaml
# Example GitHub Actions step
- name: Check documentation
  run: |
    pip install -e .[dev]
    python scripts/check_docstrings.py --min-coverage 70
    python scripts/validate_links.py
    ./scripts/build_docs.sh check
```

## Troubleshooting

### Scripts not executable

If you get permission errors:
```bash
chmod +x scripts/*.sh
chmod +x scripts/*.py
```

### Dependencies not found

Make sure development dependencies are installed:
```bash
pip install -e .[dev]
```

### Build fails

Try a clean rebuild:
```bash
./scripts/build_docs.sh rebuild
```

## Additional Resources

- See [docs/updating_documentation.md](../docs/updating_documentation.md) for comprehensive documentation guide
- See [docs/development.md](../docs/development.md) for development workflow
- See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines
