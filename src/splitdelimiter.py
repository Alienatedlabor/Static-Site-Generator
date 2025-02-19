from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_list.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(
                    "invalid markdown syntax, inline elements require opening and closing delimiters"
                )
            else:
                for i in range(len(parts)):
                    if len(parts[i]) > 0:
                        if i % 2 == 0:
                            new_list.append(
                                TextNode(
                                    text=parts[i], text_type=TextType.TEXT, url=None
                                )
                            )
                        else:
                            new_list.append(
                                TextNode(text=parts[i], text_type=text_type, url=None)
                            )
    return new_list
