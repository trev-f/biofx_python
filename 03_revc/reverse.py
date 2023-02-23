import random


def generate_dna_seq(length: int, seed: int = None) -> str:
    """Generate a random DNA sequence

    :param length: Length of the DNA sequence
    :type length: int
    :param seed: Seed for reproducible generation of a random sequence, defaults to None
    :type seed: int, optional
    :return: Random DNA sequence
    :rtype: str
    """
    random.seed(seed)

    return ''.join((random.choices('ACGT', k=length)))
