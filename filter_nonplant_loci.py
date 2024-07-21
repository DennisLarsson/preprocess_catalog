#!/bin/python3

import argparse

def check_organism(organism, keywords, blacklist, locus):
    if not any(keyword in organism for keyword in keywords):
        blacklist.add(int(locus))
    return blacklist

def filter_catalog(catalog, blacklist):
    output_list = []
    i = 0
    while i < len(catalog):
        locus = int(catalog[i].lstrip('>').split(' ')[0])
        if locus not in blacklist:
            output_string = catalog[i] + catalog[i + 1]
            output_list.append(output_string)
        i += 2
    return output_list


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="filter the catalog to only contain non-plant loci")
    argparser.add_argument("-b", help="Path to the blast results file")
    argparser.add_argument("-c", help="Path to the catalog.fa file")
    argparser.add_argument("-o", help="Path to the output file")

    args = argparser.parse_args()
    blast_file = args.b
    catalog_path = args.c
    output_file_path = args.o

    # Process blast results and categorize into plants and others
    blacklist = set()
    keywords = ["eudicots", "monocots", "seed plants", "flowering plants"]

    with open(blast_file, "r") as results_file:
        for line in results_file:
            locus, _, _, organism = line.split("@", maxsplit=3)
            blacklist = check_organism(organism, keywords, blacklist, locus)

    # Convert blacklist to a sorted list
    loci_list = sorted(blacklist)

    # Filter catalog based on loci_list (acting as a blacklist)
    with open(catalog_path, "r") as catalog_file, open(output_file_path, "w") as output_file:
        catalog = catalog_file.readlines()
        output_list = filter_catalog(catalog, blacklist)
        output_file.write("".join(output_list))
