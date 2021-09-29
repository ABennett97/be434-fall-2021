#!/usr/bin/env python3
"""
Author : abennett1 <abennett1@localhost>
Date   : 2021-09-28
Purpose: Read input file(s) and concatenate them
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default='')

    parser.add_argument('-n',
                        '--number',
                        help='Numbers every line flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print('{:6}\t{}'.format(line_num, line.rstrip()))
            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
