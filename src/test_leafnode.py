import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        node = LeafNode(tag="span", value="some text")
        self.assertEqual(node.to_html(), "<span>some text</span>")

    def test_value_None(self):
        node = LeafNode(tag="span", value=None)
        # self.assertEqual(node.to_html(), ValueError())
        self.assertRaises(ValueError, node.to_html)

    def test_value_empty_string(self):
        node = LeafNode(tag="span", value="")
        self.assertRaises(ValueError, node.to_html)

    def test_tag_None(self):
        node = LeafNode(tag=None, value="Hello")
        self.assertEqual(node.to_html(), "Hello")

    def test_with_props(self):
        node = LeafNode(
            tag="a", value="click me", props={"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">click me</a>'
        )


if __name__ == "__main__":
    unittest.main()
