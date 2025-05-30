import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        test = HTMLNode(
            "a", "link text", None, {"href": "https://github.com", "target": "_blank"}
        )
        self.assertEqual(
            test.props_to_html(), ' href="https://github.com" target="_blank"'
        )

    def test_props_to_html_2(self):
        test = HTMLNode("i", "italic text")
        self.assertEqual(test.props_to_html(), "")

    def test_repr_1(self):
        test = HTMLNode("p", "blah blah", "children")
        self.assertEqual(str(test), "HTMLNode(p, blah blah, children, None)")

    def test_repr_2(self):
        test = HTMLNode("p", "blah blah")
        self.assertEqual(str(test), "HTMLNode(p, blah blah, None, None)")

    def test_repr_3(self):
        test = HTMLNode("h1")
        self.assertEqual(str(test), "HTMLNode(h1, None, None, None)")

    def test_repr_3(self):
        test = HTMLNode("b")
        self.assertEqual(str(test), "HTMLNode(b, None, None, None)")
