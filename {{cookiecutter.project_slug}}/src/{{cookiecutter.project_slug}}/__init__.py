"""
# Overview

Say something here about the project.

{% if cookiecutter.custom_pdoc_theme == 'y' -%}
# Markdown Syntax
## Figures
Narrow image:
```markdown
![nimage](path/to/figure)
```
Medium sized image:
```markdown
![image](path/to/figure)
```
Wide image:
```markdown
![wimage](path/to/figure)
```
{% endif %}

# License

.. include:: ../../LICENSE
"""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

__all__ = ["io"]
from . import io
