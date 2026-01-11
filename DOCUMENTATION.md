# Documentation System Overview

This document provides a high-level overview of the documentation system for the richardutils repository.

## Table of Contents

1. [Documentation Structure](#documentation-structure)
2. [Getting Started](#getting-started)
3. [Available Guides](#available-guides)
4. [Helper Tools](#helper-tools)
5. [Workflow Integration](#workflow-integration)
6. [Best Practices](#best-practices)

## Documentation Structure

The documentation system consists of:

```
Repository Root
├── docs/                           # Documentation source files
│   ├── _build/                     # Generated HTML (git-ignored)
│   ├── _static/                    # Static assets (CSS, images)
│   ├── notebooks/                  # Jupyter notebook examples
│   ├── conf.py                     # Sphinx configuration
│   ├── index.rst                   # Main documentation page
│   ├── docs_quickstart.md          # Quick reference guide
│   ├── updating_documentation.md   # Complete documentation guide
│   └── *.md                        # Other documentation pages
├── scripts/                        # Documentation helper scripts
│   ├── build_docs.sh              # Build and serve documentation
│   ├── check_docstrings.py        # Check docstring coverage
│   ├── validate_links.py          # Validate documentation links
│   └── README.md                  # Scripts documentation
├── src/richardutils/               # Source code with docstrings
│   └── *.py                       # Python modules
└── README.md                       # Repository README

Documentation is published to: https://richardscottoz.github.io/geoscience-data-utils/
```

## Getting Started

### Quick Setup

1. **Install dependencies:**
   ```bash
   pip install -e .[dev]
   ```

2. **Build documentation:**
   ```bash
   ./scripts/build_docs.sh build
   ```

3. **View documentation:**
   ```bash
   ./scripts/build_docs.sh serve
   # Visit http://localhost:8000
   ```

### 5-Minute Tutorial

**Add a new function with documentation:**

1. Write the function in `src/richardutils/richardutils.py`:
   ```python
   def my_function(data: str) -> str:
       """
       Process data and return result.
       
       Args:
           data: Input data to process.
       
       Returns:
           Processed data.
       
       Examples:
           >>> my_function("test")
           'TEST'
       """
       return data.upper()
   ```

2. Rebuild documentation:
   ```bash
   ./scripts/build_docs.sh rebuild
   ```

3. Check it appears in the API reference at `docs/_build/html/richardutils.html`

## Available Guides

### 1. Quick Start Guide
**File:** `docs/docs_quickstart.md`

A concise reference for common tasks:
- Building and serving documentation
- Adding functions and pages
- Docstring templates
- Troubleshooting tips

**Best for:** Quick lookups and common operations

### 2. Complete Documentation Guide
**File:** `docs/updating_documentation.md`

Comprehensive instructions covering:
- Detailed docstring format guidelines
- Adding Markdown pages and notebooks
- Updating static assets
- Build system configuration
- CI/CD integration
- Troubleshooting

**Best for:** In-depth learning and complex tasks

### 3. Scripts Documentation
**File:** `scripts/README.md`

Documentation for helper scripts:
- Script usage and examples
- Integration into workflows
- CI/CD setup

**Best for:** Understanding and using the helper tools

## Helper Tools

### 1. build_docs.sh

**Purpose:** Build, serve, and check documentation

**Key Commands:**
```bash
./scripts/build_docs.sh build      # Build documentation
./scripts/build_docs.sh rebuild    # Clean build from scratch
./scripts/build_docs.sh serve      # Serve on localhost:8000
./scripts/build_docs.sh check      # Build and check for warnings
./scripts/build_docs.sh open       # Open in browser
```

**When to use:**
- Building documentation locally
- Previewing changes
- Checking for build warnings

### 2. check_docstrings.py

**Purpose:** Validate docstring coverage and format

**Key Commands:**
```bash
python scripts/check_docstrings.py                    # Full report
python scripts/check_docstrings.py --quiet            # Summary only
python scripts/check_docstrings.py --min-coverage 80  # Enforce minimum
```

**When to use:**
- Before committing code changes
- Checking documentation completeness
- In CI/CD pipelines

### 3. validate_links.py

**Purpose:** Check for broken links in documentation

**Key Commands:**
```bash
python scripts/validate_links.py          # Check internal links
python scripts/validate_links.py --quiet  # Summary only
```

**When to use:**
- Before committing documentation changes
- After reorganizing documentation structure
- In CI/CD pipelines

## Workflow Integration

### Development Workflow

**When adding a new feature:**

1. Write code with docstrings
2. Run docstring checker:
   ```bash
   python scripts/check_docstrings.py
   ```
3. Build and preview docs:
   ```bash
   ./scripts/build_docs.sh serve
   ```
4. Add examples/tutorials if needed
5. Validate links:
   ```bash
   python scripts/validate_links.py
   ```
6. Commit changes

**When updating documentation:**

1. Edit documentation files
2. Build and preview:
   ```bash
   ./scripts/build_docs.sh rebuild
   ./scripts/build_docs.sh serve
   ```
3. Validate links:
   ```bash
   python scripts/validate_links.py
   ```
4. Check for warnings:
   ```bash
   ./scripts/build_docs.sh check
   ```
5. Commit changes

### Pre-commit Checklist

Before committing documentation or code changes:

- [ ] Run docstring checker: `python scripts/check_docstrings.py`
- [ ] Build documentation: `./scripts/build_docs.sh rebuild`
- [ ] Validate links: `python scripts/validate_links.py`
- [ ] Check for warnings: `./scripts/build_docs.sh check`
- [ ] Preview in browser: `./scripts/build_docs.sh serve`

### CI/CD Integration

Documentation is automatically built and published via GitHub Actions:

**Workflow:** `.github/workflows/publish-docs.yml`
**Trigger:** New releases or manual workflow dispatch
**Output:** Published to GitHub Pages

**Manual trigger:**
1. Go to repository → Actions tab
2. Select "Publish docs" workflow
3. Click "Run workflow"

## Best Practices

### Docstring Best Practices

1. ✅ **Use Google-style format** consistently
2. ✅ **Include examples** with doctests
3. ✅ **Document edge cases** and exceptions
4. ✅ **Keep docstrings up-to-date** with code changes
5. ✅ **Use type hints** in function signatures
6. ❌ **Avoid redundant information** already in type hints

### Documentation Best Practices

1. ✅ **Build locally** before committing
2. ✅ **Use relative paths** for internal links
3. ✅ **Test code examples** to ensure they work
4. ✅ **Organize content** with clear headings
5. ✅ **Keep pages focused** on single topics
6. ❌ **Don't duplicate content** across multiple pages

### Tool Usage Best Practices

1. ✅ **Run scripts early** in development process
2. ✅ **Fix issues incrementally** as you work
3. ✅ **Use clean builds** when troubleshooting
4. ✅ **Check coverage regularly** to maintain quality
5. ✅ **Validate links** after structural changes

## Technology Stack

- **Sphinx** - Documentation generation
- **myst-nb** - Markdown and Jupyter notebook support
- **Furo** - Modern documentation theme
- **sphinxcontrib-apidoc** - Automatic API documentation
- **GitHub Actions** - CI/CD for publishing
- **GitHub Pages** - Documentation hosting

## Common Issues and Solutions

### Issue: "Module not found" errors

**Solution:** Ensure package is installed:
```bash
pip install -e .[dev]
```

### Issue: Changes not appearing

**Solution:** Clean rebuild:
```bash
./scripts/build_docs.sh rebuild
```

### Issue: Build warnings

**Solution:** Check the build log:
```bash
./scripts/build_docs.sh check
```

### Issue: Broken links

**Solution:** Run link validator:
```bash
python scripts/validate_links.py
```

## Getting Help

- **Quick reference:** See [docs_quickstart.md](docs_quickstart.md)
- **Detailed guide:** See [updating_documentation.md](updating_documentation.md)
- **Scripts help:** See [scripts/README.md](scripts/README.md)
- **Development guide:** See [development.md](development.md)
- **Contributing:** See [CONTRIBUTING.md](../CONTRIBUTING.md)

## Summary

The documentation system provides:

1. **Comprehensive guides** for all documentation tasks
2. **Helper scripts** to automate common operations
3. **CI/CD integration** for automatic publishing
4. **Quality checks** for docstrings and links
5. **Modern tools** (Sphinx, myst-nb, Furo)

Start with the [Quick Start Guide](docs_quickstart.md), use the helper scripts regularly, and refer to the [Complete Guide](updating_documentation.md) for detailed information.
