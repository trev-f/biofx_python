#!/usr/bin/env python3
"""Print the reverse complement of DNA
"""

import argparse
import os
from dataclasses import dataclass
from typing import TextIO


def main() -> None:
    """Main functions
    """
    args = get_args()

    print(RevComp(dna=args.dna).solve())


class RevComp:
    """A representation of reverse complement
    """

    def __init__(self, dna: str) -> None:
        """Initialize RevComp object

        :param dna: DNA sequence
        :type dna: str
        """
        self.dna = dna
    
    def solve(self) -> str:
        """Solve reverse complement problem

        :return: Reverse complement
        :rtype: str
        """
        rev = self.reverse(self.dna)
        revc = self.complement(rev)

        return revc
    
    def complement(self, dna: str) -> str:
        """Complement a DNA sequence

        :param dna: DNA sequence
        :type dna: str
        :return: Complemented DNA sequence
        :rtype: str
        """
        comp_table = self._generate_dna_complementation_table()
        
        return dna.translate(comp_table)
    
    def _generate_dna_complementation_table(self) -> dict[int, int]:
        """Generate a DNA complementation table

        :return: Complementation table.
        :rtype: dict[int, int]
        """
        return str.maketrans('ATCG', 'TAGC')

    def reverse(self, dna: str) -> str:
        """Reverse a DNA sequence

        :param dna: DNA sequence
        :type dna: str
        :return: Reversed DNA sequence
        :rtype: str
        """
        return dna[::-1]


@dataclass(frozen=True)
class Args:
    """Command-line arguments
    """
    dna: str


def get_args() -> Args:
    """Get command-line arguments

    :return: Arguments
    :rtype: Args
    """
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'dna',
        metavar='DNA',
        help='Input sequence or file',
    )

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(dna=args.dna)


if __name__ == '__main__':
    main()
