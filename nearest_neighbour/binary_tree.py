"""Recursive definition of a binary search tree."""
import numpy as np


class Node(object):
    """Node in a binary search tree"""

    def __init__(self, location, left_child, right_child):
        self.location = location
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return "({}, {}, {})".format(self.location, self.left_child,
                                     self.right_child)


def build_tree(point_list):
    """Recursively build a binary search tree."""
    if not point_list:
        return None

    root = point_list.pop(0)
    return Node(
        location=root,
        left_child=build_tree([n for n in point_list if n <= root]),
        right_child=build_tree([n for n in point_list if n > root]))


def inorder_traverse(node):
    """Root of a subtree is printed *between* the values of its left and right
    subtrees."""
    if node is None:
        return
    inorder_traverse(node.left_child)
    print(node.location)
    inorder_traverse(node.right_child)


def preorder_traverse(node):
    """Root of a subtree is printed *before* the values of its left and right
    subtrees. Topologically sorted."""
    if node is None:
        return
    print(node.location)
    preorder_traverse(node.left_child)
    preorder_traverse(node.right_child)


def postorder_traverse(node):
    """Root of a subtree is printed *after* the values of its left and right
    subtrees."""
    if node is None:
        return
    postorder_traverse(node.left_child)
    postorder_traverse(node.right_child)
    print(node.location)


def tree_search(node, key):
    pass


def tree_search_iterative(node, key):
    pass


def tree_minimum(node):
    pass


def tree_maximum():
    pass


def main():
    numbers = np.random.choice(range(100), size=20, replace=False).tolist()
    tree = build_tree(numbers)
    print(tree)
    inorder_traverse(tree)
    preorder_traverse(tree)


if __name__ == '__main__':
    main()
