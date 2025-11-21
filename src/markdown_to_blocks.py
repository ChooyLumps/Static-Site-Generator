def markdown_to_blocks(markdown_text: str) -> list:
    raw_blocks = markdown_text.split("\n\n")
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped:
            blocks.append(stripped)
    return blocks