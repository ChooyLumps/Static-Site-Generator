import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        markdown = "This is a single paragraph."
        expected = ["This is a single paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_multiple_paragraphs(self):
        markdown = "This is the first paragraph.\n\nThis is the second paragraph."
        expected = ["This is the first paragraph.", "This is the second paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_headings_and_paragraphs(self):
        markdown = "# Heading 1\nThis is a paragraph under heading 1.\n\n## Heading 2\nThis is a paragraph under heading 2."
        expected = [
            "# Heading 1",
            "This is a paragraph under heading 1.",
            "## Heading 2",
            "This is a paragraph under heading 2."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_list_items(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        expected = ["- Item 1", "- Item 2", "- Item 3"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_mixed_content(self):
        markdown = "# Heading\nThis is a paragraph.\n\n- List item 1\n- List item 2\n\nAnother paragraph."
        expected = [
            "# Heading",
            "This is a paragraph.",
            "- List item 1",
            "- List item 2",
            "Another paragraph."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)