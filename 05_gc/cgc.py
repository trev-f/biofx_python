#!/usr/bin/env python3
"""Compute GC content
"""

from __future__ import annotations
import argparse
import sys
from dataclasses import dataclass
from typing import TextIO

from Bio import SeqIO


def main() -> None:
    """Main function
    """
    print(CGC(get_args()).solve())


class CGC:
    """A representation of compute GC content
    """
    def __init__(self, args: Args) -> None:
        """Initialize the GC object

        :param args: Command-line arguments
        :type args: Args
        """
        self._args = args


    def solve(self) -> str:
        """Solve the compute GC content problem

        :return: Sequence ID and GC content
        :rtype: str
        """
        gc_percents = self.compute_fasta_records_percent_gc(fasta=self._args.file)
        max_gc_percent = self.max_dict(gc_percents)

        return self.format_max_gc_percent(max_gc_percent=max_gc_percent)


    def compute_fasta_records_percent_gc(self, fasta: TextIO | str) -> dict[str, float]:
        """Compute percent GC for every record in a FASTA file

        :param fasta: FASTA file handle or file path
        :type fasta: TextIO | str
        :return: Sequence ID key and percent GC value for each sequence in fasta
        :rtype: dict[str, float]
        """
        records = SeqIO.parse(fasta, format='fasta')
        gc_percents = {record.id: self.compute_percent_gc(dna=record.seq) for record in records}

        return gc_percents


    def compute_percent_gc(self, dna: str) -> float:
        """Compute the percent GC of a DNA sequence

        :param dna: DNA sequence
        :type dna: str
        :return: Percent of G, C, g, or c resideues
        :rtype: float
        """
        gc_count = self.count_gc(dna=dna)
        gc_percent = 100 * gc_count / len(dna)

        return gc_percent


    def count_gc(self, dna: str) -> int:
        """Count the number of G or C residues in a DNA sequence

        :param dna: DNA sequence
        :type dna: str
        :return: Count of G, C, g, or c)
        :rtype: int
        """
        gc_count = 0
        for base in dna:
            if base in 'GCgc':
                gc_count += 1

        return gc_count


    def max_dict(self, d: dict) -> dict:
        """Return the item with the maximum value from a dictionary

        :param d: Dictionary
        :type d: dict
        :return: Item with max value
        :rtype: dict
        """
        max_key, max_val = max(d.items(), key=lambda k: k[1])

        return {max_key: max_val}


    def format_max_gc_percent(self, max_gc_percent: dict[str, float]) -> str:
        """Format the maximum GC percent for the Rosalind answer

        :param max_gc_percent: Maximum GC percentage consisting of a sequence ID key and percent GC value
        :type max_gc_percent: dict[str, float]
        :return: Formatted GC percentage solution of form: '<sequence ID> <percent GC to 6 decimals>'
        :rtype: str
        """
        for item in max_gc_percent.items():
            seq_id, gc_percent = item

        return f'{seq_id} {gc_percent:.6f}'


@dataclass(frozen=True)
class Args:
    """Command-line arguments
    """
    file: TextIO


def get_args() -> None:
    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'file',
        metavar='FILE',
        type=argparse.FileType('rt'),
        nargs='?',
        default=sys.stdin,
        help='Input sequence file',
    )

    args = parser.parse_args()

    return Args(file=args.file)


if __name__ == '__main__':
    main()
