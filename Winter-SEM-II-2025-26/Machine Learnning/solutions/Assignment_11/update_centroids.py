def calculate_centroid(points, memberships, m):
    """
    Calculates a single cluster centroid using pure Python.
    
    points: List of (x, y) tuples
    memberships: List of membership values for this specific cluster
    m: Fuzziness exponent
    """
    sum_weights = 0.0
    sum_x_weighted = 0.0
    sum_y_weighted = 0.0
    
    # Process each point one by one
    for i in range(len(points)):
        # Calculate the weight: u^m
        weight = memberships[i] ** m
        
        # Add to denominator
        sum_weights += weight
        
        # Add to numerators (weight * coordinate)
        sum_x_weighted += weight * points[i][0]
        sum_y_weighted += weight * points[i][1]
    
    # Final centroid coordinates
    new_x = sum_x_weighted / sum_weights
    new_y = sum_y_weighted / sum_weights
    
    return (new_x, new_y)

# --- Input Section ---
try:
    m_val = float(input("Enter the fuzziness exponent m (e.g., 2): "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Your specific points
# A(1,2), B(3,2), C(5,2), D(1,1), E(5,1)
points = [
    (1, 2), # A
    (3, 2), # B
    (5, 2), # C
    (1, 1), # D
    (5, 1)  # E
]

# Your membership values
u_alpha= [0.892869, 0.709246, 0.082093, 0.862313, 0.071856]
u_beta= [0.107131, 0.290754, 0.917907, 0.137687, 0.928144]

# --- Calculation ---
centroid_alpha = calculate_centroid(points, u_alpha, m_val)
centroid_beta = calculate_centroid(points, u_beta, m_val)

# --- Results ---
print("\n" + "="*30)
print(f"NEW CENTROIDS (m = {m_val})")
print("="*30)
print(f"Cluster Alpha (x, y): ({centroid_alpha[0]:.4f}, {centroid_alpha[1]:.4f})")
print(f"Cluster Beta  (x, y): ({centroid_beta[0]:.4f}, {centroid_beta[1]:.4f})")
