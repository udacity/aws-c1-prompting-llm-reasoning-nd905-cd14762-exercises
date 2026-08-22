#!/usr/bin/env python3
"""
Generate template.yaml by inlining Lambda source files into template_base.yaml.

Usage:
    python generate_template.py

Edit template_base.yaml and the lambda/ Python files, then run this script
to regenerate template.yaml. Do not edit template.yaml directly.

Note on $ signs
---------------
template_base.yaml uses Python string.Template syntax: $var or ${var} marks a
placeholder. This script uses safe_substitute(), so any ${...} patterns that
are not recognised placeholder names (e.g. CloudFormation !Sub variables like
${AWS::Region}) are left unchanged in the output.

If you ever need a literal $ followed by a recognised placeholder name, write
$$ in the base template (e.g. $$get_cuisines produces $get_cuisines).
"""
from pathlib import Path
from string import Template

SCRIPT_DIR = Path(__file__).parent
BASE_TEMPLATE = SCRIPT_DIR / "template_base.yaml"
OUTPUT_TEMPLATE = SCRIPT_DIR / "template.yaml"

GENERATED_HEADER = """\
# Auto-generated from template_base.yaml — do not edit directly.
# To regenerate: edit template_base.yaml and the lambda/ files, then run
#   python generate_template.py

"""


def indented(path: Path, spaces: int = 10) -> str:
    """Read a Python file and indent every non-blank line by `spaces` spaces."""
    pad = ' ' * spaces
    lines = path.read_text().rstrip('\n').splitlines()
    return '\n'.join(pad + line if line.strip() else '' for line in lines)


def generate() -> None:
    result = Template(BASE_TEMPLATE.read_text()).safe_substitute(
        get_cuisines=indented(SCRIPT_DIR / 'lambda/get_cuisines/lambda_function.py'),
        search_restaurants=indented(SCRIPT_DIR / 'lambda/search_restaurants/lambda_function.py'),
        get_availability=indented(SCRIPT_DIR / 'lambda/get_availability/lambda_function.py'),
        get_description=indented(SCRIPT_DIR / 'lambda/get_description/lambda_function.py'),
    )
    OUTPUT_TEMPLATE.write_text(GENERATED_HEADER + result)
    print(f"Generated {OUTPUT_TEMPLATE.name}")


if __name__ == '__main__':
    generate()
