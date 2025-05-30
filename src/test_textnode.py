import unittest

from textnode import TextNode, TextType, text_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq_1(self):
        test = TextNode("normal text", TextType.ITALIC)
        other = TextNode("normal text", TextType.ITALIC)
        self.assertEqual(test, other)

    def test_eq_2(self):
        test = TextNode("link text", TextType.LINK, "https://github.com")
        other = TextNode("link text", TextType.LINK, "https://github.com")
        self.assertEqual(test, other)

    def test_neq_1(self):
        test = TextNode("normal text", TextType.ITALIC)
        other = TextNode("normal text", TextType.BOLD)
        self.assertNotEqual(test, other)

    def test_neq_2(self):
        test = TextNode("alt text", TextType.IMAGE, "./img.jpg")
        other = TextNode("alt text", TextType.IMAGE, "./img.png")
        self.assertNotEqual(test, other)

    def test_neq_3(self):
        test = TextNode("alt text", TextType.IMAGE, "./img.jpg")
        other = TextNode("alt text", TextType.IMAGE)
        self.assertNotEqual(test, other)

    def test_repr_1(self):
        test = TextNode("test link", TextType.LINK, "https://boot.dev")
        self.assertEqual(str(test), "TextNode(test link, link, https://boot.dev)")

    def test_repr_2(self):
        test = TextNode("italic", TextType.ITALIC)
        self.assertEqual(str(test), "TextNode(italic, italic, None)")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
