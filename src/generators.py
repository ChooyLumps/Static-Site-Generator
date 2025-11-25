import os

from MD_to_HTML import md_to_html_nodes
from extractors import extract_markdown_title


def generate_page(markdown_path: str, template_path: str, output_path: str, basepath: str):
    print(f"Generating page from {markdown_path} using template {template_path} to {output_path}")
    markdown = open(markdown_path).read()
    template = open(template_path).read()
    html_nodes = md_to_html_nodes(markdown)
    content_html = html_nodes.to_html()
    title = extract_markdown_title(markdown)
    final_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    with open(output_path, "w") as f:
        f.write(final_html)

def generate_page_recursive(content_path: str, template_path: str, output_dir: str, basepath: str):
    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file.endswith(".md"):
                relative_path = os.path.relpath(root, content_path)
                output_path = os.path.join(output_dir, relative_path, file.replace(".md", ".html"))
                markdown_path = os.path.join(root, file)
                generate_page(markdown_path, template_path, output_path, basepath)