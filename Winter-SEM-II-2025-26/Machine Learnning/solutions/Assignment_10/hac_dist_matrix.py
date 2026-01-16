import math

def generate_distance_matrix():
    # Define your points from the earlier coordinates
    # A(1, 2), B(3, 2), C(5, 2), D(1, 1), E(5, 1)
    points = {
        'A': (8, 9),
        'B': (9, 8),
        'C': (14, 9),
        'D': (2.5, 6),
        'E': (6, 4),
        'F': (7, 5)
    }
    
    labels = sorted(points.keys())
    
    print("--- Initial Distance Matrix (Euclidean) ---")
    print("      " + "      ".join(labels))
    
    for row_label in labels:
        row_str = f"{row_label} | "
        for col_label in labels:
            p1 = points[row_label]
            p2 = points[col_label]
            
            # Euclidean Distance formula
            dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
            
            # Formatting for alignment
            row_str += f"{dist:6.2f} "
            
        print(row_str)

if __name__ == "__main__":
    generate_distance_matrix()
