#!/usr/bin/env python3
"""Tetranucleotide frequency"""

import argparse
import os
from dataclasses import dataclass


def main() -> None:
    """Main function"""

    args = get_args()

    print(DNACounts(args.dna).solve())


class DNACounts:
    """A representation of counting bases in DNA
    """
    def __init__(self, seq: str) -> None:
        """Create the DNA counts instance

        :param seq: DNA sequence
        :type seq: str
        """
        self.seq = seq

    def solve(self) -> str:
        """Return counts of DNA bases

        :return: Space-separated counts of DNA bases in alphabetical order: A, C, G, T
        :rtype: str
        """
        counts = self.count_dna_bases(seq=self.seq)

        return self._format_counts(counts)

    def count_dna_bases(self, seq: str) -> tuple[int, int, int, int]:
        """Count the number of each base in a DNA sequence

        :param seq: DNA sequence
        :type seq: str
        :return: The count of each base in alphabetical order: A, C, G, T
        :rtype: list[int]
        """
        counts = [0, 0, 0, 0]

        for base in seq:
            if base in "Aa":
                counts[0] += 1
            elif base in "Cc":
                counts[1] += 1
            elif base in "Gg":
                counts[2] += 1
            elif base in "Tt":
                counts[3] += 1

        return counts

    def _format_counts(self, counts: tuple[int, int, int, int]) -> str:
        """Format a list of counts to the expected format of a string of counts separated by spaces

        :param counts: A list of counts
        :type counts: list[int]
        :return: Counts separated by spaces in the same order in which they are supplied
        :rtype: str
        """
        counts = [str(count) for count in counts]

        return ' '.join(counts)


@dataclass(frozen=True)
class Args:
    """Command-line arguments"""
    dna: str


def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tetranucleotide` frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'dna',
        metavar='DNA',
        help='Input DNA sequence'
    )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(dna=args.dna)


if __name__ == '__main__':
    main()
