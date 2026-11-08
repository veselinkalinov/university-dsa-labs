# Recursive


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def bst_search_recur(root, target):
    if root is None:
        return None

    elif root.value == target:
        print(root.value, end=" ")
        return

    if root.value > target:
        print(root.value, end=" ")
        bst_search_recur(root.left, target)
    elif root.value < target:
        print(root.value, end=" ")
        bst_search_recur(root.right, target)
    elif root.value != target:
        return None


# Iterative


def bst_search_iter(root, target: int) -> list:
    current = root
    bst_list = []

    while current is not None:
        if current.value > target:
            bst_list.append(current.value)
            current = current.left
            continue
        elif current.value < target:
            bst_list.append(current.value)
            current = current.right
            continue
        else:
            bst_list.append(current.value)
            return bst_list


def bst_insert(root: Node | None, value: int) -> Node:
    if root is None:
        return Node(value)

    current = root
    parent = None

    while current is not None:
        if current.value > value:
            parent = current
            current = current.left
            continue
        elif current.value < value:
            parent = current
            current = current.right
            continue
        else:
            print("You are trying to add a duplicate")
            return root

    if parent.value < value:
        parent.right = Node(value)
    else:
        parent.left = Node(value)

    return root


if __name__ == "__main__":
    root = Node(50)

    root.left = Node(30)
    root.right = Node(70)

    root.left.left = Node(20)
    root.left.right = Node(40)

    root.right.left = Node(60)
    root.right.right = Node(80)

    root.left.left.left = Node(10)
    root.left.left.right = Node(25)

    root.right.left.right = Node(65)

    bst_search_recur(root, 25)

    iter_search = bst_search_iter(root, 55)
    print()
    print(iter_search)

    root = bst_insert(root, 55)
    root = bst_insert(root, 75)
    root = bst_insert(root, 30)
