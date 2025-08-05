import re
import csv

# Paste your raw AutoCAD ID command output here
raw_data = """
Command: ID
Specify point:  X = 0.0000     Y = 0.1283     Z = 0.0360
Command:
ID
Specify point:  X = -0.0750     Y = 0.0850     Z = 0.0360
Command:
ID
Specify point:  X = -0.0850     Y = 0.0850     Z = 0.0360
Command:
ID
Specify point:  X = -0.1600     Y = 0.1283     Z = 0.0360
Command:
ID
Specify point:  X = -0.1600     Y = 0.0317     Z = 0.0360
Command:
ID
Specify point:  X = -0.0850     Y = 0.0750     Z = 0.0360
Command:
ID
Specify point:  X = -0.0750     Y = 0.0750     Z = 0.0360
Command:
ID
Specify point:  X = 0.0000     Y = 0.0317     Z = 0.0360

"""

# print("Extracted coordinates from AutoCAD ID command output:")


# Extract lines with coordinates
matches = re.findall(r'X\s*=\s*(-?\d+(?:\.\d+)?)\s+Y\s*=\s*(-?\d+(?:\.\d+)?)\s+Z\s*=\s*(-?\d+(?:\.\d+)?)', raw_data)

# Convert to list of (x, y) tuples
xy_coords = [(x, y) for x, y, _ in matches]

print(f"Extracted {len(xy_coords)} coordinate pairs.")

# Print formatted output
for i, (x, y) in enumerate(xy_coords):
    end = ',' if i < len(xy_coords) - 1 else ''  # no comma after last
    print(f"\t({x}, {y}){end}")