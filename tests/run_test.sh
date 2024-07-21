#! /bin/bash

cat test_populations.sumstats.tsv | \
    grep -v "^#" | \
    cut -f 1,4 | \
    sort -n | \
    uniq | \
    cut -f 1 | \
    uniq -c | \
    awk '$1 <= 10 {print $2}' > whitelist_R04_max10snp

gunzip test_catalog.fa.gz

./filter_catalog.py \
    --catalog test_catalog.fa \
    --whitelist whitelist_R04_max10snp \
    > catalog_R04_max10snp.fa

blastn -db nt_euk \
    -query catalog_R04_max10snp.fa \
    -task blastn \
    -max_target_seqs 1 \
    -evalue 5 \
    -outfmt "10 delim=@ qseqid qlen sscinames sblastnames sskingdoms stitle evalue bitscore score length nident qcovs" \
    -out results.out -remote

# Make script testable and create a unittest for it
./filter_nonplant_loci.py \
    -b results.out \
    -c catalog_R04_max10snp.fa \
    -o catalog_R04_max10snp_blasted.fa

diff whitelist_R04_max10snp expected_whitelist_R04_max10snp
diff catalog_R04_max10snp.fa expected_catalog_R04_max10snp.fa
# diff results.out expected_results.out
# Write a script that tests for the format of the output, rather than the exact content, which changes with database updates
diff catalog_R04_max10snp_blasted.fa expected_catalog_R04_max10snp_blasted.fa
# Modify test files to include much fewer loci to make testing easier to overview and checking for errors