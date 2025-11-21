from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter
from split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list:
    Nodes = [TextNode(text, TextType.TEXT)]
    Nodes = split_nodes_image(Nodes)
    Nodes = split_nodes_link(Nodes)
    Nodes = split_nodes_delimiter(Nodes, "**", TextType.BOLD)
    Nodes = split_nodes_delimiter(Nodes, "_", TextType.ITALIC)
    Nodes = split_nodes_delimiter(Nodes, "`", TextType.CODE)
    return Nodes