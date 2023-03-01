#!/usr/bin/env python3
"""Hamming distance
"""

from __future__ import annotations
import argparse
from dataclasses import dataclass
from itertools import zip_longest


def main() -> None:
    """Main function
    """
    print(Hamm(args=get_args()).solve())


class Hamm:
    """A representation of compute Hamming distance
    """
    def __init__(self, args: Args) -> None:
        """Intialize the Hamm object

        :param args: Command-line arguments
        :type args: Args
        """
        self._args = args

    def solve(self) -> int:
        """Solve the compute Hamming distance problem

        :return: Hamming distance
        :rtype: int
        """
        hamming_distance = self.compute_hamming_distance(self._args.seq1, self._args.seq2)

        return hamming_distance

    def compute_hamming_distance(self, seq1: str, seq2: str) -> int:
        """Compute the Hamming distance (number of differences between two strings)

        :param seq1: DNA sequence 1
        :type seq1: str
        :param seq2: DNA sequence 2
        :type seq2: str
        :return: Hamming distance
        :rtype: int
        """
        hamming_distance = 0
        for base1, base2 in zip_longest(seq1, seq2):
            if base1 != base2:
                hamming_distance += 1

        return hamming_distance


@dataclass(frozen=True)
class Args:
    """Command-line arguments
    """
    seq1: str
    seq2: str


def get_args() -> Args:
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'seq1',
        metavar='str',
        help='Sequence 1',
    )
    parser.add_argument(
        'seq2',
        metavar='str',
        help='Sequence 2',
    )

    args = parser.parse_args()

    return Args(seq1=args.seq1, seq2=args.seq2)


if __name__ == '__main__':
    main()
