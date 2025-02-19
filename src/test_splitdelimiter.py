import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter


class TestSplitDelimiter(unittest.TestCase):
    def test_no_delimit(self):
        text_node = TextNode(text="Hello World", text_type=TextType.TEXT)
        nodes = [text_node]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        # result should be the same as input since there's no delimiter in the text node. need to compare with nodes because split_nodes_delimiter returns a list.
        self.assertEqual(result, nodes)

    # this test also verifies that my split is handling spaces correctly
    def test_delimit_bold(self):
        text_node = TextNode(text="Hello **Big** World", text_type=TextType.TEXT)
        nodes = [text_node]
        expected = [
            TextNode(text="Hello ", text_type=TextType.TEXT),
            TextNode(text="Big", text_type=TextType.BOLD),
            TextNode(text=" World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(expected, result)

    # checking space-handling with no spaces
    def test_no_spaces(self):
        text_node = TextNode(text="Hello**Big**World", text_type=TextType.TEXT)
        nodes = [text_node]
        expected = [
            TextNode(text="Hello", text_type=TextType.TEXT),
            TextNode(text="Big", text_type=TextType.BOLD),
            TextNode(text="World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(expected, result)

    def test_delimit_code(self):
        text_node = TextNode(text="Hello `Big` World", text_type=TextType.TEXT)
        nodes = [text_node]
        expected = [
            TextNode(text="Hello ", text_type=TextType.TEXT),
            TextNode(text="Big", text_type=TextType.CODE),
            TextNode(text=" World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(expected, result)

    def test_delimit_italic(self):
        text_node = TextNode(text="Hello *Big* World", text_type=TextType.TEXT)
        nodes = [text_node]
        expected = [
            TextNode(text="Hello ", text_type=TextType.TEXT),
            TextNode(text="Big", text_type=TextType.ITALIC),
            TextNode(text=" World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(expected, result)

    def test_delimit_multiple(self):
        text_node = TextNode(
            text="Hello *Big* and *Italic* World", text_type=TextType.TEXT
        )
        nodes = [text_node]
        expected = [
            TextNode(text="Hello ", text_type=TextType.TEXT),
            TextNode(text="Big", text_type=TextType.ITALIC),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="Italic", text_type=TextType.ITALIC),
            TextNode(text=" World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(expected, result)

    def test_delimit_invalid(self):
        text_node = TextNode(text="Hello *Big World", text_type=TextType.TEXT)
        nodes = [text_node]

        self.assertRaises(
            ValueError, split_nodes_delimiter, nodes, "*", TextType.ITALIC
        )

    # checking if first conditional passes- appending any node that isn't type.text directly.
    def test_nontext(self):
        node = TextNode(text="*Hello World*", text_type=TextType.ITALIC)
        nodes = [node]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(nodes, result)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("World", TextType.BOLD),
            TextNode(" this is *italic* text", TextType.TEXT),
        ]
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("World", TextType.BOLD),
            TextNode(" this is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(expected, result)

    def test_empty_delimiters(self):
        node = TextNode(text="Hello **** World", text_type=TextType.TEXT)
        nodes = [node]
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode(" World", TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(expected, result)

    def test_leading_delimiters(self):
        node = TextNode(text="*Hello* World", text_type=TextType.TEXT)
        nodes = [node]
        expected = [
            TextNode(text="Hello", text_type=TextType.ITALIC),
            TextNode(text=" World", text_type=TextType.TEXT),
        ]
        result = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
