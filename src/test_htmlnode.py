import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode


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
        

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        # Test that LeafNode is initialized correctly
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.tag, "b")
        self.assertEqual(node.value, "Bold text")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html(self):
        # Test that to_html method returns correct HTML
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_to_html_no_tag(self):
        # Test that to_html method returns correct HTML without a tag
        node = LeafNode(None, "Normal text")
        self.assertEqual(node.to_html(), "Normal text")

    def test_to_html_with_props(self):
        # Test that to_html method returns correct HTML with properties
        node = LeafNode("b", "Bold text", {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), '<b class="my-class" id="my-id">Bold text</b>')

    def test_to_html_no_value(self):
        # Test that ValueError is raised if no value is provided
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_init(self):
        # Test that ParentNode is initialized correctly
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.tag, "p")
        self.assertIsNone(node.value)
        self.assertEqual(len(node.children), 4)
        self.assertIsNone(node.props)

    def test_to_html(self):
        # Test that to_html method returns correct HTML
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_props(self):
        # Test that to_html method returns correct HTML with properties
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"class": "my-class", "id": "my-id"})
        self.assertEqual(node.to_html(), '<p class="my-class" id="my-id"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_no_tag(self):
        # Test that to_html method raises ValueError if no tag is provided
        with self.assertRaises(ValueError):
            node = ParentNode(None, [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
            node.to_html()

    def test_to_html_no_children(self):
        # Test that to_html method raises ValueError if no children are provided
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            node.to_html()
            
if __name__ == "__main__":
    unittest.main()