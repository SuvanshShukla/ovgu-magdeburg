import math

def get_point_input():
    points = {}
    print("--- Input Your Points ---")
    print("Enter points as 'Label x,y' (e.g., A 1,2). Type 'done' when finished.")
    
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'done':
            break
        try:
            label, coords = user_input.split()
            x, y = map(float, coords.split(','))
            points[label] = (x, y)
        except ValueError:
            print("Invalid format. Use: Label x,y (e.g., B 3,4)")
    return points

def calculate_centroid(point_list):
    x_coords = [p[0] for p in point_list]
    y_coords = [p[1] for p in point_list]
    n = len(point_list)
    return (sum(x_coords) / n, sum(y_coords) / n)

def main():
    # 1. Get all points
    all_points = get_point_input()
    if not all_points:
        return

    # 2. Define which points were merged into a cluster
    print("\n--- Create a Cluster ---")
    merge_labels = input("Enter labels of points to merge (e.g., A B): ").split()
    
    cluster_points = [all_points[label] for label in merge_labels if label in all_points]
    
    if len(cluster_points) < 2:
        print("You need at least two points to form a cluster.")
        return

    # 3. Calculate Centroid
    centroid = calculate_centroid(cluster_points)
    cluster_name = "{" + ",".join(merge_labels) + "}"
    print(f"\nNew Centroid for {cluster_name}: ({centroid[0]:.2f}, {centroid[1]:.2f})")

    # 4. Calculate new distances
    print(f"\n--- New Distances from {cluster_name} to remaining points ---")
    for label, coords in all_points.items():
        if label not in merge_labels:
            dist = math.sqrt((coords[0] - centroid[0])**2 + (coords[1] - centroid[1])**2)
            print(f"Dist({cluster_name}, {label}) = {dist:.4f}")

if __name__ == "__main__":
    main()
