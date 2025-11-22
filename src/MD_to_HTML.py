import re
from blocktype import block_to_blocktype, BlockType
from text_to_textnodes import text_to_textnodes
from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from leafnode import LeafNode


def md_to_html_nodes(md_block: str, splitter: str = "\n\n") -> list:
    blocks = markdown_to_blocks(md_block, splitter)
    html_nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        if block_type == BlockType.HEADER:
            if splitter == "\n\n":
                html_nodes.extend(md_to_html_nodes(block, splitter="\n"))
            else:
                html_nodes.append(block_to_heading(block))
        elif block_type == BlockType.PARAGRAPH:
            html_nodes.append(block_to_paragraph(block))
        elif block_type == BlockType.LIST_ITEM:
            html_nodes.append(block_to_list_item(block))
        elif block_type == BlockType.ORDERED_LIST_ITEM:
            html_nodes.append(block_to_ordered_list_item(block))
        elif block_type == BlockType.BLOCKQUOTE:
            html_nodes.append(block_to_blockquote(block))
        elif block_type == BlockType.CODE_BLOCK:
            html_nodes.append(block_to_code_block(block))
    if splitter != "\n\n":
        return html_nodes
    return ParentNode(tag="div", children=html_nodes)
            

        
def text_to_children(text: str) -> list:
    if "```" not in text:
        parts = text.split("\n")
    else:
        parts = [text]
    text_nodes = []
    for part in parts:
        if part != parts[-1]:
            text_nodes.extend(text_to_textnodes(part+" "))
        else:
                text_nodes.extend(text_to_textnodes(part))
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(node.to_html_node())
    return html_nodes

def block_to_paragraph(block: str) -> HTMLNode:
    children = text_to_children(block)
    return ParentNode(tag="p", children=children)

def block_to_heading(block: str) -> HTMLNode:
    level = block.count("#", 0, block.find(" "))  # Count # before first space
    text = block[level + 1 :].strip()  # Remove # and space
    children = text_to_children(text)
    return ParentNode(tag=f"h{level}", children=children)

def block_to_list_item(block: str) -> HTMLNode:
    stripped_block = re.sub(r"^- +", "", block, flags=re.MULTILINE) # Remove "- " prefixes
    lines = stripped_block.split("\n")
    children = []
    for line in lines:
        grandchildren = text_to_children(line.strip())
        children.append(ParentNode(tag="li", children=grandchildren))
    return ParentNode(tag="ul", children=children)  

def block_to_ordered_list_item(block: str) -> HTMLNode:
    stripped_block = re.sub(r"^\d+\. ?", "", block, flags=re.MULTILINE) # Remove "1. ", "2. ", etc.
    lines = stripped_block.split("\n")
    children = []
    for line in lines:
        grandchildren = text_to_children(line.strip())
        children.append(ParentNode(tag="li", children=grandchildren))
    return ParentNode(tag="ol", children=children)  


def block_to_blockquote(block: str) -> HTMLNode:
    text = re.sub(r"^> ?", "", block, flags=re.MULTILINE).strip() # Remove "> " prefixes
    children = text_to_children(text)
    quote_paragraph = ParentNode(tag="p", children=children)
    return ParentNode(tag="blockquote", children=[quote_paragraph])

def block_to_code_block(block: str) -> HTMLNode:
    code_text = re.sub(r"^```[\w]*\n?", "", block)  # Remove opening ```
    code_text = re.sub(r"\n?```$", "", code_text)  # Remove closing ```
    code_text = code_text.rstrip() + "\n"  # Ensure trailing newline
    code_leaf = LeafNode(tag="code", value=code_text)
    pre_node = ParentNode(tag="pre", children=[code_leaf])
    return pre_node