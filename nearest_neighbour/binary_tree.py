"""Recursive definition of a binary search tree."""
import numpy as np

from num2words import num2words


class Node(object):
    """Node in a binary search tree"""

    def __init__(self, key, left, right, data=None):
        self.key = key
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.key, self.data,
                                         self.left, self.right)

def build_tree(point_list):
    """Recursively build a binary search tree."""
    if not point_list:
        return None

    try:
        root_loc, root_data = point_list.pop(0)
        return Node(
            key=root_loc,
            left=build_tree([n for n in point_list if n[0] <= root_loc]),
            right=build_tree([n for n in point_list if n[0] > root_loc]),
            data=root_data)
    except ValueError:  # no datafield
        root_loc = point_list.pop(0)
        return Node(
            key=root_loc,
            left=build_tree([n for n in point_list if n <= root_loc]),
            right=build_tree([n for n in point_list if n > root_loc]))


def inorder_traverse(node):
    """Root of a subtree is printed *between* the values of its left and right
    subtrees."""
    if node is None:
        return
    inorder_traverse(node.left)
    print(node.key)
    inorder_traverse(node.right)


def preorder_traverse(node):
    """Root of a subtree is printed *before* the values of its left and right
    subtrees. Topologically sorted."""
    if node is None:
        return
    print(node.key)
    preorder_traverse(node.left)
    preorder_traverse(node.right)


def postorder_traverse(node):
    """Root of a subtree is printed *after* the values of its left and right
    subtrees."""
    if node is None:
        return
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.key)


def tree_search(node, key):
    """Recursively search the tree for the node with key `key`"""
    if node is None or key == node.key:
        return node
    if key < node.key:
        return tree_search(node.left, key)
    return tree_search(node.right, key)



def tree_search_iterative(node, key):
    """Unroll the recursion and iteratively search the tree for the node with
    key `key`"""
    while node is not None and key != node.key:
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return node


def tree_minimum(node):
    """Follow the left children to find the minimum value in the tree."""
    while node.left:
        node = node.left
    return node


def tree_maximum(node):
    """Follow the left children to find the minimum value in the tree."""
    while node.right:
        node = node.right
    return node


def main():
    numbers = np.random.choice(range(100), size=20, replace=False).tolist()
    points_with_data = list(zip(numbers, map(num2words, numbers)))
    tree = build_tree(points_with_data)

    for k in range(40, 50):
        found_node = tree_search(tree, k)
        if found_node is not None:
            print(k, found_node.data)

    for k in range(50, 60):
        found_node = tree_search_iterative(tree, k)
        if found_node is not None:
            print(k, found_node.data)

    tree_min = tree_minimum(tree)
    tree_max = tree_maximum(tree)
    print("Tree minimum: ", tree_min.key, tree_min.data)
    print("Tree maximum: ", tree_max.key, tree_max.data)


if __name__ == '__main__':
    main()
