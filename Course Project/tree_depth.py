"""Задача 15: дълбочина на двоично дърво по брой възли."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_depth(node):
    if node is None:
        return 0

    left_depth = tree_depth(node.left)
    right_depth = tree_depth(node.right)
    return 1 + max(left_depth, right_depth)


def build_example():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(20)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.left.right.right = Node(9)
    return root


if __name__ == "__main__":
    root = build_example()
    print("Дълбочина по брой възли:", tree_depth(root))
