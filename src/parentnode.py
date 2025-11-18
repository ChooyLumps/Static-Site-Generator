from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if self.children is None:
            raise ValueError("ParentNode must have children to convert to HTML")
        children_html = ''.join(child.to_html() for child in self.children)
        if self.props is None:
            return f"<{self.tag}>{children_html}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"