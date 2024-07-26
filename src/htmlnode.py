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
    
    
node = HTMLNode("a","None","None",{"href": "https://www.google.com", 
    "target": "_blank",})
node.props_to_html()
