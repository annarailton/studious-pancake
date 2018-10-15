import numpy as np

from operator import itemgetter


class Node(object):
    """Node in k-dimensional tree"""

    def __init__(self, location, left_child, right_child):
        self.location = location
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return "({}, {}, {})".format(self.location, self.left_child,
                                     self.right_child)


class KDTree(object):
    """k-dimensional tree"""

    def __init__(self, data):
        """
        Args:
            data (np.array): data in the shape (n_samples, n_dimensions)
        """
        self.data = data.tolist()
        self.n_data, self.k = np.shape(data)
        self.depth = 0  # tree with just a root has depth 0
        self.tree = self.build(self.data, self.depth)

    def build(self, point_list, depth):
        """Recursively build the tree."""

        if not point_list:
            return None

        # Select axis based on depth
        axis = depth % self.k

        # Update depth of KDTree
        if depth > self.depth:
            self.depth = depth

        # Find median by sorting over axis
        median_idx = len(point_list) // 2
        point_list.sort(key=itemgetter(axis))

        # Create node and recursively create subtrees
        return Node(
            location=point_list[median_idx],
            left_child=self.build(point_list[:median_idx], depth + 1),
            right_child=self.build(point_list[median_idx + 1:], depth + 1))


def main():
    """Example usage"""
    point_list = np.array([(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)])
    kdtree = KDTree(point_list)
    print(kdtree.tree)
    print(kdtree.depth)


if __name__ == '__main__':
    main()
