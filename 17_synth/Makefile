.PHONY: test

test:
	python3 -m pytest -xv   synth.py tests/unit_test.py tests/synth_test.py

human:
	wget ftp://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz

all:
	../bin/all_test.py synth.py
