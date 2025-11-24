import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\]]+)\]\(([^)]+)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text)
    return matches

def extract_markdown_title(text):
    match = re.match(r"# (.+)", text)
    if match:
        return match.group(1)
    raise Exception("No title found")