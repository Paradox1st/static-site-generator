class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        htmlProps = ""
        if self.props is not None:
            for key, val in self.props.items():
                htmlProps += f' {key}="{val}"'
        return htmlProps

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")

        if self.tag is None:
            return str(self.value)

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: missing tag")

        if self.children is None:
            raise ValueError("invalid HTML: missing children")

        return f'<{self.tag}{self.props_to_html()}>{"".join([x.to_html() for x in self.children])}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
