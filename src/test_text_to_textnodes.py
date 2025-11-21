import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestSplitImage(unittest.TestCase):
    def test_text_to_textnodes_with_image(self):
        text = "Here is an image ![Alt Text](https://example.com/image.png) in the text"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("Alt Text", TextType.IMAGE, url="https://example.com/image.png"),
            TextNode(" in the text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_text_to_textnodes_with_link(self):
        text = "Here is a link [Link Text](https://example.com) in the text"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Here is a link ", TextType.TEXT),
            TextNode("Link Text", TextType.LINK, url="https://example.com"),
            TextNode(" in the text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_text_to_textnodes_with_multiple_images_and_links(self):
        text = "Images: ![img1](https://example.com/img1.png) and [Google](https://google.com)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Images: ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, url="https://example.com/img1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Google", TextType.LINK, url="https://google.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_fontstyle(self):
        text = "This is **bold** and _italic_ text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_code(self):
        text = "Here is some `inline code` in the text."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Here is some ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(" in the text.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_all_features(self):
        text = "This is **bold**, _italic_, an image ![Alt](https://example.com/img.png), a link [Link](https://example.com), and `code`."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", an image ", TextType.TEXT),
            TextNode("Alt", TextType.IMAGE, url="https://example.com/img.png"),
            TextNode(", a link ", TextType.TEXT),
            TextNode("Link", TextType.LINK, url="https://example.com"),
            TextNode(", and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_no_special_syntax(self):
        text = "This is a plain text without any images or links."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a plain text without any images or links.", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        expected_nodes = []
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_only_special_syntax(self):
        text = "![Img](https://example.com/img.png)[Link](https://example.com)**Bold**_Italic_`Code`"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("Img", TextType.IMAGE, url="https://example.com/img.png"),
            TextNode("Link", TextType.LINK, url="https://example.com"),
            TextNode("Bold", TextType.BOLD),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code", TextType.CODE),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_invalid_link_syntax(self):
        text = "Here is a link [Link Text(https://example.com) in the text"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text_to_textnodes_invalid_image_syntax(self):
        text = "Here is an image ![Alt Text(https://example.com/image.png) in the text"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)



