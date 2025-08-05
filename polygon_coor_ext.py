import re
import csv

# Paste your raw AutoCAD ID command output here
raw_data = """
Command: ID
Specify point:  X = 0.1600     Y = 0.0258     Z = 0.0360
Command:
ID
Specify point:  X = 0.1054     Y = 0.0750     Z = 0.0360
Command:
ID
Specify point:  X = 0.1054     Y = 0.0850     Z = 0.0360
Command:
ID
Specify point:  X = 0.1600     Y = 0.1342     Z = 0.0360

"""

# Extract lines with coordinates
matches = re.findall(r'X\s*=\s*([\d.]+)\s+Y\s*=\s*([\d.]+)\s+Z\s*=\s*([\d.]+)', raw_data)

# Convert to list of (x, y) tuples
xy_coords = [(x, y) for x, y, _ in matches]

# Print formatted output
for i, (x, y) in enumerate(xy_coords):
    end = ',' if i < len(xy_coords) - 1 else ''  # no comma after last
    print(f"\t({x}, {y}){end}")