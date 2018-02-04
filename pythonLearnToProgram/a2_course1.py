def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    cnt = 0
    for c in dna:
        if c == nucleotide:
            cnt = cnt + 1
    return cnt


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the dna sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G'). 

    >>> is_valid_sequence('ATCDG')
    False
    >>> is_valid_sequence('ATTTCGC')
    True
    >>> is_valid_sequence('aTTC')
    False
    
    """
    is_valid = True
    for c in dna:
        if c not in 'ATCG':
            is_valid = False
            return is_valid
    return is_valid

def insert_sequence(dna1, dna2, i):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index i

    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    >>> insert_sequence('AC','GG',0)
    GGAC
    >>> insert_sequence('ACCC','GT',3)
    ACCCGT
    
    """
    return dna1[:i]+dna2+dna1[i:]

def get_complement(nucleotide):
    """ (str) -> str

    return the complement of nucleotide. A and T can be bonded together, and
    thus complement each other; similarly, C and G are complements of each other.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C

    """
    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    The two strands in DNA are complementary because each nucleotide in one
    strand is bonded with its complement in the other strand.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('ACGTACG')
    'TGCATGC'

    """
    complement = ""
    for c in dna:
        complement = complement + get_complement(c)
    return complement
