import numpy as np
from shapely.geometry import Point, Polygon
import csv
import random

# === CONFIGURATION ===

# Extract from ID command at AutoCAD
# This should be the coordinates of the polygon vertices
poly_coords = [
        (0.1600, 0.0258),
        (0.1054, 0.0750),
        (0.1054, 0.0850),
        (0.1600, 0.1342)
]

radius = 0.0004 # Radius of the spheres in meters (Should correspond to the dopant atom size)
z_min = 0.0290 + radius # Minimum Z coordinate for spheres
z_max = 0.0360 - radius # Maximum Z coordinate for spheres

# === PREPARATION ===
# csv_filename = "random_sphere_centres.csv"
scr_filename = "spheres_insert.scr" # AutoCAD script file

# Convert polygon coordinates to Shapely Polygon
polygon = Polygon(poly_coords)
min_x, min_y, max_x, max_y = polygon.bounds

# Calculate area and volume of the polygon
nm_per_unit = 1e4  # Convert to nanometers
cm_per_unit = 1e-3  # Convert to centimeters
cm_per_nm = cm_per_unit / nm_per_unit
area = polygon.area * (nm_per_unit ** 2) # in square nanometers
volume = area * ((z_max - z_min) * nm_per_unit) # in cubic nanometers

# Determine the number of spheres to generate

# Calculated approach based on doping density
doping_density = 1e19 # atoms per cubic centimeter
n_spheres = int(doping_density * (volume * cm_per_nm ** 3))
# Manually set n_spheres if needed
# n_spheres = 300  # Uncomment to use a fixed number of spheres

# === GENERATE SPHERE CENTRES ===
sphere_centres = []
attempts = 0
max_attempts = n_spheres * 50

while len(sphere_centres) < n_spheres and attempts < max_attempts:

    # Generate random coordinates within the bounding box of the polygon
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    z = random.uniform(z_min, z_max)

    # Check if the circle of radius R is inside the polygon
    circle = Point(x, y).buffer(radius)
    # If the circle is inside the polygon, add the centre to the list
    if polygon.contains(circle):
        sphere_centres.append((round(x, 6), round(y, 6), round(z, 6)))
    attempts += 1

print(f"✅ {len(sphere_centres)} valid sphere centres generated.")

# === OUTPUT FUNCTIONS ===
def write_csv(filename, data):
    with open(filename, "w", newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["X", "Y", "Z"])
        writer.writerows(data)
    print(f"📁 CSV saved to: {filename}")

def write_scr(filename, data, radius):
    with open(filename, "w") as f_scr:
        for x, y, z in data:
            f_scr.write("SPHERE\n")
            f_scr.write(f"{x},{y},{z}\n")
            f_scr.write(f"{radius}\n")
    print(f"📁 AutoCAD script saved to: {filename}")

# === OUTPUT TOGGLE ===
# write_csv(csv_filename, sphere_centres)
write_scr(scr_filename, sphere_centres, radius)

# Printing area and volume of the polygon
print(f"Area of polygon: {area:.8f} nm²")
print(f"Volume of spheres: {volume:.6f} nm³")
