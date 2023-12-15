Cookiecutter Python Package
=============================

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
Python package with [pdoc](https://pdoc.dev/) for API docs.

-   GitHub repo:
    <https://github.com/gunnarvoet/cookiecutter-python-package/>
-   Free software: MIT license

# Features

- Testing setup with `pytest`
- [pdoc](https://pdoc.dev/) docs: Documentation ready
- Optionally add custom [pdoc theme](https://github.com/gunnarvoet/pdoc-theme-gv) as git submodule
- GitHub action for auto-generating & deploying docs.

# Quickstart

Install the latest Cookiecutter if you haven\'t installed it yet (this
requires Cookiecutter 1.4.0 or higher):
```sh
pip install pyyaml
pip install -U cookiecutter
```

Generate the Python package structure:
```sh
cookiecutter https://github.com/gunnarvoet/cookiecutter-python-package.git
```
