
from textnode import TextNode, TextType
import re

_IMG_RE = re.compile(r"!\[([^\]]*?)\]\((.*?)\)")
_LINK_RE = re.compile(r"\[([^\]]*?)\]\((.*?)\)")

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
        if "![" in text and not _IMG_RE.search(text):
            raise ValueError("Invalid image markdown syntax")

        idx = 0
        for m in _IMG_RE.finditer(text):
            start, end = m.span()
            if start > idx:
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))
            alt_text = m.group(1)
            url = m.group(2)
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
            idx = end

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

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
        if "[" in text and not _LINK_RE.search(text):
            raise ValueError("Invalid link markdown syntax")

        idx = 0
        for m in _LINK_RE.finditer(text):
            start, end = m.span()
            if start > idx:
                new_nodes.append(TextNode(text[idx:start], TextType.TEXT))
            link_text = m.group(1)
            url = m.group(2)
            new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
            idx = end

        if idx < len(text):
            new_nodes.append(TextNode(text[idx:], TextType.TEXT))

    return new_nodes