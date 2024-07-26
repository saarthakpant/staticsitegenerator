import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a","None","None",{"href": "https://www.google.com", 
    "target": "_blank",})
        node2 = HTMLNode("a","None","None")
        self.assertNotEqual(node, node2)
        
    def test_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)

    
    def test_props_to_html(self):
        node = HTMLNode("a","None",None,{"href": "https://www.google.com", 
    "target": "_blank",})
        self.assertEqual(node.props_to_html(),'href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()