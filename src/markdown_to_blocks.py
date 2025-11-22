def markdown_to_blocks(markdown_text: str, splitter: str = "\n\n") -> list:
    raw_blocks = markdown_text.split(splitter)
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped:
            blocks.append(stripped)
    return blocks