
from textnode import TextNode, TextType
from extractors import extract_markdown_images, extract_markdown_links
import re


def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("All nodes must be instances of TextNode")

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        # If there's an opening image marker but no valid image pattern, treat as error
        if "![" in text and not extract_markdown_images(text):
            raise ValueError("Invalid image markdown syntax")

        found = extract_markdown_images(text)
        index = 0
        for img in found:
            alt_text, url = img
            start = text.index(f"![{alt_text}]({url})", index)
            end = start + len(f"![{alt_text}]({url})")
            if start > index:
                new_nodes.append(TextNode(text[index:start], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            index = end
        if index < len(text):
            new_nodes.append(TextNode(text[index:], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("All nodes must be instances of TextNode")

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        # If there's an opening link marker but no valid link pattern, treat as error
        if "[" in text and not extract_markdown_links(text):
            raise ValueError("Invalid link markdown syntax")

        found = extract_markdown_links(text)
        index = 0
        for link in found:
            link_text, url = link
            start = text.index(f"[{link_text}]({url})", index)
            end = start + len(f"[{link_text}]({url})")
            if start > index:
                new_nodes.append(TextNode(text[index:start], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            index = end
        if index < len(text):
            new_nodes.append(TextNode(text[index:], TextType.TEXT))
    return new_nodes