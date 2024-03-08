import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("text node", "bold")
        node2 = TextNode("text node", "italic")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()