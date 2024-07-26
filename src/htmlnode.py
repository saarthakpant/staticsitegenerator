class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        res=""
        for i in self.props:
            res += f'{i}="{self.props[i]}" '
        return(res.strip())
    def __repr__(self) -> str:
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag,value, props=None) -> None:
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        props = self.props_to_html() if self.props else ""
        if props:
            return f"<{self.tag} {props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None) -> None:
        if children is None:
            raise ValueError("Children must be provided for a ParentNode")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag must be provided for a ParentNode")
        if self.children is None:
            raise ValueError("Children must be provided for a ParentNode")
        children_html = ''.join(child.to_html() for child in self.children)
        props = self.props_to_html() if self.props else ""
        if props:
            return f"<{self.tag} {props}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"
        

node = ParentNode("p", [
    LeafNode("b", "Bold text"),
    LeafNode(None, "Normal text"),
    LeafNode("i", "italic text"),
    LeafNode(None, "Normal text"),
])

print(node.to_html())