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
        records = SeqIO.parse(self._args.file.name, 'fasta')


        gc_percents = {}
        for record in records:
            gc_count = 0
            for base in record.seq:
                if base in 'GCgc':
                    gc_count += 1
            gc_percent = 100 * gc_count / len(record.seq)

            gc_percents[record.id] = gc_percent

        return gc_percents


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
