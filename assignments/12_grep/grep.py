#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-11-23
Purpose: Pseudo grep program
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Pseudo grep program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='A positional argument')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numfiles = len(args.files)

    for filehand in args.files:
        for line in filehand:
            if re.search(args.pattern, line,
                         re.IGNORECASE if args.insensitive else 0):
                print('{}{}'.format(f'{filehand.name}:' if numfiles > 1
                                    else '', line), end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
