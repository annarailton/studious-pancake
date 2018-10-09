import itertools
import numpy as np
import time

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


def brute_force_lazy(points, dist):
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


if __name__ == '__main__':
    points = np.random.random(size=[4000, 3])
    print(brute_force_lazy(points, dist_euclidean))
    # print(brute_force_closest_pair(points, dist_euclidean))
