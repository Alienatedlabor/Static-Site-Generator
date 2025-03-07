import unittest
from textnode import TextNode, TextType

# TODO test nodes should be refactored to use keyword arguments to make the test case more clear- one doesn't have to then look at another file to see what the textnode parameters are or their order.


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text in the node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
