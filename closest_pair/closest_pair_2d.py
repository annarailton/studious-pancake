"""Two dimensional implementation of divide and conquer for closest pair
problem."""
import numpy as np

from brute_force_closest_pair import brute_force_closest_pair


def dist_2d(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))


def project(points, x_value):
    """Project `points` onto the vertical line going through `x_value`."""
    # Replace 0th column with `x_value`
    points = np.array(points)
    if points.ndim == 1:
        points = np.expand_dims(points, axis=0)
    points[:, 0] = x_value
    return points


def closest_pair_2d(points, dist=dist_2d):
    """
    Divide and conquer implementation of closest pair algorithm in 2D.

    Args:
        points (np.array): list of points with some distance metric between them

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """

    if len(points) <= 3:
        return brute_force_closest_pair(points, dist=dist)

    # Sort on first column
    points = points[points[:, 0].argsort()]

    # Partition points by vertical line defined by median x-coordinate
    median = np.median(points, axis=0)
    median_x = median[0]
    s1 = points[points[:, 0] < median_x]
    s2 = points[points[:, 0] >= median_x]

    # # # Recursively compute closest pair distances
    min_distance_s1, min_points_s1 = closest_pair_2d(s1)
    min_distance_s2, min_points_s2 = closest_pair_2d(s2)
    delta = min(min_distance_s1, min_distance_s2)

    # Make P1 and P2, the slices either side of median_x
    p1 = s1[np.abs(s1[:, 0] - median_x) < delta]
    p2 = s2[np.abs(s2[:, 0] - median_x) < delta]

    min_distance_cut = np.inf
    min_points_cut = None
    if len(p1) and len(p2):  # Both need to be non-empty
        for p in p1:
            potential_points = [
                q for q in p2 if dist(project(q, median_x), p) < delta
            ]  # max 6 points here
            for q in potential_points:
                if dist(p, q) < min_distance_cut:
                    min_distance_cut = dist(p, q)
                    min_points_cut = tuple([p, q])

    dist_to_points = {  # to recover pair of points
        min_distance_s1: min_points_s1,
        min_distance_s2: min_points_s2,
        min_distance_cut: min_points_cut
    }
    min_distance = min(dist_to_points.keys())
    min_points = dist_to_points[min_distance]

    return min_distance, min_points


def main():
    points = np.random.rand(20, 2)
    print(closest_pair_2d(points))
    print(brute_force_closest_pair(points, dist=dist_2d))


if __name__ == '__main__':
    main()
