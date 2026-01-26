# Installation

At the command line:

    pip install richardutils

Or, if you use Conda environments:

    conda create -n richardutils python=3.12
    conda activate richardutils
    pip install richardutils

For developers, there are also options for installing `tests`, `docs` and `dev` dependencies, e.g. `pip install richardutils[dev]` to install all testing and documentation packages.

For development, you can also clone the repository, then change to its directory, then do the following for an "editable" install that changes while you develop:

    pip install -e .

If you want to help develop `richardutils`, please read [Development](development.md).
