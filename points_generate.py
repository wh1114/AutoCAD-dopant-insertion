import numpy as np
from shapely.geometry import Point, Polygon
import csv
import random

# === CONFIGURATION ===
poly_coords = [
        (0.1600, 0.0258),
        (0.1054, 0.0750),
        (0.1054, 0.0850),
        (0.1600, 0.1342)
]

radius = 0.0004
n_spheres = 300
z_min = 0.0294
z_max = 0.0356

csv_filename = "random_sphere_centres.csv"
scr_filename = "spheres_insert.scr"

polygon = Polygon(poly_coords)
min_x, min_y, max_x, max_y = polygon.bounds

sphere_centres = []
attempts = 0
max_attempts = n_spheres * 50

while len(sphere_centres) < n_spheres and attempts < max_attempts:
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    z = random.uniform(z_min, z_max)

    # Check if the circle of radius R is inside the polygon
    circle = Point(x, y).buffer(radius)
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
