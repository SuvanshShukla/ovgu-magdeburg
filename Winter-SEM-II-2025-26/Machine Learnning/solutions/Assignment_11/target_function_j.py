def calculate_squared_distance(p1, p2):
    """Calculates squared Euclidean distance between two (x,y) points."""
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def calculate_objective_function(points, centroids, membership_matrix, m):
    """
    Calculates the FCM Objective Function (J).
    
    points: List of (x, y) tuples
    centroids: List of (x, y) tuples
    membership_matrix: List of lists (each sub-list corresponds to a cluster)
    m: Fuzziness exponent
    """
    total_j = 0.0
    
    # Iterate through each cluster (j)
    for j in range(len(centroids)):
        cluster_centroid = centroids[j]
        cluster_memberships = membership_matrix[j]
        cluster_j_contribution = 0.0
        
        # Iterate through each point (i)
        for i in range(len(points)):
            u_ij = cluster_memberships[i]
            dist_sq = calculate_squared_distance(points[i], cluster_centroid)
            
            # (u_ij^m) * dist^2
            term = (u_ij ** m) * dist_sq
            cluster_j_contribution += term
            
        print(f"Contribution of Cluster {j} to J: {cluster_j_contribution:.4f}")
        total_j += cluster_j_contribution
        
    return total_j

# --- DATA INPUT SECTION ---
# Easily change points, centroids, or memberships here

# 1. Coordinates: A, B, C, D, E
pts = [(1, 2), (3, 2), (5, 2), (1, 1), (5, 1)]

# 2. Centroids: Alpha and Beta
cntrds = [
    (2.1313, 1.7194), # Cluster Alpha
    (4.3225, 1.4671)  # Cluster Beta
]

# 3. Membership Matrix (Rows = Clusters, Columns = Points)
# Note: Ensure the order matches the points above
u_alpha= [0.892869, 0.709246, 0.082093, 0.862313, 0.071856]
u_beta= [0.107131, 0.290754, 0.917907, 0.137687, 0.928144]
u_matrix = [u_alpha, u_beta]

# 4. Fuzziness
m_val = 2

# --- CALCULATION ---
final_j = calculate_objective_function(pts, cntrds, u_matrix, m_val)

print("-" * 35)
print(f"TOTAL OBJECTIVE FUNCTION (J): {final_j:.6f}")
