from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode):
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue
            if node.text.count(delimiter) % 2 == 0:
                parts = node.text.split(delimiter)
                for i, part in enumerate(parts):
                    if i % 2 == 0:
                        if part:
                            new_nodes.append(TextNode(part, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, text_type))
            else:
                raise ValueError("Unmatched delimiter found in text")
        else:
            raise TypeError("All nodes must be instances of TextNode")
    return new_nodes