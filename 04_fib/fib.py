#!/usr/bin/env python3
"""Calculate Fibonacci
"""

from __future__ import annotations
import argparse
from collections import deque
from dataclasses import dataclass


def main() -> None:
    """Main function
    """
    print(Fibonacci(args=get_args()).solve())


class Fibonacci:
    """A representation of calculate fibonacci
    """
    def __init__(self, args: Args) -> None:
        """Initialize the Fibonacci object

        :param args: Command-line arguments
        :type args: Args
        """
        self._args = args
        self.fib_seq = deque([0, 1])


    def solve(self) -> int:
        """Solve the calculate Fibonacci problem
        """
        for _ in range(self._args.generations - 1):
            f_n = (self.fib_seq[0] * self._args.litter) + self.fib_seq[1]
            self.fib_seq.append(f_n)
            self.fib_seq.popleft()

        return f_n


@dataclass(frozen=True)
class Args:
    """Command-line arguments
    """
    generations: int
    litter: int


def get_args() -> Args:
    """Get command-line arguments

    :return: Arguments
    :rtype: Args
    """
    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'gen',
        metavar='generations',
        type=int,
        help='Number of generations',
    )

    parser.add_argument(
        'litter',
        metavar='litter',
        type=int,
        help='Size of litter per generation',
    )

    args = parser.parse_args()

    if not 1 <= args.gen <= 40:
        parser.error(f'generations "{args.gen}" must be between 1 and 40')

    if not 1 <= args.litter <= 5:
        parser.error(f'litter "{args.litter}" must be between 1 and 5')

    return Args(generations=args.gen, litter=args.litter)


if __name__ == '__main__':
    main()
