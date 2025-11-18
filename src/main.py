from textnode import TextNode, TextType

def main():
    # Example usage of TextNode
    plain_text = TextNode("Hello, World!")
    bold_text = TextNode("This is bold text", TextType.BOLD)
    link_text = TextNode("Click here", TextType.LINK, url="https://example.com")
    
    print(plain_text)
    print(bold_text)
    print(link_text)

main()