import enum

class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADER = "header"
    LIST_ITEM = "list_item"
    ORDERED_LIST_ITEM = "ordered_list_item"
    BLOCKQUOTE = "blockquote"
    CODE_BLOCK = "code_block"
    

def block_to_blocktype(block: str) -> BlockType:
    block = block.strip()
    if block.startswith("#"):
        return BlockType.HEADER
    elif block.startswith("- "):
        return BlockType.LIST_ITEM
    elif block.startswith("1. "):
        return BlockType.ORDERED_LIST_ITEM
    elif block.startswith("> "):
        return BlockType.BLOCKQUOTE
    elif block.startswith("```"):
        if not block.endswith("```"):
            raise ValueError("Malformed code block")
        return BlockType.CODE_BLOCK
    else:
        return BlockType.PARAGRAPH