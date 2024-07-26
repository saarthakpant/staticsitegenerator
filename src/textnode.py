class TextNode:
    def __init__(self,TEXT, TEXT_TYPE, URL=None) -> None:
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, TextNode):
            return self.text == value.text and self.text_type == value.text_type and self.url == value.url
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def main():
    node = TextNode("This is a text node","bold","https://www.boot.dev")
    print(node)
    
if __name__ == "__main__":
    main()