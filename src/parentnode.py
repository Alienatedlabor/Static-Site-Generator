from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag cannot be None")
        if self.children is None or not self.children:
            raise ValueError("children cannot be None or empty")
        props_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
        else:
            child_string = ""
            for child in self.children:
                child_string += child.to_html()
            return f"<{self.tag}{props_string}>{child_string}</{self.tag}>"
