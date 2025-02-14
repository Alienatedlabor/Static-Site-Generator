import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
            tag="p",
            children=LeafNode("b", "lorem ipsum"),
            props={"class": "highlight", "id": "test-div"},
        )
        self.assertEqual(
            node.to_html(), '<p class="highlight" id="test-div"><b>lorem ipsum</b></p>'
        )

    def test_ParentNodeMultipleChildren(self):
        node = ParentNode(
            tag="p",
            children=[LeafNode("b", "lorem ipsum"), LeafNode("b", "lorem ipsum")],
            props={"class": "highlight", "id": "test-div"},
        )
        self.assertEqual(
            node.to_html(),
            '<p class="highlight" id="test-div"><b>lorem ipsum</b><b>lorem ipsum</b></p>',
        )

    def test_tag_none(self):
        node = ParentNode(
            tag=None,
            children=LeafNode("b", "lorem ipsum"),
            props={"class": "highlight", "id": "test-div"},
        )
        self.assertRaises(ValueError, node.to_html)

    def test_children_none(self):
        node = ParentNode(
            tag="p",
            children=None,
            props={"class": "highlight", "id": "test-div"},
        )
        self.assertRaises(ValueError, node.to_html)

    def test_empty_children(self):
        node = ParentNode(
            tag="p",
            children=[],
            props={"class": "highlight", "id": "test-div"},
        )
        self.assertRaises(ValueError, node.to_html)

    # because to_html() is recursive nesting should be no issue.
    def test_nested_parents(self):
        inner_node = ParentNode(
            "div", [LeafNode("b", "bold text"), LeafNode("i", "italic text")]
        )

        outer_node = ParentNode(
            "section", [inner_node, LeafNode("p", "paragraph text")]
        )

        self.assertEqual(
            outer_node.to_html(),
            "<section><div><b>bold text</b><i>italic text</i></div><p>paragraph text</p></section>",
        )


if __name__ == "__main__":
    unittest.main()
