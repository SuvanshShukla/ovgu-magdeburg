import math
import pandas as pd

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_cluster_dist(cluster1, cluster2, points_dict):
    """Calculates the average distance between all pairs in two clusters."""
    total_dist = 0
    count = 0
    for p1 in cluster1:
        for p2 in cluster2:
            total_dist += euclidean_dist(points_dict[p1], points_dict[p2])
            count += 1
    return total_dist / count

def print_matrix(clusters, points_dict):
    """Displays the current distance matrix using pandas for alignment."""
    size = len(clusters)
    matrix = []
    labels = [f"{{{','.join(c)}}}" for c in clusters]
    
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(0.0)
            else:
                d = calculate_cluster_dist(clusters[i], clusters[j], points_dict)
                row.append(round(d, 4))
        matrix.append(row)
    
    df = pd.DataFrame(matrix, index=labels, columns=labels)
    print("\n--- Current Distance Matrix (Average Linkage) ---")
    print(df)
    print("-" * 50)

def main():
    points = {}
    print("Step 1: Input Points (e.g., A 8,9). Type 'start' to begin clustering.")
    while True:
        inp = input("> ").strip()
        if inp.lower() == 'start': break
        try:
            label, coords = inp.split()
            x, y = map(float, coords.split(','))
            points[label] = (x, y)
        except: print("Invalid format. Use: Label x,y")

    # Each cluster starts as a list containing one point label
    # e.g., [['A'], ['B'], ['C']...]
    clusters = [[label] for label in sorted(points.keys())]

    while len(clusters) > 1:
        print_matrix(clusters, points)
        
        print(f"Current Clusters: {' '.join([str(c) for c in clusters])}")
        cmd = input("Enter two clusters to merge (e.g., A B) or 'done': ").strip()
        
        if cmd.lower() == 'done': break
        
        to_merge = cmd.split()
        if len(to_merge) != 2:
            print("Please enter exactly two labels.")
            continue

        # Find the clusters containing these labels
        c1, c2 = None, None
        for c in clusters:
            if to_merge[0] in c: c1 = c
            if to_merge[1] in c: c2 = c
        
        if c1 and c2 and c1 != c2:
            new_cluster = sorted(c1 + c2)
            clusters.remove(c1)
            clusters.remove(c2)
            clusters.append(new_cluster)
            print(f"\nMerged {to_merge[0]} and {to_merge[1]} into {new_cluster}")
        else:
            print("Invalid clusters. Make sure labels are in different clusters.")

    print("\nFinal clustering reached.")

if __name__ == "__main__":
    main()
