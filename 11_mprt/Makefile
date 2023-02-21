.PHONY: test

test:
	python3 -m pytest -xv   mprt.py tests/mprt_test.py

clean:
	rm -rf fasta

fasta:
	./fetch_fasta.sh tests/inputs/1.txt

# Cf. https://github.com/katef/libfsm
fsm:
	re -b -pl dot 'N[^P][ST][^P]' | dot -Tpng -ofsm.png

all:
	../bin/all_test.py mprt.py
