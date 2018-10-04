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

    min_distance = dist(points[0], points[1])
    min_points = set([points[0], points[1]])
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if dist(points[i], points[j]) < min_distance:
                min_distance = dist(points[i], points[j])
                min_points = set([points[i], points[j]])

    return min_distance, min_points
