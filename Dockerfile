FROM ubuntu:22.04 AS preprocess_catalog
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.15.0/ncbi-blast-2.15.0+-x64-linux.tar.gz
RUN tar -xvf ncbi-blast-2.15.0+-x64-linux.tar.gz && \
    cd ncbi-blast-2.15.0+/bin/ && \
    # copy only the executables that are needed
    cp * /usr/local/bin/ && \
    cd / && \
    rm -rf ncbi-blast-2.15.0+-x64-linux.tar.gz ncbi-blast-2.15.0+

RUN update_blastdb.pl --decompress taxdb

COPY filter_catalog.py /