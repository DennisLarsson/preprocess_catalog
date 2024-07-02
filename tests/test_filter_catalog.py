import unittest

from filter_catalog import filter_whitelisted_loci

class TestFilterCatalog(unittest.TestCase):
    def test_filter_whitelisted_loci(self):
        whitelist = ['locus_1', 'locus_3']
        catalog = ['>locus_1 NS=3\n', 'ACGT\n', '>locus_2 NS=3\n', 'TGCA\n', '>locus_3 NS=3\n', 'TGCA\n']
        expected_filtered_catalog = ['>locus_1 NS=3\n', 'ACGT\n', '>locus_3 NS=3\n', 'TGCA\n']
        self.assertEqual(filter_whitelisted_loci(whitelist, catalog), expected_filtered_catalog)