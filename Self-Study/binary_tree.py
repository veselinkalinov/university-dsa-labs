class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def preorder(node):
    if node is None:
        return

    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)


def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")


if __name__ == "__main__":
    root = Node("A")

    b = Node("B")
    c = Node("C")
    root.left = b
    root.right = c

    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.left = d
    b.right = e
    c.right = f

    print(root.left.right.value)
    print(root.right.right.value)

    print("\nPreodrer Traversal:")
    preorder(root)

    print("\nInodrer Traversal:")
    inorder(root)

    print("\nPostodrer Traversal:")
    postorder(root)
