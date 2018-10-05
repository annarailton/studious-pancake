import numpy as np

def brute_force_closest_pair(points, dist):
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
