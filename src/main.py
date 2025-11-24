from generators import generate_page
from copier import purge_and_copy_from_static_to_public

def main():
    purge_and_copy_from_static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")


main()