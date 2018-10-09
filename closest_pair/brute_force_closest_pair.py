import heapq
import itertools
import numpy as np

from tqdm import tqdm

from scipy.special import comb


def dist_euclidean(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))


def brute_force_closest_pair(points, dist):
    """
    Brute force closest pair algorithm.

    Args:
        points (list): list of points with some distance metric between them
        dist (func): function that takes two points and returns a distance

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """
    if len(points) == 1:
        return None, None

    # Expand dims so always > 1 (can then use row index)
    points = np.array(points)
    if points.ndim == 1:
        points = np.expand_dims(points, axis=1)

    min_distance = dist(points[0, :], points[1, :])
    min_points = tuple([points[0, :], points[1, :]])
    for i in range(points.shape[0]):
        for j in range(i + 1, points.shape[0]):
            if dist(points[i, :], points[j, :]) < min_distance:
                min_distance = dist(points[i, :], points[j, :])
                min_points = tuple([points[i, :], points[j, :]])

    return min_distance, min_points


def brute_force_lazy(points, dist=dist_euclidean):
    """
    Brute force closest pair algorithm using lazy evaluation to save on memory
    for big sets of points.

    Args:
        points (list): list of points with some distance metric between them
        dist (func): function that takes two points and returns a distance

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """
    if len(points) == 1:
        return None, None

    min_distance = np.inf
    min_points = None
    n_pairs = comb(len(points), 2, exact=True)
    pairs = itertools.combinations(points, 2)
    for p in tqdm(pairs, total=n_pairs, desc="brute_force_lazy"):
        p_dist = dist(*p)
        if p_dist < min_distance:
            min_distance = p_dist
            min_points = tuple(p)

    return min_distance, min_points


def brute_force_top_k(points, k, dist=dist_euclidean):
    """
    Brute force closest pair algorithm using lazy evaluation to save on memory
    for big sets of points. Stores the top k closest points.

    Args:
        points (list): list of points with some distance metric between them
        dist (func): function that takes two points and returns a distance

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """
    n_pairs = comb(len(points), 2, exact=True)
    if n_pairs < k:
        raise ValueError(
            "Insufficient points ({}) to take top {} distances".format(
                len(points), k))

    heap = []
    pairs = itertools.combinations(points, 2)
    for p in tqdm(pairs, total=n_pairs, desc="brute_force_top_k"):
        p_dist = dist(*p)
        if len(heap) < k:  # k is heap capacity
            heapq.heappush(heap, (-1 * p_dist, p))  # -ve dist as min heap
        else:
            # Push item on the heap, then pop and return the smallest item from
            # the heap (no need to store this)
            heapq.heappushpop(heap, (-1 * p_dist, p))

    return heap


if __name__ == '__main__':
    points = np.random.random(size=[100, 3])
    print(brute_force_lazy(points))
    h = brute_force_top_k(points, 10)
    print([-1 * i[0] for i in h])
    # print(brute_force_closest_pair(points, dist_euclidean))
