# Updating Code Documentation

This guide provides detailed instructions for updating and maintaining the code-based documentation in this repository.

## Overview

This project uses **Sphinx** with several extensions to automatically generate documentation from Python code docstrings and Markdown files. The documentation system includes:

- **Sphinx**: The main documentation generation tool
- **sphinxcontrib-apidoc**: Automatically generates API documentation from Python docstrings
- **myst-nb**: Allows mixing RST, Markdown, and Jupyter Notebooks
- **Furo theme**: Modern, clean documentation theme
- **napoleon**: Support for Google and NumPy style docstrings

## Documentation Structure

```
docs/
├── _build/           # Generated HTML output (git-ignored)
├── _static/          # Static files (CSS, images, logos)
├── _templates/       # Custom Sphinx templates (if any)
├── notebooks/        # Jupyter notebooks for examples
├── conf.py           # Sphinx configuration
├── Makefile          # Build commands
├── make.bat          # Windows build commands
├── index.rst         # Main documentation page (RST format)
├── richardutils.rst  # API documentation page (auto-generated)
└── *.md              # Various markdown documentation files
```

## Types of Documentation Updates

### 1. Updating Function/Class Docstrings

When you add or modify Python code, update the docstrings to maintain accurate API documentation.

#### Docstring Format

This project uses **Google-style docstrings**. Here's the format:

```python
def my_function(arg1: str, arg2: int = 0) -> bool:
    """
    Brief one-line description of the function.
    
    More detailed description can go here. Explain what the function
    does, any important behavior, or edge cases.
    
    Args:
        arg1: Description of the first argument.
        arg2: Description of the second argument. Defaults to 0.
    
    Returns:
        Description of what the function returns.
    
    Raises:
        ValueError: When an invalid value is provided.
        TypeError: When the wrong type is passed.
    
    Examples:
        >>> my_function("test", 5)
        True
        >>> my_function("example")
        False
    
    Note:
        Any additional notes or warnings about the function.
    """
    # Implementation here
    pass
```

#### Key Guidelines

1. **First line**: Brief one-line summary (imperative mood: "Calculate X", not "Calculates X")
2. **Args section**: Describe each parameter with its purpose
3. **Returns section**: Describe what the function returns
4. **Examples section**: Provide working doctests that can be run
5. **Type hints**: Use in function signatures, not in docstrings

### 2. Adding New Markdown Documentation Pages

To add a new documentation page:

1. Create a new `.md` file in the `docs/` directory:
   ```bash
   touch docs/my_new_page.md
   ```

2. Add content using Markdown format:
   ```markdown
   # My New Page Title
   
   Content here with standard Markdown formatting.
   
   ## Subsection
   
   More content...
   ```

3. Add the page to `docs/index.rst` in the appropriate `toctree`:
   ```rst
   .. toctree::
       :maxdepth: 2
       :caption: User guide
       
       installation
       my_new_page
       notebooks/Basic_usage.ipynb
   ```

### 3. Adding Jupyter Notebook Examples

To add example notebooks:

1. Create a new notebook in `docs/notebooks/`:
   ```bash
   jupyter notebook docs/notebooks/my_example.ipynb
   ```

2. Write your example with:
   - Clear markdown cells explaining each step
   - Code cells with working examples
   - Output cells showing results

3. Add to `docs/index.rst`:
   ```rst
   .. toctree::
       :caption: User guide
       
       notebooks/my_example.ipynb
   ```

### 4. Updating API Reference

The API documentation in `docs/richardutils.rst` is automatically updated by the `sphinxcontrib-apidoc` extension based on the module structure. 

If you add a new module:

1. The file will be auto-generated on build
2. Ensure your module has proper docstrings
3. If needed, manually edit `docs/richardutils.rst` to customize the structure

### 5. Updating Static Assets

To update logos, CSS, or other static files:

1. Add/update files in `docs/_static/`
2. Reference them in `docs/conf.py`:
   ```python
   html_logo = '_static/my_logo.png'
   html_favicon = '_static/favicon.ico'
   html_css_files = ['custom.css']
   ```

## Building Documentation Locally

### Prerequisites

Install the development dependencies:

```bash
pip install -e .[dev]
```

This installs:
- sphinx
- sphinxcontrib-apidoc
- furo (theme)
- myst_nb (for notebooks and markdown)
- And other required packages

### Build Commands

**Basic build:**
```bash
cd docs
make html
```

**Clean build** (recommended when you've made structural changes):
```bash
cd docs
rm -rf _build
make html
```

**View the documentation:**
```bash
# Open in browser (Linux/macOS)
xdg-open docs/_build/html/index.html  # Linux
open docs/_build/html/index.html      # macOS

# Or use Python's http server
cd docs/_build/html
python -m http.server 8000
# Visit http://localhost:8000 in your browser
```

### Build Options

The `Makefile` uses these options:
- `-E`: Rebuild from scratch (ignore cached environment)
- `-b html`: Build HTML output

To see all available options:
```bash
cd docs
make help
```

## Common Documentation Tasks

### Task 1: Document a New Function

1. Write the function with a complete docstring:
   ```python
   def process_raster(input_path: str, clip_bounds: tuple = None) -> xr.DataArray:
       """
       Process a raster file and optionally clip to bounds.
       
       Args:
           input_path: Path to the input raster file.
           clip_bounds: Optional bounding box as (minx, miny, maxx, maxy).
       
       Returns:
           The processed DataArray with CRS information.
       
       Examples:
           >>> da = process_raster("data/dem.tif")
           >>> da.shape
           (100, 100)
       """
       # Implementation
   ```

2. Build docs:
   ```bash
   cd docs
   make html
   ```

3. Verify in browser that your function appears in the API reference

### Task 2: Update Existing Documentation Page

1. Edit the markdown file:
   ```bash
   nano docs/installation.md
   ```

2. Make your changes

3. Rebuild:
   ```bash
   cd docs
   make html
   ```

4. Check the output in your browser

### Task 3: Add a New Tutorial Notebook

1. Create notebook:
   ```bash
   jupyter notebook docs/notebooks/
   ```

2. Create `new_tutorial.ipynb` with examples

3. Add to `docs/index.rst`:
   ```rst
   .. toctree::
       :caption: Tutorials
       
       notebooks/Basic_usage.ipynb
       notebooks/new_tutorial.ipynb
   ```

4. Build and verify:
   ```bash
   cd docs
   make html
   ```

## Continuous Integration

Documentation is automatically built and published using GitHub Actions.

### Automatic Builds

The `.github/workflows/publish-docs.yml` workflow:
- Triggers on new releases
- Can be manually triggered from GitHub UI
- Builds documentation with `make html`
- Publishes to GitHub Pages on the `gh-pages` branch

### Manual Publishing

To manually trigger documentation publishing:

1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Publish docs" workflow
4. Click "Run workflow"
5. Select branch and confirm

The documentation will be published to: `https://richardscottoz.github.io/geoscience-data-utils/`

## Troubleshooting

### Issue: Build fails with "module not found"

**Solution**: Make sure package is installed:
```bash
pip install -e .[dev]
```

### Issue: Changes not showing up

**Solution**: Do a clean rebuild:
```bash
cd docs
rm -rf _build
make html
```

### Issue: Docstring not appearing in API docs

**Checklist**:
1. Is the function/class public (no leading underscore)?
2. Does it have a proper docstring?
3. Is the module imported in `__init__.py`?
4. Did you do a clean rebuild?

### Issue: Links broken in documentation

**Solution**: Check the file paths are correct and files exist. Use relative paths from the `docs/` directory.

### Issue: Notebook not rendering

**Checklist**:
1. Is `myst_nb` installed?
2. Is the notebook in `docs/notebooks/`?
3. Is it added to a `toctree` in `index.rst`?
4. Does the notebook run without errors?

### Issue: Logo or static files not showing

**Solution**: 
1. Ensure files are in `docs/_static/`
2. Check `conf.py` references are correct
3. Do a clean rebuild

## Best Practices

### Docstring Best Practices

1. **Be concise but complete**: Cover what matters, avoid redundancy
2. **Use examples**: Add doctests that actually run
3. **Document edge cases**: Note any special behavior
4. **Keep updated**: Update docstrings when code changes
5. **Use type hints**: In function signatures, not docstrings
6. **Follow conventions**: Use Google-style format consistently

### Markdown Best Practices

1. **Use clear headings**: Organize content hierarchically
2. **Add code examples**: Show how to use features
3. **Link related pages**: Help users navigate
4. **Keep it maintainable**: Don't duplicate content unnecessarily
5. **Test code examples**: Ensure they work

### Notebook Best Practices

1. **Clear narrative**: Explain what you're doing and why
2. **Run all cells**: Before committing, restart kernel and run all
3. **Keep output**: Include cell outputs so they show in docs
4. **Use descriptive titles**: Help users find what they need
5. **Test with clean environment**: Ensure notebook runs standalone

## Configuration Reference

### docs/conf.py

Key configuration sections:

```python
# Project information
project = 'richardutils'
copyright = 'The richardutils authors'

# Extensions
extensions = [
    'sphinx.ext.githubpages',      # GitHub Pages support
    'sphinxcontrib.apidoc',        # Auto API docs
    'sphinx.ext.napoleon',         # Google/NumPy docstrings
    'myst_nb',                     # Markdown/notebooks
    'sphinx.ext.coverage',         # Coverage reports
]

# Apidoc configuration
apidoc_module_dir = '../src/richardutils'  # Source code location
apidoc_output_dir = './'                   # Output location
apidoc_separate_modules = False            # Single page for all modules

# HTML theme
html_theme = 'furo'
html_logo = '_static/richardutils_logo.png'
html_favicon = '_static/favicon.ico'
```

### Customizing the Theme

To customize colors, fonts, or layout, edit `docs/_static/custom.css`:

```css
/* Example customizations */
.sidebar {
    background-color: #f0f0f0;
}

code {
    background-color: #f5f5f5;
    padding: 2px 4px;
}
```

## Helper Scripts

This repository includes helper scripts to make documentation maintenance easier. See the sections below and check the `scripts/` directory for:

- `build_docs.sh`: Build documentation with various options
- `check_docstrings.py`: Validate docstring coverage and format
- `validate_links.py`: Check for broken links in documentation

Use `--help` with any script for detailed usage information.

## Contributing Documentation

When contributing documentation:

1. **Follow existing style**: Match the tone and format of existing docs
2. **Test your changes**: Build locally before submitting PR
3. **Update relevant sections**: If you add a feature, document it
4. **Check links**: Ensure all links work
5. **Review output**: Check the built HTML looks correct

See the [CONTRIBUTING.md](https://github.com/RichardScottOZ/geoscience-data-utils/blob/main/CONTRIBUTING.md) file for more details on the contribution process.

## Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Parser Guide](https://myst-parser.readthedocs.io/)
- [Google Style Python Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Furo Theme Documentation](https://pradyunsg.me/furo/)
