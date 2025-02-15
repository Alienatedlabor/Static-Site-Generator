from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        else:
            # I could compare these directly here easily like:
            # return (self.text == other.text and
            # self.text_type == other.text_type and
            # self.url == other.url)

            # more elegant and concise but less transparent using __dict__ "All objects in Python have an attribute __dict__, which is a dictionary object containing all attributes defined for that object itself."
            return self.__dict__ == other.__dict__

    # __repr__ is python's way of saying "if someone prints this object, here's how it should look. when you print a list,tuple, or dictionary in Python, you see their __repr__ representation"
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
