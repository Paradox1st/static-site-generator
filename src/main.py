from textnode import TextNode, TextType


def main():
    myNode = TextNode("This is a link", TextType.LINK, "https://www.github.com")
    print(myNode)


if __name__ == "__main__":
    main()
