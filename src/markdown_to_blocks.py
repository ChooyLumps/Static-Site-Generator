def markdown_to_blocks(markdown_text: str) -> list:
    blocks = markdown_text.split("\n")
    for block in blocks:
        block = block.strip()
        if block == "":
            blocks.remove(block)
    return blocks