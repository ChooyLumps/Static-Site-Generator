import unittest

from blocktype import BlockType, block_to_blocktype

class TestBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_header_block(self):
        block = "# This is a header"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADER)

    def test_list_item_block(self):
        block = "- This is a list item"
        self.assertEqual(block_to_blocktype(block), BlockType.LIST_ITEM)

    def test_ordered_list_item_block(self):
        block = "1. This is an ordered list item"
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED_LIST_ITEM)

    def test_blockquote_block(self):
        block = "<blockquote>This is a blockquote</blockquote>"
        self.assertEqual(block_to_blocktype(block), BlockType.BLOCKQUOTE)

    def test_code_block(self):
        block = "<code>print('Hello, world!')</code>"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE_BLOCK)

    def test_malformed_blockquote(self):
        block = "<blockquote>This is a malformed blockquote"
        with self.assertRaises(ValueError):
            block_to_blocktype(block)

    def test_malformed_code_block(self):
        block = "<code>print('Hello, world!')"
        with self.assertRaises(ValueError):
            block_to_blocktype(block)