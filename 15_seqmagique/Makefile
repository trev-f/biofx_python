.PHONY: test

data:
	wget ftp://ftp.imicrobe.us/projects/26/samples/578/CAM_SMPL_GS108.fa.gz

test:
	python3 -m pytest -xv   seqmagique.py tests/seqmagique_test.py

all:
	../bin/all_test.py seqmagique.py
