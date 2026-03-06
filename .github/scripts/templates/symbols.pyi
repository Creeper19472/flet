"""
Flet Material Symbols Icons Stub

To generate/update this file run from the root of the repository:

```
uv run .github/scripts/generate_icons.py
```
"""

from flet.controls.icon_data import IconData

__all__ = ["Symbols"]

class Symbols:
    {% for name, code in icons -%}
    {{ name.upper() }}: IconData
    {% endfor -%}
