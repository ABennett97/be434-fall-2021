#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-11-16
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run_Length Encoding of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for sequence in args.text.splitlines():
        print(rle(sequence))


# --------------------------------------------------
def rle(seq):
    encoded = ""
    i = 0
    while (i <= len(seq)-1):
        count = 1
        ch = seq[i]
        j = i
        while (j < len(seq)-1):     
            if (seq[j] == seq[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded = encoded + str(count) + ch
        i = j + 1
    return encoded


# --------------------------------------------------
# def test_rle():
#     """ Test rle """

#     assert rle('A') == 'A'
#     assert rle('ACGT') == 'ACGT'
#     assert rle('AA') == 'A2'
#     assert rle('AAAAA') == 'A5'
#     assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
