import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitImage(unittest.TestCase):
    def test_split_image(self):
        old_nodes = [TextNode("Here is an image ![Alt Text](https://example.com/image.png) in the text", TextType.TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        expected_nodes = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("Alt Text", TextType.IMAGE, url="https://example.com/image.png"),
            TextNode(" in the text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_multiple_images(self):
        old_nodes = [TextNode("Images: ![img1](https://example.com/img1.png) and ![img2](https://example.com/img2.png).", TextType.TEXT)]
        new_nodes = split_nodes_image(old_nodes)
        expected_nodes = [
            TextNode("Images: ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, url="https://example.com/img1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, url="https://example.com/img2.png"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_invalid_image_syntax(self):
        old_nodes = [TextNode("Here is an image ![Alt Text(https://example.com/image.png) in the text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_image(old_nodes)

    def test_non_textnode_image(self):
        old_nodes = ["This is a string, not a TextNode"]
        with self.assertRaises(TypeError):
            split_nodes_image(old_nodes)

class TestSplitLink(unittest.TestCase):
    def test_split_link(self):
        old_nodes = [TextNode("Here is a link [Link Text](https://example.com) in the text", TextType.TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("Here is a link ", TextType.TEXT),
            TextNode("Link Text", TextType.LINK, url="https://example.com"),
            TextNode(" in the text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_multiple_links(self):
        old_nodes = [TextNode("Links: [Google](https://google.com), [Bing](https://bing.com).", TextType.TEXT)]
        new_nodes = split_nodes_link(old_nodes)
        expected_nodes = [
            TextNode("Links: ", TextType.TEXT),
            TextNode("Google", TextType.LINK, url="https://google.com"),
            TextNode(", ", TextType.TEXT),
            TextNode("Bing", TextType.LINK, url="https://bing.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_invalid_link_syntax(self):
        old_nodes = [TextNode("Here is a link [Link Text(https://example.com) in the text", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_link(old_nodes)

    def test_non_textnode_link(self):
        old_nodes = ["This is a string, not a TextNode"]
        with self.assertRaises(TypeError):
            split_nodes_link(old_nodes)