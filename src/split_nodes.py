
from textnode import TextNode, TextType

def split_nodes_image(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
           parts = node.text.split("![")
           for i, part in enumerate(parts):
               if i == 0:
                   new_nodes.append(TextNode(part, TextType.TEXT))
               else:
                   alt_and_url = part.split("](")
                   if len(alt_and_url) != 2 or not alt_and_url[1].endswith(")"):
                       raise ValueError("Invalid image markdown syntax")
                   alt_text = alt_and_url[0]
                   url = alt_and_url[1][:-1]  # Remove the closing parenthesis
                   new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
        else:
            raise TypeError("All nodes must be instances of TextNode")
    return new_nodes

def split_nodes_link(old_nodes: list) -> list:
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
           parts = node.text.split("[")
           for i, part in enumerate(parts):
               if i == 0:
                   new_nodes.append(TextNode(part, TextType.TEXT))
               else:
                   text_and_url = part.split("](")
                   if len(text_and_url) != 2 or not text_and_url[1].endswith(")"):
                       raise ValueError("Invalid link markdown syntax")
                   link_text = text_and_url[0]
                   url = text_and_url[1][:-1]  # Remove the closing parenthesis
                   new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
        else:
            raise TypeError("All nodes must be instances of TextNode")
    return new_nodes