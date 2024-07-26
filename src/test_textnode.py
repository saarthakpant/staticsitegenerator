import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_default_url(self):
        node = TextNode("This is a text node","bold")
        self.assertEqual(node.url, None)
    
    def test_txt_type(self):
        node = TextNode("This is a text node","b")
        self.assertEqual(node.text_type,"b")

if __name__ == "__main__":
    unittest.main()