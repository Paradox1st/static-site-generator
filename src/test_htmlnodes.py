import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_1(self):
        test = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(test.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_2(self):
        test = LeafNode("a", "Click me!", {"href": "https://github.com"})
        self.assertEqual(test.to_html(), '<a href="https://github.com">Click me!</a>')

    def test_leaf_to_html_3(self):
        test = LeafNode("b", None)
        self.assertRaises(ValueError, test.to_html)

    def test_leaf_to_html_4(self):
        test = LeafNode(None, "Just me")
        self.assertEqual(test.to_html(), "Just me")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
