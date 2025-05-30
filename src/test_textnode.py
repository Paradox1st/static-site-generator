import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
