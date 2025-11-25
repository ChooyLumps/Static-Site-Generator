import sys

from generators import generate_page_recursive
from copier import purge_and_copy

def main():
    args = sys.argv
    if len(args) > 1:
        basepath = args[1]
    else:
        basepath = "/"
    target = "docs"
    purge_and_copy("static", f"{target}")
    generate_page_recursive("content", "template.html", f"{target}", f"{basepath}")


main()