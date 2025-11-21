import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        markdown = "This is a single paragraph."
        expected_blocks = ["This is a single paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_multiple_paragraphs(self):
        markdown = "This is the first paragraph.\n\nThis is the second paragraph."
        expected_blocks = [
            "This is the first paragraph.",
            "This is the second paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_leading_trailing_whitespace(self):
        markdown = "   This is a paragraph with leading and trailing whitespace.   \n\n   Another paragraph.   "
        expected_blocks = [
            "This is a paragraph with leading and trailing whitespace.",
            "Another paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_empty_input(self):
        markdown = ""
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_only_whitespace(self):
        markdown = "   \n\n   "
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)