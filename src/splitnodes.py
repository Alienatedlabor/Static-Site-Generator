from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)  # Extract text from TextNode
        print(matches)


# def split_nodes_link(old_nodes):

old_nodes = TextNode(
    "This is text with an image ![boot dev image](https://www.boot.dev/image) and another image ![another image](https://example.com/image2)",
    TextType.TEXT,
)
split_nodes_image([old_nodes])
