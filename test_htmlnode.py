import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("text node", "bold")
        node2 = HTMLNode("text node", "italic")

if __name__ == "__main__":
    unittest.main()