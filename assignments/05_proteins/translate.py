#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sequence to Amino Acid',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        nargs='+',
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
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
