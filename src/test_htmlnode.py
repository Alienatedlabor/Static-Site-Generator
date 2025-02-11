import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            tag="p", value="lorem ipsum", children=None, props={"class": "text"}
        )
        node2 = HTMLNode(
            tag="p", value="lorem ipsum", children=None, props={"class": "text"}
        )
        self.assertEqual(node, node2)

    def test_different_tag(self):
        node = HTMLNode(
            tag="h1", value="lorem", children=None, props={"class": "heading"}
        )
        node2 = HTMLNode(
            tag="p",
            value="lorem",
            children=None,
            props={"class": "heading"},
        )
        self.assertNotEqual(node, node2)

    def test_different_value(self):
        node = HTMLNode(
            tag="h1", value="lorem", children=None, props={"class": "heading"}
        )
        node2 = HTMLNode(
            tag="h1", value="ipsum", children=None, props={"class": "heading"}
        )
        self.assertNotEqual(node, node2)

    def test_different_children(self):
        # create child nodes to pass to the parent nodes
        child1 = HTMLNode("b", "bold text", None, None)
        child2 = HTMLNode("i", "italic text", None, None)
        # parent nodes
        node = HTMLNode(
            tag="ul", value=None, children=[child1], props={"class": "list"}
        )
        node2 = HTMLNode(
            tag="ul", value=None, children=[child2], props={"class": "list"}
        )
        self.assertNotEqual(node, node2)

    def test_different_props(self):
        node = HTMLNode(
            tag="p", value="lorem", children=None, props={"class": "heading"}
        )
        node2 = HTMLNode(
            tag="p",
            value="lorem",
            children=None,
            props={"class": "paragraph"},
        )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
