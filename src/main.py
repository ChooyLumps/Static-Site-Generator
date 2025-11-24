import sys

from generators import generate_page_recursive
from copier import purge_and_copy

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    target = "docs"
    purge_and_copy("static", f"{target}")
    generate_page_recursive("content", "template.html", f"{target}", basepath)


main()