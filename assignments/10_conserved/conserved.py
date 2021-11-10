#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-11-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sequences = args.file.read().splitlines()

    print('\n'.join(sequences))
    for i in range(len(sequences[0])):
        characters = []
        for seq in sequences:
            characters += seq[i]
        if all([characters[0] == chars for chars in characters]):
            print('|', end='')
        else:
            print('X', end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
