#!/usr/bin/env python3
"""Transcribe DNA into RNA"""

import argparse
import os
from dataclasses import dataclass
from typing import TextIO


def main() -> None:
    """Main function"""
    args = get_args()
    inout = InputOutput(out_dir=args.out_dir)

    inout.make_out_dir()

    for fh in args.files:
        with open(inout.construct_out_path(fh=fh), 'wt') as out_fh:
            out_fh.write(Transcription(dna=fh.read()).solve())


class InputOutput:
    """Representation of input/output
    """

    def __init__(self, out_dir: str) -> None:
        """Initialize an InputOutput object

        :param out_dir: _description_
        :type out_dir: str
        """
        self.out_dir = out_dir

    def make_out_dir(self) -> None:
        """Make output directory
        """
        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)

        return

    def construct_out_path(self, fh: TextIO) -> str:
        """Construct and output file path

        :param fh: File handle
        :type fh: TextIO
        :return: Output file path
        :rtype: str
        """
        basename = os.path.basename(fh.name)

        return os.path.join(self.out_dir, basename)


class Transcription:
    """A representation of transcription of DNA to RNA
    """

    def __init__(self, dna: str) -> None:
        """Create the DNA counts instance

        :param seq: DNA sequence
        :type seq: str
        """
        self.dna = dna

    def solve(self) -> str:
        return self.transcribe(dna=self.dna)

    def transcribe(self, dna: str) -> str:
        """Transcribe DNA to RNA

        :param dna: DNA sequence
        :type dna: str
        :return: RNA sequence
        :rtype: str
        """
        return dna.replace('T', 'U')


@dataclass(frozen=True)
class Args:
    """Command-line arguments"""
    files: list[TextIO]
    out_dir: str


def get_args() -> Args:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        'file',
        metavar='FILE',
        help='Input DNA sequence',
        type=argparse.FileType('rt'),
        nargs='+',
    )
    parser.add_argument(
        '-o', '--out_dir',
        metavar='DIR',
        help='Output directory',
        default='out',
        type=str,
    )

    args = parser.parse_args()

    return Args(files=args.file, out_dir=args.out_dir)


if __name__ == '__main__':
    main()
