import math

def calculate_k_means_distances():
    print("--- Central Point (Centroid) ---")
    try:
        cx = float(input("Enter Centroid x: "))
        cy = float(input("Enter Centroid y: "))
        
        print("\n--- Points to Compare ---")
        points_input = input("Enter points as x,y pairs (e.g., 1,2 3,2 5,1): ")
        
        # Split by space, then by comma
        point_list = []
        for p in points_input.strip().split():
            x_str, y_str = p.split(',')
            point_list.append((float(x_str), float(y_str)))

        print("\n--- Results (Copy-Paste to Obsidian) ---")
        
        for i, (px, py) in enumerate(point_list):
            label = chr(65 + i) 
            
            # Math calculation
            dx = px - cx
            dy = py - cy
            dist = math.sqrt(dx**2 + dy**2)
            
            # formatting: .g removes unnecessary .0, :.4f rounds the result
            # Note the double {{ }} for LaTeX commands
            output = (
                f"$$D(C_1, {label}) = \\sqrt{{({px:g} - {cx:g})^2 + "
                f"({py:g} - {cy:g})^2}} = {dist:.4f}$$"
            )
            print(output)
            
    except ValueError:
        print("Error: Please ensure you enter numbers in the correct format (x,y).")

if __name__ == "__main__":
    calculate_k_means_distances()
