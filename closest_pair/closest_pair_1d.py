"""One dimensional implementation of divide and conquer for closest pair
problem."""
import numpy as np


def dist(x, y):
    return abs(x - y)


def brute_force_closest_pair(points):
    """
    Brute force closest pair algorithm.

    Args:
        points (list): list of points with some distance metric between them

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """
    if len(points) == 1:
        return None, None

    min_distance = dist(points[0], points[1])
    min_points = set([points[0], points[1]])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if dist(points[i], points[j]) < min_distance:
                min_distance = dist(points[i], points[j])
                min_points = set([points[i], points[j]])

    return min_distance, min_points


def closest_pair(points):
    """
    Divide and conquer implementation of closest pair algorithm.

    Args:
        points (list): list of points with some distance metric between them

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """

    if len(points) <= 3:
        return brute_force_closest_pair(points)

    median = np.median(points)
    lower = [p for p in points if p < median]
    upper = list(set(points) - set(lower))

    min_distance1, min_points1 = closest_pair(list(lower))
    min_distance2, min_points2 = closest_pair(list(upper))

    # Find points closest to m in lower and upper
    lower_m = lower[np.argmin([dist(x, median) for x in lower])]
    upper_m = upper[np.argmin([dist(y, median) for y in upper])]
    assert lower_m <= median <= upper_m

    # Compare three distances
    min_distance_cut = dist(lower_m, upper_m)
    dist_to_points = {  # to recover pair of points
        min_distance1: min_points1,
        min_distance2: min_points2,
        min_distance_cut: set([lower_m, upper_m])
    }
    min_distance = min(min_distance1, min_distance2, min_distance_cut)
    min_points = dist_to_points[min_distance]

    return min_distance, min_points


def main():
    points = np.random.rand(10)
    print(points)
    print(brute_force_closest_pair(points))
    print(closest_pair(points))


if __name__ == '__main__':
    main()
