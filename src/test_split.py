import unittest

from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_split_bold(self):
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_italic(self):
        old_nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    
    def test_split_code(self):
        old_nodes = [TextNode("Here is `code` snippet", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" snippet", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_unmatched_delimiter(self):
        old_nodes = [TextNode("This is **bold text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    def test_non_textnode(self):
        old_nodes = ["This is a string, not a TextNode"]
        with self.assertRaises(TypeError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)