import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        test = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(test.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_2(self):
        test = LeafNode("a", "Click me!", {"href": "https://github.com"})
        self.assertEqual(test.to_html(), '<a href="https://github.com">Click me!</a>')

    def test_to_html_3(self):
        test = LeafNode("b", None)
        self.assertRaises(ValueError, test.to_html)

    def test_to_html_4(self):
        test = LeafNode(None, "Just me")
        self.assertEqual(test.to_html(), "Just me")


if __name__ == "__main__":
    unittest.main()
