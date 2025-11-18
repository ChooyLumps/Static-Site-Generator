import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", {"class": "container"})
        node2 = HTMLNode("div", {"class": "container"})
        self.assertEqual(node, node2)
    
    def test_neq_different_tag(self):
        node = HTMLNode("div", {"class": "container"})
        node2 = HTMLNode("span", {"class": "container"})
        self.assertNotEqual(node, node2)

    def test_neq_different_attributes(self):
        node = HTMLNode("div", {"class": "container"})
        node2 = HTMLNode("div", {"id": "main"})
        self.assertNotEqual(node, node2)

    def test_neq_different_children(self):
        node = HTMLNode("div", children=[HTMLNode("p")])
        node2 = HTMLNode("div", children=[HTMLNode("span")])
        self.assertNotEqual(node, node2)

    def test_neq_different_props(self):
        node = HTMLNode("div", props={"class": "container"})
        node2 = HTMLNode("div", props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", props={"href": "https://example.com", "target": "_blank"})
        expected_html = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)
    
