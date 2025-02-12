from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # children=[] makes it explicit that LeafNodes should have no children- otherwise it could be set since LeafNode does still inherit it from the parent.
        super().__init__(tag, value, props=props, children=[])

    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError()
        props_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
