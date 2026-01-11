
# richardutils

## Overview
A few geoscience analysis helper functions I use ad hoc for:

- Creating geodataframes from csv
- Reading a directory of rasters into rioxarray or vector data into geodataframes
- Sampling rioxarrays at point locations
- Clipping rioxarrays
- Plotting rioxarrays
- Extracting a band from a rioxarray
- Zonal statistics
- Making xarrays in 3D

Mostly for notebook style work

## Documentation

- Simple in progress https://richardscottoz.github.io/geoscience-data-utils/


## Installing and building

To install the package, before or after changing its name, you can use `pip install .` or `pip install -e .` for an æeditableæ install (useful during development).

To build an `sdist` and `wheel` for `pip` to install (it can use either; wheels are the 'modern' way), you can do `python -m build`. 

Note: building the project makes a file called `src/richardutils/_version.py` which must not be checked into version control, hence it is included in `.gitignore`.


## Command line interface

As well as the Python package with its API, the package also implements a command line interface, or CLI, called `richardcli` using Python's `script` entry point. So after installing with `pip`, there is a command-line tool you can invoke with `richardcli --help`. The CLI is implemented with a popular tool called [`click`](https://click.palletsprojects.com/en/latest/).

You can also invoke the CLI by running the module with `python -m richardutils`, which relies on `__main__.py`. So many ways to run Python code!


## Tests

These are implemented using `pytest` for both the module and the CLI. The installation also includes `coverage` for checking test coverage (how much of your code is run under testing). The `pytest` options are in `pyproject.toml`. Run tests with:

    pytest

You can get an HTML report from Coverage with `coverage html`.


## Documentation

The docs are written in Markdown, with the top-level index written in RST. The documentation pages are built by [Sphinx](https://www.sphinx-doc.org/en/master/) with the following commands:

    cd docs
    make html

The [`myst-nb` plugin](https://myst-nb.readthedocs.io/en/latest/) for Sphinx should allow you to mix RST, Markdown, and Jupyter Notebooks in your documentation.

This package uses [the Furo theme](https://pradyunsg.me/furo/), but it's easy enough to change options like this in `docs/conf.py`.

The documentation builds as [a GitHub Action](https://github.com/scienxlab/python-package-template/blob/main/.github/workflows/publish-docs.yml) and [is deployed here](https://richardscottoz.github.io/geoscience-data-utils/).

### Updating Documentation

For detailed instructions on updating and maintaining code documentation, see the comprehensive guides:

**[📚 Documentation Quick Start Guide](docs/docs_quickstart.md)** - Quick reference for common tasks

**[📖 Complete Documentation Guide](docs/updating_documentation.md)** - Detailed instructions

These guides cover:
- How to write and format docstrings
- Adding new documentation pages
- Creating tutorial notebooks
- Building and previewing documentation locally
- Common documentation tasks and troubleshooting

### Helper Scripts

The `scripts/` directory contains useful helper scripts for documentation maintenance:

- **`build_docs.sh`** - Build, serve, and check documentation
- **`check_docstrings.py`** - Validate docstring coverage
- **`validate_links.py`** - Check for broken links

Quick examples:
```bash
# Build and serve documentation locally
./scripts/build_docs.sh serve

# Check docstring coverage
python scripts/check_docstrings.py

# Validate documentation links
python scripts/validate_links.py
```

See [scripts/README.md](scripts/README.md) for detailed usage information.

## Continuous integration

The package uses GitHub Actions for the automation of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration). There are 2 so-called workflows:

- `build_test.yml` &mdash; build and test the distribution using `pytest`.
- `publish-docs.yml` &mdash; build and publish the documentation to GitHub pages. Note that this requires you to enable GitHub package on your repo.


