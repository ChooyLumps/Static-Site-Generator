import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", props={"class": "highlight"})
        parent_node = ParentNode("div", [child_node], props={"id": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="container"><span class="highlight">child</span></div>',
        )
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_child_props(self):
        child_node = LeafNode("span", "child", props={"style": "color:red;"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span style="color:red;">child</span></div>',
        )
    
    def test_to_html_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child1</span><span>child2</span></div>",
        )

    def test_to_html_grandchildren_props(self):
        grandchild_node = LeafNode("b", "grandchild", props={"class": "bold"})
        child_node = ParentNode("span", [grandchild_node], props={"style": "font-size:14px;"})
        parent_node = ParentNode("div", [child_node], props={"id": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="container"><span style="font-size:14px;"><b class="bold">grandchild</b></span></div>',
        )
    
    def test_to_html_child_no_tag(self):
        child_node = LeafNode(None, "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div>child</div>",
        )

    def test_to_html_child_no_value(self):
        child_node = LeafNode("span", None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    