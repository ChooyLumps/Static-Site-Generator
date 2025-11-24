import unittest
from MD_to_HTML import md_to_html_nodes
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType

class TestMDToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text
and an ![image](image_url) here.
This one has a [link](https://example.com) inline.

        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and an <img src=\"image_url\" alt=\"image\" /> here. This one has a <a href=\"https://example.com\">link</a> inline.</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1
Some paragraph text.
## Heading 2
More paragraph text.
### Heading 3
Even more paragraph text.
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p>Some paragraph text.</p><h2>Heading 2</h2><p>More paragraph text.</p><h3>Heading 3</h3><p>Even more paragraph text.</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote.
> It has multiple lines.
> **Bold text** inside blockquote.
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote. It has multiple lines. <b>Bold text</b> inside blockquote.</blockquote></div>",
        )
    
    def test_list_items(self):
        md = """
- First item with **bold** text
- Second item with _italic_ text
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item with <b>bold</b> text</li><li>Second item with <i>italic</i> text</li></ul></div>",
        )

    def test_ordered_list_items(self):
        md = """
1. First item with **bold** text
2. Second item with _italic_ text
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item with <b>bold</b> text</li><li>Second item with <i>italic</i> text</li></ol></div>",
        )

    def test_mixed_content(self):
        md = """
Some **bolded** and _italicised_ words.
This scentence has an ![image](image_url) inline.
This one has a [link](https://example.com) inline.

```
def example():
    return "Hello, World!"
```

- First list item. It has a **bold** word and a [link](https://example.com).
- Second list item. It has an _italic_ word and an ![image](image_url).

> This is a blockquote inside mixed content. This blockquote has **bold** text.
> This is the second line of the blockquote. It has an _italic_ word and an ![image](image_url).
> This third line has a [link](https://example.com).

1. First ordered item. It has a **bold** word and a [link](https://example.com).
2. Second ordered item. It has an _italic_ word and an ![image](image_url).
        """
        node = md_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>Some <b>bolded</b> and <i>italicised</i> words. This scentence has an <img src=\"image_url\" alt=\"image\" /> inline. This one has a <a href=\"https://example.com\">link</a> inline.</p><pre><code>def example():\n    return \"Hello, World!\"\n</code></pre><ul><li>First list item. It has a <b>bold</b> word and a <a href=\"https://example.com\">link</a>.</li><li>Second list item. It has an <i>italic</i> word and an <img src=\"image_url\" alt=\"image\" />.</li></ul><blockquote>This is a blockquote inside mixed content. This blockquote has <b>bold</b> text. This is the second line of the blockquote. It has an <i>italic</i> word and an <img src=\"image_url\" alt=\"image\" />. This third line has a <a href=\"https://example.com\">link</a>.</blockquote><ol><li>First ordered item. It has a <b>bold</b> word and a <a href=\"https://example.com\">link</a>.</li><li>Second ordered item. It has an <i>italic</i> word and an <img src=\"image_url\" alt=\"image\" />.</li></ol></div>",
        )