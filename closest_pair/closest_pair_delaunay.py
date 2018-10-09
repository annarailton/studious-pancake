import numpy as np
import time

from scipy.spatial import Delaunay

from closest_pair_2d import closest_pair_2d


def closest_pair_delaunay(points):
    """
    Finding the closest pair by using the Delaunay triangulation the iterating
    over the neighbours in the triangulation for every point.

    NB only works with the Euclidean distance as that is built into the scipy
    implementation of scipy.spatial.Delaunay.

    Args:
        points (np.array): list of points with some distance metric between them

    Returns:
        min_distance: minimum distance between points
        min_points: set of pair of points that are closest_pair
    """

    tri = Delaunay(points)

    min_distance = np.inf
    min_points = None
    for p in points:
        for q in points[tri.simplices[tri.find_simplex(p)]]:
            dist = np.linalg.norm(np.array(p) - np.array(q))
            if dist != 0.0 and dist < min_distance:
                min_distance = dist
                min_points = ([p, q])

    return min_distance, min_points


def main():

    n_per_centroid = 1000
    points = [[0, 0] + p for p in np.random.normal(scale=0.5, size=[n_per_centroid, 2])] +\
             [[5, 5] + p for p in np.random.normal(scale=0.5, size=[n_per_centroid, 2])] +\
             [[6, 0] + p for p in np.random.normal(scale=1.2, size=[n_per_centroid, 2])]

    points = np.array(points)

    t0 = time.time()
    print(closest_pair_delaunay(points))
    t1 = time.time()
    print("Time = {}".format(t1 - t0))
    print(closest_pair_2d(points))
    t2 = time.time()
    print("Time = {}".format(t2 - t1))


if __name__ == '__main__':
    main()
