# ==========================================
# EDIT YOUR DATA HERE
# ==========================================
m = 2.0  # Fuzziness exponent

# Distance Matrix: [ [d_i1, d_i2, ... d_ic], ... ]
# Each sub-list represents one point's distances to all clusters.
# For example, Point A is 1.642 units from Alpha and 2.628 units from Beta.

# 1.6522, 2.6355
# 0.4012, 0.8754
# 2.3648, 1.6083
# 1.8349, 2.5643
# 2.4958, 1.4888

distance_matrix = [
    [1.1656, 3.3650], # Point A distances to [Alpha, Beta]
    [0.9129, 1.4258], # Point B
    [2.8824, 0.8620], # Point C
    [1.3407, 3.3552], # Point D
    [2.9575, 0.8229]  # Point E
]
# ==========================================

def calculate_fuzzy_memberships(dist_matrix, m_val):
    print(f"--- Fuzzy Membership Output (m={m_val}) ---")
    
    num_points = len(dist_matrix)
    num_clusters = len(dist_matrix[0])
    exponent = 1 / (m_val - 1)
    
    # Initialize matrix for results (Clusters as rows, Points as columns)
    u_matrix = [[] for _ in range(num_clusters)]

    for i in range(num_points):
        distances = dist_matrix[i]
        
        for j in range(num_clusters):
            d_alpha = distances[j]
            
            # Applying the formula: 1 / sum( (d_alpha^2 / d_beta^2)^(1/(m-1)) )
            try:
                sum_val = 0
                for d_beta in distances:
                    if d_beta == 0:
                        # Handle point sitting exactly on a centroid
                        sum_val = float('inf') if d_alpha != 0 else 1.0
                        break
                    
                    term = (d_alpha**2 / d_beta**2) ** exponent
                    sum_val += term
                
                u_ij = 1 / sum_val if sum_val != 0 else 0
                
            except ZeroDivisionError:
                u_ij = 0.0
                
            u_matrix[j].append(round(u_ij, 6))

    # Print results for easy copying
    for idx, row in enumerate(u_matrix):
        cluster_name = "Alpha" if idx == 0 else "Beta" if idx == 1 else f"Cluster {idx}"
        print(f"u_{cluster_name}: {row}")

if __name__ == "__main__":
    calculate_fuzzy_memberships(distance_matrix, m)
