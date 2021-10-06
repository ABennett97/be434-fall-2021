#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sequence to Amino Acid',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA or RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'),
                        help='Input codon file')

    parser.add_argument('-o',
                        '--output',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    codon_table = {}
    for line in args.codons:
        key, val = line.split()
        codon_table[key] = val

    k = 3
    seq = args.sequence.upper()
    protein = ''
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        protein += codon_table.get(codon, '-')
        # print(codon, codon_table.get(codon, '-'), end='')
        
    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
