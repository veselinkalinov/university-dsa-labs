# Задача 15: дълбочина на двоично дърво
# Дълбочината се брои във върхове (нива):
# празно дърво = 0, дърво само с корен = 1.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth(node):
    if node is None:
        return 0
    left_depth = depth(node.left)
    right_depth = depth(node.right)
    return 1 + max(left_depth, right_depth)


def build_example_tree():
    #          12
    #         /  \
    #        7    5
    #       / \    \
    #      9   3    8
    #         /
    #        6
    root = Node(12)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(9)
    root.left.right = Node(3)
    root.right.right = Node(8)
    root.left.right.left = Node(6)
    return root


def build_chain(n):
    # дърво, в което всеки връх има само ляво дете
    root = Node(1)
    current = root
    for i in range(2, n + 1):
        current.left = Node(i)
        current = current.left
    return root


if __name__ == "__main__":
    root = build_example_tree()
    print("Примерно дърво:", depth(root))

    print("Празно дърво:", depth(None))

    print("Само корен:", depth(Node(1)))

    balanced = Node(1)
    balanced.left = Node(2)
    balanced.right = Node(3)
    balanced.left.left = Node(4)
    balanced.left.right = Node(5)
    balanced.right.left = Node(6)
    balanced.right.right = Node(7)
    print("Балансирано дърво със 7 върха:", depth(balanced))

    print("Верига от 5 върха:", depth(build_chain(5)))

    try:
        print("Верига от 5000 върха:", depth(build_chain(5000)))
    except RecursionError:
        print("Верига от 5000 върха: RecursionError")
