def k_means_clustering(
    points: list[tuple[float, ...]], 
    k: int, 
    initial_centroids: list[tuple[float, ...]], 
    max_iterations: int
) -> list[tuple[float, ...]]:

    def euclidean(p1, p2):
        return sum((x - y) ** 2 for x, y in zip(p1, p2)) ** 0.5

    def compute_centroid(cluster_points):
        total = len(cluster_points)
        # Average each dimension using zip(*cluster_points)
        return tuple(sum(dim) / total for dim in zip(*cluster_points))

    centroids = list(initial_centroids)

    for _ in range(max_iterations):
        # 1. Group points by assigned centroid index
        clusters = {i: [] for i in range(k)}

        for p in points:
            min_dist = float('inf')
            closest_idx = 0
            for idx, c in enumerate(centroids):
                dist = euclidean(p, c)
                if dist < min_dist:
                    min_dist = dist
                    closest_idx = idx
            
            clusters[closest_idx].append(p)

        # 2. Recompute centroids for the next iteration
        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroids.append(compute_centroid(clusters[i]))
            else:
                # Fallback: keep old centroid if no points were assigned
                new_centroids.append(centroids[i])

        centroids = new_centroids

    return centroids