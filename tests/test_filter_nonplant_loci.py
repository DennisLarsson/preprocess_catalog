import unittest
from filter_nonplant_loci import check_organism, filter_catalog

class TestFilterNonplantLoci(unittest.TestCase):
    def test_check_organism_true(self):
        keywords = ["eudicots", "monocots"]
        blacklist = set()
        organism = "eudicots"
        locus = "1"

        expected_blacklist = set()
        actual_blacklist = check_organism(organism, keywords, blacklist, locus)
        self.assertEqual(expected_blacklist, actual_blacklist)
    
    def test_check_organism_false(self):
        keywords = ["eudicots", "monocots"]
        blacklist = set()
        organism = "bacteria"
        locus = "1"

        expected_blacklist = {1}
        actual_blacklist = check_organism(organism, keywords, blacklist, locus)
        self.assertEqual(expected_blacklist, actual_blacklist)

    def test_check_organism_set_extended(self):
        keywords = ["eudicots", "monocots"]
        blacklist = {1}
        organism = "bacteria"
        locus = "2"
        
        expected_blacklist = {1, 2}
        actual_blacklist = check_organism(organism, keywords, blacklist, locus)
        self.assertEqual(expected_blacklist, actual_blacklist)
    
    def test_filter_catalog(self):
        catalog = [
            ">1 NS=3\n", "ACGT\n",
            ">2 NS=5\n", "TGCA\n",
            ">5 NS=21\n", "TGCA\n"
                   ]
        blacklist = {2}

        expected_output = [
            ">1 NS=3\nACGT\n",
            ">5 NS=21\nTGCA\n"
            ]
        actual_output = filter_catalog(catalog, blacklist)
        self.assertEqual(expected_output, actual_output)
    