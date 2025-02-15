import unittest
from textnode import TextNode, TextType
from texttohtml import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode(text="hello, world", text_type=TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(text_node.text, html_node.value)
        self.assertEqual(html_node.tag, None)

    def test_bold(self):
        text_node = TextNode(text="hello, world", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(text_node.text, html_node.value)
        self.assertEqual(html_node.tag, "b")

    def test_italic(self):
        text_node = TextNode(text="hello, world", text_type=TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(text_node.text, html_node.value)
        self.assertEqual(html_node.tag, "i")

    def test_code(self):
        text_node = TextNode(text="print(hello, world)", text_type=TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(text_node.text, html_node.value)
        self.assertEqual(html_node.tag, "code")

    def test_link(self):
        text_node = TextNode(
            text="click me", text_type=TextType.LINK, url="https://www.boot.dev"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(text_node.text, html_node.value)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        text_node = TextNode(
            text="description", text_type=TextType.IMAGE, url="https://www.boot.dev"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props, {"src": "https://www.boot.dev", "alt": "description"}
        )


if __name__ == "__main__":
    unittest.main()
