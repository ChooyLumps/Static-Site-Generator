import unittest

from extractors import extract_markdown_images, extract_markdown_links

class TestExtractors(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "Images: ![img1](https://example.com/img1.png) and ![img2](https://example.com/img2.png)."
        )
        self.assertListEqual(
            [("img1", "https://example.com/img1.png"), ("img2", "https://example.com/img2.png")],
            matches
        )
    
    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "Links: [Google](https://google.com), [Bing](https://bing.com), and [DuckDuckGo](https://duckduckgo.com)."
        )
        self.assertListEqual(
            [
                ("Google", "https://google.com"),
                ("Bing", "https://bing.com"),
                ("DuckDuckGo", "https://duckduckgo.com")
            ],
            matches
        )

    def test_no_markdown_images(self):
        matches = extract_markdown_images("This text has no images.")
        self.assertListEqual([], matches)

    def test_no_markdown_links(self):
        matches = extract_markdown_links("This text has no links.")
        self.assertListEqual([], matches)

    def test_malformed_markdown_image(self):
        matches = extract_markdown_images("This is a malformed image ![alt text](missing-end")
        self.assertListEqual([], matches)
    
    def test_malformed_markdown_link(self):
        matches = extract_markdown_links("This is a malformed link [link text](missing-end")
        self.assertListEqual([], matches)