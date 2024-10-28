#!/usr/bin/python3
"""
Markdown to HTML!
"""

import sys
import os
import re


def markdown_to_html(f_input, f_output):
    """
    Markdown to HTML.
    """

    if not (os.path.exists(f_input) and os.path.isfile(f_input)):
        print(f"Not found the {f_input} file", file=sys.stderr)
        sys.exit(1)

    with open(f_input, encoding="utf-8") as f:
        l_html = []
        for line in f:

            match = re.match(r"^(#+) (.*)$", line)
            if match:
                l_heading = len(match.group(1))
                t_heading = match.group(2)
                l_html.append
                (f"<h{l_heading}>{t_heading}</h{l_heading}>")
            else:
                l_html.append(line.rstrip())

    with open(f_output, "w", encoding="utf-8") as f:
        f.write("\n".join(l_html))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <f_input> <f_output>",
              file=sys.stderr)
        sys.exit(1)
    f_input = sys.argv[1]
    f_output = sys.argv[2]

    markdown_to_html(f_input, f_output)
