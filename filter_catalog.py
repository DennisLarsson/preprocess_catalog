#!/bin/python3

import argparse
import sys

def filter_whitelisted_loci(whitelist, catalog):
	index_whitelist=0
	index_catalog=0
	filtered_catalog = []

	while index_whitelist < len(whitelist):
		while '>' + whitelist[index_whitelist].rstrip() != catalog[index_catalog].split(' ')[0]:
			index_catalog += 2
		filtered_catalog.append(catalog[index_catalog])
		filtered_catalog.append(catalog[index_catalog + 1])
		index_whitelist += 1
		index_catalog += 2
	
	return filtered_catalog

if __name__ == "__main__":
	argparser = argparse.ArgumentParser(description="filter the catalog to only contain whitelisted loci")
	argparser.add_argument("--whitelist", help="Path to the whitelist file")
	argparser.add_argument("--catalog", help="Path to the catalog.fa file")

	args = argparser.parse_args()
	whitelist_file_path = args.whitelist
	catalog_path = args.catalog
	sys.stderr.write(f"{whitelist_file_path} {catalog_path}\n")
	sys.stderr.flush()
			
	with open (whitelist_file_path) as whitelist_file:
		whitelist = whitelist_file.readlines()

	with open (catalog_path) as catalog_file:
		catalog_list = catalog_file.readlines()

	filtered_catalog = filter_whitelisted_loci(whitelist, catalog_list)

	for line in filtered_catalog:
		print(line, end='')
