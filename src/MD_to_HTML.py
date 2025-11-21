import re
from blocktype import block_to_blocktype, BlockType
from split_nodes import split_nodes
from text_to_textnodes import text_to_textnodes
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from html_nodes import HTMLNode, HTMLType
from markdown_to_blocks import markdown_to_blocks

def md_block_to_html_nodes(md_block: str) -> list:
    blocks = markdown_to_blocks(md_block)
    html_nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.HEADING:
            html_nodes.append(block_to_heading(block))
        elif block_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            html_nodes.append(ParentNode(tag="p", children=children))
        elif block_type == BlockType.LIST_ITEM:
            html_nodes.append(block_to_list_item(block))
        elif block_type == BlockType.ORDERED_LIST_ITEM:
            html_nodes.append(block_to_ordered_list_item(block))
        elif block_type == BlockType.BLOCKQUOTE:
            html_nodes.append(block_to_blockquote(block))
        elif block_type == BlockType.CODE_BLOCK:
            html_nodes.append(block_to_code_block(block))
    return ParentNode(tag="div", children=html_nodes)
            

        
def text_to_children(text: str) -> list:
    parts = text.split("\n")
    text_nodes = []
    for part in parts:
        text_nodes.extend(text_to_textnodes(part))
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(node.to_html_node())
    return html_nodes

def block_to_heading(block: str) -> HTMLNode:
    level = block.count("#", 0, block.find(" "))  # Count leading #
    text = block[level + 1 :].strip()
    children = text_to_children(text)
    return ParentNode(tag=f"h{level}", children=children)

def block_to_list_item(block: str) -> HTMLNode:
    text = block[2:].strip()  # Remove "- " prefix
    grand_children = text_to_children(text)
    children = []
    for grand_child in grand_children:
        children.append(ParentNode(tag="li", children=[grand_child]))
    return ParentNode(tag="ul", children=children)  

def block_to_ordered_list_item(block: str) -> HTMLNode:
    new_text = re.sub(r"\d.", "", block) # Replace "1. ", "2. ", etc. with ""
    grand_children = text_to_children(new_text.strip())
    children = []
    for grand_child in grand_children:
        children.append(ParentNode(tag="li", children=[grand_child]))
    return ParentNode(tag="ol", children=children)

def block_to_blockquote(block: str) -> HTMLNode:
    text = block[2:].strip()  # Remove "> " prefix
    children = text_to_children(text)
    return ParentNode(tag="blockquote", children=children)

def block_to_code_block(block: str) -> HTMLNode:
    code_text = "\n".join(block.split("\n")[1:-1])  # Remove ``` markers
    return LeafNode(tag="code", value=code_text)