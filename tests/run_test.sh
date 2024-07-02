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

../filter_catalog.py \
    -i test_catalog.fa \
    -w whitelist_R04_max10snp \
    -o catalog_R04_max10snp.fa

blastn -db nt_euk \
    -query catalog_R04_max10snp.fa \
    -task megablast \
    -max_target_seqs 1 \
    -evalue 5 \
    -outfmt "10 delim=@ qseqid qlen sscinames sblastnames sskingdoms stitle evalue bitscore score length nident qcovs" \ 
    -out results.out -remote

diff whitelist_R04_max10snp expected_whitelist_R04_max10snp
diff catalog_R04_max10snp.fa expected_catalog_R04_max10snp.fa
diff results.out expected_results.out