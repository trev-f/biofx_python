#!/usr/bin/env python3
"""Tetranucleotide frequency"""

import argparse
import os
from dataclasses import dataclass


def main() -> None:
    """Main function"""

    args = get_args()

    counts = count_dna_bases(seq=args.dna)

    print(format_counts(counts=counts))


def count_dna_bases(seq: str) -> list[int]:
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


def format_counts(counts: list[int]) -> str:
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
