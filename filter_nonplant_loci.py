#!/bin/python3

import sys

# Initialize variables
blast_file = ""
catalog_path = ""
output_file_path = ""

# Parse command-line arguments
for i, arg in enumerate(sys.argv):
    if arg == "-b":
        blast_file = sys.argv[i + 1]
    elif arg == "-c":
        catalog_path = sys.argv[i + 1]
    elif arg == "-o":
        output_file_path = sys.argv[i + 1]

# Process blast results and categorize into plants and others
loci_set = set()
keywords = ["eudicots", "monocots", "seed plants", "flowering plants"]

with open(blast_file, "r") as results_file:
    for line in results_file:
        organism = line.split("@")[3]
        if not any(keyword in organism for keyword in keywords):
            loci_set.add(int(line.split("@")[0]))

# Convert loci_set to a sorted list
loci_list = sorted(loci_set)

# Filter catalog based on loci_list (acting as a blacklist)
counter = 0
with open(catalog_path, "r") as catalog_file, open(output_file_path, "w") as output_file:
    catalog_lines = catalog_file.readlines()
    i = 0
    while i < len(catalog_lines):
        loci = int(catalog_lines[i].lstrip('>').split(' ')[0])
        if loci not in loci_set:
            output_file.write(catalog_lines[i] + catalog_lines[i + 1])
        else:
            counter += 1
        i += 2

print("Number of loci removed:", counter)