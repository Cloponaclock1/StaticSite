class HTMLNode:
    def __init__(self, tag= None,value = None,children = None,props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        return f'href="{self.props["href"]}" target="{self.props["target"]}"'
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, props)

    def to_html(self):
        if self.tag == None:
            return 